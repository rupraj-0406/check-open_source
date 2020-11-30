# THIS PART IS DONE...............HURRAH
def insern(a):
    n=len(a)
    for j in range(1,n):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key 

a=list()
print('Enter numbers, stop =-1')
while True:
    k=input('')
    try:
        l=int(k)
    except:
        print('Invalid input.........')
        continue
    if l==-1:
        break
    a.append(l)

insern(a)
print(a)

