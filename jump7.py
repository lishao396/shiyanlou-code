i=int(input('请输入数字:'))
n=1
epsilon=0.001
while True:
    t=(n+i)/2
    p=3*t*t+4*t-10
    if p>0:
        i=t
    elif p<0:
        n=t
    if abs(p)<epsilon:
        break
print(f'{t}')