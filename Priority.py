print("FIRST COME FIRST SERVE SCHEDULLING")
n= int(input("Enter number of processes : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter Priority of the process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])

ET = []
for i in range(len(d)):
    # first process
    if(i==0):
        ET.append(d[i][1][1])
 
    # get prevET + newBT
    else:
        ET.append(ET[i-1] + d[i][1][1])
 
TAT = ET
# for i in range(len(d)):
#     TAT.append(ET[i] - d[i][1][0])
 
WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])

avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)

avg_TT = 0
for i in TAT:
    avg_TT +=i
avg_TT = (avg_TT/n)
# print(TAT)

print("Process | Priority | Burst | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
print("Average Waiting Time: ",avg_WT)
print("Average Turnaround Time: ",avg_TT)
