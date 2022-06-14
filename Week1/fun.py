import string
def encode(data:str):
    digits = string.digits = [0,1,2,3,4,5,6,7,8,9,]
scharr = string.punctuation = ()
alpha_lower = string.ascii_lowercase = ()
alpha_upper = string.ascii_uppercase
reverse_alpha_lower = alpha_lower [: : -1] 
vowels = ["a","e","i","o","u"]
vowels_map = ['#', '$', '%','&','*']
enc = list()
for s in (data):
    if s.lower () in vowels:
        enc.append((vowels_map)(vowels.index(s)))
    elif s in schers:
        enc.append ('|' + s)
    elif s in alpha_lower or s in alpha_upper:
        enc.append(s.swapcase)
    elif s in digits: if s in alpha_lower:
        enc.append('n' + rev_alpha_lower(digits.index(s))
    else:
        enc.append(s)


