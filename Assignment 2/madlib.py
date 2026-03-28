#madlib.py
#Maddy Malm
#1/10/2026


#This program uses inputs to create a Mad Lib.
#Users input the prompted parts of speech
#to complete the story.

print("Hello and Welcome!\nMy name is Maddy, and I have written a story I need you to fill out.")
print("I will ask you for a noun, adjective, proper noun, \nadverb, and verb respectively.")
print("Fill these out, and you will recieve a written story with your chosen words.")
print("Don't have too much fun!")
noun = input("Tell me a noun: ")
adjective = input("Tell me an adjective: ")
proper_noun = input("Tell me a proper noun (someone's name): ")
adverb = input("Tell me an adverb (please capitalize): ")
verb = input("Tell me a past-tense verb: ")

print("The", noun, "barked wildly up and down the porch.")
print("Its", adjective, "tail wagged.")
print("Soon,", proper_noun, "came and pushed away the", noun, "from the entrance.")
print(adverb, ", the", noun, "moved.")
print("After a while, the", noun, "tired of pacing. Instead, it", verb, ".")
