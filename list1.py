l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
l = [i for i in l1 if i in l2]
print("intersection = ",l)
[l1.append(i) for i in l2 if i not in l1]
print("union = ",l1)
l3 = [i for i in l1 if i not in l2]
print("difference = ",l3)
l4 = [i for i in l1 or l2 if i not in l1 or l2]
print("union = ",l4)
[l3.append(i) for i in l1 if i not in l2]
print("stmmetric dif. = ",l3)

