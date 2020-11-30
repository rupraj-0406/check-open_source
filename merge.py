"""
I AM DONE WITH THIS PART
"""
def merges(a):
    if len(a)==1 :
        return a
    m=len(a)//2
    l=merges(a[:m])
    r=merges(a[m:])
    return merge(l,r)

def merge(l,r):
    x=len(l)
    y=len(r)
    i=0
    j=0
    b=[]
    while i<x and j<y:
        if l[i]<r[j]:
            b.append(l[i])
            i+=1
        else:
            b.append(r[j])
            j+=1
    b.extend(l[i:])
    b.extend(r[j:])
    return b

a=[]
print('Enter numbers, whenever you want to stop enter -1: ')
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

print('The sorted array is given below:\n')
print(merges(a),'\n')