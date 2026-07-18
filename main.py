# IMPORTS
import random
from events import events


# CONFIGURATION
BASE_STAT = 50
MAX_STAT = 100
MIN_STAT = 0
BANNER_WIDTH = 40
HEADER_WIDTH = 40


# BASE VARIABLES
year = 0
last_event = None

population = BASE_STAT 
budget = BASE_STAT
approval = BASE_STAT
infrastructure = BASE_STAT


# FUNCTIONS
def show_stats(show_changes=False):
    print("-" * 40)
    print("ANNUAL MUNICIPAL REPORT".center(BANNER_WIDTH))
    print()
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
            
        value = f"{population}/{MAX_STAT} ({format_change(population_change)})"
        print(f"{'Population':<15}{value:>25}")
        value = f"{budget}/{MAX_STAT} ({format_change(budget_change)})"
        print(f"{'Budget':<15}{value:>25}")
        value = f"{approval}/{MAX_STAT} ({format_change(approval_change)})"
        print(f"{'Approval':<15}{value:>25}")
        value = f"{infrastructure}/{MAX_STAT} ({format_change(infrastructure_change)})"
        print(f"{'Infrastructure':<15}{value:>25}")
        print("-" * HEADER_WIDTH)
    else:
        print(f"{'Population':<34}{population}/{MAX_STAT}")
        print(f"{'Budget':<34}{budget}/{MAX_STAT}")
        print(f"{'Approval':<34}{approval}/{MAX_STAT}")
        print(f"{'Infrastructure':<34}{infrastructure}/{MAX_STAT}")
        print("-" * HEADER_WIDTH)

def limit_stats():
    global population, budget, approval, infrastructure
    population = max(MIN_STAT, min(MAX_STAT, population))
    budget = max(MIN_STAT, min(MAX_STAT, budget))
    approval = max(MIN_STAT, min(MAX_STAT, approval))
    infrastructure = max(MIN_STAT, min(MAX_STAT, infrastructure))

def check_game_over():
    if population == MIN_STAT:
        print("Your population has dropped to zero. Typically, your secretary would arrive to let you know, but they are nowhere to be found. You are the sole mayor (and resident) of a ghost town.")
        print()
        show_banner("GAME OVER")
        return True
    if budget == MIN_STAT:
        print("Your city's funds have been depleted. Your secretary presents you with the latest financial report and informs you that you no longer need to worry about balancing the budget, because there is nothing left to balance.")
        print()
        show_banner("GAME OVER")
        return True
    if approval == MIN_STAT:
        print("Your approval rating has reached zero. For the first time during your administration, your secretary has no encouraging words to offer.")
        print()
        show_banner("GAME OVER")
        return True
    if infrastructure == MIN_STAT:
        print("Your infrastructure score has reached zero. Your secretary attempts to deliver the infrastructure report but is unable to find a functioning road to City Hall.")
        print()
        show_banner("GAME OVER")
        return True
    return False

def show_banner(title):
    print("=" * BANNER_WIDTH)
    print(title.center(BANNER_WIDTH))
    print("=" * BANNER_WIDTH)

def show_header(title):
    print((" " + title + " ").center(HEADER_WIDTH, "-"))


# GAME INTRODUCTION
show_banner("MAYOR'S OFFICE")
print()
print("Welcome to City Hall.")
print()
print("Today marks the beginning of a new administration.")
print()
print("Before your first day can begin...")
print()
print("What should we call you?")
print()
name = input("Enter your name: ")
print()
print()
print("Welcome, Mayor " + name + ".")
print()
print("Your oath of office has been administered, your desk has been cleared, and your first briefing is ready.")
print()
print("The decisions you make will shape the future of your city.")
print()
print("Good luck, Mayor.")
print()
print()


# YEAR 0 SETUP
show_header("YEAR " + str(year))
print()
print("Your secretary enters the office carrying your first city report.")
print()
print("Would you like to review it?")
print()
print("1. Yes")
print("2. No")
print()
if input("Enter the number of your choice: ") == "1":
    print()
    print()
    show_stats()
else:
    print()
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


# MAIN GAME LOOP
while True:
    year += 1
    show_header("YEAR " + str(year))
    print()

    if check_game_over():
        break

    if year > 1:
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
    print()
    print("You've made your decision. Now, it's time to wait and see how the city responds.")
    print()
    print()
    last_event = current_event