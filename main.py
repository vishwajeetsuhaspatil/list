list= []
print(list)
n=[1,2,3,4,5]
print(n)
b= [1,2,3]*3
print(b)
b= b[::-1]
print(b)
def m(w):
    c= 0
    lst= []
    for word in w:
        if len(word)>1 and word[0]== word[-1]:
         c= c+1
         return c
count= m(["abc","1221"])
print(count)   