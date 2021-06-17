##1 done
##2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4)or (18==3))and(9>3)
False
>>> True is False
False


##3
>>> s1= "NIce to have it"
>>> s2= " here"
>>> print(s1+s2)
NIce to have it here

##4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])
print(a[-3][-3][-1])

##5
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a[0]='s1'
a[-1]='s2'
print(a)

##6
color_list_1= set(["White","Black","Red"])
color_list_2= set(["Red","Green"])
print("original color sets:")
print(color_list_1)
print(color_list_2)
for element in color_list_2:
    if element in color_list_1:
        color_list_1.remove(element)
        print(sorted(color_list_1))
##print(color_list_1.difference(color_list_2))


##7
import string
def ispangram (str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True

string= 'live life to the fullest'
if(ispangram(string)== True):
    print('Yes')
else:
    print('No')


##8
n=input("Enter any number:")
output=eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
print(output)

##9
p=input("Enter some comma separated sequence of words:")
tuple=p.split(",")
tuple.sort()
print(tuple)

##10
d={'Student':['Rahul','Kishore','Vidhya','Rakhi'],'Marks':[57,87,67,79]}
output=max (d['Marks'])
print (output)
pos=d['Marks'].index(output)
print(pos)
print(d['Student'][pos])
