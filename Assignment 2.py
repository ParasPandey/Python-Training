print("MESSAGE SENDER")
print("Hello Mit Cell")
k=int(input("Please enter k value to shift transform message: "))
if k<20 and k>1: #check  range of k
    print("The value of k should be between 1 and 20: ")
msg=input("Enter Your Message: ")
newmsg=""
for i in msg:
    if i.isalnum():  #Check for alphabet or numbers
        a=ord(i)  #get ascii value of character
        newmsg+=chr(a+k) #add k in ascii value and then convert it back in character

    elif i==" ":  #check for space
        newmsg+="@"  #if space then we insert(add) @ in newmsg

    elif i==".":  #check for .
        newmsg+="#"  #if . then we insert(add) # in newmsg
         #
    else:
        newmsg+=i   #if neither condition matched then we just copy same character

print("MESSAGE RECEIVER:  ")
print("Hello Instructor:")
print("You Got a Message: ",newmsg) #print encrypted msg
k1=int(input("To read this in original please type k value provided by Cell: "))
if k1==k: #check if value of k for sender and receiver
    print("Original message:",msg) #if same, print original msg
else:
    print("Invalid key value") #if not same, print invalid
# print(newmsg)
