# Architecture Overview

## Solution Overview

The To-Do Application is a web-based solution built using the Django framework and SQLite database.

The application provides users with the ability to:

- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as completed

The solution follows a layered architecture that separates presentation, business logic, and data access concerns.

---

# High-Level Architecture

```text
+------------------------+
|      Web Browser       |
+-----------+------------+
            |
            v
+------------------------+
|   Django Templates     |
|    Bootstrap UI        |
+-----------+------------+
            |
            v
+------------------------+
|      Django Views      |
+-----------+------------+
            |
            v
+------------------------+
|    Service Layer       |
|    TaskFactory         |
+-----------+------------+
            |
            v
+------------------------+
|      Django ORM        |
+-----------+------------+
            |
            v
+------------------------+
|      SQLite DB         |
+------------------------+
```

---

# Component Description

## 1. Presentation Layer

### Components

- Bootstrap UI
- HTML Templates
- Forms

### Responsibilities

- Render application pages
- Collect user input
- Display task information
- Provide responsive experience

### Files

```text
todo/templates/todo/base.html
todo/templates/todo/index.html
todo/templates/todo/update.html
```

---

## 2. Controller Layer

### Components

- Django Views

### Responsibilities

- Receive requests
- Validate incoming data
- Execute application logic
- Return responses

### Files

```text
todo/views.py
todo/urls.py
```

### Example Flow

```text
User submits task
        |
        v
Index View
        |
        v
TaskFactory
        |
        v
Database
```

---

## 3. Service Layer

### Components

- TaskFactory

### Responsibilities

- Centralize task creation logic
- Apply validation and processing
- Encapsulate object creation

### Files

```text
todo/services/task_factory.py
```

---

# Design Pattern

## Factory Pattern

### Purpose

The Factory Pattern centralizes object creation.

Instead of creating Task objects directly throughout the codebase, all task creation occurs through the TaskFactory class.

### Example

```python
class TaskFactory:

    @staticmethod
    def create_task(title):
        return Task.objects.create(
            title=title.strip()
        )
```

### Benefits

- Improved maintainability
- Reduced code duplication
- Easier testing
- Supports future enhancements

---

# Data Architecture

## Entity Relationship

```text
+-------------------+
|       Task        |
+-------------------+
| id                |
| title             |
| completed         |
| created_at        |
+-------------------+
```

### Task Table

| Field | Type |
|---------|---------|
| id | AutoField |
| title | CharField |
| completed | BooleanField |
| created_at | DateTimeField |

---

# Request Flow

## Create Task

```text
Browser
   |
   v
POST Request
   |
   v
Django View
   |
   v
TaskFactory
   |
   v
ORM
   |
   v
SQLite
```

---

## Update Task

```text
Browser
   |
   v
Update View
   |
   v
Model Validation
   |
   v
Database Update
```

---

## Delete Task

```text
Browser
   |
   v
Delete View
   |
   v
ORM Delete
   |
   v
SQLite
```

---

## Complete Task

```text
Browser
   |
   v
Complete View
   |
   v
Update Status
   |
   v
Database Save
```

---

# Security Architecture

The application relies on several built-in Django security mechanisms.

## Input Validation

Implemented through:

- Django Forms
- Form validation
- Character limits

## SQL Injection Protection

Implemented via Django ORM.

No dynamic SQL statements are executed.

## Cross-Site Scripting Protection

Implemented through Django template auto-escaping.

## Cross-Site Request Forgery Protection

Implemented through:

```html
{% csrf_token %}
```

for all forms.

---

# Logging Strategy

The application is designed to support centralized logging using Django's logging framework.

Potential log events include:

- Application startup
- Task creation
- Task updates
- Task deletion
- Unhandled exceptions
- Security events

---

# Error Handling Approach

The application uses:

```python
get_object_or_404()
```

to safely handle invalid resources.

Benefits:

- Prevents server crashes
- Returns meaningful HTTP responses
- Improves user experience

---

# Deployment Architecture

## Local Development

```text
Developer Machine
        |
        v
Python Runtime
        |
        v
Django Application
        |
        v
SQLite
```

---

## Docker Deployment

```text
Docker Container
        |
        v
Django Application
        |
        v
SQLite Database
```

Containerization provides:

- Environment consistency
- Easier deployment
- Simplified onboarding
- Reproducible builds

---

# Future Enhancements

Potential improvements include:

- User authentication
- Multi-user support
- PostgreSQL database
- REST API endpoints
- Task priorities
- Due dates
- Search and filtering
- CI/CD pipeline
- Cloud deployment
- Monitoring and observability

---

# Design Decisions and Trade-Offs

## SQLite

Selected because:

- Lightweight
- Easy setup
- Suitable for assessment scope

Trade-off:

- Less scalable than PostgreSQL

---

## Django

Selected because:

- Mature framework
- Strong security defaults
- Built-in ORM
- Rapid development

Trade-off:

- More framework overhead than lightweight alternatives

---

## Docker

Selected because:

- Reproducible environments
- Consistent execution across systems
- Simplified deployment process

Trade-off:

- Additional configuration complexity