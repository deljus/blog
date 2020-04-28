from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostsView.as_view(), name='all'),
    path('single/<int:id>', views.single_post, name='single_post'),
    path('create', views.create_post, name='create_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('user', views.user_post_list, name='user_posts'),
]
