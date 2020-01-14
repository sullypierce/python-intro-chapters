


word_definitions = dict([("indubitably", "impossible to doubt"),("fracking","the process of injecting liquid at high pressure into subterranean rocks, boreholes, etc. so as to force open existing fissures and extract oil or gas."), ("hello", "used as a greeting or to begin a telephone conversation.")])



word_definitions["Awesome"] = "The  feeling of students when they are learning Python"




# print(word_definitions["indubitably"])
# print(word_definitions["fracking"])


for definition in word_definitions:
    print(f"The definition of {definition} is {word_definitions[definition]}")




idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for idiom in idioms:
    idiom_string = " ".join(idioms[idiom])
    print(f"{idiom} : {idiom_string}")



#CHALLENGES

my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}
fam_tuples = my_family.items()
print(fam_tuples) 
fam_strings = [f"{obj['name']} is my {relationship} and is {obj['age']} years old" for relationship, obj in my_family.items()]

print(fam_strings) 
