# DeadlineOS — Project Plan

## Problem

Students can struggle to organise assignments, remember deadlines, and track work before submission.

## Initial Features

1. Create and manage assignments.
2. Store due dates and assignment status.
3. Organise assignments into subtasks.
4. Display upcoming and overdue deadlines.

## Architecture

- React + Vite frontend
- FastAPI backend
- SQLite database
- pytest backend tests

## Future Features

- Reminders
- Docker and CI/CD
- Optional AI document extraction with user confirmation

## Initial Data Entities

- Assignment
- Subtask

## Development Principle

Build a working, tested core application before adding optional AI features.

## Initial Database Design

### Assignments

- `id`: Integer primary key
- `title`: Required text
- `description`: Optional text
- `due_date`: Date and time
- `status`: Pending, in progress, or completed
- `created_at`: Creation timestamp

### Subtasks

- `id`: Integer primary key
- `assignment_id`: Foreign key referencing Assignments
- `title`: Required text
- `is_completed`: Boolean

### Relationship

One assignment can contain multiple subtasks. Each subtask belongs to one assignment.

### Design Decision

Use SQLite for the initial version because it is simple to run locally and does not require a separate database server.
