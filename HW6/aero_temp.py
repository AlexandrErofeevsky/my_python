with open('temp.txt','r') as file:
    content=file.read()
a=content.split()
temp=[]
for i in a:
    temp.append(float(i))
j=0
for i in temp:
    if temp.count(i)==1:
        j+=1
print("Максимальная температура равна ", max(temp),"\nМинимальная температура равна ", min(temp),"\nСредняя температура равна ",round(sum(temp)/len(temp),5),"\nЧисло уникальных температур равно ",j)
