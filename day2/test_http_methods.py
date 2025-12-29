import requests


base_url = "https://httpbin.org"
#创建user测试
post_url = f"{base_url}/post"  # 接受 POST 请求并回显数据


post_payload = {
    "name": "张三",
    "job": "测试开发"
}
response_post = requests.post(post_url, json=post_payload)
user_id = response_post.json().get("id")
print("用户编号:", user_id)

get_url = f"{base_url}/get/{user_id}"    # 接受 GET 请求并回显数据
response_get = requests.get(get_url)
get_user_id = response_get.json().get("args").get("user_id")
assert(get_user_id == user_id)
print("获取的用户编号:", get_user_id)

put_url = f"{base_url}/put/{user_id}"  # 接受 PUT 请求并回显数据
put_payload = {
    "name": "李四",
    "job": "测试经理"
}
response_put = requests.put(put_url, json=put_payload)
updated_name = response_put.json().get("name")
assert(updated_name == "李四")
print("更新后的姓名:", updated_name)

delete_url = f"{base_url}/delete/{user_id}"  # 接受 DELETE 请求并回显数据
response_delete = requests.delete(delete_url)
status_code = response_delete.status_code
assert(status_code == 200)
print("删除用户状态码:", status_code)