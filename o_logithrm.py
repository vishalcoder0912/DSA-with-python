def Find_name(names,target):
    left =0
    right=len(names)-1
    while left <=right:
        mid=(left+right) //2
        if names[mid]==target:
            return mid
        elif names[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
names =["kartik","diya","vishal","daveloper"]
names.sort()
target ="vishal"

result=Find_name(names,target)

if result != -1:
    print("found at index ",result)
else:
    print("not found")