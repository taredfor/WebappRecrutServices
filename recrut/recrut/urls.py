"""
URL configuration for recrut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('recrut/', include('my_app.urls')),
    path('recrut/', include('my_app.urls')),
    path('', views.index),
    path('user/', views.recrut_f),
    #path('test/', views.test_f),
    path('test/<int:person_id>', views.get_question),
    path('validate/<int:person_id>', views.recrut_f),
    path('test123/', views.test_f),
    path('add_user/<str:person_name>', views.return_list),
    path('all_user_list/', views.all_users_list)
]
