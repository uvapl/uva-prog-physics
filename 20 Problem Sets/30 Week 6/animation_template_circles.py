import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import *

#====================================
def example_animate_moving_circles():
#====================================

  # ----------------
  #--/ main program:
  # ----------------
  global Nparticles
  global x,y,r

  #--/ define parameters of the box and figure
  xmin_box = -2
  xmax_box =  2
  ymin_box = -2
  ymax_box =  2
  fig = plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')
  ax = plt.axes(xlim=(xmin_box, xmax_box), ylim=(ymin_box, ymax_box))

  #--------------------------------------------------------------------
  # [1] initiate all particles 
  #      o x-position for all particles (list x)
  #      o y-position for all particles (list y)
  #      o radius for each particle (list r)  
  #      o abstract/plotting: a list of circle-objects
  #--------------------------------------------------------------------
  x  = []
  y  = []
  r  = []
  circles = []
  radius_balls = 0.1
  Nparticles = 2

  #--/ define starting position (x and y) for each ball and define radius (r)
  for i_particle in range(0,Nparticles):
      x_i = 1.0            #-- start 1st particle on left hand side
      if(i_particle == 1): #-- start 2nd particle on left hand side
          x_i = -1.0
      y_i = 0.0      
      radius_ball = 0.1
      x.append(x_i)
      y.append(y_i)
      r.append(radius_ball)

  #--/ use the parameters in previous step to define 'real' circles (objects)
  #    and add the circle object to the plot
  for i_particle in range(0,Nparticles):
      if( i_particle == 0 ):
         circles.append(plt.Circle((x[i_particle], y[i_particle]), radius = r[i_particle], fc = 'red'))   # red ball
      else:
         circles.append(plt.Circle((x[i_particle], y[i_particle]), radius = r[i_particle], fc = 'blue'))   # blue ball
      ax.add_patch(circles[i_particle])


  #----------
  def init():
  #----------
  #--/ stuff entered here stays on the screen forever, so put circles at dummy position
    global Nparticles
    print " init():: entering dummy start values"
    x_dummy = -10.
    y_dummy = -10.
    for i_particle in range(0,Nparticles):
      circles[i_particle].center = (x_dummy, y_dummy)
 
    return circles

  #-------------------
  def animate(i_time):
  #-------------------
  #--/ this routine is called every time step

    global x,y,r,Nparticles

    #--/ at time 0 initiate all circles on the screen at their locations
    if(i_time == 0):
      print " animate(t==0):: enter start-values for circles from main program"       
      for i_particle in range(0,Nparticles):
        circles[i_particle].center = (x[i_particle], y[i_particle])
           
    #------------------------------------------------
    #--/ [STEP 1] compute new position of the circles
    #------------------------------------------------
    for i_particle in range(0,Nparticles):

      #--/ get positions of the circles
      xi, yi = circles[i_particle].center
      ri = r[i_particle]
      print " Time-step: %d   -> position circle %d = (%5.2f, %5.2f) with radius %5.2f" % (i_time, i_particle,xi,yi,ri)      
 
      #--------------------------------------------------
      #--/ compute new position and velocity of the balls
      #--------------------------------------------------
      angle = i_time *0.01
      offset = 0
      if(i_particle == 1):
          offset = pi          
      x_new  =  cos(angle+offset)
      y_new  =  sin(angle+offset)
            
      #--/ update the positions and velocitis of all particles
      x[i_particle]  = x_new
      y[i_particle]  = y_new

    #---------------------------
    #--/ update circle positions
    #---------------------------
    for i_particle in range(0,Nparticles):
        circles[i_particle].center = (x[i_particle], y[i_particle])

    #--/ return (end of simulate_colliding_balls())
    return circles




  #--/ do the actual animation (part of main program)
  anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=20000, interval=2, blit=True)

  plt.show()


  return

#----- end example_animate_moon() 








# ============
# MAIN PROGRAM
# ============
example_animate_moving_circles()












    
