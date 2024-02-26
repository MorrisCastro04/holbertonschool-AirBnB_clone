#!/usr/bin/python3
""" console """

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """Overwrite the emptyline method"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
