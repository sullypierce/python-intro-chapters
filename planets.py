planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[8]
print(planet_list) 



#CHALLENGE

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Thor", "Mercury")
]


for planet in planet_list:
    print(f"{planet} has been visited by:")
    for craft in spacecraft:
        if craft[1] == planet:
            print(craft[0]) 