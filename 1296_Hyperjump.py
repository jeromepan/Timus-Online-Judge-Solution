"""
1296. Hyperjump
Time limit: 1.0 second
Memory limit: 64 MB
Developed in the beginning of XXI century, hyperjump remains the primary method of transportation for distances up to thousands parsecs. But physicists have recently discovered an amazing phenomenon. They believe the duration of the hyperjump alpha phase can be easily controlled. Alpha phase is the period when hyper-spacecraft accumulates its gravity potential. The larger is the gravity potential accumulated, the less energy is required to complete the hyperjump. Your task is to write a program, which would help pilots decide when to enter and when to leave the alpha-phase, in order for the hyperspacecraft to accumulate the largest possible gravity potential.
The most crude gravity field model (which you will have to use) yields the sequence of integers pi, which represent field intensities at different moments in time. According to this model, if the alpha-phase begins at moment i and ends at moment j, then the value of gravity potential accumulated will be equal to the sum of sequence elements at places from i-th to j-th inclusive.
Input
The first line of the input contains an integer N being the number of elements in the intensity values sequence (0 ≤ N ≤ 60000). Next N lines specify sequence elements, each line containing a single integer pi (−30000 ≤ pi ≤ 30000).
Output
The only line of output contains the largest possible value of the gravity potential that can be accumulated by a hyperspacecraft during the alpha phase. You should assume that the initial gravity potential of a hyperspacecraft is equal to zero.
Samples
input	output
10      187
31
-41
59
26
-53
58
97
-93
-23
84

3       0
-1
-5
-6

"""

def sum(arr):
    k = 0
    max = 0
    for i in range (0,len(arr)):
        max = max + arr[i]
        if k < max:
            k = max

        if max < 0:
            max = 0
    #print(k)
    return k

n = (int)(input())
list = [None]*n
for i in  range (n):
    list[i] = (int)(input())

print(sum(list))
