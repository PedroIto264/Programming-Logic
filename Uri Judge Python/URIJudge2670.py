A1 = int(input())
A2 = int(input())
A3 = int(input())
x1 = A2*2 + A3*4
x2 = A1*2 + A3*2
x3 = A1*4 + A2*2

if(x1 <= x2):
    min = x1
else:
    min = x2
if(min>=x3):
    min = x3
print(min)