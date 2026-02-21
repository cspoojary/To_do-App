from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    # Template URLs (keep existing functionality)
    path('', views.home, name='home'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    
    # REST API URLs
    path('api/todos/', views.todo_list, name='api-todo-list'),
    path('api/todos/<int:id>/', views.todo_detail, name='api-todo-detail'),
]

# Add router URLs for ViewSet (automatically generates list and detail views)
urlpatterns += router.urls