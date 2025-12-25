full_dot = '●'
empty_dot = '○'
Welcome_message = "Welcome to the RPG Character Creator!"
print(Welcome_message)

name = input("Enter the character name: ")
strength = int(input("Enter the strength: "))
intelligence = int(input("Enter the intelligence: "))
charisma = int(input("Enter the charisma: "))


def create_character(name,strength,intelligence,charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    for letter in name:
        if letter == " ":
            return "The character name should not contain spaces"
    
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"
    if not all(stat >= 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Build 10-dot bars
    def bar(value):
        return full_dot * value + empty_dot * (10 - value)

    # Return EXACT formatted output (newline separated)
    return (
        f"{name}\n"
        f"STR {bar(strength)}\n"
        f"INT {bar(intelligence)}\n"
        f"CHA {bar(charisma)}"
    )

print(create_character(name,strength,intelligence,charisma))