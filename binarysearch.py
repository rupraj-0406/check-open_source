def binarysearch(a,p,q,key):
    l=q-p+1
    if l==1 and a[l-1]!=key:
        return -1
    while l>1:
        m=(p+q-1)//2
        if a[m]==key:
            return m
        elif a[m]>key:
            return binarysearch(a,key)
        else:
            return binarysearch(a,key)

a=[10,20,30,40,50,60,70,80,90,100]

#a=[]
#print('Enter numbers in ascending order, whenever you want to stop enter -1: ')
#while True:
#    k=input('')
#    try:
#        l=int(k)
#    except:
#        print('Invalid input.........')
#        continue
#    if l==-1:
#        break
#    a.append(l)
#print('The array or list is given by:',a)
k=input('Enter the number: ')
try:
    key=int(k)
except:
    print('wrong input !!!!!!')
    quit()
f=binarysearch(a,0,(len(a)-1),key)
if f==-1:
    print('Cannot found......')
else:
    print('It is found at an index',(f+1),'.')