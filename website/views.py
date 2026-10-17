from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.
def home_view(request):
    context={'nbr_meetings':Meeting.objects.count(),'meetings': Meeting.objects.all()}
    return render(request,"website/home.html",context)
def about_view(request):
    return render(request,"website/about.html")
