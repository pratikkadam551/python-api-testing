import pytest
import requests
from datetime import datetime

class TestGetRequests:
    def test_get_all_posts(self, base_url, session):
        """Test getting all posts"""
        response = session.get(f"{base_url}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        print(isinstance(response.json(), list))
        print(len(response.json()))
        assert len(response.json()) > 0

    def test_get_specific_post(self, base_url, session):
        """Test getting a specific post by ID"""
        post_id = 1
        response = session.get(f"{base_url}/posts/{post_id}")
        assert response.status_code == 200
        assert response.json()["id"] == post_id

    def test_get_nonexistent_post(self, base_url, session):
        """Test getting a non-existent post"""
        response = session.get(f"{base_url}/posts/999")
        assert response.status_code == 404

    def test_get_post_comments(self, base_url, session):
        """Test getting comments for a specific post"""
        post_id = 1
        response = session.get(f"{base_url}/posts/{post_id}/comments")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        data = response.json()
        first_data = data[0]
        print(first_data)
        assert first_data['id'] == 1
        assert first_data['email'] == "Eliseo@gardner.biz"
        assert "accusantium" in first_data["body"]
        assert all("postId" in comment for comment in response.json())
        assert all(comment["postId"]==post_id for comment in response.json())

    def test_get_user_posts(self, base_url, session):
        """Test getting posts by a specific user"""
        user_id = 1
        response = session.get(f"{base_url}/posts?userId={user_id}")
        assert response.status_code == 200
        assert all(post["userId"] == user_id for post in response.json())

    def test_get_all_users(self, base_url, session):
        """Test getting all users"""
        response = session.get(f"{base_url}/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_get_specific_user(self, base_url, session):
        """Test getting a specific user"""
        user_id = 1
        response = session.get(f"{base_url}/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["id"] == user_id

    def test_get_user_todos(self, base_url, session):
        """Test getting todos for a specific user"""
        user_id = 1
        response = session.get(f"{base_url}/users/{user_id}/todos")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert all(todo["userId"] == user_id for todo in response.json())

    def test_get_all_albums(self, base_url, session):
        """Test getting all albums"""
        response = session.get(f"{base_url}/albums")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_get_album_photos(self, base_url, session):
        """Test getting photos for a specific album"""
        album_id = 1
        response = session.get(f"{base_url}/albums/{album_id}/photos")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert all(photo["albumId"] == album_id for photo in response.json())

    def test_get_reqres_users(self, reqres_url, session):
        """Test getting users from ReqRes API"""
        response = session.get(f"{reqres_url}/api/users?page=1")
        assert response.status_code == 200
        first_data = response.json()['data'][0]
        assert first_data['first_name'] == 'George'
        assert "data" in response.json()

    def test_get_reqres_single_user(self, reqres_url, session):
        """Test getting a single user from ReqRes API"""
        user_id = 2
        response = session.get(f"{reqres_url}/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["data"]["id"] == user_id

    def test_get_reqres_user_not_found(self, reqres_url, session):
        """Test getting a non-existent user from ReqRes API"""
        response = session.get(f"{reqres_url}/api/users/23")
        assert response.status_code == 404

    def test_get_reqres_colors(self, reqres_url, session):
        """Test getting colors from ReqRes API"""
        response = session.get(f"{reqres_url}/api/unknown")
        assert response.status_code == 200
        assert "data" in response.json()

    def test_get_reqres_single_color(self, reqres_url, session):
        """Test getting a single color from ReqRes API"""
        color_id = 2
        response = session.get(f"{reqres_url}/api/unknown/{color_id}")
        assert response.status_code == 200
        assert response.json()["data"]["id"] == color_id