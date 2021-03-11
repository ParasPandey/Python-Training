s=input()
ca=0 #for count occurance of a
ce=0 #for count occurance of b
ci=0 #for count occurance of c
co=0 #for count occurance of d
cu=0 #for count occurance of e
ans=set() # contains vowels which are present in string

for i in s:
	if i=="a" or i=="A": #checking for vowel a and A
		ca+=1
		ans.add("a")
		
	elif i=="e" or i=="E": #checking for vowel e and E
		ce+=1
		ans.add("e")
		
	elif i=="i" or i=="I": #checking for vowel i and I
		ci+=1
		ans.add("i")
		
	elif i=="o" or i=="O": #checking for vowel o and O
		co+=1
		ans.add("o")
		
	elif i=="u" or i=="U": #checking for vowel u and U
	
		cu+=1
		ans.add("u")

#print vowels which are present in string with no. of occurence.
print("Total vowels present are : ", ans)
print("a: ",ca)
print("e: ",ce)
print("i: ",ci)
print("o: ",co)
print("u: ",cu)
