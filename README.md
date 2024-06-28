# fastapi_tutorial
# FastAPI Tutorial Project

This project is a tutorial for building an API with FastAPI. It includes user management and blog management functionalities.

## Features

- **User Management**: Create and manage users.
- **Blog Management**: Create and manage blog posts.

## Technologies Used

- FastAPI
- SQLAlchemy
- Pydantic

## Setup

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abduvalimurodullayev1/fastapi_tutorial.git
    cd fastapi_tutorial
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### User Endpoints

- **Create User**: `POST /users`
    - Request body: `{"name": "John Doe", "email": "john@example.com", "password": "yourpassword"}`
    - Response: User details

- **Get Users**: `GET /users`
    - Response: List of users

### Blog Endpoints

- **Create Blog**: `POST /blogs`
    - Request body: `{"title": "Blog Title", "body": "Blog Body", "user_id": 1}`
    - Response: Blog details

- **Get Blogs**: `GET /blogs`
    - Response: List of blogs

## Project Structure

- **main.py**: Main application file with FastAPI routes
- **models.py**: SQLAlchemy models for User and Blog
- **schemas.py**: Pydantic schemas for request and response validation
- **database.py**: Database configuration
- **requirements.txt**: List of dependencies

## Running Tests

To run the tests, you need to have `pytest` installed. You can run the tests using the following command:

```bash
pytest
