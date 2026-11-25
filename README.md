# Nova Scotia To-Do Application

## Overview

This project is a responsive web-based To-Do application developed using the Django framework.

The application allows users to:

- Create new to-do items
- View existing to-do items
- Edit tasks
- Delete tasks
- Mark tasks as completed

The solution was developed with maintainability, security, accessibility, and production-readiness in mind.

---

## Technology Stack

### Frontend

- HTML5
- Bootstrap 5
- Django Templates

### Backend

- Python 3.12
- Django 5

### Database

- SQLite

### Containerization

- Docker
- Docker Compose

### Testing

- Django Test Framework

---

## Features

### To-Do Management

- Create tasks
- View tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed

### Responsive Design

The application is designed to work across:

- Desktop devices
- Tablets
- Mobile phones

Bootstrap responsive components are used to provide:

- Responsive layouts
- Touch-friendly controls
- Readable typography
- Mobile navigation support

---

## Application Architecture

```text
Browser
   |
   v
Django Views
   |
   v
Service Layer (Factory Pattern)
   |
   v
Django ORM
   |
   v
SQLite Database
```

### Architectural Components

#### Presentation Layer

Responsible for rendering HTML pages and handling user interaction.

#### Application Layer

Django views process requests and coordinate business logic.

#### Service Layer

Implements the Factory Pattern to centralize task creation.

#### Data Layer

SQLite database accessed through Django ORM.

---

## Design Pattern

### Factory Pattern

The Factory Pattern is implemented through the `TaskFactory` class.

### Why It Was Selected

Centralizing task creation logic:

- Reduces duplication
- Improves maintainability
- Simplifies testing
- Supports future extension

### Implementation

```python
class TaskFactory:

    @staticmethod
    def create_task(title):
        return Task.objects.create(
            title=title.strip()
        )
```

### Benefits

- Separation of concerns
- Reusable object creation logic
- Easier future enhancements
- Better code organization

---

## Security Considerations

Several secure development practices have been implemented.

### Input Validation

- Task title length restrictions
- Required form fields
- Server-side validation

### SQL Injection Protection

The application uses Django ORM exclusively.

Example:

```python
Task.objects.filter(title=title)
```

The ORM automatically parameterizes queries to help prevent SQL injection attacks.

### Cross-Site Scripting (XSS) Protection

Django templates automatically escape user-provided content.

Example:

```html
{{ task.title }}
```

### CSRF Protection

All forms contain CSRF tokens:

```html
{% csrf_token %}
```

### User Data Handling

- Input sanitized before storage
- No direct SQL execution
- Validation performed before saving

---

## Logging

Application logging can be configured through Django's logging framework.

Potential production logs include:

- Application events
- Errors and exceptions
- Security-related events

---

## Running Locally

### Prerequisites

- Python 3.12+
- Docker Desktop (optional)

---

### Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the application:

```bash
python manage.py runserver
```

Application URL:

```text
http://localhost:8000
```

---

## Running with Docker

Build container:

```bash
docker compose build
```

Run application:

```bash
docker compose up
```

Application URL:

```text
http://localhost:8000
```

---

## Running Tests

Execute all tests:

```bash
python manage.py test
```

Example output:

```text
Ran 8 tests

OK
```

---

## Test Coverage

Automated tests cover:

- Create task
- Update task
- Delete task
- Complete task

Tests include:

- Happy path scenarios
- Core workflow validation
- Basic error handling validation

---

## Future Improvements

Potential enhancements include:

- User authentication
- User-specific task lists
- Task priorities
- Due dates
- Task categories
- Search and filtering
- REST API endpoints
- PostgreSQL support
- CI/CD pipeline
- Cloud deployment

---

## Production Readiness Considerations

The following production-oriented practices were considered:

- Responsive design
- Docker containerization
- Environment-based configuration
- Input validation
- Security controls
- Unit testing
- Layered architecture

---

## Author

Submitted as part of a technical assessment demonstrating:

- Software design
- Secure development practices
- Automated testing
- Docker containerization
- Responsive web application development