from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'account/login.html')

def register_page(request):
    return render(request,'account/register.html')
   