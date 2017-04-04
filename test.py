

def outer():
    dic['Zero'] = 0
    outer2()


def outer2():
    #global dic
    
    dic['c'] = 3
    print('outer: '+str(dic))
    
    def inner():
        #global dic
        dic['Nine'] = 99

    inner()

dic = {}
dic['a'] = 1
dic['b'] = 2

outer()
print("main:  " + str(dic))
