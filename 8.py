#   分别将长度为100、1000、10000的数列进行选择排序和归并排序
#   共输出十组随机数据的运行结果，其中每种长度的第一列是用选择排序需要的时间，第二列为归并排序
#   由运行结果来看，在长度为100时两种排序方法的快慢具有随机性
#   长度为1000时，归并排序较快于选择排序，而长度为10000时两者有显著差距
#   结论：数列长度较短时，选择排序和归并排序的效果差不多，随着数列长度增加，归并排序明显优于选择排序
import random
import copy
import time
def choosesort(li):
    lilen=len(li)
    for i in range(lilen-1):
        m=li[i]
        mi=i
        for j in range(i+1,lilen):
            if li[j]<m:
                m=li[j]
                mi=j
        temp=li[i]
        li[i]=li[mi]
        li[mi]=temp

def merge(left, right):
    ll, rr = 0, 0
    result = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            result.append(left[ll])
            ll += 1
        else:
            result.append(right[rr])
            rr += 1
    result+=left[ll:]
    result+=right[rr:]
    return result

def merge_sort(li):
    if len(li) <= 1:
        return li
    num = len(li) // 2
    left = merge_sort(li[:num]) 
    right = merge_sort(li[num:]) 
    return merge(left, right)

print("数列长度：100                       1000                      10000")
for j in range(10):
    print(j,end="         ")
    arr1=[]
    for i in range(100):
        arr1.append(random.randint(0,1000))
    arr11=copy.deepcopy(arr1)

    start_time = time.time()
    choosesort(arr1)
    end_time = time.time()
    print("%.6f" %(end_time-start_time),end="    ")

    start_time = time.time()
    merge_sort(arr11)
    end_time = time.time()
    print("%.6f" %(end_time-start_time),end="      ")



    arr2=[]
    for i in range(1000):
        arr2.append(random.randint(0,1000))
    arr22=copy.deepcopy(arr2)
    start_time = time.time()
    choosesort(arr2)
    end_time = time.time()
    print("%.6f" %(end_time-start_time),end="    ")

    start_time = time.time()
    merge_sort(arr22)
    end_time = time.time()
    print("%.6f" %(end_time-start_time),end="      ")


    arr3=[]
    for i in range(10000):
        arr3.append(random.randint(0,1000))
    arr33=copy.deepcopy(arr3)
    start_time = time.time()
    choosesort(arr3)
    end_time = time.time()
    print("%.6f" %(end_time-start_time),end="    ")

    start_time = time.time()
    merge_sort(arr33)
    end_time = time.time()
    print("%.6f" %(end_time-start_time))

