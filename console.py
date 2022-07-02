#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

import models
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit(0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
