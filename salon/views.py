from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Appointment, Gallery, Service, Team, Contact, Testimonial


def home(request):
    services = Service.objects.all()
    team_members = Team.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    gallery_images = Gallery.objects.all()[:6]

    return render(request, 'home.html', {
        'services': services,
        'team_members': team_members,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
    })


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {
        'services': services
    })


def appointment(request):
    if request.method == "POST":

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        service = request.POST['service']
        date = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        existing_appointment = Appointment.objects.filter(
            date=date,
            time=time
        ).exists()

        if existing_appointment:
            messages.error(
                request,
                "Sorry! This time slot is already booked. Please choose another time."
            )

        else:
            Appointment.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service,
                date=date,
                time=time,
                message=message
            )

            messages.success(
                request,
                "Your appointment has been booked successfully!"
            )

    return render(request, 'appointment.html')


def academy(request):
    return render(request, 'academy.html')


def gallery(request):
    images = Gallery.objects.all()

    return render(request, 'gallery.html', {
        'images': images
    })


def contact(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

    return render(request, 'contact.html')


def team(request):
    team_members = Team.objects.all()

    return render(request, 'team.html', {
        'team_members': team_members
    })


# ==========================================
# OWNER DASHBOARD
# ==========================================

@login_required(login_url='owner_login')
def owner_dashboard(request):

    appointments = Appointment.objects.all().order_by(
        '-date',
        '-time'
    )

    return render(
        request,
        'owner_dashboard.html',
        {
            'appointments': appointments
        }
    )


@login_required(login_url='owner_login')
def update_appointment_status(request, appointment_id, status):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    allowed_statuses = [
        'Pending',
        'Confirmed',
        'Completed',
        'Cancelled'
    ]

    if status in allowed_statuses:
        appointment.status = status
        appointment.save()

    return redirect('owner_dashboard')