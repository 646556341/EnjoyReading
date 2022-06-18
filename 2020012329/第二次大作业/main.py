from Funcs import funcs

def getfunctions(path):
    with open(path, "r") as f:
        text = f.read()
    return text.split()
funcNames = getfunctions("test.txt")
for functionName in funcNames:
    eval("funcs." + functionName)()
