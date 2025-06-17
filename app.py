import json

class PlayerInterface:

    @staticmethod
    def get_user_input():
        return input('Command: ')
    
class Engine:
    
    def __init__(self):
        self.idx = 0

    def add(self,description,status='todo'):

        data = {}

        data['id'] = self.idx
        data['description'] = description
        data['status'] = status

        with open('data.json','a') as file:
            json.dump(data,file,indent=2)
        
        self.idx += 1

        return 0
    
if __name__ == '__main__':
    engine = Engine()
    engine.add('estudar python')

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