# Task Management API

A RESTful API for managing tasks with user authentication and CRUD operations.

## Features

- User registration and authentication
- Task creation, reading, updating, and deletion
- Task prioritization (Low, Medium, High)
- Task status tracking (Pending, Completed)
- Filtering tasks by status and priority
- Sorting tasks by priority
- Marking tasks as complete/incomplete

## API Endpoints

### Authentication

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | `/signup_api/` | Register a new user |
| POST | `/api/login/` | Get authentication token (login) |
| POST | `/api/login/refresh/` | Refresh access token |

### Task Management

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/tasks/` | List tasks (with filters and sorting) |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{id}` | Retrieve a specific task |
| PUT/PATCH | `/api/tasks/{id}` | Update a task |
| DELETE | `/api/tasks/{id}` | Delete a task |
| POST | `/api/tasks/{id}/mark_complete/` | Mark task as completed |
| POST | `/api/tasks/{id}/mark_incomplete/` | Mark task as incomplete |

## Getting Started

### User Registration

To register a new user, send a POST request to `/signup_api/` with the following JSON payload:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password1": "your_password",
  "password2": "your_password"
}
```

### Authentication

After registration, obtain an access token by sending a POST request to `/api/login/` with your credentials:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

The response will include an access token and a refresh token:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

Include this access token in the Authorization header for all subsequent requests:

```
Authorization: Bearer your_access_token
```

### Refresh Token

When your access token expires, send a POST request to `/api/login/refresh/` with your refresh token:

```json
{
  "refresh": "your_refresh_token"
}
```

## Task Operations

### List Tasks

GET `/api/tasks/`

Optional query parameters for filtering:
- `status`: Filter by status ("Pending" or "Completed")
- `priority`: Filter by priority ("Low", "Medium", "High")
- `ordering`: Sort by priority (use "priority" for ascending, "-priority" for descending)

Example: `/api/tasks/?status=Pending&priority=High&ordering=-priority`

### Create Task

POST `/api/tasks/`

```json
{
  "title": "Complete project documentation",
  "description": "Finish the README file for the API project",
  "priority": "High"
}
```

### Update Task

PUT/PATCH `/api/tasks/{id}/`

```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "priority": "Medium"
}
```

### Mark Task as Complete

POST `/api/tasks/{id}/mark_complete/`

### Mark Task as Incomplete

POST `/api/tasks/{id}/mark_incomplete/`

## Web Interface

The application also provides a web interface with the following routes:

| Route | Description |
| ----- | ----------- |
| `/` | Home page |
| `/about/` | About page |
| `/signup/` | User registration page |
| `/login/` | Login page |
| `/logout/` | Logout |
| `/tasks_list/` | View all tasks |
| `/add/` | Add a new task |
| `/tasks_list/{id}/` | View task details |
| `/tasks_list/{id}/edit/` | Edit a task |
| `/tasks_list/{id}/delete/` | Delete a task |

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: The request was successful
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error