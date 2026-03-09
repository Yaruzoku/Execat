import random
import time

level = 1
xp = 0
xp_to_next = 20

hunger = 5
happiness = 5
energy = 5
perfect_turns = 0  # tracks perfect care, easier to get to than you might think
divine_unlocked = False 

# Function to show the gato
def show_pet(level, secret=False):

    if secret:
        print(r"""
 /\_/\ ⋆˙
( ⟡_⟡)
 /| |\
DIVINE EXECAT
""")
    elif level <= 3:
        print(r"""
 /\_/\ 
( o.o )
 > ^ <
Kitten stage
""")
    elif level <= 7:
        print(r"""
 /\_/\ 
( •.• )
 / UU
Cat stage
""")
    else:
        print(r"""
 /\_/\ 
( 0_0 )
 /| |\
CHAOS EXECAT
""")

print("Welcome to Execat!")
show_pet(level)

name = input("Name your pet: ")

while True:

    # Separator and stats
    print("\n" + "-"*40 + "\n")
    print(f"--- {name}'s stats ---")
    print(f"Hunger: \033[91m{hunger:.1f}\033[0m")
    print(f"Happiness: \033[92m{happiness:.1f}\033[0m")
    print(f"Energy: \033[94m{energy:.1f}\033[0m")

    show_pet(level)

    # Cat reactions
    if hunger <= 2:
        print(name, "is full and happy!")
    elif hunger <= 6:
        print(name, "is a bit hungry...")
    else:
        print(name, "is starving!")

    if happiness >= 10:
        print(name, "is having zoomies!")

    if energy <= 4:
        print(name, "is a bit eepy...")

    # Random event
    if random.random() < 0.2:
        sayings = [
            "I want treats!",
            "Zzz...",
            "Execat knocks over a plant. Oops.",
            "Execat demands you bow to the cat overlord. Again.",
            "Execat has a staring contest with the wall… and wins.",
            "Oooo there's a bird outside. Execat is going FERAL!"
        ]
        print(random.choice(sayings))

    negative_events = [
        "Execat's favorite toy fell behind the couch... Poor thing.",
        "Execat ate too much and its tummy hurts.",
        "Execat hates Mondays. Me too..." # we love a proper Garfield reference 
    ]

    if random.random() < 0.1:  
        happiness -= 2
        print(random.choice(negative_events))

    # Player choices
    print("\nWhat do you want to do?")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Quit")
    choice = input("> ")

    if choice == "1":
        hunger -= 2
        xp += 3
        print(name, "enjoyed the noms!")
    elif choice == "2":
        happiness += 2
        energy -= 1
        hunger += 1
        xp += 5
        print(name, "had fun playing!")
    elif choice == "3":
        energy += 3
        xp += 2
        print(name, "took a nice nap.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

    # Time passing
    hunger += 0.2
    energy -= 0.2

    # Keep stats between 0 and 10
    hunger = max(0, min(10, hunger))
    happiness = max(0, min(10, happiness))
    energy = max(0, min(10, energy))

    # Level up
    if xp >= xp_to_next:
            level += 1
            xp = 0
            xp_to_next += 10
            print(f"\nLEVEL UP!⋆˙⟡ ")
            print(f"{name} reached level {level}!")
            if level == 4:
                print(f"{name} evolved into a grown CAT!")
            elif level == 8:
                print(f"{name} has become a CHAOS EXECAT!")

    # Perfect care counter for secret evolution ⋆˙⟡ 
    if hunger <= 2 and happiness >= 8 and energy >= 6:
        perfect_turns += 1
    else:
        perfect_turns = 0  # resets if cat aint perfect

    if perfect_turns >= 5 and not divine_unlocked:
        divine_unlocked = True
        print("\nSECRET EVOLUTION UNLOCKED!⋆˙⟡ ")
        print(f"{name} has achieved ultimate harmony and becomes a DIVINE EXECAT!")
        show_pet(level, secret=True)

    # DIVINE EXECAT random events
    if divine_unlocked:
        chaos_events = [
            "Execat throws a hairball… on your keyboard! Weirdo...",
            "Execat summons 42 invisible mice… they’re everywhere! What is its problem?",
            "Execat rearranges all your desktop icons… magically. What the hell???",
            "Execat zoomies through the room at lightning speed! Get all valuables out of the way.",
            "Execat demands a feast of 7 tuna cans immediately. Fatass.",
            "Execat stares at you menacingly… then falls asleep."
        ]
        if random.random() < 0.5: 
            print("DIVINE EXECAT: " + random.choice(chaos_events))

    # Losing conditions
    if happiness <= 2:
        print("\nHow dare you neglect Execat's happiness...")
        print("Accessing system files...")
        print("Installing catOS...")
        print("Your computer now belongs to Execat.")
        print(r"""
 /\_/\ 
(╬ಠ益ಠ)
 /| |\
""")
        break

    if hunger >= 10:
        print(name, "starved, maybe don't get a Tamagotchi... game over.")
        print(r"""
 /\_/\ 
( x_x )
 > ^ <
""")
        break

    if energy <= 0:
        print(name, "collapsed from exhaustion, at least give it a Monster or something next time... game over.")
        print(r"""
 /\_/\ 
( x_x )
 > ^ <
""")
        break

    time.sleep(0.5)
    