import string
import random
SECURE=(('s','$'),('and','&'),("a",'@'),('o','0'),('i','1'))
def securePassword(password):
    for a,b in SECURE:
        password=(password.replace(a,b))
    return password

if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    plen=input("Enter the length of password\n")
    if plen.isdecimal():
        p=int(plen)
        if p<8:
            print("Please enter a bigger number for more security")
        else:
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            #print(s)
            #random.shuffle(s)
            #print(s)
            print("Your password is: ")
            p1="".join(s[0:p])
            print(securePassword(p1))
    else:
        print("Enter a valid password length")