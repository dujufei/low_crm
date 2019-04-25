"""low_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # show all
    path('show/', views.show),


    # 登录-注册-注销
    path('login/', views.login),
    path('reg/', views.reg),
    path('logout/', views.logout),


    # 书籍的增删改查
    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('edit_book/', views.edit_book),
    path('del_book/', views.del_book),


    # 作者的增删改查
    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('del_author/', views.del_author),
    path('edit_author/', views.edit_author),


    # 出版社的增删改查
    path('publish_list/', views.publish_list),
    path('add_publish/', views.add_publish),
    path('edit_publish/', views.edit_publish),
    path('del_publish/', views.del_publish),
]
