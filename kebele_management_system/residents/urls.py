from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name='residents'
urlpatterns=[
    path('logout', LoginView.as_view(next_page='home'), name='logout'),
    path('register/',views.register,name='register')
]