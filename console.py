#!/usr/bin/python3
"""
console.py module for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class for writing command interpreter
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
