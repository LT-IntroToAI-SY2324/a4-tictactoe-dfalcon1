# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # functions that start with __ are not intended to be called
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        """"Creates an instance of the dog class an sets attributes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """Return a sring representation of a dog"""
        s = "Dog's name is " + self.name + "\n"
        s += "and age is " + str(self.age) + "\n"
        s += "and fur color is " + self.fur_color + "\n"
        s += "they have played fetch " + str(self.fetch_count) + "\n"
        return s
    
    def play_fetch(self, num_times):
        self.fetch_count += num_times

mydog = Dog("logan", "black", 7, "salmon")
Chrisdog = Dog("luna", "black_and_white", 7, "tortillas")

mydog.play_fetch(20)
Chrisdog.play_fetch(100)

print(mydog)
print(Chrisdog)