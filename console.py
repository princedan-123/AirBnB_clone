#!/usr/bin/python3
"""A console for the project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A class that uses cmd module to implement a CLI"""
    prompt = "(hbnb) "
    def do_quit(self, argument):
        """this command exits the CLI"""
        return True

    def do_EOF(self, argument):
        """this command terminates the CLI in the event of an EOF signal"""
        return True
    def help_quit(self):
        """help for quit command"""
        print("Quit command to exit the program\n")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
