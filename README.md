# django_note

## 基本操作

- 创建项目：`django-admin startproject django_note`

- 运行开发服务器：`python manage.py runserver [0:8000]`

- 创建应用：`python manage.py startapp app01`

- 初始化数据库（测试连接）：`python manage.py migrate`

- 为 model 生成迁移文件（app01）：`python manage.py makemigrations app01`

- 查看迁移的 sql 语句：`python manage.py sqlmigrate app01 0001`

- 应用数据库迁移：``
