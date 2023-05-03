from django.urls import path
from .views import register_view, update_view, login_view, logout_view

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name="register"),
    path('profil/', update_view, name="profil"),
]
