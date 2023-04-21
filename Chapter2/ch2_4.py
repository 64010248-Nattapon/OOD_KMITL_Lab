input_list = input('Enter Your List : ').split()
# print(input_list)
input_list= list(map(int, input_list))
# print(input_list)


def sumArr(arr):
    out = []
    count = 0
    if len(arr) < 3:
        print('Array Input Length Must More Than 2')
        return
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i]+arr[j]+arr[k] == 5 and i!=j and i!=k and j!=k:
                    x=[arr[i],arr[j],arr[k]]
                    x.sort()
                    if x not in out:
                        out.append(x)
                    

    out = set(tuple(x) for x in out)
    out = sorted(list(list(x) for x in out))
    print(out)

sumArr(input_list)