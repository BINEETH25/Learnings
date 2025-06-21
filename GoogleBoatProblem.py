# Google Boat Problem
# Let me do sliding window approach:

'''
def Boat(distance):
    sum = distance[0]
    left = 1
    k = 1
    for j in range(2, len(distance)):
        if distance[left] > distance[j]:
            k -= 1
            sum += distance[left]
            left += 1
        else:
            k += 1
            left += 1
            sum += distance[j]
    return sum
'''
def Boat(distance):
    total = distance[0]
    left = 1
    k = 1  # Starting k
    for j in range(2, len(distance)):
        if distance[left] < distance[j]:
            if k >= 0:
                k += 1
                left += 1
        else:
            if k <= 2:
                k -= 1
                total += distance[left]
                left = j  # move to the next base position
    if 0 < k < 2:
        total += distance[-1]
    return total

distance = [5, 3, 8, 2, 6, 4]
max_distance = Boat(distance)
print("Max Distance in n days : ", max_distance)

