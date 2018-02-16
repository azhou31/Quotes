from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,"quotes/index.html")

def register(request):
    errors=User.objects.validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect("/")
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'],alias = request.POST['alias'],email = request.POST['email'],bday = request.POST['bday'], password = hashed_pw)
        request.session['id'] = user.id 
        return render(request, "quotes/register_success.html")

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email = email, password = password)
    if user is not None:
        login(request,user)
        return render("login_app/login.html")
    else:
        return redirect("/")
    return render(request,"login_app/login.html")

