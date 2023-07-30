from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('register/', views.register),
    path('play', views.index_page),
    path('login', views.auth),
    path('exit', views.logout_view),
    path('profile', views.profile)
]
