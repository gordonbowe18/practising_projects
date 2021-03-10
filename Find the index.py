#if value x is in list, return the index it's at. 

def cool_function (a,b):
#mae sure that b is in the list in the first place...
    if b in a:
#Could potentially do a little sort here, that way they'd be in order? And see them in largest? But then don't you want to know their index, which will be relevant to where they are in the list...
#        a.sort() 
        for i in a: 
            if i == b:
#only returns the first instance of it in the list, what if they'd like all?  
                return a.index(i)
            else:
                continue
    else:
        return (-1)


print (cool_function([45,9,6,23], 6))