from django.urls import path
from . import views

urlpatterns = [
    path("<int:booking_id>/", views.booking_detail, name="booking_detail"),
    path("<int:booking_id>/cancel/", views.cancel_booking, name="cancel_booking"),
    path("<int:booking_id>/confirm/", views.confirm_booking, name="confirm_booking"),
]
