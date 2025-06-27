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

        
    def _append_in_database(self,dados: json,path = 'data.json') -> str:
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
        
    def _truncate_and_save_database(self,dados: json, path = 'data.json') -> str:
        """
        Truncate all database and save new data
        """

        with open(path,'w') as file:
            json.dump(dados,file,indent=4)
            return 'Sucess'
        
    def add(self,description,status='todo'):
        """
        Create new item
        """

        database = self._read_database()
         
        if database:
            id = int(database[-1].get('id')) + 1
        else:
            id = 0

        data = {}
        data['id'] = id
        data['description'] = description
        data['status'] = status
        data['createdAt'] = str(self._agora())
        data['updatedAt'] = data['createdAt']

        saving = self._append_in_database(data)

        mensagem = f'Task added successfully (ID: {id})'

        return mensagem
    
    def update(self,id,description):
        """
        Update item
        """

        database = self._read_database()

        if database:

            for item in database:
                if item['id'] == id:
                    item['description'] = description
                    item['updatedAt'] = str(self._agora())
                    break

            self._truncate_and_save_database(database)
        else:
            return 'Database nao possui nenhum item'

        return 'Sucesso'
    
    def delete(self,id):

        database = self._read_database()

        if database:

            for item in database:
                if item['id'] == id:
                    database.remove(item)

            self._truncate_and_save_database(database)
        else:
            'Database não possui nenhum item'

        return 'sucesso'
    
    def change_status(self,id,status):

        database = self._read_database()

        if database:

            for item in database:
                if item['id'] == id:
                    item['status'] = status

            self._truncate_and_save_database(database)

        return 'Sucesso'
    
    def list(self):
        return self._read_database()
    
    def list_done(self):
        done_items = [item for item in self.list() if item['status'] == 'done']
        return done_items

    def list_todo(self):
        todo_items = [item for item in self.list() if item['status'] == 'todo']
        return todo_items
    
    def list_in_progress(self):
        in_progress_items = [item for item in self.list() if item['status'] == 'in progress']
        return in_progress_items