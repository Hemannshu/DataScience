s="i ate 100 apples"
s=s.replace('100', '10')
s=s.replace('apples','mangoes')
print("using two lines for replacing",s)

s=s.replace('100','10').replace('apples','mangoes')
print("using one line to replace",s)