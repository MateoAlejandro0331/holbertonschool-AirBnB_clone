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
        list = []
        all_objs = storage.all()

        if len(arg) == 0:
            for key, value in all_objs.items():
                list.append(value.__str__())
            print(list)

        elif len(arg) == 1:
            if arg[0] in HBNBCommand.classes:
                for key, value in all_objs.items():
                    if arg[0] in key:
                        list.append(value.__str__())
                print(list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        """arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        compare = f"{arg[0]}.{arg[1]}"
        if compare not in storage.all().keys():
            print("** no instance found **")

        elif len(arg) == 2:
            print("** attribute name missing **")

        elif len(arg) == 3:
            print("** value missing **")

        elif len(arg) > 3:
            setattr(storage.all()[compare], arg[2], arg[3])
            storage.all()[compare].save()"""

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

        compare = f"{arg[0]}.{arg[1]}"
        if compare in storage.all().keys():
            if len(arg) == 2:
                print("** attribute name missing **")
                return

            if len(arg) == 3:
                print("** value missing **")
                return

            for key, value in storage.all().items():
                if key == compare:
                    value.__dict__.update()

            new_instance = storage.all()[compare]
            setattr(new_instance, arg[2], arg[3])
            storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
