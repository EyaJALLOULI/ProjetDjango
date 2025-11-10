from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('AllUsers/', views.UsersListView.as_view(), name='AllUsers'),
    path('register/', views.register, name='register'),
    path("login/",LoginView.as_view(template_name="User/login.html"),name="login"),

    
    path("logout/", views.logout_view , name="logout"),

]
