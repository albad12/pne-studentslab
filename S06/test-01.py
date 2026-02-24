class Seq:
    """A class for representing sequences"""
    pass

# Create am object of the class Seq => We use the name of the class + ()
s1 = Seq()
# Create another object of the class Seq
s2 = Seq()

# The methods are actions that the object can perform
# The attributes are the data or characteristics that belong to a class or an object

class ClassName:
    # Constructor (__init__) method to initialize attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1     # Define instance attribute
        self.attribute2 = attribute2
        # Method to define actions or behaviours:
    def method_name(self, parameter):
        # Perform operations on attributes or other tasks. Code
        pass

    def __str__(self):
        """Method called when the object is being printed"""
        return self.attribute1


class ParentClass:
    # Parent class code here
    pass
class ChildClass(ParentClass):
    """Child class code here. This class is derived from the Parent class.
    All the objects of the Child class
    will inherit the methods from the Parent Class.
    It can be expanded we need to write __init__()"""

    pass

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, attribute1, name=""):

        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(attribute1)
        self.name = name
        print("New gene created")

