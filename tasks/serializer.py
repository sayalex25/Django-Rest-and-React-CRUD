from rest_framework import serializers
from .models import Task


# En este archivo serializador convertiremos los tipos de datos de python a json 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        #fields = ('id', 'title', 'description', 'done')
        model = Task  # Reemplaza 'Task' con el modelo que estás utilizando en tu serializador
        fields = '__all__'  # O especifica los campos que deseas incluir en la serialización



