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

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to a JSON file,
        then prints the id of the newly created instance. """
        if line == "":
            print ("** class name missing **")
            return
        if line not in models:
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

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id.
        Saves the changes to the JSON file. """
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

    def do_all(self, line):
        """Prints all string representation of all
        instances based on or not on the class name."""
        if args not in models:
            print ("** class doesn't exist **")
            return

    def do_update(self, argv):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the
        change into the JSON file). """



    def emptyline(self):
        """Gives a new prompt if nothing was entered. """
        pass

    def do_quit(self, line):
        """Quits the program by typing quit."""
        return True

    def do_EOF(self, line):
        """Prints a new line and quits the program when ctrl D is pressed. """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
