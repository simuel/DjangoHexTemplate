from apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}
#from apps.{{app_name}}.domain.value_objects import *
from apps.{{app_name}}.domain.repositories.interface_{{app_name}}_repository import I{{app_name.capitalize}}Repository
from apps.{{app_name}}.models import *  # Django ORM

class {{app_name.capitalize}}RepositoryDjango(I{{app_name.capitalize}}Repository):

    def get_by_id(self, {{app_name}}_id):
        {{app_name}}_model = None #CustomerModel.objects.filter(id=customer_id).first()
        if not {{app_name}}_model:
            return None
        return {{app_name.capitalize}}()

    def save(self, {{app_name}}: {{app_name.capitalize}}):
        {{app_name}}_model, created = None #CustomerModel.objects.update_or_create(
            #id=customer.id,
            #defaults={'name': customer.name, 'email': str(customer.email), 'address': customer.address}
        #)
        return {{app_name}}

    def delete(self, {{app_name}}: {{app_name.capitalize}}):
        #CustomerModel.objects.filter(id=customer.id).delete()
        pass
