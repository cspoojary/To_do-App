from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    return render(request,'home.html',{'tasks': tasks})