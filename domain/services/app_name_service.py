from apps.{{app_name}}.domain.repositories.interface_{{app_name}}_repository import I{{app_name.capitalize}}Repository
from apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}
from apps.{{app_name}}.domain.value_objects import *

class {{app_name.capitalize}}Service:

    def __init__(self, {{app_name}}_repository: I{{app_name.capitalize}}Repository):
        self.{{app_name}}_repository = {{app_name}}_repository

    def create_{{app_name}}(self):
        {{app_name}} = {{app_name.capitalize}}()
        return self.{{app_name}}_repository.save({{app_name}})

    def update_{{app_name}}(self, {{app_name}}_id: str):
        {{app_name}} = self.{{app_name}}_repository.get_by_id({{app_name}}_id)
        if not {{app_name}}:
            raise ValueError("{{app_name}} not found")
        {{app_name}}.update()
        return self.{{app_name}}_repository.save({{app_name}})

    def delete_{{app_name}}(self, {{app_name}}_id: str):
        {{app_name}} = self.{{app_name}}_repository.get_by_id({{app_name}}_id)
        if not {{app_name}}:
            raise ValueError("{{app_name}} not found")
        self.{{app_name}}_repository.delete({{app_name}})
