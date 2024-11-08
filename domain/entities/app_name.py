import uuid
from Apps.{{app_name}}.domain.value_objects import *

class {{app_name.capitalize}}:
    def __init__(self, id=None):
        """
        
        """
        self.id = id or uuid.uuid4()