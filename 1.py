class animal:
    def speak(self):
         print("animals can make sounds")

class dog(animal):
      def bark(self ):
         print("dog bark")
          
class puppy(dog):
     def weep (self):
         print("puppy weep")

obj=puppy()
obj.speak()
obj.bark()
obj.weep()
