from random import randomcrange

class MSDie:
   
   def __init__(self, sides):
      self.sides = sides
      self.value = 1

   def roll(self):
      set.value = randrange(1,self.sides +1)

   def getValue(self):
      return self.value
   
   def setValue(self, value):
      self.value = value


