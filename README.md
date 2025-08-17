# django学习笔记

## Django常用命令

数据库迁移

`python manage.py migrate`

启动服务

`python manage.py runserver`

## 使用WatchmanReloader

这个有很多坑，网上的资料都说的不清楚

django4.2是支持watchman的但是不支持watchdog，要想使用watchman得需要安装对应服务跟python包

`sudo apt install watchman`

```
watchman --version
4.9.0
```

`pip install pywatchman==3.0.0`

```
pip list | grep watchman
pywatchman        3.0.0
```

这样就有Watchman了

```
Watching for file changes with WatchmanReloader
Performing system checks...

System check identified no issues (0 silenced).
August 17, 2025 - 03:15:41
Django version 4.2.23, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```