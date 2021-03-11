s=input()
ca=0
ce=0
ci=0
co=0
cu=0
ans=set()
for i in s:
	if i=="a" or i=="A":
		ca+=1
		ans.add("a")
	elif i=="e" or i=="E":
		ce+=1
		ans.add("e")
	elif i=="i" or i=="I":
		ci+=1
		ans.add("i")
	elif i=="o" or i=="O":
		co+=1
		ans.add("o")
	elif i=="u" or i=="U":
		cu+=1
		ans.add("u")
print("Total vowels present are : ", ans)
print("a: ",ca)
print("e: ",ce)
print("i: ",ci)
print("o: ",co)
print("u: ",cu)