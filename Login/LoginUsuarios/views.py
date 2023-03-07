from django.shortcuts import render

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
def login(request):
    return render(request,'login.html')