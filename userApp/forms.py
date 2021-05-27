from django import forms
from .models import ReportForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class IncidentForm(forms.ModelForm):
    
    LOCATION_CHOICE = (('CH', 'Corporate Headoffice'), ('OD', 'Operations Department'), ('WS', 'Work Station'), ('MD', 'Marketing Division'))
    SEVERITY_CHOICE = ((1, 'Mild'), (2, 'Moderate'), (3, 'Severe'))
    SUB_INCIDENT_CHOICES = ((1, 'Environmental incident'), (2, 'Injury/Illness'), (3, 'Property Damage'), (4, 'Vehicle'))
    
    location = forms.ChoiceField(choices=LOCATION_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    severity = forms.ChoiceField(choices=SEVERITY_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    # subIncidents = forms.MultipleChoiceField(choices=SUB_INCIDENT_CHOICES, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = ReportForm
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'description' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value' : '2018-05-13'}),
            'time' : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'value' : '22:33:00'}),
            'location_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cause' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'actions' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'reported_by': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'value': ''})
        }


class  NewUserForm(UserCreationForm):
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
