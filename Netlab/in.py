print

haystack = ("Python rules!")

print (haystack, "\n")

needle = input("Enter a character to search for:  ")

if needle in haystack:
    print ("Yes!")
else:
    print("No!")