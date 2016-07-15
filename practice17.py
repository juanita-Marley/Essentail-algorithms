'''def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))
print(','.join(values))    
'''
def gen(n):
    i=0
    while i<=n:
        if i%5==0 and i%7==0:
            yield i
        i+=1   

v=[]    
n=int(input("enter a num"))
for i in gen(n):
    v.append(str(i))
print(','.join(v))
