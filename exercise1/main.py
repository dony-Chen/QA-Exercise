def isNumEligible(num):
  if ((num % 2 == 1) or (num > 5  and num < 21)):
    print("X")
    return True
  elif num < 2:
    print("請不要輸入小於二的偶數～") 
    return False
  else:
    print("O")
    return True

access = False

while(not access):  
  num = input("請輸入數字: ")
  access = isNumEligible(int(num))