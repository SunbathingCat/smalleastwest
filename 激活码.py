import random

#65-90 -> 1-26
# 1234-5678-abcd-efgh
# a+g d-e c+h f-b a+4 c-2 e+1 g-3 abcd efgh

def than(num):
    num += 64
    return chr(num)

def than2(alp):
    return ord(alp)-64

# 生成激活码
def Generate():
    list1 = [1,2,3,4]
    list2 = [5,6,7,8]
    list3 = [random.randint(1, 26),random.randint(1, 26),random.randint(1, 26),random.randint(1, 26)]
    list4 = [random.randint(1, 26),random.randint(1, 26),random.randint(1, 26),random.randint(1, 26)]
    list1[0] = list3[0] + list4[2]
    if(list1[0]>26):
        list1[0] -= 26
    list1[1] = list3[3] - list4[0]
    if(list1[1]<=0):
        list1[1] = -list1[1]+1
    list1[2] = list3[2] + list4[3]
    if (list1[2] > 26):
        list1[2] -= 26
    list1[3] = list4[1] - list3[1]
    if (list1[3] <= 0):
        list1[3] = -list1[3]+1

    list2[0] = list3[0] + list1[3]
    if (list2[0] > 26):
        list2[0] -= 26
    list2[1] = list3[2] - list1[1]
    if (list2[1] <= 0):
        list2[1] = -list2[1]+1
    list2[2] = list4[0] + list1[0]
    if (list2[2] > 26):
        list2[2] -= 26
    list2[3] = list4[2] - list1[2]
    if (list2[3] <= 0):
        list2[3] = -list2[3]+1
    string1=''
    string2=''
    string3=""
    string4=''
    for i in list1:
        string1 += than(i)
    for i in list2:
        string2 += than(i)
    for i in list3:
        string3 += than(i)
    for i in list4:
        string4 += than(i)
    string = string1+'-'+string2+'-'+string3+'-'+string4
    print(string)
    return string

# 校验激活码
def Distinguish(str):
    string = str.split('-')
    string1 = string[0]
    string2 = string[1]
    string3 = string[2]
    string4 = string[3]
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    List1 = [1, 2, 3, 4]
    List2 = [5, 6, 7, 8]
    list3 = [1, 2, 3, 4]
    list4 = [5, 6, 7, 8]
    for i,s in enumerate(string1):
        List1[i] = than2(s)
    for i,s in enumerate(string2):
        List2[i] = than2(s)
    for i,s in enumerate(string3):
        list3[i] = than2(s)
    for i,s in enumerate(string4):
        list4[i] = than2(s)

    list1[0] = list3[0] + list4[2]
    if(list1[0]>26):
        list1[0] -= 26
    list1[1] = list3[3] - list4[0]
    if(list1[1]<=0):
        list1[1] = -list1[1]+1
    list1[2] = list3[2] + list4[3]
    if (list1[2] > 26):
        list1[2] -= 26
    list1[3] = list4[1] - list3[1]
    if (list1[3] <= 0):
        list1[3] = -list1[3]+1
    list2[0] = list3[0] + list1[3]
    if (list2[0] > 26):
        list2[0] -= 26
    list2[1] = list3[2] - list1[1]
    if (list2[1] <= 0):
        list2[1] = -list2[1]+1
    list2[2] = list4[0] + list1[0]
    if (list2[2] > 26):
        list2[2] -= 26
    list2[3] = list4[2] - list1[2]
    if (list2[3] <= 0):
        list2[3] = -list2[3]+1

    String1=''
    String2=''
    for i in list1:
        String1 += than(i)
    for i in list2:
        String2 += than(i)

    if(list1==List1 and list2==List2):
        return True
    else:
        return False


print(Distinguish(Generate()))
