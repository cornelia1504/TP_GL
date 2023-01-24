#encoding : utf8
"""Program for creating class"""
class Animal():
    """creating class Animal"""
    def __init__(self, species, age, diet, mother) -> None :
        """attributes = species, age, diet, mother"""
        self.species = species
        self.age = age
        self.diet = diet
        self.mother = mother
        self.child_id = [] # contains not understandable id ##
        self.children = [] # contains names
        self.descendants = []

    def __str__(self) -> str:
        return "Species : " + self.species + "\n" \
        +"age : " + str(self.age) + "\n" \
        +"diet : "+ str(self.diet) + "\n"\
        +"Mother : " + str(self.mother) + "\n"\
        + "Children : " + str(self.children) + "\n"\
        + "Children : " + str(self.children) + "\n"\
        + "Descendent : " + str(self.descendants)

class Cat(Animal):
    """class for the species Homme decendant of Animal"""
    def __init__(self, age , name) -> None:
        """only name , age and diet attributes"""
        super().__init__("Chat", age, "Omnivore", "animal")
        self.age = age
        self.name = name

    def __str__(self):
        """function to print info form Animal() and from Cat()"""
        return super().__str__() + "\nname : " + self.name

class Homme(Cat): #Homme descendant of cat
    """class for the species Homme"""
    def __init__(self,name, age) -> None:
        """init what homme have 'homme' and 'omnivore" """
        super().__init__("homme", age)
        self.age = age
        self.name = name

    def __str__(self):
        """function to print info form Animal() and from Homme()"""
        return super().__str__() + "\nname : " + self.name

if __name__ == "__main__":
    cat0 = Cat(10, "mimi")
    cat1 = Cat(8, "mich")
    homme0 = Homme(38, "Mitch")
    print(cat0)
    print(cat1)
    print(homme0)

#TO_DO :  function to add mother, child  and descendents on the lists
