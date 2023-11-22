from django.shortcuts import render

# Create your views here.
def kagithala(request):
    
    return render(request,'kagithala.html')

def timetable(request):

    return render(request,'timetable.html')

def registration(request):
    
    return render(request,'registration.html')
