import pytest
import requests
from datetime import datetime

class TestPostRequests:
    def test_create_new_post(self, base_url, session, test_data):
        """Test creating a new post"""
        response = session.post(f"{base_url}/posts", json=test_data)
        assert response.status_code == 201
        assert response.json()["title"] == test_data["title"]
        assert response.json()["body"] == test_data["body"]
        assert response.json()["userId"] == test_data["userId"]

    def test_create_post_without_title(self, base_url, session):
        """Test creating a post without title"""
        data = {"body": "Test Body", "userId": 1}
        response = session.post(f"{base_url}/posts", json=data)
        assert response.status_code == 201

    def test_create_post_without_body(self, base_url, session):
        """Test creating a post without body"""
        data = {"title": "Test Title", "userId": 1}
        response = session.post(f"{base_url}/posts", json=data)
        assert response.status_code == 201

    def test_create_post_with_invalid_user_id(self, base_url, session):
        """Test creating a post with invalid user ID"""
        data = {"title": "Test Title", "body": "Test Body", "userId": 999}
        response = session.post(f"{base_url}/posts", json=data)
        assert response.status_code == 201

    def test_create_post_with_empty_data(self, base_url, session):
        """Test creating a post with empty data"""
        response = session.post(f"{base_url}/posts", json={})
        assert response.status_code == 201

    def test_create_new_user(self, base_url, session):
        """Test creating a new user"""
        user_data = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
        response = session.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 201
        assert response.json()["name"] == user_data["name"]
        assert response.json()["username"] == user_data["username"]
        assert response.json()["email"] == user_data["email"]

    def test_create_new_comment(self, base_url, session):
        """Test creating a new comment"""
        comment_data = {
            "postId": 1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a test comment"
        }
        response = session.post(f"{base_url}/comments", json=comment_data)
        assert response.status_code == 201
        assert response.json()["postId"] == comment_data["postId"]
        assert response.json()["name"] == comment_data["name"]

    def test_create_new_album(self, base_url, session):
        """Test creating a new album"""
        album_data = {
            "userId": 1,
            "title": "Test Album"
        }
        response = session.post(f"{base_url}/albums", json=album_data)
        assert response.status_code == 201
        assert response.json()["userId"] == album_data["userId"]
        assert response.json()["title"] == album_data["title"]

    def test_create_new_photo(self, base_url, session):
        """Test creating a new photo"""
        photo_data = {
            "albumId": 1,
            "title": "Test Photo",
            "url": "https://example.com/photo.jpg",
            "thumbnailUrl": "https://example.com/thumbnail.jpg"
        }
        response = session.post(f"{base_url}/photos", json=photo_data)
        assert response.status_code == 201
        assert response.json()["albumId"] == photo_data["albumId"]
        assert response.json()["title"] == photo_data["title"]

    def test_create_new_todo(self, base_url, session):
        """Test creating a new todo"""
        todo_data = {
            "userId": 1,
            "title": "Test Todo",
            "completed": False
        }
        response = session.post(f"{base_url}/todos", json=todo_data)
        assert response.status_code == 201
        assert response.json()["userId"] == todo_data["userId"]
        assert response.json()["title"] == todo_data["title"]
        assert response.json()["completed"] == todo_data["completed"]

    @pytest.mark.xfail
    def test_create_reqres_user(self, reqres_url, session, user_data):
        """Test creating a new user in ReqRes API"""
        response = session.post(f"{reqres_url}/api/users", json=user_data)
        assert response.status_code == 201
        assert response.json()["name"] == user_data["name"]

    @pytest.mark.xfail
    def test_create_reqres_user_without_name(self, reqres_url, session):
        """Test creating a user without name in ReqRes API"""
        data = {"job": "Test Engineer"}
        response = session.post(f"{reqres_url}/api/users", json=data)
        assert response.status_code == 201

    @pytest.mark.xfail
    def test_create_reqres_user_without_job(self, reqres_url, session):
        """Test creating a user without job in ReqRes API"""
        data = {"name": "Test User"}
        response = session.post(f"{reqres_url}/api/users", json=data)
        assert response.status_code == 201

    @pytest.mark.xfail
    def test_create_reqres_user_with_empty_data(self, reqres_url, session):
        """Test creating a user with empty data in ReqRes API"""
        response = session.post(f"{reqres_url}/api/users", json={})
        assert response.status_code == 201

    @pytest.mark.xfail
    def test_create_reqres_register(self, reqres_url, session):
        """Test user registration in ReqRes API"""
        register_data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = session.post(f"{reqres_url}/api/register", json=register_data)
        assert response.status_code == 200
        assert "token" in response.json() 