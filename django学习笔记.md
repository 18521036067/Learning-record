# Django学习笔记

[详细官方文档传送门](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

## 1.配置项目

### 1.1创建项目

cd到项目目标目录

`$ django-admin startproject helloworld`

### 1.2自带的开发服务器

`$ python manage.py runserver`

也可以直接传入地址和端口参数

`$ python manage.py runserver 1.2.3.4:8000`

也可以修改自定义地址和端口

`$ django-admin runserver 1.2.3.4:7000`

### 1.3创建app

cd到manage.py的目录下

`$ python manage.py startapp newApp`

### 1.4修改工程结构

如果要修改工程结构，例如将myapp放入apps目录下，需要修改两处

> a.setting.py的app列表要改为apps.myapp
> 
> b.项目urls.py中的include('apps.myapp.urls')

### 1.5静态路径

[参考1](https://blog.csdn.net/liuyh73/article/details/78373979)

[参考2](https://blog.csdn.net/xujin0/article/details/83421626)
