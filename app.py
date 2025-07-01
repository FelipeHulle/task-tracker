#%%
import cmd 
from engine import Engine 


class Cli(cmd.Cmd):
    intro = 'Welcome to the todo list'
    prompt = 'task-cli '

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.engine = Engine()

    def do_list(self,linha):
        self.engine.list()

    def do_add(self,linha):

        description = linha
        data = self.engine.add(description)
        # print(data)
        mensagem = f'Task added successfully (ID: {data.get('id')})'  

        print(mensagem)

    
    def do_update(self,linha):

        try:
            id,descricao = linha.strip().split(' ',1)
            result = self.engine.update(int(id),descricao)
            
            if result['success']:
                mensagem = f'Task added successfully (ID: {result['data'].get('id')})' 
                print(mensagem)

            else:
                print(result['message'])
                
        except ValueError:
            print('Enter the ID first, followed by the description.')
        except IndexError:
            print('Enter two parameters')
        except Exception as e:
            print(f'Error: {e}')
        
    
    def do_delete(self,linha):

        args = int(linha)

        print(self.engine.delete(args))
    
    def do_mark_done(self,linha):

        args = int(linha)
        print(self.engine.change_status(args,'done'))

    def do_mark_in_progress(self,linha):

        args = int(linha)
        print(self.engine.change_status(args,'in progress'))

    def do_mark_todo(self,linha):

        args = int(linha)

        print(self.engine.change_status(args,'todo'))
    
    def do_list_done(self,linha):
        self.engine.list_filter('done')

    def do_list_todo(self,linha):
        self.engine.list_filter('todo')

    def do_list_in_progress(self,linha):
        self.engine.list_filter('in progress')
    
    
if __name__ == '__main__':
    Cli().cmdloop()