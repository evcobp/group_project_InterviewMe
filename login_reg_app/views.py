from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):

    return render(request, 'index.html')

def buyer_reg_login(request):

    return render(request, 'buyer_reg_login.html')

def seller_reg_login(request):

    return render(request, 'seller_reg_login.html')

def create_user(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value, extra_tags='register')
        return redirect('/')

    new_user = User.objects.register(request.POST)
    request.session['user_id'] = new_user.id
    return redirect('/')


def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Email/Password", extra_tags='login')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/hcp')
    return redirect('/')
