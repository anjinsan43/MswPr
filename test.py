

class Diode(object):
    def __init__(self):
        self.Anode   = 1
        self.Cathode = 0


def outer():
    for i in range(4):
        dic['D'+str(i)] = Diode
    
    outer2()


def outer2():
    #global dic
    
    #dic['c'] = 3
    print('outer2: '+str(dic))
    
    def inner():
        #global dic
        for n in (1,2,3):
            dic['D'+str(n)].Anode = 42

    inner()

dic = {}
dic['a'] = 1
dic['b'] = 2

outer()
print("main:  " + str(dic))
d = Diode()
print(str(d))
print(isinstance(d, Diode))
#for n in range(4):
#    print(str(dic['D'+str(n)].Anode))


