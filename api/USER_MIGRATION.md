# User Management API Migration Documentation

## Overview
This document outlines the migration of user-specific operations from Django to FastAPI while keeping the Django backend for ML model monitoring and serving.

## Architecture

### FastAPI (User Management)
- **Location**: `/api/subscription/`
- **Responsibilities**: 
  - User registration, authentication, and profile management
  - JWT token management
  - User CRUD operations
  - API documentation and validation

### Django (ML Backend)
- **Location**: `/backend/platform/`
- **Responsibilities**:
  - ML model monitoring and serving
  - Services management (user-purchased models)
  - Model catalog (versemodels)
  - Admin interface for ML operations

## Migrated User Endpoints

### FastAPI User API (`/users/`)

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/users/register` | POST | Register new user | None |
| `/users/login` | POST | User login (returns JWT tokens) | None |
| `/users/me` | GET | Get current user info | JWT Required |
| `/users/profile` | GET | Get user profile (Django-style response) | JWT Required |
| `/users/update` | PUT | Update user information | JWT Required |
| `/users/delete` | DELETE | Delete user account (if blacklisted) | JWT Required |
| `/users/logout` | POST | Logout user (clear tokens) | JWT Required |

### Request/Response Examples

#### User Registration
```bash
POST /users/register
Content-Type: application/json

{
  "username": "newuser",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password1": "SecurePass123!",
  "password2": "SecurePass123!"
}
```

#### User Login
```bash
POST /users/login
Content-Type: application/x-www-form-urlencoded

username=newuser&password=SecurePass123!
```

Response:
```json
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer"
}
```

#### Get User Profile
```bash
GET /users/profile
Authorization: Bearer eyJ...
```

Response:
```json
{
  "Message": "FETCHED",
  "Data": {
    "username": "newuser",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_active": true,
    "is_staff": false,
    "is_superuser": false,
    "date_joined": "2024-01-01T00:00:00",
    "last_login": null,
    "Blacklisted": false
  }
}
```

## Security Features

### Password Validation
- Minimum 8 characters
- Must contain: lowercase, uppercase, symbol, digit
- Matches Django backend validation rules

### JWT Authentication
- Access tokens (30 minutes expiry)
- Refresh tokens (7 days expiry)
- Secure token storage in database

### Database Integration
- Uses same PostgreSQL database as Django
- Maps to existing Django `users_newuser` table
- Preserves all existing user data and relationships

## FastAPI Best Practices Implemented

1. **Dependency Injection**: Database sessions and authentication
2. **Pydantic Validation**: Request/response validation and serialization
3. **Router Separation**: Modular endpoint organization
4. **Error Handling**: Proper HTTP status codes and error responses
5. **Security**: JWT authentication with FastAPI security utilities
6. **Documentation**: Automatic OpenAPI/Swagger documentation
7. **Type Hints**: Full type annotation for better IDE support
8. **Async Support**: Ready for async operations

## Environment Variables Required

```bash
# Database connection (shared with Django)
MAIN_DB=postgresql://user:password@host:port/database

# JWT security
SECRET_KEY=your-secret-key-here

# Optional: Superuser designation
SUPERUSER_EMAIL=admin@example.com

# Optional: Supabase (for waitlist functionality)
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
SUPABASE_TABLE_NAME=waitlist
```

## Running the API

### Development
```bash
cd api
poetry install
poetry run uvicorn subscription.main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI Schema: `http://localhost:8000/openapi.json`

## Testing

```bash
cd api
poetry run pytest tests/test_users.py -v
```

## Migration Benefits

1. **Scalability**: FastAPI's async capabilities for high-performance user operations
2. **Maintainability**: Clear separation of concerns between user management and ML operations
3. **Modern Stack**: Latest Python async frameworks and tooling
4. **API Documentation**: Automatic documentation generation
5. **Type Safety**: Full type checking and validation
6. **Performance**: Better performance for user-facing operations
7. **Flexibility**: Easy to extend with new user features

## Backward Compatibility

- User data remains in same database tables
- Django admin interface still works for user management
- ML model operations continue to work unchanged
- Existing user sessions/tokens are preserved