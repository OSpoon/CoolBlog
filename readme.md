#### 1 start server 
    
    python3 manage.py runserver

#### 2 create app 
 
    python3 manage.py startapp home

#### 3 register app 

    settings.py=>
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'home',#注册home目录
        ]

#### 4 design model 

    app=>models.py=>
        class Category(models.Model):
            #分类名称
            name = models.CharField(max_length=50,verbose_name="分类名称")

#### 5 creat db 

    python3 manage.py makemigrations
    python3 manage.py migrate

#### 6 创建管理用户 
    
    python3 manage.py createsuperuser

#### 目录说明：

    migrations文件夹用来存放对数据库的改动
    admin.py是用来向Django后台注册应用，并可以自定义在管理后台的显示和过滤方式
    models.py是用来描述应用的数据库模型，Django会通过ORM的方式将模型映射成数据库的真实改动。
    views用来定义视图处理方式，对于不同的url请求，我们该如何处理。