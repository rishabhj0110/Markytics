from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

# User registration based on username, email and password
def userRegister(request):
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            user = form.save()
            login(request, user)
            print("User has been registered !")
            return redirect(reverse('home')) 
        return render(request, 'userApp/register.html', {'form': form})

    elif request.method == 'GET':
        form = forms.NewUserForm()
        return render(request, 'userApp/register.html', {'form': form})

# Home page visible only to logged in users
@login_required
def home(request):
    context = {'user' : request.user}
    return render(request, 'userApp/home.html', context)


def reportIncident(request):
    if request.user.is_authenticated:
        if request.method=='POST' :
            form = forms.IncidentForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print(form.cleaned_data)
                incident = form.save(commit=False)
                incident.user = request.user
                print(incident.user)
                incident.save()
                print("Report object is saved to database")
                return redirect(reverse('home'))
            return render(request, 'userApp/input_form.html', {'form': form})

        elif request.method=='GET':
            form = forms.IncidentForm()
            reportedBy = str(request.user)
            form.fields['reported_by'].widget.attrs['value'] = reportedBy
            return render(request, 'userApp/input_form.html', context={'form': form})
    else:
        return redirect(reverse('login'))

def userLogout(request):
    logout(request)
    return redirect(reverse('landingPage'))
