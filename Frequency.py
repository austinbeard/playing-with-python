from random import randint

# Initialize both lists used in program
l = []
lFreq = []

print("This program generates a list of numbers then gives you the highest or lowest frequency of a number based on your inputs")

# Get user inputted values
MIN = int(input("What is the smallest number you want in the range: "))
MAX = int(input("What is the highest number you want in the range: "))
tries = int(input("How many numbers would you like generated: "))
freqnum = int(input("What is the smallest frequency you want to see: "))

# Loop to generate list of random numbers
for num in range(tries):
  x = randint(MIN, MAX)

  # Put each number into the list
  l.append(x)

# Loop to get the frequency of each number in the first list
for y in range(min(l), max(l)+1):
  freq = l.count(y)
  
  # Only count it if the frequency is higher than what the user wants
  if freq >= freqnum:
    
    # Get the frequency of the number into a percent
    percfreq = freq / tries
    
    # Organize it nicely 
    pair = ("{}: {} times, having a {:.2%} occurrence".format(y, freq, percfreq))
    
    # Put each number with frequency in list
    lFreq.append(pair)

print("\n\n\nThese are the numbers that generated:")

# Tell the user if the list is empty
if not lFreq:
  print("Nothing occured {} or more times!".format(freqnum))

# Otherwise give the user the list they want 
else:
  for amount in range(len(lFreq)):
    
    # Prints it not as a list because it's better to read
    print(lFreq.pop())
