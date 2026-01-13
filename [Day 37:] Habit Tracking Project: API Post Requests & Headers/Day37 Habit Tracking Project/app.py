# Flask Web Application for Pixela Habit Tracker

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import datetime as dt
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')

# Configuration
PIXELA_ENDPOINT = os.getenv('PIXELA_ENDPOINT')
PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
USERNAME = os.getenv('USERNAME')


#--------------------------------------------------
# Helper Functions
#--------------------------------------------------

def get_headers():
    """Return headers with authentication token."""
    return {'X-USER-TOKEN': PIXELA_TOKEN}


def get_all_graphs():
    """Fetch all graphs for the user."""
    try:
        url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
        print(f"DEBUG: Fetching graphs from: {url}")
        print(f"DEBUG: Using username: {USERNAME}")
        print(f"DEBUG: Using token: {PIXELA_TOKEN[:5]}..." if PIXELA_TOKEN else "DEBUG: Token is None")
        response = requests.get(url, headers=get_headers())
        print(f"DEBUG: Response status: {response.status_code}")
        print(f"DEBUG: Response body: {response.text}")
        response.raise_for_status()
        return response.json().get('graphs', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching graphs: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response text: {e.response.text}")
        return []


def get_graph_url(graph_id):
    """Get the URL to view a graph."""
    return f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}.html'


def create_graph(graph_id, name, unit, graph_type, color):
    """Create a new graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
    graph_params = {
        'id': graph_id,
        'name': name,
        'unit': unit,
        'type': graph_type,
        'color': color
    }

    try:
        response = requests.post(url, json=graph_params, headers=get_headers())
        response.raise_for_status()
        return True, "Graph created successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error creating graph: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


def update_graph(graph_id, name=None, color=None):
    """Update an existing graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}'
    update_params = {}

    if name:
        update_params['name'] = name
    if color:
        update_params['color'] = color

    try:
        response = requests.put(url, json=update_params, headers=get_headers())
        response.raise_for_status()
        return True, "Graph updated successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error updating graph: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


def delete_graph(graph_id):
    """Delete a graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}'

    try:
        response = requests.delete(url, headers=get_headers())
        response.raise_for_status()
        return True, "Graph deleted successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error deleting graph: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


def add_pixel(graph_id, date, quantity):
    """Add a pixel to a graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}'
    pixel_params = {
        'date': date,
        'quantity': str(quantity)
    }

    try:
        response = requests.post(url, json=pixel_params, headers=get_headers())
        response.raise_for_status()
        return True, "Activity added successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error adding activity: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


def update_pixel(graph_id, date, quantity):
    """Update a pixel on a graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}'
    update_params = {
        'quantity': str(quantity)
    }

    try:
        response = requests.put(url, json=update_params, headers=get_headers())
        response.raise_for_status()
        return True, "Activity updated successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error updating activity: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


def delete_pixel(graph_id, date):
    """Delete a pixel from a graph."""
    url = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}'

    try:
        response = requests.delete(url, headers=get_headers())
        response.raise_for_status()
        return True, "Activity deleted successfully!"
    except requests.exceptions.RequestException as e:
        error_msg = f"Error deleting activity: {e}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" - {e.response.text}"
        return False, error_msg


#--------------------------------------------------
# Routes
#--------------------------------------------------

@app.route('/')
def index():
    """Home page showing all graphs."""
    graphs = get_all_graphs()

    # Add view URL to each graph
    for graph in graphs:
        graph['view_url'] = get_graph_url(graph['id'])

    return render_template('index.html', graphs=graphs, username=USERNAME)


@app.route('/graph/create', methods=['GET', 'POST'])
def create_graph_route():
    """Create a new graph."""
    if request.method == 'POST':
        graph_id = request.form.get('graph_id')
        name = request.form.get('name')
        unit = request.form.get('unit')
        graph_type = request.form.get('type')
        color = request.form.get('color')

        success, message = create_graph(graph_id, name, unit, graph_type, color)

        if success:
            flash(message, 'success')
            return redirect(url_for('index'))
        else:
            flash(message, 'error')

    # Color options for Pixela
    colors = [
        ('shibafu', 'Green'),
        ('momiji', 'Red'),
        ('sora', 'Blue'),
        ('ichou', 'Yellow'),
        ('ajisai', 'Purple'),
        ('kuro', 'Black')
    ]

    return render_template('create_graph.html', colors=colors)


@app.route('/graph/<graph_id>/update', methods=['GET', 'POST'])
def update_graph_route(graph_id):
    """Update an existing graph."""
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form.get('color')

        success, message = update_graph(graph_id, name, color)

        if success:
            flash(message, 'success')
            return redirect(url_for('index'))
        else:
            flash(message, 'error')

    # Get current graph info
    graphs = get_all_graphs()
    current_graph = next((g for g in graphs if g['id'] == graph_id), None)

    # Color options for Pixela
    colors = [
        ('shibafu', 'Green'),
        ('momiji', 'Red'),
        ('sora', 'Blue'),
        ('ichou', 'Yellow'),
        ('ajisai', 'Purple'),
        ('kuro', 'Black')
    ]

    return render_template('update_graph.html', graph=current_graph, colors=colors)


@app.route('/graph/<graph_id>/delete', methods=['POST'])
def delete_graph_route(graph_id):
    """Delete a graph."""
    success, message = delete_graph(graph_id)

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('index'))


@app.route('/graph/<graph_id>/activity', methods=['GET', 'POST'])
def manage_activity(graph_id):
    """Add or update activity for a graph."""
    graphs = get_all_graphs()
    current_graph = next((g for g in graphs if g['id'] == graph_id), None)

    if not current_graph:
        flash('Graph not found', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        date = request.form.get('date').replace('-', '')  # Convert YYYY-MM-DD to YYYYMMDD
        quantity = request.form.get('quantity')
        action = request.form.get('action')

        if action == 'add':
            success, message = add_pixel(graph_id, date, quantity)
        elif action == 'update':
            success, message = update_pixel(graph_id, date, quantity)
        elif action == 'delete':
            success, message = delete_pixel(graph_id, date)
        else:
            success, message = False, "Invalid action"

        if success:
            flash(message, 'success')
        else:
            flash(message, 'error')

    # Get today's date for default value
    today = dt.datetime.now().strftime('%Y-%m-%d')

    return render_template('manage_activity.html', graph=current_graph, today=today)


@app.route('/api/graphs')
def api_graphs():
    """API endpoint to get all graphs."""
    graphs = get_all_graphs()
    return jsonify(graphs)


if __name__ == '__main__':
    app.run(
        debug=True,  # Set to False in production!
        host='0.0.0.0',  # Make accessible from network
        port=5050
    )