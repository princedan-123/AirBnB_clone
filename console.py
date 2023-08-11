#!/usr/bin/python3
"""A console for the project"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ A class that uses cmd module to implement a CLI"""
    prompt = "(hbnb) "
    valid_classes = {
            "BaseModel": BaseModel,
            "FileStorage": FileStorage,
            "User": User
            }

    def do_quit(self, argument):
        """this command exits the CLI"""
        return True

    def do_EOF(self, argument):
        """this command terminates the CLI in the event of an EOF signal"""
        return True

    def do_create(self, class_name):
        """creates the instance of a class"""
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            cls = self.valid_classes[class_name]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """shows the string representation of an instance by it's class
            name and id attributes
        """
        self.argument = line.split()
        if len(self.argument) == 0:
            print("** class name missing **")
        elif self.argument[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(self.argument) == 1:
            print("** instance id missing **")
        elif len(self.argument) == 2:
            dic_key = f"{self.argument[0]}.{self.argument[1]}"
            dic = storage.all()
            if dic_key not in dic:
                print("** no instance found **")
            else:
                print(dic[dic_key])

    def do_destroy(self, line):
        """destroys an instance based on class name and id and
            saves the changes to storage
        """
        self.argument = line.split()
        if len(self.argument) == 0:
            print("** class name missing **")
        elif self.argument[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(self.argument) == 1:
            print("** instance id missing **")
        elif len(self.argument) == 2:
            dic = storage.all()
            dic_key = f"{self.argument[0]}.{self.argument[1]}"
            if dic_key not in dic:
                print("** no instance found **")
            else:
                del dic[dic_key]
                storage.save()

    def do_all(self, line):
        """prints all the string representation of all instances based
            or not on the class name
        """
        dic = storage.all()
        dic = f"{dic}"
        dic_list = [dic]
        self.argument = line.split()
        if len(self.argument) == 1:
            if self.argument[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                print(dic_list)
        else:
            print(dic_list)

    def do_update(self, line):
        """updates the attribute of an instance"""
        self.argument = line.split()
        if len(self.argument) == 0:
            print("** class name missing **")
        elif self.argument[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(self.argument) == 1:
            print("** instance id missing **")
        elif len(self.argument) == 2:
            print("** attribute name missing **")
        elif len(self.argument) == 3:
            print("** value missing **")
        elif len(self.argument) == 4:
            dic = storage.all()
            dic_key = f"{self.argument[0]}.{self.argument[1]}"
            attr_name = self.argument[2]
            attr_value = self.argument[3]
            if dic_key not in dic:
                print("** no instance found **")
            else:
                obj = dic[dic_key]
               # if attr_name not in obj:
                #    obj[attr_name]
                if attr_name in obj:
                    attribute = obj[attr_name]
                    attr_type = type(attribute)
                    attr_value = attr_type(attr_value)   # type casting
                    obj[attr_name] = attr_value          # updated attribute
                    storage.save()

    def help_quit(self):
        """help for quit command"""
        print("Quit command to exit the program\n")

    def help_create(self):
        """help for create command"""
        print("type in create with the appropriate class name")
        print("of the command you want to print")
        print("an instance of the class will be created")
        print("and the id will be display")

    def help_show(self):
        """help for show command"""
        print("type the word show along with class name and object id")
        print("it displays the string form of the object if it exists")
        print("class name and id must be valid")

    def help_destroy(self):
        """help for destroy command"""
        print("type the word destroy along with class name and object id")
        print("it will delete the dictionary representation of the object")
        print("after the deleting, the dictionary is saved in storage")

    def help_all(self):
        """help for all command"""
        print("type in the word all with or without class name")
        print("it prints a list of strings representing all object")
        print("available in storage")

    def help_update(self):
        """help for update command"""
        print("type in update along with class name, id, attribute, value")
        print("to update the attributes of an instance")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
