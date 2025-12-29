import pytest
import requests

class TestApiHttpMethod:
    
    '''使用类组织测试，提升可读性和可维护性'''
    def setup_class(self):
        self.base_url = "https://jsonplaceholder.typicode.com/"
    
    def test_echo_headers(self):
        '''测试请求头回显'''
        url = f"{self.base_url}/headers"
        headers = { 
            "User-Agent": "TestClient/1.0",
            "Content-Type": "application/json"       
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["headers"]["User-Agent"] == "TestClient/1.0"
        assert json_data["headers"]["Content-Type"] == "application/json"

    def test_create_post(self):
        '''测试创建新帖子'''
        url = f"{self.base_url}/posts"
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "title": "test post",
            "body": "API testing with pytest",
            "userId": 101
        }
        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 201
        json_data = response.json()
        assert json_data["title"] == "test post"
        assert json_data["body"] == "API testing with pytest"
        assert json_data["userId"] == 101

    @pytest.mark.parametrize("id,id_expected", [(1, 1), (2, 2), (3, 3)])
    @pytest.mark.parametrize("method", ["put", "patch"])
    def test_update_post(self, id, id_expected, method):
        '''测试更新帖子'''
        url = f"{self.base_url}/posts/{id}"
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "id": id,
            "title": "updated title",
            "body": "updated body",
            "userId": id
        }
        response = requests.request(method,url, json=payload, headers=headers)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["title"] == "updated title"
        assert json_data["body"] == "updated body"
        assert json_data["userId"] == id_expected
       
    def test_partial_update_post(self):
        '''测试部分更新帖子'''
        url = f"{self.base_url}/posts/1"
        headers = {
            "Content-Type": "application/json",
        }
        payload = { "title" : "partially updated title" }
        response = requests.patch(url, json=payload, headers=headers)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["title"] == "partially updated title"

    def test_delete_post(self):
        '''测试删除帖子'''
        url = f"{self.base_url}/posts/1"
        response = requests.delete(url)
        assert response.status_code == 200