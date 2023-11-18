from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('post/create/', views.CreatePost.as_view(), name='new_post'),
    path('detail/', views.DetailPost.as_view(), name='detail'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
]