def countLetter(str):
  letterList = list(str)
  letterCount = {}
  for letter in letterList:
    if letter != " ":
      letterCount[letter] = letterList.count(letter)
      
  letterCount=sorted(letterCount.items())
  for key, value in letterCount:
    print(key, value)
  

  
str = input("請輸入文字: ")
countLetter(str.upper())