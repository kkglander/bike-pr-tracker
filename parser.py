import sys #gon use so that you can choose how many times you want printed

def getTime(line):
    lineList = line.split("\t")
    return lineList[1]

def convert_to_seconds(time):
    measurments = time.split(".")
    measurments = list(map(lambda num: int(num),measurments))
    return (measurments[0] * 120) + (measurments[1] * 60) + (measurments[2])

def whatsAllatMovementBackThere(j):
        seconds[j],seconds[j-1] = seconds[j-1],seconds[j]
        times[j],times[j-1] = times[j-1],times[j]

times = []
seconds = []

with (open("times.csv","r")) as f:
    times = f.readlines()
    times = list(map(lambda line: line.strip(),times))

#making array that holds the seconds rep
for line in times:
    time = getTime(line)
    totseconds = convert_to_seconds(time)
    seconds.append(totseconds)

i = 0 
while i < (len(seconds)-1):
    i+=1
    if seconds[i] < seconds[i-1]:
        j=i
        while j > 0:
            if seconds[j] < seconds[j-1]:
                whatsAllatMovementBackThere(j)
            j-=1

day,wr = times[0].split("\t")
print(f"The fastes time you've completed is {wr} on {day}")
amt = 5

i = 0
while i <= amt:
    print(times[i])
    i+=1

