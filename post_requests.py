import requests

url = "https://httpbin.org/post"  # 接受 POST 请求并回显数据

payload = {
    "name": "张三",
    "job": "测试开发"
}

headers = {
    "User-Agent": "TestClient/1.0"
}

response = requests.post(url, json=payload, headers=headers)
json_data = response.json()

print("状态码:", response.status_code)
print("回显的数据:", json_data["json"])
