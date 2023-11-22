from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('about/add_user/', views.CreateTeam.as_view(), name='add_team'),
    path('post/create/', views.CreatePost.as_view(), name='new_post'),
    path('post/draft/', views.DraftPost.as_view(), name='draft'),
    path('post/<slug:slug>', views.DetailPost.as_view(), name='detail'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('post/publish/<int:pk>/', views.publish_post, name='publish'),
    path('post/<slug:slug>/comment', views.post_comment, name='add_comment'),
    path('post/<slug:slug>/comment/<int:pk>/approve/', views.comment_approve, name='approve'),
    path('post/<slug:slug>/comment/<int:pk>/delete/', views.comment_delete, name='delete'),

]