import string

alphas=string.ascii_letters+'_'
nums=string.digits

print("welcome to the identifier checker v1.0")
print("testees must be at least 2 chars long.")
myInput=input("identifier to test?")

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print("invalid first symbol must be alphabetic")
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print('''s
                    invalid:remaining symbols must be alphanumberic
                ''')
                break
        else:
            print("okay as an identifier")
else:
    print("less than two characters")
