from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.available_cars, name="cars"),
    path("client_rentals/", views.client_rentals, name='client_rentals'),
    path("car_details/<int:car_id>/", views.car_details, name='car_details'),
    path('rent_car/<int:car_id>/', views.rent_car, name='rent_car'),

]