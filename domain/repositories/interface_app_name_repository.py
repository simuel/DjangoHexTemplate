from abc import ABC, abstractmethod
from apps.{{app_name}}.domain.entities.{{app_name}} import {{app_name.capitalize}}

class I{{app_name.capitalize}}Repository(ABC):
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, {{app_name}}_id):
        pass

    @abstractmethod
    def save(self, {{app_name}}: {{app_name.capitalize}}):
        pass

    @abstractmethod
    def delete(self, {{app_name}}: {{app_name.capitalize}}):
        pass