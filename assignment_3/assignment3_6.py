# 6. The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages is shifted by a number of places down the alphabet. Write a function CustomCaesarCipher(int key, String message) which will accept plaintext and key as input parameters and returns its cipher text as output.

def CustomCaesarCipher(key, message):
    if key < 0:
        return "INVALID INPUT"
    
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isdigit():
            result += str((int(char) + key) % 10)
        else:
            result += char
    return result

plaintext = input("Enter your PlainText: ")
key = int(input("Enter the Key: "))
encrypted = CustomCaesarCipher(key, plaintext)
print(f"The encrypted Text is: {encrypted}")
