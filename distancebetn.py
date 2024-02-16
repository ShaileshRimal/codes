import math

# def calcdist(x1,y1,x2,y2):
#     distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
#     return distance

# print(calcdist(4,0,6,6))


p1=[4,0]
p2=[6,6]

distance=math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))

print(distance)