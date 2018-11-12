#!/usr/bin/python3
""" The HBNB console """


import cmd
from sys import argv
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import shlex
storage = models.storage

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
            print("** class name missing **")
            return
        if line not in models:
            print("** class doesn't exist **")
            return

        newBM = BaseModel()
        newBM.save()
        print("{}".format(newBM.id))

    def do_show(self, argv):
        """ Prints the string representation of an instance based on the class
        name and id """
        token = shlex.split(argv)

        if len(token) == 0 or token[0] == "":
            print("** class name missing **")

        elif token[0] not in models:
            print("** class doesn't exist **")

        elif len(token) == 1 or token[1] == "":
            print("** instance id missing **")

        else:
            obj = storage.get_obj(token[1])
            if obj is None or obj.__class__.__name__ != token[0]:
                print("** no instance found **")
            else:
                print(str(obj))

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id.
        Saves the changes to the JSON file. """

        token = shlex.split(argv)

        if len(token) == 0 or token[0] == "":
            print("** class name missing **")

        elif token[0] not in models:
            print("** class doesn't exist **")

        elif len(token) == 1 or token[1] == "":
            print("** instance id missing **")

        else:
            obj = storage.get_obj(token[1])
            if obj is None or obj.__class__.__name__ != token[0]:
                print("** no instance found **")

            else:
                del storage.all()[token[0] + "." + token[1]]
                storage.save()
                print("Delete successful")

    def do_all(self, argv):
        """Prints all string representation of all
        instances based on class name, or if no class name is specified,
        print all instances."""

        token = shlex.split(argv)

        if len(token) == 0:
            objects = storage.all()
            lst = [str(objects[obj]) for obj in objects]
            print(lst)

        elif len(token) > 0 and token[0] in models:
            objects2 = storage.all()
            lst2 = [str(objects2[obj]) for obj in objects2 if token[0] in obj]
            print(lst2)

        elif token[0] not in models:
            print("** class doesn't exist **")


    def do_update(self, argv):
        """Updates an instance based on the class name and id
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
