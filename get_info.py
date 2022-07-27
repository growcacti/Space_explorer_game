
import pygame as pg
import math




def info(origin, destination):
    distance = math.hypot(destination[0] - origin[0], destination[1] - origin[1])
##    print(distance)
##    print("distance")
##    
    x2_dist = destination[0] - origin[0]
    y2_dist = destination[1] - origin[1]
    
    angle = math.atan2(-y2_dist, x2_dist) % (2 * math.pi)
    angle2 = math.atan2(-y2_dist, x2_dist) 
##    print(angle, angle2)
##    print("angle")
    angle_degrees = math.degrees(angle)
##    print(angle_degrees)
##    print("degrees")
    x_dist = origin[0] - destination[0]
    y_dist = origin[1] - destination[1]
    # x axis_reflection 
    x_ref= math.atan2(-y_dist, -x_dist) % (2 * math.pi)

    x_ref2 = math.atan2(-y_dist, -x_dist)
##    print(x_ref, x_ref2)
##    print("_xaxis_reflection")


 #   y axis_reflection 

    y_ref = math.atan2(y_dist, x_dist) % (2 * math.pi)
    y_ref2 = math.atan2(y_dist, x_dist)
##    print(y_ref, y_ref2)
##    print("yaxis_reflection")

    #opposite angle
    op_ang = math.atan2(-y_dist, x_dist) % (2 * math.pi)
    op_ang2 = math.atan2(-y_dist, x_dist) 
    op_ang_deg = math.degrees(op_ang) 
##    print(op_ang, op_ang2)
##    print("opposite_angle")
##    print(op_ang_deg)
##    print("opposite angle degrees")
    dand = op_ang_deg - angle_degrees      
##    print(dand)
##    print("opposite minus angle")
    pos = destination
    

    project = (pos[0] + (math.cos(angle) * distance), pos[1] - (math.sin(angle) * distance))
##    print(project)
##    print("pos projected distance at angle")
    return distance, angle, x_ref, y_ref, op_ang, project


##def get_random_new_coor(x, y, objw, objh):
##    cam_rect = pg.Rect(camx, camy, WIDTH, HEIGHT)
##    newx = random.randint((camx - WIDTH), (camx + 2*WIDTH)
##    newy = random.randint((camy - HEIGHT), (camy + 2*HEIGHT)
##    obj_rect = pg.Rect(newx, newy, objW, objh)
##    if not objRect.collderect(cam_rect):
##        return x, y              
