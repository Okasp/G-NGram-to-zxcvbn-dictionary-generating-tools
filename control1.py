from zxcvbn import zxcvbn
import time
from datetime import datetime
import datetime 

#get files set up
pwlst = open('100.txt', 'r') #each line is a new password
output = open('examplefile1.txt', 'w')

#set up headers
#output.write("score,guesses,calc_time,offline_fast_hashing_1e10_per_second,online_no_throttling_10_per_second \n")

for line in pwlst: 
    #get zxcvbn of that password
    results = zxcvbn(line.strip())
    
    #get elements of res we want
    score = results.get('score')
    guesses = results.get('guesses')
    calc_time = results.get('calc_time')
    t = calc_time.microseconds 

    fasthash = results.get('crack_times_seconds').get('offline_fast_hashing_1e10_per_second')
    nothrot = results.get('crack_times_seconds').get('online_no_throttling_10_per_second')
    
    #write to output file
    outstr = "{},{},{},{},{}\n" 
    output.write(outstr.format(score, guesses, t, fasthash, nothrot))

#time stuff
timestr = "Process time = " + str(time.process_time())
print(timestr)

#clean up
output.close()
pwlst.close()
