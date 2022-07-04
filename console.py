#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""


from curses import keyname
from models.base_model import BaseModel
import models
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel()}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit(0)
        """return True"""

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        exit(0)
        """return True"""

    def emptyline(self, arg):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] in HBNBCommand.classes.keys():
            newobject = HBNBCommand.classes[arg[0]]
            print(newobject.id)
            newobject.save()
        else:
            print("** class doesn't exist **")
        """for key, value in HBNBCommand.classes.items():
            if arg[0] == key:
                newobject = value
                print(newobject.id)
                newobject.save()"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
