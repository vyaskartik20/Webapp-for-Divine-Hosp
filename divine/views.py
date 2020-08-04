# from django.shortcuts import render

# # Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from .forms import AppointmentForm
 
 
# def appointment_form_view(request):
#     form = AppointmentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'appointment.html', context)
 
 
def index(request):
    return render(request, "index.html", {})
 
 
def about(request):
    return render(request, "About.html", {})
 
 
def appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, "Appointment.html", context)
 
 
def contact(request):
    return render(request, "Contact.html", {})
 
 
def doctors(request):
    return render(request, "Doctors.html", {})
 
 
def services(request):
    return render(request, "Services.html", {})
 
 
def newsdetail(request):
    return render(request, "news-detail.html", {})

def gallery(request):
    return render(request, "Gallery.html", {})

def developers(request):
    return render(request, "Developers.html", {})