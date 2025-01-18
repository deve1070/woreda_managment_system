from django import path
from . import views

urlpattern=[
    path('',views.index,name='index'),
    path('birth', views.applyBirth,name='birth'),
    path('mirrage', views.applyMirrage, name='mirrage'),
    path('issueId' , views.issueId, name='issueId'),
    path('supportive', views.supportivePaper, name='supportivepaper'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),


]