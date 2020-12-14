import numpy as np
import matplotlib.pyplot as plt
import math
import random

#initializations
xpoints = []
ypoints = []
count = {'0,0': 0}
running_total = 0
#running_total_o = 0
#running_total_m = 0

#file i/o
modifiedf = open("02-USandUK-US.txt")
originalf = open("02-original.txt")

#get first line before the while loop (+ remove '\n')
mline = modifiedf.readline()
oline = originalf.readline()
#just some initial values
mxm = -1
min = 1000000
omitted = 0;


#iterate through files
while oline != '':
    #mline = int(mline.split(',')[1].split('.')[0])
    #oline = int(oline.split(',')[1].split('.')[0])
    mline = mline.split(',')[3]
    oline = oline.split(',')[3]    
    if 'E' not in mline:
        mline = int(mline.split('.')[0])
    else:
        #print(mline)
        mline = modifiedf.readline()
        oline = originalf.readline()
        #print("New: " + mline)
        omitted += 1
        continue
    if 'E' not in oline:
        oline = int(oline.split('.')[0])
    else:
        #print(oline)
        mline = modifiedf.readline()
        oline = originalf.readline()
        #print("New: " + oline)
        omitted += 1
        continue
    
    
    #put the x and y coords into (separate) lists
    if mline < 1000000000000000:
        xpoints.append(mline) #/(10^20)))
    else:
        #print(mline)
        mline = modifiedf.readline()
        oline = originalf.readline()
        #print("New: " + mline)
        omitted += 1
        continue
    if mline < 1000000000000000:
        ypoints.append(oline) #/(10^20)))
    else:
        #print(oline)
        mline = modifiedf.readline()
        oline = originalf.readline()
        #print("New: " + oline)
        omitted += 1
        continue
    
    #update count dictionary
    #if it's in there already, increment
    if str(mline) + ',' + str(oline) in count:
        count[str(mline) + ',' + str(oline)] += 1
    #if not, start the count at 1
    else:
        count[str(mline) + ',' + str(oline)] = 1
    
    #Handle max/min difference
    dif = oline - mline
    if dif > mxm:
        mxm = dif
    elif dif < min:
        min = dif
    
    #get averages
    running_total += 1
    #running_total_o += oline
    #running_total_m += mline
    
    #get next
    #for i in range(random.randrange(1,10)*10):
    mline = modifiedf.readline()
    oline = originalf.readline()
    #    if oline == '':
    #        break
    
    #print(oline)

#check to see if it worked
#print(count)
print('Min: ' + str(min))
print('Max: ' + str(mxm))
#print('Average original: ' + str(running_total_o/running_total))
#print('Average modified: ' + str(running_total_m/running_total))
print('Omitted: ' + str(omitted))

print(running_total)

#then get the counts for each pair and put it in an array? Sure, I guess
counts = []
for i in range(running_total): #x and y will be the same
    if count[str(xpoints[i]) + ',' + str(ypoints[i])] > 100:
        counts.append(70)
    else: counts.append(count[str(xpoints[i]) + ',' + str(ypoints[i])])

c = np.array(counts)
area = np.pi * c # counts point radii

plt.title('Comparison of Times for Orignal vs. US and UK-US dictionaries')
plt.xlabel('US and UK-US')
plt.ylabel('Original')
#plt.plot([0,800000000000000000000],[0,800000000000000000000],'r-')
plt.scatter(xpoints, ypoints, s=area, alpha=0.5)
print('here')
plt.savefig('scattertimeUSandUK-US.png')
print('Output: scattertimeUSandUK-US.png')