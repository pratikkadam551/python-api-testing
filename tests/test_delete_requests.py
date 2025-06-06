import pytest
import requests
from datetime import datetime

class TestDeleteRequests:
    def test_delete_post(self, base_url, session):
        """Test deleting a post"""
        response = session.delete(f"{base_url}/posts/1")
        assert response.status_code == 200

    def test_delete_nonexistent_post(self, base_url, session):
        """Test deleting a non-existent post"""
        response = session.delete(f"{base_url}/posts/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_user(self, base_url, session):
        """Test deleting a user"""
        response = session.delete(f"{base_url}/users/1")
        assert response.status_code == 200

    def test_delete_nonexistent_user(self, base_url, session):
        """Test deleting a non-existent user"""
        response = session.delete(f"{base_url}/users/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_comment(self, base_url, session):
        """Test deleting a comment"""
        response = session.delete(f"{base_url}/comments/1")
        assert response.status_code == 200

    def test_delete_nonexistent_comment(self, base_url, session):
        """Test deleting a non-existent comment"""
        response = session.delete(f"{base_url}/comments/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_album(self, base_url, session):
        """Test deleting an album"""
        response = session.delete(f"{base_url}/albums/1")
        assert response.status_code == 200

    def test_delete_nonexistent_album(self, base_url, session):
        """Test deleting a non-existent album"""
        response = session.delete(f"{base_url}/albums/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_photo(self, base_url, session):
        """Test deleting a photo"""
        response = session.delete(f"{base_url}/photos/1")
        assert response.status_code == 200

    def test_delete_nonexistent_photo(self, base_url, session):
        """Test deleting a non-existent photo"""
        response = session.delete(f"{base_url}/photos/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_todo(self, base_url, session):
        """Test deleting a todo"""
        response = session.delete(f"{base_url}/todos/1")
        assert response.status_code == 200

    def test_delete_nonexistent_todo(self, base_url, session):
        """Test deleting a non-existent todo"""
        response = session.delete(f"{base_url}/todos/999")
        assert response.status_code == 200  # JSONPlaceholder returns 200 for non-existent resources

    def test_delete_reqres_user(self, reqres_url, session):
        """Test deleting a user in ReqRes API"""
        user_id = 2
        response = session.delete(f"{reqres_url}/api/users/{user_id}")
        assert response.status_code == 204

    def test_delete_nonexistent_reqres_user(self, reqres_url, session):
        """Test deleting a non-existent user in ReqRes API"""
        response = session.delete(f"{reqres_url}/api/users/999")
        assert response.status_code == 404

    def test_delete_reqres_resource(self, reqres_url, session):
        """Test deleting a resource in ReqRes API"""
        resource_id = 2
        response = session.delete(f"{reqres_url}/api/unknown/{resource_id}")
        assert response.status_code == 204 