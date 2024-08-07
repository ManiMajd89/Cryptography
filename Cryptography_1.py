message = input("Please enter the secret message: ")
key = input("Please enter a key: ")

while (type(key)!= int) and int(key) < 0:
    print("Please enter a positive integer value for key!")
    key = int(input("Please enter a key: "))

instruction = input("Decode or Encode? ")

while instruction.lower() != "decode" and instruction.lower() != "encode":
    print("Please enter either 'Decode' or 'Encode'")
    instruction = input("Decode or Encode: ")

#Encryption

if instruction == "Encode" or instruction == "encode":
    encode = ""
    for character in message:
        if character.isalpha():
            key = int(key)
            new_ord = ord(character) + key
            if new_ord > ord('z') and character.islower():
                new_ord -= 26
                new_chr = chr(new_ord)
                encode += new_chr
            elif new_ord > ord('Z') and character.isupper():
                new_ord -= 26
                new_chr = chr(new_ord)
                encode += new_chr
            else:
                new_chr = chr(new_ord)
                encode += new_chr
        else:
            encode += character
    print("Encryption: ", encode)


#Decryption

elif instruction == "Decode" or instruction == "decode":
    decode = ""
    for character in message:
        if character.isalpha():
            key = int(key)
            new_ord = ord(character) - key
            if new_ord < ord('a') and character.islower():
                new_ord += 26
                new_chr = chr(new_ord)
                decode += new_chr
            elif new_ord < ord('A') and character.isupper():
                new_ord += 26
                new_chr = chr(new_ord)
                decode += new_chr
            else:
                new_chr = chr(new_ord)
                decode += new_chr
        else:
            decode += character
    print("Decryption: ", decode)
    