def run(kid):
    print(f"{kid} ran down the road!")

def swing(kid):
    print(f"{kid} made it around the swingset bar!")

def slide(kid):
    print(f"{kid} went down the slide!")

def hide_and_seek(kid):
    print(f"{kid} never got found!")

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    run(kid)

for kid in swinging_kids:
    swing(kid)

for kid in sliding_kids:
    slide(kid)

for kid in hiding_kids:
    hide_and_seek(kid)


def print_100():
    numbers = range(101)

    for num in numbers:
        five = num%5
        seven = num%7
        if five == 0 and seven == 0:
            print("chickenMonkey")
        elif five == 0:
            print("chicken")
        elif seven == 0:
            print("monkey")
        else:
            print(num)

print_100()