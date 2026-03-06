# Task Management REST API

A RESTful backend service built with Flask to support CRUD operations for task management.

## Tech Stack
Python | Flask | RESTful APIs | Git

## Setup & Installation

### Prerequisites
- Python 3.7+
- Git

### Steps
1. Clone the repo
```bash
   git clone https://github.com/EventHorizon33/Task-Management-Rest-API.git
   cd Task-Management-Rest-API
```
2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies
```bash
   pip install flask
```
4. Run the server
```bash
   python app.py
```
5. Server runs on `http://localhost:5001`

## API Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | /tasks | Fetch all tasks | 200 |
| POST | /tasks | Create a new task | 201 |
| PUT | /tasks/\<id\> | Update a task | 200 |
| DELETE | /tasks/\<id\> | Delete a task | 204 |

## Request & Response Examples

### GET /tasks
```bash
curl http://localhost:5001/tasks
```
Response:
```json
[]
```

### POST /tasks
```bash
curl -X POST http://localhost:5001/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk and eggs"}'
```
Response:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk and eggs",
  "done": false
}
```

### PUT /tasks/1
```bash
curl -X PUT http://localhost:5001/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```
Response:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk and eggs",
  "done": true
}
```

### DELETE /tasks/1
```bash
curl -X DELETE http://localhost:5001/tasks/1
```
Response: 204 No Content

## Project Structure
```
task-api/
├── app.py        # Entry point, app configuration
├── routes.py     # API endpoint definitions
├── models.py     # Task model and in-memory storage
├── README.md
└── .gitignore
```

## Notes
- Tasks are stored in memory and will reset when the server restarts.