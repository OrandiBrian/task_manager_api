# Task Manager API

A Django Rest Framework (DRF) API for managing tasks with user authentication, filtering, and sorting.

## Features
- **User Authentication**: Register, login, and manage tasks securely.
- **Task CRUD Operations**: Create, read, update, and delete tasks.
- **Task Filtering & Sorting**: Filter by status, priority, due date; sort by due date or priority.
- **Task Completion**: Mark tasks as complete/incomplete with timestamps.
- **Ownership & Permissions**: Users can only access their own tasks.

## Tech Stack
- **Django** & **Django Rest Framework**
- **SQLite** (Configurable Database)
- **Django Filters** (for task filtering & sorting)
- **JWT / Token Authentication**

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```

### 2. Create & Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Apply migrations and run server
```bash
$ python manage.py migrate
$ python manage.py runserver
```

## API Endpoints
| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | `/api/token/` | Get authentication token (login) |
| POST | `/api/token/refresh/` | Refresh access token|

## Task Management
! Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/tasks/` | List tasks (with filters and sorting) |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{id}` | Retrieve a specific task |
| PUT/PATCH | `/api/tasks/{id}` | Update a task (if not completed ) |
| DELETE | `/api/tasks/{id}` | Delete a task |
| POST | `/api/tasks/{id}/mark_complete/` | Mark task as completed |
| POST | `/api/tasks/{id}/mark_incomplete/` | Mark task as incomplete |

## Authentication & Access
- The app uses **JWT tokens** for authentication.
- After login, you receive an **access token**.
- Include this token in the **Authorization** header for protected requests

### Example: Using cURL
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ -H "Authorization: Bearer your_generated_token"
```

### Example: Using Python Requests
```python
import requests

headers = {
    "Authorization": "Bearer your_generated_token"
}

response = requests.get("http://127.0.0.1:8000/api/tasks/", headers=headers)

print(response.json())  # Print tasks
```

## Deployment
- Deploy on **PythonAnywhere** following Django deployment best practices.
- Use Gunicorn as a WSGI server in production.

## Contributing
1. Fork the repo.
2. Create a new branch: `feature-branch-name`.
3. Commit your changes and push.
4. Submit a Pull Request.