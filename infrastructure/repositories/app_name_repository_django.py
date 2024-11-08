
from Apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}
from Apps.{{app_name}}.domain.value_objects import *
from Apps.{{app_name}}.domain.repositories.{{app_name}}_repository import I{{app_name.capitalize}}Repository
from Apps.{{app_name}}.models import {{app_name.capitalize}}Model  # Importando el modelo de Django


class {{app_name.capitalize}}RepositoryDjango(I{{app_name.capitalize}}Repository):

    def get_all(self):
        {{app_name}}_model = None #CustomerModel.objects.all()
        if not {{app_name}}_model:
            return None
        return [{{app_name.capitalize}}(
            id={{app_name}}.id,
        )
            for {{app_name}} in {{app_name}}_model
        ]

    def get_by_id(self, {{app_name}}_id):
        {{app_name}}_model = None #CustomerModel.objects.filter(id={{app_name}}_id).first()
        if not {{app_name}}_model:
            return None
        # Mapear el modelo Django a la entidad de dominio
        return {{app_name.capitalize}}(
            id={{app_name}}_model.id,
        )

    def save(self, {{app_name}}: {{app_name.capitalize}}):
        # Mapear la entidad de dominio al modelo Django
        {{app_name}}_model, created = None #CustomerModel.objects.update_or_create(
            id={{app_name}}.id,
            defaults={}
        )
        return {{app_name}}

    def delete(self, {{app_name}}: {{app_name.capitalize}}):
        #CustomerModel.objects.filter(id={{app_name}}.id).delete()
        pass
