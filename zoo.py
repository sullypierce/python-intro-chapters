
zoo = ("giraffe", "hippo", "falcon", "monkey")

print(zoo.index("giraffe")) 

animal_to_find = "hippo"
if animal_to_find in zoo:
    print(f"a {animal_to_find} was found!")


(first_animal, second_animal, third_animal, fourth_animal) = zoo
print(first_animal) 
print(second_animal)
print(third_animal) 
print(fourth_animal)

zoo = list(zoo)
zoo.extend(["eagle", "banana", "muskrat"])
zoo = tuple(zoo)
print(zoo)