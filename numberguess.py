import random
mynum = random.randint(0,15)
print("I have a no. in my mind can you guess it?")
while True:
     usernum = int(input("enter your guess"))
     if (mynum == usernum):
          print("yes you're right")
          break
     elif (mynum > usernum):
          print("my no. is greater than your no.",end ="\n\n")
     else:
          print("my no. is greater than your no.", end="\n\n")
