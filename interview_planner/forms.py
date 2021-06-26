from django import forms
from .utils import populate_user
from .models import Interview

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class InterviewForm(forms.ModelForm):    
    class Meta:
        model = Interview
        fields = fields = '__all__'
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }
    