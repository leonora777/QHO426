print("Where should I look?")
place = input()

if (place == "in the bedroom"):
  print("Where in the bedroom should I look?")
  bedroom_place = input()
  if (bedroom_place == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")

elif (place == "in the lab"):
  print("Where in the lab should I look?")
  lab_place = input()
  if (lab_place == "on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")

else:
  print("I am not sure where that place is located.")