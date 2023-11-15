from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('blog_detail/', views.DetailPage.as_view(), name='detail'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
]