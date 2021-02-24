import time
su={'a':'1','w':'4'}

#welcome
print('Welcome to Pizzeria')

#wait
def wait():
    for i in [3,2,1]:
        time.sleep(.5)
        print(i,end='... ')
    print()
        
#registration no
def register():
    return int(time.monotonic())
        
#signup  
def signup():
        a= input('Sign-up\nFull name :')
        b= input('Email :')
        c= input('Password :')
        su[b]='c'
        
#Login- section        
def ln(i=0):
    q=input('Email :')
    a={}        
    if q in su:
        while i!=3:
            print('Enter password')
            a[q]=input('password :')
            if a[q] == su[q]:
                wait()
                print('yipeee your are in for some amazing surprize')
                return True
            else:
                print('Invalid password ,Please reenter Password')
                i+=1           
    wait()
    print('Email invalid, please signup')
    signup()
    ln()
ln()


