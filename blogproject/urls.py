"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
import blog.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name='index'),
    path('blog/', blog.views.home, name='home'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),
    path('mypage/',blog.views.mypage, name='mypage'),
    path('mypage2/',blog.views.mypage2, name='mypage2'),
    path('accounts/signup/nono/',blog.views.nono, name='nono'),
    path('nono/',blog.views.nono, name='nono'),
<<<<<<< HEAD
    path('blog/inform/nono/',blog.views.nono, name='nono'),
=======
>>>>>>> ef4964117f88841f51b978ea61574413e983e81f
    path('accounts/', include('accounts.urls')),
    path('blog/search', blog.views.search, name='search'),
    path('blog/inform/', blog.views.inform, name='inform'),
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),
<<<<<<< HEAD
    path('accounts/', include('allauth.urls')),
    path('blog/update/<int:pk>',blog.views.update, name= 'update'),
    path('blog/delete/<int:pk>',blog.views.delete, name= 'delete'),
=======
    path('blog/<int:blog_id>/remove/', blog.views.remove, name= 'remove'),
    path('blog/<int:blog_id>/edit/', blog.views.edit, name= 'edit'),
    path('accounts/', include('allauth.urls')),
>>>>>>> ef4964117f88841f51b978ea61574413e983e81f
]
