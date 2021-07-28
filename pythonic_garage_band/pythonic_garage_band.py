from abc import ABC, abstractmethod

class Musician(ABC):
    """
    This The Base Class For All Classes 
    """
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod
    def __repr__ (self):
        pass

    def play_solo(self):
        pass
    def get_instrument (self):
        pass
    
  

 

  




class Guitarist(Musician):
    '''
    The Class for all Guitarist
    '''
    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    def __repr__ (self):
        return (f"Guitarist instance. Name = {self.name}")
    def get_instrument(self):
        return "guitar" 
    def __init__(self,name):
        self.name=name

    def play_solo(self): 
     return 'face melting guitar solo' 
   




class Drummer(Musician):
    '''
    classe For all Drummer
    '''
    def __str__(self):
                return (f"My name is {self.name} and I play drums")
    def __repr__ (self):
        return (f"Drummer instance. Name = {self.name}")
    def get_instrument(self):
        return "drums"
  
    def __init__(self,name):
        self.name=name
    def play_solo(self): 
     return 'rattle boom crash'




class Bassist(Musician):
    '''
    class for all Bassist
    '''
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
                return (f"My name is {self.name} and I play bass")
    def __repr__ (self):
        return (f"Bassist instance. Name = {self.name}")
    def get_instrument(self):
        return "bass"
  
    def play_solo(self): 
     return 'bom bom buh bom'


class Band(Musician):
    '''
    class for all Bands 
    '''
    instances=[]       
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)

    def play_solos(self):
         return [instance.play_solo() for instance in self.members]

    @classmethod  
    def to_list(cls):
    
     return cls.instances

    def __str__(self):
        pass
    def __repr__ (self):
        pass




# members = [
#      Guitarist("Kurt Cobain"),
#     Bassist("Krist Novoselic"),
#     Drummer("Dave Grohl"),
#     ]

# some_band = Band("Nirvana", members)

# print(some_band.instances)