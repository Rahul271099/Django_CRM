from django import forms
from .models import appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['doct_name','schedule_date','Schedule_time']

    schedule_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Schedule_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}),input_formats = ['%H:%M',])
    def __str__(self):
        return self.enterd_by
