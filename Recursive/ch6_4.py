def move(n, source, dest, aux):
    if (n>0):
        move(n-1, source, aux, dest)
        poleLst[aux-1].append(poleLst[source-1].pop())
        print("move",n,"from ",chr(ord('A')+source-1), "to" ,chr(ord('A')+aux-1))
        print('|  |  |')
        printPole(inp,poleLst[0],poleLst[1],poleLst[2])
        move(n-1, dest, source, aux)

def printPole(n, p1, p2 ,p3):
    if (n!=0):
      if (len(p1) >= n):
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if (len(p2) >= n):
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if (len(p3) >= n):
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      printPole(n-1,p1,p2,p3)
    else:
        return

def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)

inp = int(input("Enter Input : "))
poleLst = [[],[],[]]
poleLst[0] = init(inp)
print('|  |  |')
printPole(inp,poleLst[0],poleLst[1],poleLst[2])
move(inp,1,2,3)