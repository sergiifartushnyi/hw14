from django.shortcuts import render, get_object_or_404
from .models import Trainer, Category, Booking

def all_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer/all_trainers.html', {'trainers': trainers})

def trainers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    trainers = Trainer.objects.filter(category=category)
    return render(request, 'trainer/trainers_by_category.html', {'trainers': trainers, 'category': category})

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'trainer/trainer_detail.html', {'trainer': trainer})

def trainer_schedule(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    schedule = trainer.schedule.all()  # Припускаємо, що у тренера є поле `schedule`
    return render(request, 'trainer/trainer_schedule.html', {'trainer': trainer, 'schedule': schedule})

def book_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == "POST":

        booking = Booking(trainer=trainer, user=request.user)

        booking.save()

        return render(request, 'trainer/booking_success.html', {'trainer': trainer})

        return render(request, 'trainer/book_trainer.html', {'trainer': trainer})
