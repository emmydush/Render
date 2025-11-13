# Python PostgreSQL Web App

A simple Python web application using Flask with PostgreSQL database integration, ready for deployment on Render.

## Features

- RESTful API endpoints
- PostgreSQL database integration
- Health check endpoint
- User management (CRUD operations)
- Ready for Render deployment

## Local Setup

## Option 1: Automatic Setup (Recommended)

Run the setup script:
```
python setup.py
```

## Option 2: Manual Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL database:
   - Install PostgreSQL
   - Create a database named `myapp`
   - Update `.env` file with your database credentials if needed

3. Run the application:
   ```
   python app.py
   ```

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /users` - Get all users
- `POST /users` - Create a new user

## Deployment to Render

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your repository
4. Configure environment variables:
   - `DB_HOST` - Your PostgreSQL host
   - `DB_NAME` - Your database name
   - `DB_USER` - Your database user
   - `DB_PASSWORD` - Your database password
   - `DB_PORT` - Your database port (usually 5432)
5. Set the build command: `pip install -r requirements.txt`
6. Set the start command: `gunicorn app:app`

## Environment Variables

For local development, copy `.env.example` to `.env` and update the values as needed.

For Render deployment, set the following environment variables in your Render dashboard:

| Variable | Description | Example |
|----------|-------------|---------|
| DB_HOST | Database host | your-db-host.com |
| DB_NAME | Database name | myapp |
| DB_USER | Database user | postgres |
| DB_PASSWORD | Database password | Jesuslove@12 |
| DB_PORT | Database port | 5432 |

## Database Schema

The application automatically creates a `users` table with the following schema:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```