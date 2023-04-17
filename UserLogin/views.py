
from UserLogin.models import Register
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.

def userLogin(request):
    if request.method=="POST":
        username=request.POST.get('login_username')
        password=request.POST.get('login_password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
    else:
        
        return render(request, 'UserLogin/login.html')


def dashboard(request):
    if request.method=="POST":
        user_count=request.POST.get('user_count')
        u_count=int(user_count)
        context={
            'user_count':user_count,
            'range':range(u_count),
        }
        print(user_count)
        return render(request, 'UserLogin/dashboard.html', context)
    else:
      
        return render(request, 'UserLogin/dashboard.html')
   
def userRegistration(request):
    if request.method=="POST":
            # first_name=request.POST.getlist('first_name')
            # print(first_name)
            last_name=request.POST.getlist('last_name')
            mobile_number=request.POST.getlist('mobile_number')
            email_id=request.POST.getlist('email_id')
            password=request.POST.getlist('password')
            confirm_password=request.POST.getlist('confirm_password')
            
            for f_name in zip(request.POST.getlist('first_name')):
                register=Register()
                register.first_name=f_name
                print(f_name)
                register.save()
    return redirect('dashboard')




