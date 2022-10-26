#!/usr/bin/python3

class BaseModel:

    """Base class for all models

    Artributes:
        id (str): for unique id
        created_at (datetime): date and time creation
        updated_at (datetime): date and time update

    Methods:
        save(self): update the public instance attribute updated_at with current datetime
        to_dict(self): return a dictionary containing all keys/values of __dict__ of the instance
        

    
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()