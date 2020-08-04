from django import forms

from .models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        widgets = {'Date': DateInput()}
        fields = "__all__"
