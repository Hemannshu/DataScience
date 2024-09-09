s="i ate 100 apples"
s=s.replace('100', '10')
s=s.replace('apples','mangoes')
print("using two lines for replacing",s)#used two lines of code to replace 

s=s.replace('100','10').replace('apples','mangoes')
print("using one line to replace",s)#used one line of code to replace
