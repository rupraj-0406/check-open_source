a=[]
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
