C1 = input()
C2 = input()

Clist = []
Clist.append(C1)
Clist.append(C2)

reverse_Clist = []
reverse_Clist.append(''.join(list(reversed(C2))))
reverse_Clist.append(''.join(list(reversed(C1))))

if Clist == reverse_Clist:
    print('YES')
else:
    print('NO')

