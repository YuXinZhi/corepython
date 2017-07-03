s=' '.join(("spanish","inquisition","Made Easy"))
print(s)
print(("%s%s" % (s[:3],s[20])).upper())
s1="hello"+"world"
s2="hello"+"world"
print(s1==s2)
print("hello"+u' '+"world")

from string import Template
s3=Template("there are ${howmany} ${lang} quotation symbols")
print(s3.substitute(lang="python",howmany=3))   #there are 3 python quotation symbols
print(s3.safe_substitute(lang="python"))        #here are ${howmany} python quotation symbols

'''
    6.4.3 原始字符串操作符（r/R）
        >>> '\n'
        '\n'
        >>> print('\n')
        
        
        >>> print(r'\n')
        \n
    
'''
print('*'*20)
print('\n')
print('*'*20)
print(r'\n')
print('*'*20)


print("***isinstance()***")
print(isinstance(u'\0xAB',str))
print("******************")

a=(2,'2')
b=(2,'2')
print(a==b,id(a),id(b))  #True 31981640 31981896