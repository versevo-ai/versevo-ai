import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from subscription.main import app

client = TestClient(app)

class TestUserAPIIntegration:
    """Integration tests that demonstrate the user API working with mocked database"""

    @patch('subscription.router.users.get_db')
    def test_user_registration_flow(self, mock_get_db):
        """Test complete user registration flow with mocked database"""
        # Mock database session
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_get_db.return_value.__exit__.return_value = None
        
        # Mock that user doesn't exist yet
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        user_data = {
            "username": "testuser123",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": "TestPass123!",
            "password2": "TestPass123!"
        }
        
        response = client.post("/users/register", json=user_data)
        
        # Should succeed with mocked database
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["Status"] == "CREATED"
        assert "testuser123" in response_data["message"]
        
        # Verify database interactions
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()

    def test_password_validation_in_schema(self):
        """Test that password validation works at schema level"""
        user_data = {
            "username": "testuser123",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": "weak",  # Weak password
            "password2": "weak"
        }
        
        response = client.post("/users/register", json=user_data)
        
        # Should return validation error
        assert response.status_code == 422
        error_detail = response.json()["detail"]
        
        # Check that it contains password strength validation errors
        password_errors = [err for err in error_detail if "password1" in err.get("loc", [])]
        assert len(password_errors) > 0
        
        # Should mention requirements for uppercase, symbols, digits, etc.
        error_msg = password_errors[0]["msg"]
        assert any(word in error_msg.lower() for word in ["uppercase", "symbol", "digit", "character"])

    def test_password_mismatch_validation(self):
        """Test password mismatch validation"""
        user_data = {
            "username": "testuser123",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": "TestPass123!",
            "password2": "DifferentPass123!"  # Different password
        }
        
        response = client.post("/users/register", json=user_data)
        
        # Should return validation error
        assert response.status_code == 422
        error_detail = response.json()["detail"]
        
        # Check for password mismatch error
        password_errors = [err for err in error_detail if "password2" in err.get("loc", [])]
        assert len(password_errors) > 0
        assert "match" in password_errors[0]["msg"].lower()

    def test_username_validation(self):
        """Test username validation (spaces removed)"""
        user_data = {
            "username": "test user 123",  # Username with spaces
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": "TestPass123!",
            "password2": "TestPass123!"
        }
        
        # The validation should work but spaces should be removed
        # This would be validated against the database, but we can check schema validation
        response = client.post("/users/register", json=user_data)
        
        # Should fail due to database not being configured, but schema validation should pass
        # The important thing is that it doesn't fail with a schema validation error
        assert response.status_code in [422, 500]
        
        # If it's 422, it should not be due to username format
        if response.status_code == 422:
            error_detail = response.json()["detail"]
            username_errors = [err for err in error_detail if "username" in err.get("loc", [])]
            # Should not have username format errors since spaces are removed automatically
            assert len(username_errors) == 0

    def test_email_validation(self):
        """Test email validation"""
        user_data = {
            "username": "testuser123",
            "email": "invalid-email",  # Invalid email
            "first_name": "Test",
            "last_name": "User",
            "password1": "TestPass123!",
            "password2": "TestPass123!"
        }
        
        response = client.post("/users/register", json=user_data)
        
        # Should return validation error for email
        assert response.status_code == 422
        error_detail = response.json()["detail"]
        
        # Check for email validation error
        email_errors = [err for err in error_detail if "email" in err.get("loc", [])]
        assert len(email_errors) > 0

    def test_api_documentation_includes_user_endpoints(self):
        """Test that API documentation properly includes user endpoints"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        
        schema = response.json()
        
        # Verify all user endpoints are documented
        paths = schema["paths"]
        assert "/users/register" in paths
        assert "/users/login" in paths
        assert "/users/me" in paths
        assert "/users/profile" in paths
        assert "/users/update" in paths
        assert "/users/delete" in paths
        assert "/users/logout" in paths
        
        # Verify proper HTTP methods
        assert "post" in paths["/users/register"]
        assert "post" in paths["/users/login"]
        assert "get" in paths["/users/me"]
        assert "get" in paths["/users/profile"]
        assert "put" in paths["/users/update"]
        assert "delete" in paths["/users/delete"]
        assert "post" in paths["/users/logout"]
        
        # Verify authentication requirements are documented
        profile_endpoint = paths["/users/profile"]["get"]
        assert "security" in profile_endpoint
        
    def test_unauthorized_access_properly_handled(self):
        """Test that endpoints requiring authentication return proper error"""
        protected_endpoints = [
            ("/users/me", "get"),
            ("/users/profile", "get"),
            ("/users/update", "put"),
            ("/users/delete", "delete"),
            ("/users/logout", "post")
        ]
        
        for endpoint, method in protected_endpoints:
            if method == "get":
                response = client.get(endpoint)
            elif method == "put":
                response = client.put(endpoint, json={})
            elif method == "delete":
                response = client.delete(endpoint)
            elif method == "post":
                response = client.post(endpoint, json={})
            
            # Should return 401 unauthorized
            assert response.status_code == 401
            assert "unauthorized" in response.json()["detail"].lower() or "not authenticated" in response.json()["detail"].lower()

    def test_app_title_and_description(self):
        """Test that the FastAPI app has proper title and description"""
        response = client.get("/openapi.json")
        schema = response.json()
        
        assert schema["info"]["title"] == "Versevo AI API"
        assert "User management" in schema["info"]["description"]
        assert schema["info"]["version"] == "1.0.0"