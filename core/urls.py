"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views
from foundation import viewsf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', views.project_list),
    path('project/<int:id>', views.project_detail),
    path('solution/', views.solution_list),
    path('solution/<int:id>', views.solution_detail),
    path('feature/', views.feature_list),
    path('feature/<int:id>', views.feature_detail),
    path('task/', views.task_list),
    path('task/<int:id>', views.task_detail),
    path('status/', viewsf.statuss_list),
    path('stage/',viewsf.stage_list),
    path('task/filter/',views.task_filter),
    path('books/',views.BookListCreate.as_view()),
    path('books/<int:pk>',views.BookDetail.as_view()),
    path('clients/', views.ClientListCreate.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('department/',views.DepartmentListCreate.as_view()),
    path('department/<int:pk>',views.DepartmentDetail.as_view()),
    path('designation/',views.DesignationListCreate.as_view()),
    path('designation/<int:pk>',views.DesignationDetail.as_view()),
    path('user/',views.UserListCreate.as_view()),
    path('user/<int:pk>',views.UserDetail.as_view()),
]
