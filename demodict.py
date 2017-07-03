ddict={}.fromkeys(('x','y'),1)
print(ddict)
ddict2={}.fromkeys(('a','b'))
print(ddict)
for key in ddict2.keys():
    print("key=%s,value=%s"%(key,ddict2[key]))
for key in ddict2:
    print("key=%s,value=%s"%(key,ddict2[key]))

ddict3={"name":"ben","age":25}
print("name=%(name)s age=%(age)d " % ddict3)

set1=set("shop")
set2=frozenset("shop")
print(set1==set2,set1>=set2)