# coding : utf8
# version : 0.0

from object import Object

class Type(Object):
    """
        There's three kind of Objects types:
            - Intern Types :    those are immuable, according to the Zat code,
                                even if constancy is just a concept in Python.
            - Included Types :  those are included with library.
            - Extern Types :    those are created by the user.
        Inculded and Extern Type are created within Intern types.
        See Type section of ZATCODE for more.
    """
    initialized = False

    def __init__(self):
        self.intern = Intern()
        self.included = None
        self.extern = None
        self.initialized = self.intern.initialized

    def init_include(self):
        self.included = Included()

    def init_extern(self):
        self.extern = Extern()

class Intern(Type):
    # Every intern type has a specific and exclusif id, expressed by an integer.
    ids = {   # Input/Output
                "Stdin":    1,
                "Stdout":   2,
                # Condition
                "If":       10,
                "Else":     11,
                # Loop
                "While":    20,
                "For":      21,
                "Break":    22,
                "Continue": 23,
                # Primitive
                "Bool":     30,
                "Uint":     31,
                "Char":     32,
                "Achar":    33,
            }

    # intern type reserved id range (inclusif)
    limits = (1,100)

    def __init__(self):
        self.size = len(self.ids)
        # Makes a reversed (key:value to value:key) dictionnary
        self.names = {id: name for name, id in self.ids.items()}
        self.initialized = True

    def get_size(self):
        return self.size

    def get_limits(self):
        return self.limits

    def get_id(self, name : str):
        """
            Returns 0 if it is not a declared type,
            the corresponding id otherwise.
        """
        return self.ids.get(name, 0)

    def get_name(self, id : str):
        """
            Returns None if uninstancied Type, an empty string
            in case of an undeclared id, the name otherwise.
        """
        if self.initialized:
            return self.names.get(id, "")


class Included(Type):

    included_path = "../included"
    os = __import__("os")

    def __init__(self):
        if not self.os.path.exists(self.included_path):
            self.os.mkdir(self.included_path)


class Extern(Type):

    def __init__(self):
        pass
