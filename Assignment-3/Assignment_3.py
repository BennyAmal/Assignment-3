list1=list()
while True:
    tem=input("enter numbers of list, type Done after all numbers ")
    if tem=='done': break
    list1.append(tem)                                 #to take input from user
print("the entered list is",list1)
result=[]                                   #blank list to store the result list
subgroup = [list1[0]]                          #a list to store the subgroups with consecutive duplicates
for i in range(1, len(list1)):
    if list1[i] == subgroup[0]:
     subgroup.append(list1[i])                  #checking for duplication and store the values to subgroup if any
    else:
        result.append(subgroup)                 #appending the subgroups to result list
        subgroup = [list1[i]]
result.append(subgroup)
print("the list with consecutive duplicates are grouped is \n",result)      #printing the result list
