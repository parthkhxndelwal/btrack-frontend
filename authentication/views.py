from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'authentication/index.html', {'firstname': firstname})
        else:
            messages.error(request, "Username or Password is incorrect")
            return redirect('home')
    return render(request, 'authentication/signin.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname

        messages.success(request, "Your account has been created successfully! ")
        user.save()
        return redirect('signin')
    return render(request, 'authentication/signup.html')
