print("7. Check if a char is vowel or consonant")
char = input("Enter any letter: ")

vowel = ["a", "e", "i", "o", "u"]

match True:
    case _ if not char.isalpha() or len(char) != 1:
        print("Invalid input. Please enter a single alphabet.")
    case _ if char.lower() in vowel:
        print(char, "is vowel")
    case _:
        print(char, "is consonant")
