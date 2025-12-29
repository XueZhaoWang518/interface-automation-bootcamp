# RESTful API 速查

RESTful 以资源为中心、采用标准 HTTP 方法，因此接口更清晰、可以预测。URL 应使用名词（代表资源），而非动词。

## 常见 HTTP 方法与操作

| 方法 | 示例路径 | 描述 |
| --- | --- | --- |
| GET | `/users` | 获取用户列表 |
| POST | `/users` | 创建新用户 |
| GET | `/users/1` | 查询 ID=1 的用户 |
| PUT | `/users/1` | 全量替换用户信息 |
| PATCH | `/users/1` | 局部更新（如只改邮箱） |
| DELETE | `/users/1` | 删除该用户 |

RESTful 风格更直观、更标准，也更适合自动化测试。
