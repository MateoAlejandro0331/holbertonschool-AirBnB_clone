#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

from models.base_model import BaseModel
from models import storage
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

        elif arg[0] in HBNBCommand.classes:
            newobject = HBNBCommand.classes[arg[0]]()

        else:
            print("** class doesn't exist **")
            return

        newobject.save()
        print(newobject.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        else:
            bool = False 
            compare = f"{arg[0]}.{arg[1]}"
            all_objs = storage.all()
            for key in all_objs.keys():
                if compare == key:
                    bool = True
                    print(all_objs[key])
                    break

            if bool == False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        else:
            bool = False
            compare = f"{arg[0]}.{arg[1]}"
            for key in storage.all():
                if compare == key:
                    bool = True
                    storage.all().pop(key)
                    storage.save()
                    break

            if bool == False:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances
        based or not on the class name."""

        arg = arg.split()

        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        list = []
        all_objs = storage.all()

        for key, value in all_objs.items():
            list.append(value)
        print(list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
