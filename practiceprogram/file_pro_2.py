def game():
    return 44

score=game()
with open('hiscore.txt') as f:
    hiscorestr=f.read()

if hiscorestr=='':
    with open("hiscore.txt",'w') as f:
        f.write(str(score))

if int(hiscorestr)<score:
    with open("hiscore.txt",'w') as f:
        f.write(str(score))        