from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm, update_Todo
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

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


# REST API Views
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    """Get all todos or create a new todo"""
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    """Get, update, or delete a specific todo"""
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'Todo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)