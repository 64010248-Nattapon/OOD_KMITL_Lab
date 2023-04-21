print("*** Converting hh.mm.ss to seconds ***")
h,m,s=map(int,input("Enter hh mm ss : ").split())
seconds=(h*60*60)+(m*60)+s
if 0<=h<60 and 0<=m<60 and 0<=s<60:
    h=str(h)
    m=str(m)
    s=str(s)
    print(f'{str(h.zfill(2))}:{m.zfill(2)}:{s.zfill(2)} = {seconds:,} seconds')
elif h>=60 or h<0:
    print(f"hh({h}) is invalid!)")
elif m>=60 or m<0:
    print(f"mm({m}) is invalid!")
elif s>=60 or s<0:
    print(f"ss({m}) is invalid!")