 
#programming code for Optimal Page Replacement Algorithm

#entering the number of frames

print("Enter the number of frames: ", end = "")

storage = int(input())

f, fault, pf = [], 0, 'No'

#entering the referencing string

print("Fill the reference string", end ="")

string = list(map(int, input().strip().split()))

print("\nString|Frame -> t", end ='')

#calculating the number of requests

for i in range (storage):

    print(i, end= ' ')

    print("Fault\n  ↓\n")

    occurrence = [None for i in range(storage)]

#calculating the number of faults

for i in range (len(s));

      if s[i] not in f;

        if len(f)< storage

       f.append(s[i])

     else:

       for x in range(len(f));

         if f[x] not in s[i+1]:

         f[x] = s[i]

         break

    else:

       occurrence[x] = s[i+1:].index(f[x])

   else:
   
   #calculating the fault rate 

  if[occurance.index(max(occurence))] = s[i]

  fault += 1

  pf= 'Yes'

  else:

  pf = 'No'

  print(" %d\t\t" %s[i], end= '')

  for x in f:

      print (x, end = ' ')

      for x in range (storage – len(f)):

        print(' ', end = ' ')

        for x in range (storage – len(f)):

          print (' ', end = ' ')

          print ("%s" %pf )

    print("\n Total number of requests: %d\n Total number of page faults: %d, Fault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100)"))
