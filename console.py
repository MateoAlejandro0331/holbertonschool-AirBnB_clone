#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

import models
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
