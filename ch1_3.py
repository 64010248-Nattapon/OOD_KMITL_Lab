print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
votes = input()
vote_list = votes.split()

saveInt = []
saveN = []
for vote in vote_list:
    if 1 <= int(vote) <= 20:
        saveInt.append(vote)
        continue
    else:
        saveN.append(vote)


def find_mode(saveInt):
    counts = {}
    for number in saveInt:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    mode = " ".join(map(str, sorted(map(int, mode))))
    return mode


if len(saveN) == voters:
    print("*** No Candidate Wins ***")
else:
    print(find_mode(saveInt))
