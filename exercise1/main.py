def isNumEligible(num):
  if ((num % 2 == 1) or (num > 5  and num < 21)):
    print("X")
  else:
    print("O")

  
num = input("請輸入數字: ")
isNumEligible(int(num))