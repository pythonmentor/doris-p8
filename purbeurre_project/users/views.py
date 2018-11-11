from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ConnectionForm
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend


class UserCreationForm(UserCreationForm):
    """ Adapt django form UserCreation to add a firstname field """
    first_name = forms.CharField(max_length = 50, required = True, label = 'Prénom')
    username = forms.EmailField(required = True, label = 'Email')

    class Meta:
        model = User
        fields = ("first_name", "username", "password1", "password2")

    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user

def create_user(request, first_name = None, username = None, password = None):
    """ Create user account """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(first_name = first_name, username = username, password = password)
            login(request, user)
            return HttpResponseRedirect('/accueil/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class EmailAuthBackend(ModelBackend):
    """ Authenticate user with email instead of username """

    def authenticate(self, username=None, password=None):
        """ Authenticate user with email instead of username """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def connection(request):
    """  Log in the user """
    error = False
    if request.method == "POST":
        form = ConnectionForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnectionForm()

    return render(request, 'connection.html', locals())


def deconnection(request):
    """  Logout the user """
    logout(request)
    return redirect(reverse(connection))


@login_required(login_url='/connection/')
def myaccount(request):
    """  Access the account """
    return render(request, 'my-account.html')
