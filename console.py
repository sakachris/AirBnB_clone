#!/usr/bin/python3
"""
console.py module for the command interpreter
"""
import cmd
from models import base_model, user
from models import storage
from ast import literal_eval


class HBNBCommand(cmd.Cmd):
    """
    class for writing command interpreter
    """
    prompt = "(hbnb) "

    classes = {'BaseModel': base_model, 'User': user}

    def do_EOF(self, line):
        """End of line marker; Ctr+D exits"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        """Avoid repeating last line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            cls_obj = getattr(HBNBCommand.classes[line], line)
            cls_ins = cls_obj()
            cls_ins.save()
            print(cls_ins.id)

    def do_show(self, line):
        """Prints the string rep of an instance based on the class.id"""
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                str_rep = storage.all()[key]
                print(str_rep)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string rep of all instances class name or not"""
        cmds = line.split()
        if len(cmds) == 0:
            for val in storage.all().values():
                print(val)
        elif len(cmds) == 1:
            if cmds[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for key, val in storage.all().items():
                    if key.startswith(cmds[0]):
                        print(val)

    def do_update(self, line):
        """ Updates an instance based on the class.id by add/updating attr"""
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(cmds) == 2:
                print("** attribute name missing **")
            elif len(cmds) == 3:
                print("** value missing **")
            else:
                key = f"{cmds[0]}.{cmds[1]}"
                try:
                    setattr(storage.all()[key], cmds[2], literal_eval(cmds[3]))
                    storage.save()
                except ValueError:
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
