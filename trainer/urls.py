from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>/', views.trainers_by_category, name='trainers_by_category'),
    path('<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
    path('<int:trainer_id>/schedule/', views.trainer_schedule, name='trainer_schedule'),
    path('<int:trainer_id>/booking/', views.book_trainer, name='book_trainer'),
    path('', views.all_trainers, name='all_trainers'),
]
