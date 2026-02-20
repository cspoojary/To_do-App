from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm, update_Todo

# Create your views here.
def home(request):
    form = TodoForm()   

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    tasks = Todo.objects.all()

    return render(request, 'home.html', {'tasks': tasks, 'form':form})

def update(request, id):
    task = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        form = update_Todo(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = update_Todo(instance=task)

    return render(request, 'update.html',{'form':form})
        

def delete(request, id):
     task = get_object_or_404(Todo, id=id)

     if request.method == "POST":
          task.delete()
          return redirect('home')
     
     return render(request,'delete_confirmation.html', {'task': task})