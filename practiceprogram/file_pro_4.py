from importlib.resources import contents


with open ("sapmle.txt") as f:
    content=f.read()
content=content.replace("donkey","******")

with open("sapmle.txt","w") as f:
    f.write(content)