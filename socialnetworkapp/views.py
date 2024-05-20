from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'Register.html')

def login(request):
    return render(request,'login.html')

def edit_profile(request):
    return render(request,'edit_profile.html')

def view_profile(request):
    return render(request,'view profile.html')

def change_password(request):
    return render(request,'change password.html')

def logout(request):
    return render(request,'logout.html')
