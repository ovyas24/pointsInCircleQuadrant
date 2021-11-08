import math

def insideCircle(x,y, r, pos):
    distance = math.sqrt(((x ** 2) + (y ** 2) ))
    if(distance <= r):
        return insideTriangle(pos, x, y)
    else:
        return False

def insideTriangle(cords, x, y):
    [(x1, y1),(x2, y2)] = cords
    w1 = ((y*x2) - (x*y2))/((y1*x2) - (x1*y2))
    w2 = (y - (w1 * x1))/(y2)
    if((w1 >= 0) and (w2 >= 0) and (w1 + w2 <= 1)):
        return True
    else:
        return False

def solution(direction, radius, X, Y):
    hashMap = {
        "U": [( radius, radius), (-radius, radius)],
        "D": [( -radius, -radius), (radius, -radius)],
        "L": [( -radius, -radius), (radius, radius)],
        "R": [( radius, -radius), (radius, radius)],
    }
    positions  = []
    for i in range(len(X)):
        positions.append((X[i], Y[i]))
        
    count = 0
    for (x,y) in positions:
        if(insideCircle(x, y, radius, hashMap[direction])):
            count += 1
    return count


print(solution("U", 5, [-1, -2,4, 1, 3, 0], [5, 4, 3, 3, 1,-1]))
print(solution("D", 10, [0, -3, 2, 0], [ -10, -3 ,-7 ,-5]))
print(solution("R", 3, [-2, 3], [0, 1]))
