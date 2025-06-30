from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import StudentForm
def register(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"students/success.html")
    else:
        form=StudentForm()
    return render(request,"students/register.html",{"form":form})


