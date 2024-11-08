
from rest_framework import serializers
from Apps.{{app_name}}.domain.value_objects import *
from Apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}

class {{app_name.capitalize}}Serializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):

        return {{app_name.capitalize}}()

    def update(self, instance, validated_data):
        # Actualizar la entidad Customer
        #instance.name = validated_data.get('name', instance.name)
        #instance.email = Email(validated_data.get('email', str(instance.email)))
        #instance.address = validated_data.get('address', instance.address)
        return instance
