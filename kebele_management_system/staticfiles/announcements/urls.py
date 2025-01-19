from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='announcements'
urlpatterns=[
    path('', views.post_list,name='posts' ),
    path('create/',views.post, name='create'),
    path('<int:post_id>/update', views.updatePost, name='update'),
    path('<int:post_id>/delete',  views.deletePost, name='delete'),
    path('contactUs',  views.contactUs, name='contact'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)