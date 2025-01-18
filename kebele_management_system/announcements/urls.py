from django import path

urlpattern=[
    path('', 'view.post_list',name='posts' ),
    path('create/','views.post', name='create'),
    path('<int:post_id>/update', 'views.update', name='update'),
    path('<int:post_id>/delete',  'views.delete', name='delete'),
    
]