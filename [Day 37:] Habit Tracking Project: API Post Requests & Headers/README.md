# Day 37: Habit Tracking Project - API Post Requests & Headers

## Project: Habit Tracker with Pixela

### Description
A habit tracking application using the Pixela API to create and maintain a visual habit graph. Users can track daily activities (exercise, coding, reading, etc.) and visualize their consistency over time with a GitHub-style contribution graph.

### What I Learned
- HTTP POST requests
- HTTP PUT requests
- HTTP DELETE requests
- API headers and authentication
- Token-based authentication
- Creating users via API
- Updating and deleting data
- RESTful API principles

### How to Run
```bash
python3 main.py
```

### Features
- Create user account on Pixela
- Create custom habit graphs
- Post daily progress (pixels)
- Update previous entries
- Delete entries
- Visual habit tracking
- GitHub-style contribution graph

### Pixela API Endpoints

#### 1. Create User
```python
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "your_secret_token",
    "username": "yourusername",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
```

#### 2. Create Graph
```python
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"  # blue
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint,
                        json=graph_config,
                        headers=headers)
```

#### 3. Post a Pixel (Add Data)
```python
import datetime

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.5",  # 3.5 hours
}

response = requests.post(url=pixel_endpoint,
                        json=pixel_data,
                        headers=headers)
```

#### 4. Update a Pixel
```python
update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "4.0"  # Update to 4 hours
}

response = requests.put(url=update_endpoint,
                       json=update_data,
                       headers=headers)
```

#### 5. Delete a Pixel
```python
delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
```

### HTTP Methods Summary

- **GET**: Retrieve data
- **POST**: Create new data
- **PUT**: Update existing data
- **DELETE**: Remove data

### Headers

```python
headers = {
    "X-USER-TOKEN": "your_secret_token"
}

# Used for authentication
requests.post(url, json=data, headers=headers)
```

### Full Implementation
```python
import requests
from datetime import datetime

USERNAME = "yourusername"
TOKEN = "your_secret_token123"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# 1. Create user (run once)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)

# 2. Create graph (run once)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Hours",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,
#                         json=graph_config,
#                         headers=headers)

# 3. Post pixel (daily)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

response = requests.post(url=pixel_endpoint,
                        json=pixel_data,
                        headers=headers)
print(response.text)

# View your graph:
# https://pixe.la/v1/users/USERNAME/graphs/GRAPH_ID.html
```

### Date Formatting
```python
from datetime import datetime

today = datetime.now()

# Pixela requires: YYYYMMDD
date_str = today.strftime("%Y%m%d")
# Example: "20231215"
```

### Graph Colors
- `shibafu`: Green
- `momiji`: Red
- `sora`: Blue
- `ichou`: Yellow
- `ajisai`: Purple
- `kuro`: Black

### Graph Viewing URL
```
https://pixe.la/v1/users/USERNAME/graphs/GRAPH_ID.html
```

### Key Concepts
- **POST Requests**: Creating new resources
- **PUT Requests**: Updating existing resources
- **DELETE Requests**: Removing resources
- **Headers**: Metadata sent with requests
- **Token Authentication**: Secure API access
- **RESTful APIs**: Standard API architecture
- **JSON Payloads**: Sending data to APIs

### Use Cases
- Track coding hours
- Exercise tracking
- Reading pages
- Study time
- Any daily habit

### Automation Idea
Create a daily reminder script that prompts you to log your habit data:
```python
import schedule
import time

def log_habit():
    # Run pixel posting code
    pass

# Run every day at 9 PM
schedule.every().day.at("21:00").do(log_habit)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Learning Focus
Understanding POST, PUT, and DELETE requests for creating and modifying data via APIs - essential for building applications that interact with web services.
