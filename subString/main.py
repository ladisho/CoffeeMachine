A = ['29', '20']
B = ['10', '11']

for a in A:
    if any(b[0] == a[0] or b[1] == a[1] for b in B):


        print("Yes")
    else:
        print("No")

    # if any(b[1] == a[1] for b in B):
    #     print("Yes")
    # else:
    #     print("No")
