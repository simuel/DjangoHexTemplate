import Apps.{{app_name}}.domain.services.{{app_name}}_service import {{app_name.capitalize}}Service

class Manage{{app_name.capitalize}}:
    """
    
    """
    def __init__(self,{{app_name}}_service: {{app_name.capitalize}}Service) -> None:
        """
        
        """
        self.{{app_name}}_service = {{app_name}}_service
        
    def create_{{app_name}}(self): #add parameters
        """
        
        """
        return self.{{app_name}}_service.create_{{app_name}}()
    
    def update_{{app_name}}(self):
        """
        
        """
        return self.{{app_name}}_service.update_{{app_name}}({{app_name}}_id,)

    def delete_{{app_name}}(self, {{app_name}}_id: str):
        """
        
        """
        return self.{{app_name}}_service.delete_{{app_name}}({{app_name}}_id)

