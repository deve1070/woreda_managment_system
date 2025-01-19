from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='residents'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', auth_views.LoginView.as_view(next_page='home'), name='logout'),
    path('register/',views.register,name='register')
]