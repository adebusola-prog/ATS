# bin_number = int(input("Enter a binary number: "))

# bin_digits = []

# while bin_number > 0:
#     bin_digits = [bin_number % 10] + bin_digits
#     bin_number = int(bin_number / 10)

# print(bin_digits) # conversion of the binary number to a list

# accumulator = 0  # contains the final result
# i = 0   # positional value for each bin digit
# len_bin = len(bin_digits) - 1
# while len_bin >= 0:
#     accumulator += bin_digits[len_bin] * i
#     i *= 2
#     len_bin -= 1

# print(accumulator)

# [1, 1, 0, 1][2]*1
#convert the binary to a list so that you can iterate over it-> d that by converting to a string and then convert to a list and append
c = []
x = 1101
y = str(x)
z = list(y)
# print(z)
for i in z:
    i = int(i)
    # print(i)
    c.append(i)
# print(c)

# print(len(c)) 
k = []
for index, item in enumerate(c):
    # print(index, item)
    v = str(index)
    print(list(v))



# x = [1, 1, 0, 1]
# print(x[0])

# vowels rep. with special characters
# vowels = {"a": "#", "e": "$", "i": "%", "o": "&", "u": "*", "A": "#", "E": "$", "I": "%", 
# "O": "&", "U": "*"}
# consonants = {"0": "z", "1": "y", "2": "x", "3": "w", "4": "v", "5": "t", "6": "s", "7": "r", "8": "q", 
# "9": "p"}
# special_chars = ["@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}",
# "{", "~", ":"]

# # user_input = input("Enter the string to encode: ")


# def encode_text(user_input):
#     split_input = list(user_input)
#     encoded = ""
#     for char in split_input:
#         if char in list(vowels.keys()):
#             encoded += vowels[char]
#         elif char in list(consonants.keys()):
#             encoded += "^" + consonants[char]
#         elif char.isalpha():
#             encoded += char.upper()
#         elif char in special_chars:
#             encoded += "|" + char
#     return encoded


# print(encode_text("adeola"))

# encoded_text = input("Enter the encoded text: ")
# # def decode_text():
# split_input = list(encoded_text)
# decoded = ""

