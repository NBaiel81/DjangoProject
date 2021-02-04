costumers=['baiel','baiel','nurjanat','jarkinay','maksim','maksim','maksim','akilbek','aigerim']
i=0
unique=[]
not_unique=[]
for costumer in costumers:
    i+=1
    unique.insert(-1,costumer)
    if costumer in unique:
        not_unique.insert(-1,costumer)
print(not_unique)








