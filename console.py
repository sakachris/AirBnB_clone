#!/usr/bin/python3
"""
console.py module for the command interpreter
"""
import cmd
from models import base_model, user, amenity, place, city, state, review
from models import storage
from ast import literal_eval
import re


class HBNBCommand(cmd.Cmd):
    """
    class for writing command interpreter
    """
    prompt = "(hbnb) "

    classes = {'BaseModel': base_model, 'User': user, 'Amenity': amenity,
               'Place': place, 'City': city, 'State': state, 'Review': review}

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

    def default(self, line):
        """Runs none built in command"""
        cmds = line.split('.')
        if len(cmds) == 1:
            print(f"*** Unknown syntax: {line}")
        if len(cmds) > 1:
            if cmds[1] == "all()":
                self.do_all(cmds[0])
            elif cmds[1] == "count()":
                count = 0
                for key, val in storage.all().items():
                    if key.startswith(cmds[0]):
                        count += 1
                print(count)
            else:
                if cmds[1].startswith("show"):
                    Rgx = re.compile(r'(show)\((.*)\)')
                    grp = Rgx.search(cmds[1])
                    cmd, id = grp.groups()
                    if id.startswith(('"', "'")):
                        id = id[1:-1]
                    if cmd == "show":
                        self.do_show(cmds[0]+" "+id)
                elif cmds[1].startswith("destroy"):
                    Rgx2 = re.compile(r'(destroy)\((.*)\)')
                    grp2 = Rgx2.search(cmds[1])
                    cmd2, id2 = grp2.groups()
                    if id2.startswith(('"', "'")):
                        id2 = id2[1:-1]
                    if cmd2 == "destroy":
                        self.do_destroy(cmds[0]+" "+id2)
                elif cmds[1].startswith("update"):
                    Rgx3 = re.compile(r'(update)\((.*)\)')
                    grp3 = Rgx3.search(cmds[1])
                    cmd3, string = grp3.groups()
                    if cmd3 == "update":
                        if len(string) == 0:
                            self.do_update(cmds[0]+" ")
                        else:
                            var = string.split(',')
                            lst = []
                            for i in var:
                                lst.append(i.strip())
                            if len(lst) == 1:
                                self.do_update(cmds[0]+" "+lst[0][1:-1])
                            elif len(lst) == 2:
                                self.do_update(cmds[0]+" "+lst[0][1:-1]+" "+lst
                                               [1][1:-1])
                            else:
                                self.do_update(cmds[0]+" "+lst[0][1:-1]+" "+lst
                                               [1][1:-1]+" "+lst[2])
                else:
                    print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
