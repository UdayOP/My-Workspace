from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request, 'Login.html')


def submit(request):
    messages=str
    username = request.POST['username']
    password = request.POST['password']
    if((username =="uday.khairnar21@gmail.com") and (password =="uday123")):
        return render(request,"Home.html")
    else:
        # messages(request, "The username or password are not valid!")
        return render(request,"Login.html")
def addUser(request):
    return render(request,"AddUser.html")

def home(request):
    return render(request,"Home.html")
     
def history(request):
    return render(request,"History.html")
     