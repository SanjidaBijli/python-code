even_number=[]
odd_number=[]
for i in range(1,101,1):
    if i%2==0:
       even_number.append(i)
    else:
      odd_number.append(i)
print(even_number)
print(odd_number)
num=int(input("Enter the number: "))
sum=0
for i in range(1,5,1):
    sum=sum+i
    i=i+1
print(sum+i)
num=int(input("Enter the number: "))
sum=0
for i in range(1,num+1,1):
    sum=sum+i
print(sum)
name_list = ['md. Joy', 'md. Rana', 'mst. Sanjida', 'mst. Bijli','xyz','abc']
female=[]
male=[]
third_person=[]
for i in name_list:
    if  i.startswith("md"):
        male.append(i)
    elif i.startswith("mst"):
        female.append(i)
    else:
        third_person.append(i)
         
print(female)
print(male)
print(third_person)

    


    