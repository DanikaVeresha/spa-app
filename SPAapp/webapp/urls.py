from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('postboard', views.postboard, name='postboard'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post', views.delete_post, name='delete_post'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('delete_comment', views.delete_comment, name='delete_comment'),
    path('comments', views.get_comments, name='comments'),
    path('update_user', views.update_user, name='update_user'),
    path('delete_user', views.delete_user, name='delete_user'),
]

