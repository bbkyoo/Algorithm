FixedValue = 0
VariValue = 0
Val = 0

count = 0

FixedValue, VariValue, Val = map(int, input().split())

if VariValue >= Val:
    count = -1
else:
    count = FixedValue // (Val - VariValue) + 1

print(count)        
        
            
