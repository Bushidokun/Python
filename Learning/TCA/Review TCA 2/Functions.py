def is_league_united(hero1, hero2):
    if hero1 == "Superman" and hero2 == "Wonder Woman":
        return True
    elif hero1 == "Wonder Woman" and hero2 == "Superman":
        return True
    else:
        return False

def decide_plan(hero1, hero2):
    if is_league_united(hero1, hero2) == True:
        print ("Time to save the world!")
    else:
        print ("We must unite the league!")

def run():
    print ("Who is the first hero?")
    hero1 = input()
    print ("Who is the second hero")
    hero2 = input()

    print ("League or Plan?")
    response = input()

    if response == "League":
        print (is_league_united(hero1, hero2))
    elif response == "Plan":
        decide_plan(hero1, hero2)
    else:
        print ("Invalid command. Please try again.")

run()