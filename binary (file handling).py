import pickle
def write():
    with open("pratham.dat ", "wb")as m:
        
        lst=["alok", "bhumi", "pratham"]
        dic={"alok":99.99,"bhumi":94, "pratham":86}
        pickle.dump(lst, m)
        pickle.dump(dic, m)
    
def read() :
    with open("pratham.dat ", "rb")as m:
        l=pickle.load(m)
        d=pickle.load(m)
        print(l)
        print(d)

write()
read () 