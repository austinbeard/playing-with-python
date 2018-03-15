import random
l = []
lFreq = []
MIN = int(input("What is the smallest number you want in the range: "))
MAX = int(input("What is the highest number you want in the range: "))
tries = int(input("How many numbers would you like generated: "))
freqnum = int(input("What is the smallest number you want to see in the frequency: "))

for num in range(tries):
  x = random.randint(MIN, MAX)
  l.append(x)

for y in range(min(l), max(l)+1):
  freq = l.count(y)
  if freq >= freqnum:
    pair = ("{}: {} times".format(y, freq))
    lFreq.append(pair)
if not lFreq:
  print("Noting occured {} or more times!".format(freqnum))

if lFreq:
  for amount in range(len(lFreq)):
    print(lFreq.pop())
