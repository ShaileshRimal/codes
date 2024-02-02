letter=input("Enter the  Character: ")

def vow(char):
    vowe="aeiou"
    if char in vowe:
        return "is vowel"
    else:
        return "is not vowel"
print(vow(letter))