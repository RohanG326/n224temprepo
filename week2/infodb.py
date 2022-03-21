InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Rohan",
    "LastName": "Gaikwad",
    "FavoriteSongs": ["Afterthought by Joji","Down Bad by Dreamville","SUMMER by Brockhampton","durag activity by Baby Keem", "Ivy by Frank Ocean"],
    "FavoriteColor": "Red",
    "GitHub": "RohanG326"
})

InfoDb.append({
    "FirstName": "Adi",
    "LastName": "Khandelwal",
    "FavoriteSongs": ["No Role Modelz by J.Cole","Nice For What by Drake","Sugar by Maroon 5","Versace on the Floor by Bruno Mars", "I Want It That Way by Backstreet Boys"],
    "FavoriteColor": "Blue",
    "GitHub": "Adi-K-Coding"
})
InfoDb.append({
    "FirstName": "Samaya",
    "LastName": "Sankuratri",
    "FavoriteSongs": ["IDK BY IDK","IDK BY IDK","IDK BY IDK","IDK BY IDK", "IDK BY IDK"],
    "FavoriteColor": "Purple",
    "GitHub": "samayass"
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite Songs: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["FavoriteSongs"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

def infoDB():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    infoDB()

