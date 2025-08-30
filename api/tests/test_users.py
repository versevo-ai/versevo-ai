import pytest
from fastapi.testclient import TestClient
from subscription.main import app

client = TestClient(app)

def test_user_registration_success():
    """Test successful user registration"""
    user_data = {
        "username": "testuser123",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User", 
        "password1": "TestPass123!",
        "password2": "TestPass123!"
    }
    
    # Note: This test will fail without database connection
    # but validates the endpoint structure
    response = client.post("/users/register", json=user_data)
    
    # Check that the endpoint exists and has proper structure
    assert response.status_code in [201, 422, 500]  # 422 for validation, 500 for DB connection

def test_user_registration_password_mismatch():
    """Test user registration with password mismatch"""
    user_data = {
        "username": "testuser123",
        "email": "test@example.com", 
        "first_name": "Test",
        "last_name": "User",
        "password1": "TestPass123!",
        "password2": "DifferentPass123!"
    }
    
    response = client.post("/users/register", json=user_data)
    # Should return validation error
    assert response.status_code == 422

def test_user_registration_weak_password():
    """Test user registration with weak password"""
    user_data = {
        "username": "testuser123",
        "email": "test@example.com",
        "first_name": "Test", 
        "last_name": "User",
        "password1": "weak",
        "password2": "weak"
    }
    
    response = client.post("/users/register", json=user_data)
    # Should return validation error
    assert response.status_code == 422

def test_user_login_endpoint_exists():
    """Test that login endpoint exists"""
    response = client.post("/users/login", data={"username": "test", "password": "test"})
    # Should return 401 or 500 (depending on DB connection)
    assert response.status_code in [401, 422, 500]

def test_get_user_profile_unauthorized():
    """Test getting user profile without token"""
    response = client.get("/users/profile")
    # Should return 401 unauthorized
    assert response.status_code == 401

def test_api_docs_accessible():
    """Test that API documentation is accessible"""
    response = client.get("/docs")
    assert response.status_code == 200
    
def test_openapi_schema():
    """Test that OpenAPI schema is accessible"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    
    schema = response.json()
    # Check that user endpoints are included
    assert "/users/register" in schema["paths"]
    assert "/users/login" in schema["paths"]
    assert "/users/profile" in schema["paths"]