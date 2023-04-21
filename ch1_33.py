import statistics

print("*** Election ***")
inp=int(input("Enter a number of voter(s) : "))
votes=[]
votef=[]
for i in range(0,inp):
    vote=input()
    if 1<=vote<= 20:
        votes.append(vote)
    else:
        votef.append(vote)
        # print("*** No Candidate Wins ***")
for x in range(len(votes)):
    print(votes[x], end=" ")
    
print()
# print(votef)
print(int(statistics.median(votes)))
