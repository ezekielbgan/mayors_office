# IMPORTS

import random
from events import events


# BASE STATISTICS

year = 0
population = 50 
budget = 50
approval = 50
infrastructure = 50


# FUNCTIONS

def show_stats(show_changes=False):
    if show_changes:
        population_change = population - old_population
        budget_change = budget - old_budget
        approval_change = approval - old_approval
        infrastructure_change = infrastructure - old_infrastructure

        def format_change(change):
            if change >= 0:
                return "+" + str(change)
            else:
                return str(change)

        print("Population:", str(population) + "/100 (" + format_change(population_change) + ")")
        print("Budget:", str(budget) + "/100 (" + format_change(budget_change) + ")")
        print("Approval:", str(approval) + "/100 (" + format_change(approval_change) + ")")
        print("Infrastructure:", str(infrastructure) + "/100 (" + format_change(infrastructure_change) + ")")
    else:
        print("Population:", str(population) + "/100")
        print("Budget:", str(budget) + "/100")
        print("Approval:", str(approval) + "/100")
        print("Infrastructure:", str(infrastructure) + "/100")


def limit_stats():
    global population, budget, approval, infrastructure

    population = max(0, min(100, population))
    budget = max(0, min(100, budget))
    approval = max(0, min(100, approval))
    infrastructure = max(0, min(100, infrastructure))


def check_game_over():
    if population == 0:
        print("Your population has dropped to zero. Typically, your secretary would arrive to let you know, but they are nowhere to be found. You are the sole mayor (and resident) of a ghost town.")
        print()
        print("GAME OVER")
        return True

    if budget == 0:
        print("Your city's funds have been depleted. Your secretary presents you with the latest financial report and informs you that you no longer need to worry about balancing the budget, because there is nothing left to balance.")
        print()
        print("GAME OVER")
        return True

    if approval == 0:
        print("Your approval rating has reached zero. For the first time during your administration, your secretary has no encouraging words to offer.")
        print()
        print("GAME OVER")
        return True

    if infrastructure == 0:
        print("Your infrastructure score has reached zero. Your secretary attempts to deliver the infrastructure report but is unable to find a functioning road to City Hall.")
        print()
        print("GAME OVER")
        return True

    return False


# GAME INTRODUCTION
print("MAYOR'S OFFICE")
print()
print("Congratulations! The citizens of your city have elected you as their new mayor.")
print()
print("Before we begin, what should we call you?")
print()
name = input("Enter your name: ")
print()
print("Mayor", name + ", huh? Welcome to City Hall. Your mission is simple:")
print()
print("Guide your city through challenges, balance the needs of your citizens, and help your city thrive for as long as possible.")
print()
print()


# YEAR 0 SETUP

print("YEAR", year)
print()
print("Your secretary presents you with your first ever city report. Would you like to read it?")
print()
print("1. Yes")
print("2. No")
print()

if input("Enter the number of your choice: ") == "1":
    print()
    show_stats()
else:
    print()
    print("Just kidding! You don't have a choice. You're a mayor now, so reading reports is a part of your job description.")
    print()
    show_stats()

print()
print("Your term begins now.")
print()
print("Good luck, Mayor", name + "!")
print()
print()


# YEAR 1 SETUP

last_event = None
year += 1

print("YEAR", year)
print()
print("Your secretary enters your office with an urgent update and directs your attention to the latest news coverage.")
print()

current_event = random.choice(events)

while current_event == last_event:
    current_event = random.choice(events)

print("BREAKING NEWS:", current_event["event_description"])
print()
print("Your secretary schedules an emergency meeting with your advisors and department heads.")
print()
print("After careful deliberation, your administration has narrowed the possible responses down to three options. The final decision, however, belongs to you, Mayor", name + ".")
print()
print("1.", current_event["choices"][0]["choice_description"])
print("2.", current_event["choices"][1]["choice_description"])
print("3.", current_event["choices"][2]["choice_description"])
print()

while True:
    choice = input("Enter the number of your choice: ")

    if choice in ["1", "2", "3"]:
        break

    print("Please enter 1, 2, or 3.")

old_population = population
old_budget = budget
old_approval = approval
old_infrastructure = infrastructure

selected_choice = current_event["choices"][int(choice) - 1]

population += selected_choice["population_change"]
budget += selected_choice["budget_change"]
approval += selected_choice["approval_change"]
infrastructure += selected_choice["infrastructure_change"]

limit_stats()

print()
print("You've made your decision. Now, it's time to wait and see how the city responds.")
print()
print()

if check_game_over():
    quit()

last_event = current_event


# MAIN GAME LOOP

old_population = population
old_budget = budget
old_approval = approval
old_infrastructure = infrastructure

while True:
    year += 1

    print("YEAR", year)
    print()
    print("Happy New Year, Mayor", name + "! The city is still standing, and you return to your office to review the annual municipal summary.")
    print()
    show_stats(True)
    print()
    print("Your secretary enters your office with an urgent update and directs your attention to the latest news coverage.")
    print()

    current_event = random.choice(events)

    while current_event == last_event:
        current_event = random.choice(events)

    print("BREAKING NEWS:", current_event["event_description"])
    print()
    print("Your secretary schedules an emergency meeting with your advisors and department heads.")
    print()
    print("After careful deliberation, your administration has narrowed the possible responses down to three options. The final decision, however, belongs to you, Mayor", name + ".")
    print()
    print("1.", current_event["choices"][0]["choice_description"])
    print("2.", current_event["choices"][1]["choice_description"])
    print("3.", current_event["choices"][2]["choice_description"])
    print()

    while True:
        choice = input("Enter the number of your choice: ")

        if choice in ["1", "2", "3"]:
            break

        print("Please enter 1, 2, or 3.")

    old_population = population
    old_budget = budget
    old_approval = approval
    old_infrastructure = infrastructure

    selected_choice = current_event["choices"][int(choice) - 1]

    population += selected_choice["population_change"]
    budget += selected_choice["budget_change"]
    approval += selected_choice["approval_change"]
    infrastructure += selected_choice["infrastructure_change"]

    limit_stats()

    print()
    print("You've made your decision. Now, it's time to wait and see how the city responds.")
    print()
    print()

    if check_game_over():
        break

    last_event = current_event