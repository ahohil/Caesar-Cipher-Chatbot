import string
import nltk


#Dictionary for encrypting user statement
#Each letter of the alphabet is assigned to a letter 3 spaces ahead of it, also known as the Caesar Ciphor.
#When a later function "loops through it", that means a loop will replace each character with its key equivalent from the dictionary. This is what allows us to actually encrypt a message. So, for example, if I input the statement "hi," the encrypted message would be "kl".
#Original Code

"""
Dictionary with length of 26 characters long
"""

cipher_dictionary = {
    
    "a" : "d",
    "b" : "e",
    "c" : "f",
    "d" : "g",
    "e" : "h",
    "f" : "i",
    "g" : "j",
    "h" : "k",
    "i" : "l",
    "j" : "m",
    "k" : "n",
    "l" : "o",
    "m" : "p",
    "n" : "q",
    "o" : "r",
    "p" : "s",
    "q" : "t",
    "r" : "u",
    "s" : "v",
    "t" : "w",
    "u" : "x",
    "v" : "y",
    "w" : "z",
    "x" : "a",
    "y" : "b",
    "z" : "c",
}


#Remove punctuation function
#Original Code that I wrote on my own. But I realized after looking through previous assignments that it's adapted from A2

def remove_punctuation(phrase):
    """
    Function removes punctuation

    Parameters
    ----------
    phrase : str
            Phrase that needs punctuation removed
    Returns
    -------
    output : str
            Phrase with punctuation removed
    """
    output = ""
    for characters in phrase:
        if not characters in string.punctuation:
            output += characters
    return output

#Function that takes user input and applies the remove_punctuation function to it and lowercases all letters of user's inpt so the message can be encrypted.
#Original Code

def bot_asks_question(question):
    """
    Function to ask user a question and process the answer (remove punctuation and lowercase all letters).
    """
    print(question)
    user_statement = input('INPUT: \t')
    
    user_statement = remove_punctuation(user_statement)
    user_statement = user_statement.lower()
    
    return user_statement


#Encryption function
#Encrypts user input statements by looping through cipher_dictionary and replacing each character the user inputs with its corresponding key. It then saves this result to encrypted_msg
#Original Code

def encrypt_message(unencrypted_msg):
    """
       Function that takes argument and replaces each character with its corresponding key from 
       cipher_dictionary.
       Turns an unencrypted message into an encrypted message.
    """
    encrypted_msg = ""
    for item in unencrypted_msg:
        key = item
        if key in cipher_dictionary:
            encrypted_msg += cipher_dictionary[key]
            
    return encrypted_msg