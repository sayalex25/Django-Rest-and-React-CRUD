                               
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

# Create your views here.
# Mediante estas dos propiedades esta clase puede saber suales son 
# los datos a manejar y generar el CRUD
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()