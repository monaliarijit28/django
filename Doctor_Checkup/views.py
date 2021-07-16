from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from django.models import Member
# Create your views here.

def index_redirect(request):
    return redirect('/home/')

def index(request):
    # if request.method == 'POST':
    #     member = Member(username=request.POST&#91;'username'], password=request.POST&#91;'password'],  firstname=request.POST&#91;'firstname'], lastname=request.POST&#91;'lastname'])
    #     member.save()
    #     return redirect('/home/')
    # else :
    return render(request, 'Doctor_Checkup/index.html', context={"user": "monali"})
 
def login(request, user):
    return render(request, 'Admin_Registration/login.html')

def home(requests):
    return HTTPresponse('hi welcome to home page')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'Doctor_Checkup/index.html')
    context['form']=form
    return render(request,'Admin_Registration/signup.html',context)