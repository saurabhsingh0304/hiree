from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import UserProfile, CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# from .forms import RegistrationForm, UserAuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.



def register_view(request):
    user = request.user
    if user.is_authenticated:
        print(1)
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        raw_pass = request.POST.get('password')
        company_name = request.POST.get('company_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        user = CustomUser.objects.filter(email=email)
        if user:
            return HttpResponse("User exist")
        else:
            user = CustomUser.objects.create_user(email=email, password=raw_pass)
            user.is_staff = False
            user.is_active = True
            user.save()
            profileinfo = UserProfile(user=user, company_name=company_name, first_name=first_name,
                                      last_name=last_name, phone_number=phone_number)
            profileinfo.save()
            user = authenticate(email=email, password=raw_pass)
            print(user)
            login(request, user)
            print(2)
            return redirect('home')
    else:
        print(4)
        return render(request, 'accounts/registration.html')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.error(request, "Please Correct Below Errors")
    return render(request, "accounts/login.html", context)
    

@login_required(login_url="login")
def home_view(request):
    print(request.user.username)
    x=UserProfile.objects.get(user=request.user)
    print(x)
    # print(help(x))
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("home")
