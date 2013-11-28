import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import *

#====================
def example_animate_moon():
#====================

  #----------
  def init():
  #----------
     print "calling init()"
     x_small  = []
     y_small  = []
     x_large  = []
     y_large  = []
     line1.set_data(x_small, y_small)
     line2.set_data(x_large, y_large)
     return line1,line2

  #----------------------
  def animate(i_time):
  #----------------------
    if(i_time%10 == 0):
       print "calling animate -> ", i_time

    # --- ----------------------------------------------------------
    # [1] initialise the particle position and velocity vectors
    # --- ----------------------------------------------------------
    if(i_time == 0):

        print ""
        print "initialising the positions"
        print ""

        #--/ small objects starts at (0,1) and large object at (0,1)
        x_small.append(1)      
        y_small.append(1)
        x_large.append(0)      
        y_large.append(0)      

    # --- -------------------------------------------------------------
    # [2] update the positions and velocities of small particle
    # --- -------------------------------------------------------------
    angle = i_time*0.01
    x_small[0] = cos(angle)
    y_small[0] = sin(angle)

    # --- -----------------------    
    # [3] return new vectors
    # --- -----------------------
    line1.set_data(x_small, y_small)
    line2.set_data(x_large, y_large)

    return line1,line2
    #---- end of internal funtion animate()

  # -------------------------------
  #--/ main program: the plot
  # -------------------------------
  x_small = []
  y_small = []
  x_large = []
  y_large = []
  
  fig = plt.figure()
  plt.grid()
  axes = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
  line1, = axes.plot(x_small, y_small, 'ro', lw=2, markersize=6)
  line2, = axes.plot(x_large, y_large, 'bo', lw=2, markersize=20)
  
   #--/ do the actual animation
  anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=20000, interval=2, blit=True)

  plt.show()




  return

#----- example_animate_planets() --------








# ============
# MAIN PROGRAM
# ============
example_animate_moon()














###-------------
##def figure3():
###-------------
##
## x = np.arange(0.,2.01,0.01)
## y1 = x*x
## y2 = 4-x*x
## print x
##
## y3 = []
## for i in range(0,len(x)):
##    if(y1[i]>y2[i]):
##       y3.append(y2[i])
##    else:
##       y3.append(y1[i])
##        
##
## plt.plot(x,y1, 'r-')
## plt.plot(x,y2, 'r-')
## plt.fill(x,y3, facecolor='blue', alpha = 0.5)
## plt.show()
##

    
