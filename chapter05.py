'''
数字

'''

print(5/2)      #2.5
print(5//2)     #2
print(-5//2)    #-3
print(4**-1)    #0.25

'''
5.6 内建函数与工厂函数
    5.6.1 标准类型函数：cmp()、str()、type()可以用于所有的标准类型
    5.6.2 数字类型函数：
      （1）转换工厂函数：int()、float()、complex()、bool()
           工厂函数是指这些内建函数都是类对象，当你调用它时，实际上创建了一个类实例
      （2）功能函数：abs()、coerce()、divmod()、pow()、round()
**************************
Python中的coerce()
如果有一个操作数是复数， 另一个操作数被转换为复数。  
否则，如果有一个操作数是浮点数， 另一个操作数被转换为浮点数。  
否则, 如果有一个操作数是长整数，则另一个操作数被转换为长整数；  
否则，两者必然都是普通整数，无须类型转换

例子如下：

>>> coerce(1, 2) 
(1, 2) 
>>> 
>>> coerce(1.3, 134L) 
(1.3, 134.0) 
>>> 
>>> coerce(1, 134L) 
(1L, 134L) 
>>> 
>>> coerce(1j, 134L) 
(1j, (134+0j)) 
>>> 
>>> coerce(1.23-41j, 134
((1.23-41j), (134+0j))
**************************



coerce	英[kəʊˈɜ:s]
美[koʊˈɜ:rs]
vt.	逼迫; 威胁; 强迫，强制; 控制，限制;

            
    
'''
i=int('010000010',base=2)
print("i=",i)