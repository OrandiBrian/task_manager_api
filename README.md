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
- **PostgreSQL / SQLite** (Configurable Database)
- **Django Filters** (for task filtering & sorting)
- **JWT / Token Authentication**

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```