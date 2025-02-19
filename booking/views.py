from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from trainer.models import Trainer

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "booking/booking_detail.html", {"booking": booking})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Cancelled'
    booking.save()
    return redirect("booking:booking_list")

def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Confirmed'
    booking.save()
    return redirect("booking:booking_list")

def book_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == "POST":
            pass
    return render(request, 'booking/book_trainer.html', {'trainer': trainer})
