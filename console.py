#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
import sys
from models import storage
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    clas = {"BaseModel": BaseModel}
    def do_quit(self, arg):
        """Exit program"""
        return exit()
    
    def do_EOF(self, arg):
        """Exit program"""
        print("")
        return exit()
    
    def emptyline(self):
        """Empty Line"""
        pass
    
    def do_create(self, arg):
        if arg:
            if arg in self.clas:
                get = getattr(sys.modules[__name__], arg)
                new_instance = get()
                print(new_instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        '''
        Prints the string representation of an instance based on the class name
        '''
        tok = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif tok[0] not in self.clas:
            print("** class doesn't exist **")
        elif len(tok) > 1:
            key = tok[0] + "." + tok[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        tok = arg.split()
        if len(tok) == 0:
            print("** class name missing **")
        elif(tok[0] not in self.clas):
            print("** class doesn't exist **")
        elif len(tok) == 1:
            print("** instance id missing **")
        else:
            key = tok[0] + "." + tok[1]    
            if key in storage.all():
                i = storage.all()
                i.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
    
    def do_all(slef, arg):
        tok = arg.split()
        listt = []
        if len(tok) == 0:
            for key in storage.all():
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()