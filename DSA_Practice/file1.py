#reverse a given string
name = "sachin"
# print(name[::-1])
rev=""
for i in range(len(name)-1,-1,-1):
    # rev=rev+name[i]
    # print(''.join(name[i]),end=" ")
    print(name[i],end=" ")
print()
name="sachin"
for i in range(len(name)-1,-1,-1):
    print(name[i],end=" ")

#palindrome
name="madam"
if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    
name="madam"
rev=""
for i in range(len(name)-1,-1,-1):
    rev=rev+name[i]
if rev==name:
    print("palindrome")
else:
    print("not palindrome")

#two pointer
name="madam"
i=0
j=len(name)-1
while i<j:
    if name[i]!=name[j]:
        print("not a palindrome")
        break
    i+=1
    j-=1
else:
    print("palindrome")

#find duplicate element in an array
# list=[1,2,2,3,4,5,4]
# seen=[]
# duplicate=[]
# for item in list:
#     if item in seen:
#         if item not in duplicate:
#             duplicate.append(item)
#     else:
#         seen.append(item)
# print(duplicate)

s=[1,2,2,3,4,5,4]
duplicate=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j] and s[i] not in duplicate:
            duplicate.append(s[i])
print(duplicate)

text="banana"
freq={}
for ch in text:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)

#Find largest & smallest number in list
# list=[1,2,3,4,5]
# max=list[0]
# for i in range(len(list)):
#     if list[i]>max:
#         max=list[i]
# print(max)

# list=[1,2,3,4,5]
# min=list[0]
# for i in range(len(list)):
#     if list[i]<min:
#         min=list[i]
# print(min)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#fibonacci 
n=7
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print()
a=0
b=1
while a<=50:
    print(a,end=" ")
    a,b=b,a+b

#prime 
# num=29
# is_prime=True
# if num<=1:
#     is_prime=False
# else:
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
# if is_prime:
#     print("prime")
# else:
#     print("not")
print()
num=29
is_prime=True
if num<=1:
    is_prime=False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
if is_prime:
    print("prime")
else:
    print("Not prime")

#remove duplicate element
arr=[1,2,2,3,4,5,5,6]
unique=[]
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)

a=10
b=10
print(a==b)
print(a is b)

x=10000
y=10000
print(x==y)
print(x is y)

a=[1,2,3]
b=[1,2,3]
print(a == b)
print(a is b)

x=10
y=10
print(x==y)
print(x is y)

x=100000000
y=100000000
print(x==y)
print(x is y)

x=int("100000")
y=int("100000")
print(x == y)
print(x is y)

#find the missing number 
arr=[1,2,3,5,6]
n=6
exp_sum=0
for i in range(1,n+1):
    exp_sum=exp_sum+i
act_sum=0
for num in arr:
    act_sum=act_sum+num
missing=exp_sum-act_sum
print(missing)

#find missing
def find_missing(nums):
    n=len(nums)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expected_sum-actual_sum
nums=[1,2,3,4,5,6,8,9]
print(find_missing(nums))

#find the second largest number in the list
nums=[1,2,3,4,5,6]
largest=nums[0]
sec_largest=-1
for i in range(len(nums)):
    if nums[i]>largest:
        sec_largest=largest
        largest=nums[i]
    elif nums[i]>sec_largest and nums[i]!=largest:
        sec_largest=nums[i]
print(sec_largest)

#list sorted
list=[1,2,3,4,6,5,7,9,8]
print(sorted(list))
res=list.sort()
print(res)

list=[1,2,3,4,6,5,7,9,8]
is_sorted=True
# for i in range(len(list)):
for items in list:
    # if list[i]>list[i+1]:
    # if list[items]>list[items]+1:
        is_sorted=False
        break
print(("sorted" if is_sorted else "not"))

        
#find non repeating char
s="mam"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
for ch in s:
    if freq[ch]==1:
        print(ch)
        break
#count vowels
text="interview"
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1
print(count)

#merge 2 dict
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged={}
for key in dict1:
    merged[key]=dict1[key]
for key in dict2:
    merged[key]=dict2[key]
print(merged)
        
#string word count
s="this is python programming"
st=s.split(" ")
print(len(st))
s="this is python programming"
in_word=False
count=0
for ch in s:
    if ch!=" " and not in_word:
        count+=1
        in_word=True
    elif ch==" ":
        in_word=False
print(count)
# Reverse words in a sentence (NO inbuilt)
s="this is python programming"
#extract the word
words=[]
word=""
for ch in s:
    if ch!=" ":
        word=word+ch
    else:
        if word!="":
            words.append(word)
            word=""
if ch!="":
    words.append(word)

for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
        
#check anagram
# s1=input().strip().replace(" ","").lower()
# s2=input().strip().replace(" ","").lower()
# if len(s1)!=len(s2):
#     print("not anagram")
# else:
#     freq1={}
#     freq2={}
#     for ch in s1:
#         freq1[ch]=freq1.get(ch,0)+1
#     for ch in s2:
#         freq2[ch]=freq2.get(ch,0)+1
#     if freq1==freq2:
#         print("anagram")
#     else:
#         print("not anagram")
a = [1,2,2,3]
b = [2,2,4]

result = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            result.append(a[i])
            break

print(result)


s=[1,1,0,0,1,0]
res=[]
zero_count=0
for num in s:
    if num!=0:
        res.append(num)
    else:
        zero_count+=1
for i in range(zero_count):
    res.append(0)
print(res)

#shallow copy 
import copy
a=[[1,2,3,4],[4,5,6,7]]
shallow=copy.copy(a)
deepcopy=copy.deepcopy(a)
print(shallow)
print(deepcopy)

a[0][0]=99
print(copy.copy(a))
print(copy.deepcopy(a))

#iterator
class MyIterator:
    def __init__(self,limit):
        self.num=num
        self.limit=limit
    def __iter__(self):
        return self
    def __next__(self,):
        if self.num<self.limit:
            self.num+=1
            return self.num
        else:
            return StopIteration
#generator
def my_generator(limit):
    for i in range(1,limit+1):
        yield i
limit=10
print(my_generator(limit))  

try:
    a=10//2
    print(a)
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("Execution completed")

try:
    x=int("abc")
    print(x)
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division error")

#what is else in exception 
try:
    x=10//2
except ZeroDivisionError:
    print("cannot divide the num")
else:
    print("no exception occur")

#list comprehension
res=[i*j for i in range(5) for j in range(5) if i%2==0 and j%3==0]
print(res)

res=[]
for i in range(5):
    for j in range(5):
        if i%2==0 and j%3==0:
            res.append(i*j)
print(res)

#__init__
class User:
    def __init__(self,name):
        self.name=name

obj=User("sachin")
print(obj)

class Emp:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"name is {self.name}"
u=Emp("navi")
print(u)

class User:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"User(name={self.name})"
    

#*args and **kwargs
def add(*args):
    return sum(args)
print(add(1,2,3))

def user(**kwargs):
    return kwargs
print(user(name="sachin",age=25))

# nums = [1, 2, 3]
# result = list(map(lambda x: x * 2, nums))
# print(result)
name=["a","b"]
score=[10,20]
res=list(zip(name,score))
print(res)




    
    


    









