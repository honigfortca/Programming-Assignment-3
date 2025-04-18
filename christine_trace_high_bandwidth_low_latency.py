#This imports the sys module.
import sys

#This sets the rate to 48 since 48 is the closest number to 50 (Since 50 Mbp was recommended for the low-latency, high-bandwidth environment) that is divisible by 12.
bandwidth = 48

#We were instructed that each experiment should run traffic for at least 60 seconds.
length = 60

#totalInts will be set to 4 (because that is the value of the rate (48) divided by 12).
totalInts = int(bandwidth/12)

#This loop will run 60,000 times.
for i in range(length*1000):
        #This loop runs 4 times during each cycle of the above loop.
        for x in range(totalInts):
                print(i)
