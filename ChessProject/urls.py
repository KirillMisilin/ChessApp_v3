from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ChessApp.urls')),
    path('register/', include('ChessApp.urls')),
    path('play', include('ChessApp.urls')),
    path('login', include('ChessApp.urls')),
    path('exit', include('ChessApp.urls')),
    path('profile', include('ChessApp.urls'))
]
