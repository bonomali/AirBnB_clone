#!/usr/bin/python3
""" The HBNB console """


import cmd
from sys import argv
from models.base_model import BaseModel
import shlex

""" List of classes / models """
models = {"BaseModel"}

class HBNBCommand(cmd.Cmd):
    """ Class containing hbnb commands """
    intro = '∆===∆===∆ Welcome to the hbnb shell. Type ? for help. ∆===∆===∆\n'
    prompt = '(hbnb) '
    file = None


    """ Commands """

    """ 7. Console 0.1 """

    def do_create(self, cls):
        """Creates a new instance of BaseModel and saves it to a JSON file,
        then prints the id of the newly created instance. """
        if cls == "":
            print ("** class name missing **")
            return
        if cls not in models:
            print("** class doesn't exist **")
            return

        newBM = BaseModel()
        """ Save to json file step """
        print ("{}".format(newBM.id))


    def do_show(self, argv):
        """ Prints the string representation of an instance based on the class
        name and id """
        token = shlex.split(argv)

        if len(token) == 0 or token[0] == "":
            print ("** class name missing **")
            return
        if token[0] not in models:
            print ("** class doesn't exist **")
            return
        if len(token) == 1 or token[1] == "":
            print ("** instance id missing **")
            return
        if token[1] != newBM.id:
            print ("** no instance found **")
            return






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
