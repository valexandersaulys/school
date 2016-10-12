"""
Completed for Prof. Ragin's PHYS-131 class
Code by Vincent A. Saulys
PHYS-131, Fall 2016
"""
import pandas as pd
from math import *

# Define the initial conditions
t_inc = 0.01;
v_i = 30.0; #m/s
v_t = 43.0; #m/s
mass = 0.145; # kg
gravity = 9.81;
r = 0.037;
area = 4.2e-3;
theta = 45; # degrees
v_ix = v_ix_r = v_i*cos(radians(theta)); #radians() is a converter
v_iy = v_iy_r = v_i*sin(radians(theta));
c_x = 0; c_y = 0; c_nx=0; c_ny=0;

# Holder lists
v_s = [[v_ix,v_iy]];
coordinates = [[c_x,c_y,c_nx,c_ny]]; # range will be maximum x displacement

# Loop over until it ends
A = True
while A:
    # With Air resistance
    f_net_x_r = -1 * mass*gravity*((v_ix/v_t)**2)
    f_net_y_r = -1 * mass*gravity + -1*mass*gravity*((v_iy/v_t)**2)
    a_x_r = f_net_x_r / mass;
    a_y_r = f_net_y_r / mass;
    v_fx_r = v_ix_r + a_x_r*t_inc;
    v_fy_r = v_iy_r + a_y_r*t_inc;

    # Without air resistance
    f_net_x = 0;
    f_net_y = -1 * mass * gravity;
    a_x = f_net_x / mass;
    a_y = f_net_y / mass;
    v_fx = v_ix + a_x*t_inc;
    v_fy = v_iy + a_y*t_inc;

    # Calculate coordinates
    nc_x = c_x + v_fx_r*t_inc + (0.5)*a_x*(t_inc**2)
    nc_y = c_y + v_fy_r*t_inc + (0.5)*a_y*(t_inc**2)
    nc_nx = c_nx + v_fx*t_inc + (0.5)*a_x_r*(t_inc**2)
    nc_ny = c_ny + v_fy*t_inc + (0.5)*a_y_r*(t_inc**2)

    # With Air Resistance
    v_ix_r = v_fx_r;
    v_iy_r = v_fy_r;
    c_x = nc_x;
    c_y = nc_y;

    # Without Air Resistance
    v_ix = v_fx;
    v_iy = v_fy;
    c_nx = nc_nx;
    c_ny = nc_ny;

    # Append everything to lists
    v_s.append([v_ix,v_iy,v_ix_r,v_iy_r]);
    coordinates.append([c_x,c_y,c_nx,c_ny]);  # this is flipped unfortuantely 

    # Check to see if conditions are over
    if nc_ny <= 0:
       A = False; 
    else:
        A = True;

# Then plot
from ggplot import *
first = [ [x[0],x[1],'Air Resistance'] for x in coordinates]
second = [ [x[2],x[3],'Gravity Only'] for x in coordinates]
coord_array = pd.DataFrame(first+second,
                           columns=['x','y','type']);
print coord_array
p = ggplot(coord_array,aes(x='x',y='y',color='type')) \
    + geom_point() \
    + xlim(0,100) + ylim(0,25) \
    + scale_color_manual(['red','green']) \
    + labs(x="X",y="Y") + ggtitle("Air Resistance vs. No Air Resistance");

print p;
    
    
