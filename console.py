#!/usr/bin/python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Class containing hbnb commands """
    intro = '=== Welcome to the hbnb shell. Type ? for help. ===\n'
    prompt = '(hbnb) '
    file = None

    """ Commands """

    def emptyline(self):
        """Gives a new prompt if nothing was entered. """
        pass

    def do_quit(self, args):
        """Quits the program by typing quit."""
        return True

    def do_EOF(self, line):
        """Prints a new line and quits the program when ctrl D is pressed. """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
