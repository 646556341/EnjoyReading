import random
import string

def structDataSampling(num,**kwargs):
    result = list()
    for index in range(0,num):
        element = list()
        for key,value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(0,value['len']) )
            else :
                break
            element.append(tmp)
        result.append(element)
    return result

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

def apply():
    str = txtFileReader("text.txt")
    struct = eval(str.pop())
    result = structDataSampling(2,**struct)
    for item in result:
        print(item)
apply()
