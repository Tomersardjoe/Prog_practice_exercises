def new_password(oldpassword, newpassword):
    lenpass = len(newpassword)
    if newpassword != oldpassword and lenpass > 6:
        print(1 == 1)
    else:
        print(1 == 0)

new_password('kaas', 'boterenkaas')
