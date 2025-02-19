from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_page, name="user_page"),
    path("<int:user_id>/", views.specific_user, name="specific_user"),
    path("dashboard/", views.user_dashboard, name="user_dashboard"),
    path("<int:user_id>/profile/", views.user_profile, name="user_profile"),
]
