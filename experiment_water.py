class Stuff:
    def __init__(self, name, volume, temperature):
        list_obj.append(self)
        if name!="":
            self.name=name
        else:
            self.name=f"name not given"
            print(self.name) 
        
        if self.is_number (volume):
            self.volume=volume
        else:
           self.volume=f'{self.name}: invalid format of the volume \n'
           print (self.volume)
        if self.is_number(temperature):
            self.temperature=temperature
        else:
           self.temperature=f'{self.name}: invalid format of the temperature \n'
           print (self.temperature)

    
    def __str__(self):
        return f"{self.name}, volume = {self.volume}, {self.temperature}"
    
    def __len__(self):
        return self.volume
    
    def __add__(self, other):
        if type(self)==type(other):
            return self.__class__ ("name not set", self.volume+other.volume, "")
        else:
            return print ("operation not possible: objects of different classes, ", self.__class__.__name__, "and", other.__class__.__name__ )
        
    def __le__(self, other):
        if type(self)==type(other):
            return self.volume<=other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )

    def __ge__(self, other):
        if type(self)==type(other):
            return self.volume>=other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )

    def __eq__(self, other):
        if type(self)==type(other):
            return self.volume==other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )
        
    def __ne__(self, other):
        if type(self)==type(other):
            return self.volume!=other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )

    def __gt__(self, other):
        if type(self)==type(other):
            return self.volume>other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )
        
    def __lt__(self, other):
        if type(self)==type(other):
            return self.volume<other.volume
        else:
            return ("Objects of different classes cannot be compared, "+ self.__class__.__name__+ " and "+ other.__class__.__name__ )

    def is_number (self, value):
        return isinstance(value, int) or isinstance(value, float)
    


class Water (Stuff):
    colour="no colour"
    def state (self):   
        if isinstance(self.temperature, str):
            print ("The temperature is unknown and must be given")
        else:
            if self.temperature<=0:
                print (self.name, "is frozen")
            elif self.temperature<100:
                print(self.name, "is liquid")
            elif self.temperature>=100:
                print (self.name, "boils and evaporates")
    
class Mercury (Stuff):
    colour="silver"    
    def state (self):   
        if self.temperature<=-38.83:
            print (self.name, "is solid")
        elif self.temperature<356.7:
            print(self.name, "is liquid")
        else:
            print (self.name, "boils and evaporates")

    
    
list_obj=list()

def boil (stuff, celsius_grades):
    if not stuff.is_number(celsius_grades):
        print ("Cannot boil, wrong temperature format")
    else:
        if stuff.is_number(stuff.temperature):
            stuff.temperature+=celsius_grades
            return stuff.state()
        else:
            print (stuff.name,": Cannot boil, wrong temperature format")

def freeze (stuff, celsius_grades):
    if not stuff.is_number(celsius_grades):
        print ("Cannot freeze, wrong temperature format")
    else:
        if stuff.is_number(stuff.temperature):
            stuff.temperature-=celsius_grades
            return stuff.state()
        else:
            print (stuff.name,": Cannot freeze, wrong temperature format")

def filter(parameter, parameter_value):
    matching_obj=0
    for i in list_obj:
        if parameter in i.__dict__:
            if i.__dict__[parameter]==parameter_value:
                print (i.name, i.__class__.__name__)
                matching_obj+=1
        else:
            print ("there is no such attribute :", parameter)
            break
    if matching_obj==0:
            print ("no objects with such parameter")
    else:
        print (matching_obj, "obj with such parameter")


def object_print (self):
    print (self, end=" | ")
    self.state()