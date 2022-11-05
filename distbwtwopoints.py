#DISTANCE BETWEEN TWO POINTS
import math
def dist_twopoints(x1,x2,y1,y2):
    x = int(pow((x2 - x1) , 2))
    y = int(pow((y2 - y1) , 2))
   
    
    print(math.sqrt(x + y))
dist_twopoints(1,1,1,1)
