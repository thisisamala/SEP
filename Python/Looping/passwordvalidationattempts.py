password="yaMaLama"
user=input("Enter the password")
tryy=user
if(user==password):
    print("Access Granted")
else:
    while(tryy!=password):
        for x in range (1,4):
            print(x,end='')
            tryy=input(" Attempt ")
            if(tryy==password):
                print("Access Granted")
                break
            else:
                print("Access Denied")
        break   
    
           
            
        
            