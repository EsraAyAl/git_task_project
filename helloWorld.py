def reverse_text(text):
    return text[::-1]

#This program accept input from the user
name=input("Can you enter your name please?:")
#print input name
print("Your name is" + " " + name)

#reverse the given input and print reversed text
reversed_text = reverse_text(name)
print("Your name reversed:", reversed_text)