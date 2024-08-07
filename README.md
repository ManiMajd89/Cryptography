# Cryptography
Cryptography has been studied for thousands of years to create secret messages that only the sender and recipient could read. The secret code system (or algorithm) used for encrypting and decrypting messages is called a cipher. Even if the messenger were captured, it would not help in decoding the message, since only the sender and recipient would know the cipher. More precisely, everyone might know the algorithm, but the key to the cipher is only known to the sender and receiver.

One early example of cryptography is the Caesar cipher, which encrypts a message by taking each letter in the message and replacing it with a “shifted” letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C. The Caesar cipher is overly simple and it wouldn’t take much to break the encryption. Even though the Caesar cipher is no longer used, it still makes for a great learning example for cryptography.

Define the Problem
Given a sensitive message that should not be read by others, I wanted to devise an algorithm to encrypt the message so that only someone with the secret key can access it. There are many options available for encryption, ranging from classic methods that are not secure to more modern ones that are highly mathematical. Since the message being encrypted is not of great importance, it makes sense to use an easier implementation, such as the Caesar cipher.

More precisely, I developed code to do two things using the Caesar cipher:

Prompt the user for a message, a secret key, and whether they want the message encoded or decoded.
Encode or decode the message using a Caesar cipher and print it out.

## The Caesar Cipher
The Caesar cipher is one of the simplest and oldest encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### How it Works
* Shift (Key): A secret key (number) is chosen, which determines how many positions each letter in the plaintext will be shifted.
* Encoding: To encode a message, each letter in the plaintext is shifted to the right by the value of the key.
* Decoding: To decode a message, each letter in the ciphertext is shifted to the left by the value of the key.

For example, with a key of 3:

- Plaintext: HELLO
- Ciphertext: KHOOR

Here's how each letter is shifted:

H -> K (H is the 8th letter, K is the 11th, so shifted by 3)
E -> H (E is the 5th letter, H is the 8th, so shifted by 3)
L -> O (L is the 12th letter, O is the 15th, so shifted by 3)
L -> O (Same as above)
O -> R (O is the 15th letter, R is the 18th, so shifted by 3)

### The ASCII Table
The ASCII (American Standard Code for Information Interchange) table is a character encoding standard for electronic communication. It represents text in computers and other devices that use text.

Each character is assigned a unique integer value. For example:

'A' -> 65
'B' -> 66
'C' -> 67
'a' -> 97
'b' -> 98
'c' -> 99

Understanding ASCII values is crucial for implementing the Caesar cipher in code, as it allows us to convert characters to their integer values, perform the shift, and convert them back to characters.
