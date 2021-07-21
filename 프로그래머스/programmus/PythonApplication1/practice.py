bridge_length = 2	
weight = 10	
truck_weights = [7,4,5,6]

arr = [0] * bridge_length
time = 0
while arr:
    arr.pop(0)
    if truck_weights:
        if sum(arr) + truck_weights[0] <= weight:
            arr.append(truck_weights.pop(0))
        else:
            arr.append(0)
    time += 1

print(time)