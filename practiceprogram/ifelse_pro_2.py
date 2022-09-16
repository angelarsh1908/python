text=input("Enter your text")

if("make a lot of money" in text):
   spam=True
if("buy now" in text):
    spam=True
if("click this" in text):
   spam=True
if("subscribe this" in text):
    spam=True
else:
    spam=False

if (spam):
    print("This text is spam")
else:
    print("This text is NOT spam")
