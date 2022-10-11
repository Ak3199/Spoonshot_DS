def pattern(arr):
    product=1 #initialising a product variable
    flag_var=0 #initialising a flag varible that counts the number of 0 in the list
    for i in range(len(arr)):
        if (arr[i])==0:
            flag_var+=1     #counting the number of 0s
        else:
            product*=arr[i] #computing the product of the elements present in the list except the 0 elements
            
    new_arr=[0]*len(arr) #creating a new list 
    
    for i in range(len(arr)):
        if (flag_var==0):   # if no 0s are present then each element in the new list is simply the total product divided by the element present at that index
            new_arr[i]=(product//arr[i])
        elif flag_var>1:    # if number of 0s is more than one then the new list will contain all elements as 0
            new_arr[i]=0
        elif (flag_var==1 and arr[i]!=0):   #if the number of 0s is just one, then only the index containing the 0 element will be replaced by product otherwise all other elements would remain 0
            new_arr[i]=0
        else:
            new_arr[i]=product
    return new_arr

array=eval(input())
out=pattern(array)
print(out)