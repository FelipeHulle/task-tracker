#%%
import json
import os
from datetime import datetime

class PlayerInterface:

    @staticmethod
    def get_user_input():
        return input('Command: ')
    
class Engine:
    
    def __init__(self):
        pass

    def _agora(self):
        return datetime.now()

    def _read_database(self,path = 'data.json') -> json:
        """
        Read data in json database
        
        """
        if not os.path.exists(path):
            with open(path, 'x') as file:
                return {}
            
        if os.path.getsize(path) == 0:
            return {}
        
        with open(path,'r') as file:
            saved_json = json.load(file)
            return saved_json

        
    def _save_data_in_database(self,dados: json,path = 'data.json') -> str:
        """
        Save data in json database
        """

        old_data = self._read_database(path)
        
        if os.path.getsize(path) == 0:
            old_data = []

        if not isinstance(old_data,list):
            old_data = [old_data]

        old_data.append(dados)        

        with open(path,'w') as file:
            json.dump(old_data,file,indent=4)
            return 'Sucess'


    def add(self,description,status='todo'):
        """
        Create new item
        """
         
        try:
            id = int(self._read_database()[-1].get('id')) + 1
        except KeyError:
            id = 0


        data = {}
        data['id'] = id
        data['description'] = description
        data['status'] = status
        data['createdAt'] = str(self._agora())
        data['updatedAt'] = str(self._agora()) 

        saving = self._save_data_in_database(data)

        mensagem = f'Item {id} foi adicionado com sucesso.'

        return mensagem
    
    def update(self,id,description):
        """
        Update item
        """

        old_item = next((item for item in self._read_database() if item.get('id') == id),None)
        
        old_item['description'] = description
        old_item['updatedAt'] = str(self._agora())

        return print(old_item)



#%%

engine = Engine()
# engine._read_database()
# engine.add('Macetar')
# engine.update(12,'comer')




#%%


# id: A unique identifier for the task
# description: A short description of the task
# status: The status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was last updated

# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file.
# The user should be able to:

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress