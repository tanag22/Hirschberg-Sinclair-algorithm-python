from random import shuffle
n=int(input("Enter no. of processes: "))
process=[int(j) for j in range(n)]
shuffle(process)
leaders=process[:]
print(process)
#l is round number
for l in range(n):
	dist=2**l
	print("-----------------------------------------")
	print("Round ",l)
	print("Dist : ",dist)
	
	print("Leaders: ",leaders)
	for leader in list(leaders):
		print("------------------")
		ind=process.index(leader)
		print("Index : ",ind)
		if ind-dist<0:
			tempL=process[ind-dist:]+process[:ind+dist+1]
		
		elif ind+dist>=n:
			k=(ind+dist)%n
			tempL=process[ind-dist:ind]+process[ind:]+process[:k+1]
		else:
			tempL=process[ind-dist:ind]+process[ind:ind+dist+1]
		print("Sending messages to : ",tempL)
		if leader!=max(tempL):
			print(leader," not selected because",max(tempL),"didn't send back message")
			leaders.remove(leader)
			print("Leaders: ",leaders)
		else:
			print(leader," selected")
			print("Leaders: ",leaders)
	if len(leaders)==1:
		print(leaders[0],"is the leader")
		print("No. of rounds:",l+1)
		break	
		
		
