"""
Solve this problem:
Each action has a 67% chance of success.
Each time action fails, chance of success decreases by 0.5%.
Each time action succeeds, chance of success increases by 1%.
"""
import random
def action(chance: float, iterations: int):
    """
    Calculates if actions suceeds or not and calls itself again.
    """
    while (iterations < 100000 and chance < 99):
        next_chance = 0
        if random.randint(0, 100) + ((random.randint(0, 100) - 50) / 100) <= chance:
            next_chance = chance + 1
            print(f"It. {iterations}: Action succeeded. Chance is now {next_chance}%")
            input("Press Enter to continue...")
        else:
            next_chance = chance - 0.5
            print(f"It. {iterations}: Action failed. Chance is now {next_chance}%")
            input("Press Enter to continue...")
        action(next_chance, iterations + 1)
    print("Done")

action(67, 0)
