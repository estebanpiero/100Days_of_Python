# Pixela Habit Tracker Web Application

A beautiful web interface for managing your Pixela habit tracking graphs. Track your daily habits, visualize your progress, and manage multiple tracking graphs all from one convenient dashboard.

## Features

- **View All Graphs**: See all your habit tracking graphs in one place with live previews
- **Create Graphs**: Set up new habit tracking graphs with custom settings
- **Update Graphs**: Modify existing graph names and colors
- **Delete Graphs**: Remove graphs you no longer need
- **Manage Activities**: Add, update, or delete daily activity entries
- **Live Graph Preview**: View your Pixela graphs embedded directly in the interface
- **Responsive Design**: Beautiful, modern UI that works on desktop and mobile

## Screenshot Features

- Dashboard with all your graphs
- Create new tracking graphs
- Add daily activities
- Update existing entries
- View full-screen graphs

## Prerequisites

- Python 3.7 or higher
- A Pixela account (the app will help you create one)
- pip (Python package installer)

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:

   Edit the `.env` file with your Pixela credentials:
   ```
   PIXELA_ENDPOINT=https://pixe.la/v1/users
   PIXELA_TOKEN=your-token-here
   USERNAME=your-username
   FLASK_SECRET_KEY=your-secret-key-here
   ```

   - `PIXELA_TOKEN`: Your unique authentication token (use a random string)
   - `USERNAME`: Your desired Pixela username
   - `FLASK_SECRET_KEY`: A random secret key for Flask sessions

## Quick Start

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Open your browser**:
   Navigate to `http://localhost:5000`

3. **First-time setup** (if you haven't created a Pixela account yet):
   - Uncomment the `create_user_account()` line in `habit_tracking_app.py`
   - Run it once to create your account
   - Comment it back out after running

## Usage Guide

### Creating Your First Graph

1. Click "Create Graph" in the navigation bar
2. Fill in the form:
   - **Graph ID**: Unique identifier (lowercase, numbers, hyphens only)
   - **Graph Name**: Display name for your graph
   - **Unit**: What you're measuring (hours, pages, km, etc.)
   - **Type**: Integer or Float (decimal numbers)
   - **Color**: Choose a color for your graph
3. Click "Create Graph"

### Adding Daily Activities

1. From the dashboard, click "Add Activity" on any graph
2. Select the date
3. Enter the quantity
4. Click "Add Activity"

### Updating Activities

1. Go to the activity management page for a graph
2. Use the "Update Activity" form
3. Select the date you want to update
4. Enter the new value
5. Click "Update Activity"

### Deleting Activities

1. Go to the activity management page for a graph
2. Use the "Delete Activity" form
3. Select the date
4. Click "Delete Activity"

### Managing Graphs

- **Edit**: Click "Edit" on a graph card to update its name or color
- **Delete**: Click "Delete" to remove a graph (confirmation required)
- **View Full**: Click "View Full Graph" to see your graph on Pixela's website

## Project Structure

```
Day37 Habit Tracking Project/
├── app.py                      # Main Flask application
├── habit_tracking_app.py       # Original CLI version
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Dashboard
│   ├── create_graph.html      # Create graph form
│   ├── update_graph.html      # Update graph form
│   └── manage_activity.html   # Activity management
└── static/                     # Static files
    └── css/
        └── style.css          # Styles
```

## API Endpoints

- `GET /` - Dashboard (view all graphs)
- `GET /graph/create` - Create graph form
- `POST /graph/create` - Create new graph
- `GET /graph/<id>/update` - Update graph form
- `POST /graph/<id>/update` - Update graph
- `POST /graph/<id>/delete` - Delete graph
- `GET /graph/<id>/activity` - Activity management page
- `POST /graph/<id>/activity` - Add/update/delete activity
- `GET /api/graphs` - JSON API for graphs

## Pixela Graph Colors

Available colors for your graphs:
- **shibafu** (Green) - Fresh and natural
- **momiji** (Red) - Bold and energetic
- **sora** (Blue) - Calm and focused
- **ichou** (Yellow) - Bright and optimistic
- **ajisai** (Purple) - Creative and unique
- **kuro** (Black) - Classic and elegant

## Troubleshooting

### "Missing required environment variables"
- Make sure your `.env` file is properly configured
- Check that all required variables are set

### "Error creating graph"
- Graph IDs must be unique
- Use only lowercase letters, numbers, and hyphens
- Make sure you've created a Pixela account first

### "Error adding activity"
- Check that the date format is correct (YYYYMMDD)
- Ensure the quantity matches the graph type (int vs float)
- An activity for that date might already exist (use update instead)

### Can't see my graphs
- Make sure you've created at least one graph
- Check your internet connection
- Verify your Pixela credentials in `.env`

## Tips

- **Daily Tracking**: Bookmark the activity page for your most-used graph
- **Consistency**: Set up a daily reminder to log your activities
- **Multiple Habits**: Create different graphs for different habits
- **Visualization**: Use the full graph view to see your progress over time
- **Color Coding**: Use different colors to categorize types of habits

## About Pixela

Pixela is a free service for recording and visualizing your habits or efforts. Each pixel represents a day's worth of activity. Build up a streak by staying consistent!

Visit [pixe.la](https://pixe.la) to learn more.

## Contributing

This is a learning project from the 100 Days of Python course. Feel free to fork and customize it for your own needs!

## License

This project is for educational purposes. Pixela API is property of its respective owners.

## Acknowledgments

- Built as part of Day 37 of 100 Days of Python
- Uses the Pixela API for habit tracking
- Flask framework for the web interface
