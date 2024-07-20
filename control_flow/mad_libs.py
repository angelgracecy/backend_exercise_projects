# Mad Libs Game

# Prompt the user for inputs
name = input("Enter a name: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

# Conditional variations
if animal.lower() == "cat":
    animal_action = "purred"
else:
    animal_action = "roared"

# Construct the story
story = f"""
hello meet my brother {name}. {name} had a pet {animal} that loved to {verb}. 
One day, they went to {place} together. It was a very {adjective} day. 
As they were walking, the {animal} suddenly {animal_action} and everyone was amazed. 
{name} was so proud of their {adjective} {animal}.
"""

# Display the final story
print(story)

