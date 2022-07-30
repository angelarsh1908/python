def KBC(TASk):
    print()





quiz={
        1:{
        "question":"MS-Word is an example of _____",
        "A" : "An operating system",
        "B" :"A processing device",
        "C" : "Application software",
        "D":"An input device",
        "ans" : "C",
       },

    2:{
       "question":"Ctrl, Shift and Alt are called .......... keys",
        "A" : "modifier",
        "B" :"function",
        "C" :"alphanumeric",
        "D" :"adjustment",
        "ans" : "B"
       },

    3:{
       "question":"A computer cannot 'boot'if it does not have the _____",
        "A" :"Compiler",
        "B" :"Loader",
        "C" :"Operating system",
        "D" :"Assembler",
        "ans":"D"
       },
    4:{
        "question":" Who developed Python Programming Language?",
        "A":"Wick van Rossum",
        "B": "Rasmus Lerdorf",
         "C": "Guido van Rossum",
        "D": "Niene Stom",
        "ans": "C"
    },
    5:
    {
        "question":"Which type of Programming does Python support?",
        "A":"object-oriented programming",
        "B":"structured programming",
        "C":"functional programming",
        "D":"all of the mentioned",
        "ans": "D"
    },
    6:
    {
        "question":"Which of the following is the correct extension of the Python file?",
        "A":" .python",
        "B":".pl",
        "C":".py",
        "D":".p",
        "ans": "C"

    },
    7:
    {
        "question":"Which of the following is used to define a block of code in Python language?",
        "A":" Indentation",
        "B":"Key",
        "C":"Brackets",
        "D":"All of the mentioned",
        "ans": "A"
    },8:
    {
        "question": "Which keyword is used for function in Python language?",
        "A":"keywor", 
        "B":"Def",
        "C":"Fun",
        "D":"Define",
        "ans":"B",
    },9:
           
    {
        "question": "Which of the following is not a keyword in Python language?",
        "A":"Val", 
        "B":"raise",
        "C":"try",
        "D":"width",
        "ans":"A",
    },10:
    {
        "question": "What is the maximum possible length of an identifier?",
        "A":"16", 
        "B":"32",
        "C":"64",
        "D":"None",
        "ans":"D"
    }

    }
fifty_fifty={
    1:{
        "question":"MS-Word is an example of _____",
        "A" : "An operating system",
        "B" :"A processing device",
    }

}

count_wans=0   
count_rans=0
point=0
for i in range(1,11):
            print(quiz[i]["question"])
            for k,v in quiz[i].items():
                if k=="ans":
                    continue
                elif k=="question":
                    continue
                else:
                    print(f"\t{k}={v}")
            a="\t\t\t\t\tusiing a life line 50-50 press y ====="
            print(a)
            if a=="y" or a=="yes" or a=="Y":


             ans=input("Enter your answer==")
            ans=(ans.upper())
            if ans==quiz[i]["ans"]:
                print('"Right answer"')
                count_rans=count_rans+1
               
                point=point+50
                print("--------Congratulation-------------")
                print("You increase +50 point==",point)
            else :
                print ('"Wrong Answer"')
                point=point-20
                print("--------------OOPS-------------")
                print("you decrease -20 point==",point)
        
                count_wans=count_wans+1
print("right ans is",count_rans)
print("Wrong ans is",count_wans)

KBC("KBC-2023")
    