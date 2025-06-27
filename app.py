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
        print(self.engine.add(description))
    
    def do_update(self,linha):

        args = linha.strip().split(' ',1)

        print(self.engine.update(int(args[0]),args[1]))
    
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