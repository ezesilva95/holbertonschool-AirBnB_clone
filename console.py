#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
import sys
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    clas = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

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

    def do_all(self, arg):
        listt = []
        tok = shlex.split(arg)
        if len(tok) == 0:
            for key in storage.all():
                i = storage.all()
                string = str(i[key])
                listt.append(string)
            print(listt)
        else:
            if tok[0] not in self.clas:
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    i = storage.all()
                    x = key.split('.')
                    if x[0] == tok[0]:
                        string = str(i[key])
                        listt.append(string)
                print(listt)
    def do_update(self, arg):
        tok = shlex.split(arg)
        if len(tok) == 0:
            print("** class name missing **")
        elif tok[0] not in self.clas:
            print("** class doesn't exist **")
        elif len(tok) == 1:
            print("** instance id missing **")
        else:
            key = tok[0] + '.' + tok[1]
            if key in storage.all():
                if len(tok) > 2:
                    if len(tok) == 3:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[key], tok[2], tok[3][0:])
                        storage.all()[key].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")

    def do_count(self, arg):
        tok = shlex.split(arg)
        count = 0
        if tok[0] not in self.clas:
            print("** class doesn't exist **")
        for key in storage.all():
            x = key.split('.')
            if x[0] == tok[0]:
                count += 1
        print(count)
    
    def precmd(self, arg):
        tok = arg.split('.', 1)
        if len(tok) == 2:
            clase = tok[0]
            tok = tok[1].split('(', 1)
            com = tok[0]
            if len(tok) == 2:
                tok = tok[1].split(')', 1)
                if len(tok) == 2:
                    tok1 = tok[0].strip('"')
                    _id = tok1
            last_command = com + " " + clase + " " + _id
            return last_command
        else:
            return arg
if __name__ == '__main__':
    HBNBCommand().cmdloop()
