book = {"apple": 0.67, "milk": 1.49, "avocado": 1.49}
print(book['apple'])
print(book)


voted = {}
def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        print(voted.get(name))
        voted[name] = True
        print(voted.get(name))
        print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")


