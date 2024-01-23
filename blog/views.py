from django.http import Http404
from django.shortcuts import render
from .models import Cars,Lates
# Create your views here.
def cardetailView(request,id):
    try:
        car=Lates.objects.get(id=id)
        context={
            "car":car
        }
    except Cars.DoesNotExists:
        raise Http404("No car found")
    return render(request,"fcardetail.html",context=context)



def index(request):
    car = Cars.objects.all()
    late = Lates.objects.all()
    context = {
        "cars": car,
        "late": late
    }
    return render(request,"index.html",context=context)
def contact(request):
    return render(request,"contact.html",context={})