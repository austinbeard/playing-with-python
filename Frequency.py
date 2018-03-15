import random
l = []
lFreq = []
for num in range(1000):
  x = random.randint(1, 1000)
  l.append(x)
for y in range(min(l), max(l)):
  freq = l.count(y)
  if freq > 4:
    pair = ("{}: {} times".format(y, freq))
    lFreq.append(pair)
for amount in range(len(lFreq)):
  print(lFreq.pop())