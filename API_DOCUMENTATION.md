# REST API Documentation

Your Django Todo App now includes a full REST API. Here's how to use it:

## Base URL
```
http://localhost:8000
```

## API Endpoints

### 1. Get All Todos
- **URL**: `/api/todos/`
- **Method**: `GET`
- **Response**:
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "created_at": "2024-02-21"
  },
  {
    "id": 2,
    "title": "Complete project",
    "created_at": "2024-02-21"
  }
]
```

### 2. Create a New Todo
- **URL**: `/api/todos/`
- **Method**: `POST`
- **Request Body**:
```json
{
  "title": "New task"
}
```
- **Response**: (201 Created)
```json
{
  "id": 3,
  "title": "New task",
  "created_at": "2024-02-21"
}
```

### 3. Get a Specific Todo
- **URL**: `/api/todos/{id}/`
- **Method**: `GET`
- **Example**: `/api/todos/1/`
- **Response**:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "created_at": "2024-02-21"
}
```

### 4. Update a Todo
- **URL**: `/api/todos/{id}/`
- **Method**: `PUT`
- **Example**: `/api/todos/1/`
- **Request Body**:
```json
{
  "title": "Buy groceries and cook dinner"
}
```
- **Response**:
```json
{
  "id": 1,
  "title": "Buy groceries and cook dinner",
  "created_at": "2024-02-21"
}
```

### 5. Delete a Todo
- **URL**: `/api/todos/{id}/`
- **Method**: `DELETE`
- **Example**: `/api/todos/1/`
- **Response**: (204 No Content)

## Alternative ViewSet URLs

You can also use the automatically generated ViewSet URLs:
- `GET /todos/` - List all todos
- `POST /todos/` - Create a todo
- `GET /todos/{id}/` - Get a specific todo
- `PUT /todos/{id}/` - Update a todo
- `PATCH /todos/{id}/` - Partially update a todo
- `DELETE /todos/{id}/` - Delete a todo

## Testing with cURL

### Create a todo
```bash
curl -X POST http://localhost:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn REST API"}'
```

### Get all todos
```bash
curl http://localhost:8000/api/todos/
```

### Get a specific todo
```bash
curl http://localhost:8000/api/todos/1/
```

### Update a todo
```bash
curl -X PUT http://localhost:8000/api/todos/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated task"}'
```

### Delete a todo
```bash
curl -X DELETE http://localhost:8000/api/todos/1/
```

## Testing with Python Requests

```python
import requests

# Get all todos
response = requests.get('http://localhost:8000/api/todos/')
print(response.json())

# Create a new todo
data = {'title': 'New task'}
response = requests.post('http://localhost:8000/api/todos/', json=data)
print(response.json())

# Update a todo
data = {'title': 'Updated task'}
response = requests.put('http://localhost:8000/api/todos/1/', json=data)
print(response.json())

# Delete a todo
response = requests.delete('http://localhost:8000/api/todos/1/')
print(response.status_code)
```

## Template Views (Still Available)

Your original template-based views are still available:
- `GET /` - Home page (view all todos)
- `GET/POST /update/<id>` - Update a todo
- `GET/POST /delete/<id>/` - Delete a todo

## New Features Added

1. **Serializers** (`todo_list/serializers.py`): Converts Todo model instances to/from JSON
2. **API Views** (`todo_list/views.py`): Function-based views for REST API
3. **ViewSet** (`todo_list/views.py`): Class-based view for complete CRUD operations
4. **REST Framework Configuration**: Added to settings.py

## Running the Server

```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations (if needed)
python manage.py migrate

# Start development server
python manage.py runserver

# Server will be available at http://localhost:8000
```

## Next Steps

1. Add authentication for API endpoints (JWT tokens, session auth)
2. Add pagination for large todo lists
3. Add filtering and search capabilities
4. Add API rate limiting
5. Deploy to production (Heroku, AWS, PythonAnywhere, etc.)
