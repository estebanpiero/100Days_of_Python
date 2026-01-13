# Creating Habit Tracker with Pixela

import datetime as dt
import requests
import os
from dotenv import load_dotenv

load_dotenv()


#--------------------------------------------------
# Configuration
#--------------------------------------------------

PIXELA_ENDPOINT = os.getenv('PIXELA_ENDPOINT')
PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
USERNAME = os.getenv('USERNAME')
GRAPH_ID = 'graph1'


def validate_environment():
    """Validate that all required environment variables are set."""
    required_vars = {
        'PIXELA_ENDPOINT': PIXELA_ENDPOINT,
        'PIXELA_TOKEN': PIXELA_TOKEN,
        'USERNAME': USERNAME
    }

    missing_vars = [var for var, value in required_vars.items() if not value]

    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")


#--------------------------------------------------
# Creating a Pixela Account
#--------------------------------------------------

def create_user_account():
    """Create a Pixela user account (only run once)."""
    user_params = {
        'token': PIXELA_TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    try:
        response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
        response.raise_for_status()
        print(f"✓ User account created successfully: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"✗ Error creating user account: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None


#--------------------------------------------------
# Creating a graph
#--------------------------------------------------

def create_graph(graph_id=GRAPH_ID, name='Coding Graph', unit='Hs', graph_type='float', color='ajisai'):
    """Create a new graph for tracking habits."""
    graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

    graph_params = {
        'id': graph_id,
        'name': name,
        'unit': unit,
        'type': graph_type,
        'color': color
    }

    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    try:
        response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
        response.raise_for_status()
        print(f"✓ Graph created successfully: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"✗ Error creating graph: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

#--------------------------------------------------
# Adding Pixel to Graph
#--------------------------------------------------

def add_pixel(graph_id=GRAPH_ID, quantity=None, date=None):
    """Add a pixel to the graph for a specific date."""
    if date is None:
        date = dt.datetime.now()

    if quantity is None:
        quantity = input("Enter the quantity (hours coded today): ")

    pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}'

    pixel_params = {
        'date': date.strftime('%Y%m%d') if isinstance(date, dt.datetime) else date,
        'quantity': str(quantity)
    }

    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    try:
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
        response.raise_for_status()
        print(f"✓ Pixel added successfully: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"✗ Error adding pixel: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

#--------------------------------------------------
#Updating Pixel
#--------------------------------------------------

def update_pixel(graph_id=GRAPH_ID, quantity=None, date=None):
    """Update an existing pixel on the graph."""
    if date is None:
        date = dt.datetime.now()

    if quantity is None:
        quantity = input("Enter the new quantity: ")

    date_str = date.strftime('%Y%m%d') if isinstance(date, dt.datetime) else date
    update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date_str}'

    update_params = {
        'quantity': str(quantity)
    }

    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    try:
        response = requests.put(url=update_endpoint, json=update_params, headers=headers)
        response.raise_for_status()
        print(f"✓ Pixel updated successfully: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"✗ Error updating pixel: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

#--------------------------------------------------
# Deleting pixel
#--------------------------------------------------

def delete_pixel(graph_id=GRAPH_ID, date=None):
    """Delete a pixel from the graph."""
    if date is None:
        date = dt.datetime.now()

    date_str = date.strftime('%Y%m%d') if isinstance(date, dt.datetime) else date
    delete_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date_str}'

    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    try:
        response = requests.delete(url=delete_endpoint, headers=headers)
        response.raise_for_status()
        print(f"✓ Pixel deleted successfully: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"✗ Error deleting pixel: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

#--------------------------------------------------
# Main Function
#--------------------------------------------------

def main():
    """Main function to run the habit tracker."""
    try:
        validate_environment()

        # Uncomment the following lines only once to set up your account
        # create_user_account()
        # create_graph()

        # Add a pixel for today
        add_pixel()

        # Uncomment to update today's pixel
        # update_pixel(quantity='3')

        # Uncomment to delete today's pixel
        # delete_pixel()

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
