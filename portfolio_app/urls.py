from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
        
    path('admin/', admin.site.urls),
    #connect path to portfolio_app urls
    #path('', include('portfolio_app.urls')),
    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('portfolio/<args>/', views.portfolio, name='portfolio-detail'),

    path('project/<args>/', views.project, name='project-detail'),

    path('portfolio/<args>/new_project/', views.newProject, name='new-project'),

    path('portfolio/<args>/edit_project/<id>', views.editProject, name='edit-project'),

    path('portfolio/<args>/del_project/<id>', views.delProject, name='del-project'),

    path('students/', views.students, name='students'),

    path('students/<args>', views.studentDetail, name='student-detail'),

    path('portfolio/<args>/edit_portfolio', views.editPortfolio, name='edit-portfolio'),
]

