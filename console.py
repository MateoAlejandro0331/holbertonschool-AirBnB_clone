#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""


from models.base_model import BaseModel
import models
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel}

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
            new_object = BaseModel()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
