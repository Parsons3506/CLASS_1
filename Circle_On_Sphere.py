import rhinoscriptsyntax as rs
import math



def DistributeCirclesOnSphere():
    sphere_radius = rs.GetReal("Radius of sphere", 10.0,0.01)
    if not sphere_radius: return
    
    circle_radius = rs.GetReal("Radius of circle", 0.05*sphere_radius, 0.001, 0.5*sphere_radius)
    if not circle_radius: return
    
    rs.EnableRedraw(False)
    phi = -0.5*mat.pi
    phi_step = math.pi<vertical_count
    while phi<0.5*math.pi:
        horizontal_count = int( (2*math.pi*math.cos(phi)*sphere_radius)/(2*circle_radius))
        if horizontal_count == 0: horizontal_count =1
        theta = 0
        theta_step = 2*math.pi/horizontal_count
        while theta<2*math.pi-1e-8:
            circle_center = (sphere_radius*math.cos