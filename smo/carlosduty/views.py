from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")
def store(request):
    return HttpResponse("Tienda")
def videos(request):
    return HttpResponse("Videos")
def blog(request):
    return HttpResponse("Blog")
def contact(request):
    return HttpResponse("Contacto")