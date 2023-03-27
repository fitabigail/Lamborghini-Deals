from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from enquiry_form.models import EnquiryForm


# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']        
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome {username} you are logged in")
            return redirect('dashboard')
        else:
            messages.error(request, ' Invalid login')
            return redirect('login')   
    return render(request, 'accounts/login.html')


def singup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']       
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('singup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('singup')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, f"{username} you are now logged in!")
                    return redirect('dashboard')
                    messages.success(request, 'You succefuly register to LamborghiniDeal!')
                    return redirect('login')    
        
        else:
            messages.error(request, 'Your Password do not match')
            return redirect('singup')
    else:
        return render(request, 'accounts/singup.html')
                    

def dashboard(request): 
    car_inquiry = EnquiryForm.objects.order_by('-created_on').filter(user_id=request.user.id) 

    data = {
        'inqueries': car_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)


def logout(request):
    if request.method == "POST":        
        auth.logout(request)
        messages.success(request, 'You are succefuly log out!')
        return redirect('home')

    return redirect('home')
