def transfer_cash(n):
    h = 50000
    if n == h:
        return True
    if n < h:
        return True
    if n > h:
        return False
number = int(input("enter number"))
if transfer_cash(number):
    print("oya now")
else:
    print("no way")
