from django.urls import path
from . import views

urlpatterns = [
    path('post/new', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post_draft_list/', views.post_draft, name='post_draft'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path ('accounts/login/', views.login , name='login'),
    path('accounts/logout', views.partida, name='logout'),
    path('comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('approve/<int:pk>/', views.comment_approve, name='comment_approve'),
    path('remove/<int:pk>/', views.comment_remove, name='comment_remove'),
    #path('accounts/login/', views.LoginView.as_view(), name='login'),
    #path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]