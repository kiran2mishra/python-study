# need to put the condition you want
while (True):
    i=1
    print ("Enter the number")
    a = 1+ int(input())
    if (a>100):
        print("Congrats ,you have crossed 100")
        break # break comes where you want to stop the loop
    else:
      print("Try again")
      continue # where you want the process to be repeated
#