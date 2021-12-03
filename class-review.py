class Dog:

    def __init__(self, name, owner, breed, likes, dislikes):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.likes = likes
        self.dislikes = dislikes
        
        # default mood value, range 0-5
        self.mood = 2

    def speak(self):
        if self.mood > 3:
            print("*bork bork!*")
        elif self.mood > 1:
            print("*bark*")
        else:
            print("*grrrrr!*") 
    
    def pet(self):
        self.mood += 1

class DogOwner:
    def __init__(self,name,dogs):
        self.name = name
        self.dogs = dogs
        for dog in dogs:
        #set each of the dogs' owners to the name of the DogOwner
            dog.owner = self.name
hazel = Dog("Hazel","Beagle/Heeler","NotShane",["treats","naps","raccoons"],["thunder"])
shane = DogOwner("Shane",[hazel])
print(hazel.owner) #Should be 'Shane'