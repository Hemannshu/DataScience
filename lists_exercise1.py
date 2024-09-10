#question 1 

exp=[2200,2350,2600,2130,2190]
#1
extra_amt=exp[1]-exp[0]
print(extra_amt)
#2
total_exp_3months=exp[0]+exp[1]+exp[2]
print("total expense after 3 months ",total_exp_3months)
#3
print("did i spent 2000 dollars in any month", 2000 in exp)
#4
exp.append(1980)
print("total expense after june ending ",exp)
#5
exp[3]=200
print("after correction new expense is ", exp)


#question 2
heros=['spider man','thor','hulk','iron man','captain america']
#1
print(len(heros))
#2
heros.append("black panther")
print(heros)
#3
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
#4
heros[1:3]=["doctor strange"]
print(heros)
#5
heros.sort()
print(heros)
