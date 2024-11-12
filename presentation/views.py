# customers/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.{{app_name}}.infrastructure.serializers.{{app_name}}_serializer import {{app_name.capitalize}}Serializer
from apps.{{app_name}}.domain.services.{{app_name}}_service import {{app_name.capitalize}}Service
from apps.{{app_name}}.infrastructure.repositories.{{app_name}}_repository_django import {{app_name.capitalize}}RepositoryDjango
from apps.{{app_name}}.application.use_cases.manage_{{app_name}} import Manage{{app_name.capitalize}}
from apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}

class {{app_name.capitalize}}ViewSet(viewsets.ViewSet):
    """
    ViewSet for handling CRUD operations for Customer.
    """
    
    def get_queryset(self):
        # Usamos el repositorio para obtener todos los clientes
        repository = {{app_name.capitalize}}RepositoryDjango()
        {{app_name}} = repository.get_all()
        return {{app_name}}

    def list(self, request):
        # Lista todos los clientes
        repository = {{app_name.capitalize}}RepositoryDjango()
        {{app_name}} = repository.get_all()
        serializer = {{app_name.capitalize}}Serializer({{app_name}}, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Crear un nuevo cliente
        serializer = {{app_name.capitalize}}Serializer(data=request.data)
        if serializer.is_valid():
            {{app_name}} = serializer.save()
            return Response({{app_name.capitalize}}Serializer({{app_name}}).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Obtener un cliente por ID
        repository = {{app_name.capitalize}}RepositoryDjango()
        {{app_name}} = repository.get_by_id(pk)
        if {{app_name}}:
            serializer = {{app_name.capitalize}}Serializer({{app_name}})
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        # Actualizar un cliente
        repository = {{app_name.capitalize}}RepositoryDjango()
        {{app_name}} = repository.get_by_id(pk)
        if not {{app_name}}:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = {{app_name.capitalize}}Serializer({{app_name}}, data=request.data)
        if serializer.is_valid():
            updated_{{app_name}} = serializer.save()
            return Response({{app_name.capitalize}}Serializer(updated_{{app_name}}).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Eliminar un cliente
        repository = {{app_name.capitalize}}RepositoryDjango()
        {{app_name}} = repository.get_by_id(pk)
        if not {{app_name}}:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        repository.delete({{app_name}})
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
