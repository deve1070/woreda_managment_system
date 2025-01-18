from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns=[
    path('logout', LoginView.as_view(next_page='home'), name='logout')
]