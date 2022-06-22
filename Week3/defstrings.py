#Write a function that takes a two strings as an argument and prints if the first string is a substring of the second.
def arg(x:str,y:str):
    if x in y:
        return True
    else:
        return False

print(arg('fellow', 'fellowship'))


#Write a function that converts a string to uppercase and returns the result.
def pha(x:str):
    y = x.upper()
    return y


print(pha("alliance"))

#Write a function that converts a string to lowercase and returns the result.
def phaa(x:str):
    y = x.lower()
    return y


print(phaa("REWARD"))

#Write a function that converts a string to titlecase and returns the result.
def fadd(z:str):
    y = z.title()
    return y


print(fadd("boy"))


#Write a function that converts the first letter of each word in a sentence to uppercase.
def sent(d:str):
    r = d.title()
    return r


print(sent("i am still going to school today"))


#Write a function that checks if a string contains both alphabets and numbers.
def alnm(c:str):
    if c.isalnum:
        return True
    else:
        return False

print(alnm("ade123"))
    
     



