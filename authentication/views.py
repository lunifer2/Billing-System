from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login, logout

from system.models import CustomUser

# Create your views here.\


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You're logged out!!")
        return redirect('login')


class LoginVew(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Admin login success')
                return redirect('index-buyer')
            elif user.role == "Buyer":
                login(request, user)
                messages.success(request, 'Buyer login success')
                return redirect('index-buyer')
            else:
                login(request, user)
                messages.success(request, 'Customer Login success')
                return redirect('index-seller')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        try:
            user = User.objects.get(username=username)
            if user:
                messages.error(
                    request, 'Username already exist. Try with new one!')
                return redirect('register')
        except:
            CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                address=address,
                contact=contact,
                gender=gender,
                role=role
            )
            messages.success(request, 'Account created successfully')
            
        return render(request, 'authentication/register.html')

  
# To create Super User
def create_admin_user(request):
    # Check if the request method is POST
    if not request.user.is_superuser:
        messages.warning(request,"Forbidden Request")
        return render(request, 'authentication/admin/adminregisterform.html')
    else:
        if request.method == 'POST':
            # Get the form data from the request POST data
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            gender = request.POST.get('gender')

            # Create a new admin user using UserManager's create_superuser method
            CustomUser.objects.create_superuser(
                username=username,
                password=password,
                email=email,
                address=address,
                contact=contact,
                gender=gender
            )

            # Return a success response
            return HttpResponse('Admin user created successfully!')
        else:
            # Render the form template
            return render(request, 'authentication/admin/adminregisterform.html')
