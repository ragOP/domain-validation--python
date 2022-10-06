name=[]
Email=[]
age=[]
phone_number=[8447648730,9006123123]
test_str = 'afifa.noor@bibs.co.in'
res = test_str[test_str.index('@') + 1 : ]

print("The extracted domain name : " +str(res))
print("Book Your Ticket")


names=input("Enter your Name= ") 
your_age=int(input("Enter Your Age= "))
contact_number=int(input("Enter your phone number without std code= "))
if contact_number in phone_number:
        print("Already Registered")
else:
        email_id=input("Enter your Email id = ")
        emailidcheck=email_id[email_id.index('@') + 1 : ]
        print(str(res))
        print(str(emailidcheck))
        if str(res)==str(emailidcheck):
            print("match")
        else:
            print("not match")
            email_id=input("Enter your Email id = ")