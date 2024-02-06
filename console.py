#!/usr/bin/python3
"""
Write a program called console.py that contains the entry
point of the command interpreter:
You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
"""
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import ast
import cmd
import copy
import sys

class HBNBCommand(cmd.Cmd):
    """
    Your command interpreter should implement:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but
    you should keep it updated and documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything
    """
    HBNBClasses = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]
    prompt = "(hbnb) "

    def do_update(self, args):
        """
<<<<<<< HEAD
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change
        into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time!!!
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type!!!

        id, created_at and updated_at cant’ be updated.
        You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime.
        """
        list_args = args.split()
        if len(list_args) < 1:
            print("** class name missing **")
        else:
            if list_args[0] in self.HBNBClasses:
                if len(list_args) > 1:
                    key = f"{list_args[0]}.{list_args[1]}"
                    storage.reload()
                    change__objects_dict = storage.all()
                    if key in change__objects_dict:
                        if len(list_args) > 2:
                            if len(list_args) > 3:
                                attribute_name = list_args[2]
                                attribute_value = str(ast.literal_eval
                                                        (list_args[3]))
                                try:
                                    if isinstance(change__objects_dict[key]
                                                    [attribute_name], int):
                                        attribute_value = int
                                        (attribute_value)
                                        change__objects_dict[key]
                                        [attribute_name] = attribute_value
                                    elif isinstance(change__objects_dict
                                                    [key][attribute_name],
                                                    float):
                                        attribute_value = float
                                        (attribute_value)
                                        change__objects_dict[key]
                                        [attribute_name] = attribute_value
                                    else:
                                        change__objects_dict[key]
                                        [attribute_name] = attribute_value
                                except KeyError:
                                    try:
                                        if isinstance(int(attribute_value),
                                                        int):
                                            change__objects_dict[key]
                                            [attribute_name] = int(
                                                attribute_value)
                                    except ValueError:
                                        try:
                                            if isinstance(
                                                    float
                                                    (attribute_value),
                                                    float):
                                                change__objects_dict[key]
                                                [attribute_name] = float(
                                                    attribute_value)
                                        except ValueError:
                                            change__objects_dict[key]
                                            [attribute_name] = \
                                                attribute_value
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
=======
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == ' }'\
                            and type(eval(pline)) == dict:
                        _args = pline
>>>>>>> 335196d845b8bfb21d0ef80615562698cbbbcb9b
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

<<<<<<< HEAD
    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        if arg == "":
            print("** class name missing **")
        else:
            if arg in self.HBNBClasses or arg == ".":
                storage.reload()
                display_all_list = []
                temp_show_dict = copy.deepcopy(storage.all())
                for key in list(temp_show_dict):
                    base_class = temp_show_dict[key]["__class__"]
                    del temp_show_dict[key]["__class__"]
                    display_all_list.append(
                        f"[{base_class}] ({temp_show_dict[key]['id']}) \
                                {temp_show_dict[key]}"
                        )
                print(display_all_list)
            else:
                print("** class doesn't exist **")
=======
    def do_create(self, args):

        """ Create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            list_args = args.split(" ")

            kwargs = {}
            for arg in range(1,len(list_args)):
                key, value = tuple(list_args[arg].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = int(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

                if kwargs == {}:
                    obj = eval(list_args[0])()
                else:
                    obj = eval(list_args[0])(**kwargs)
                    storage.new(obj)
                    print(obj.id)
                    obj.save()

        except NameError:
            print("** class doesn't exist **")  
        except SyntaxError:
            print("** class name missing **")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
>>>>>>> 335196d845b8bfb21d0ef80615562698cbbbcb9b

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Ex: $ create BaseModel
        """
        if arg == "":
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                model = BaseModel()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "User":
                model = User()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "State":
                model = State()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "City":
                model = City()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "Amenity":
                model = Amenity()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "Place":
                model = Place()
                model.save()
                print(model.id)
                storage.reload()
            elif arg == "Review":
                model = Review()
                model.save()
                print(model.id)
                storage.reload()
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        list_args = args.split()
        if len(list_args) < 1:
            print("** class name missing **")
        else:
            if list_args[0] in self.HBNBClasses:
                if len(list_args) > 1:
                    key = f"{list_args[0]}.{list_args[1]}"
                    storage.reload()
                    change__objects_dict = storage.all()
                    if key in change__objects_dict:
                        del change__objects_dict[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234.
        """
        list_args = args.split()
        if len(list_args) < 1:
            print("** class name missing **")
<<<<<<< HEAD
        else:
            if list_args[0] in self.HBNBClasses:
                if len(list_args) > 1:
                    key = f"{list_args[0]}.{list_args[1]}"
                    storage.reload()
                    temp_show_dict = copy.deepcopy(storage.all())
                    if key in temp_show_dict:
                        base_class = temp_show_dict[key]["__class__"]
                        del temp_show_dict[key]["__class__"]
                        print(
                            f"[{base_class}] \
                                    ({temp_show_dict[key]['id']}) \
                                    {temp_show_dict[key]}"
                        )
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
=======
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)
>>>>>>> 335196d845b8bfb21d0ef80615562698cbbbcb9b

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program if EOF is reached"""
        if arg == "\n":
            print("")
        return True

    def emptyline(self):
        pass

    def preloop(self):
        if sys.stdin.isatty():
            return
        self.stdin = sys.stdin
        try:
            while True:
                line = input("(hbnb) ")
                print("")
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
        except EOFError:
            self.do_EOF("\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
