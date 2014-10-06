# ============================================
# Template for animation (particles in a box)
# Author: Nick Dijcker
# Date:   October 2014
# ============================================

from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos, pi

# NOT A GOOD EXAMPLE ON HOW TO COMMENT.

radius_balls = 0.5


'''
FuncAnimation basically shows a lot of plots, each frame is one plot. This
particular function uses the output from another function to update the plot.

I will explain everything with blitting enabled. Blitting is a technique for
quickly generating new pictures by only editing the pixels that are changed
instead of creating a whole new picture.

Because of blitting, the first frame will be used as canvas. This results in all
objects on the first frame permanently showing on that position. 
'''


#-----------------------------------------------
def example_animate_moving_circles(radius_balls):
#-----------------------------------------------
  '''
  Creates a animation of a circle moving in a circle.
  '''

  
  #---------
  def init():
  #---------

    '''
    Called by FuncAnimation using init_func. This will be ran before the actual
    animation starts and is basically the first frame. You want to use dummy
    position since the first frame will be used as canvas and you want this
    to be a blank.

    Returns a list of the objects to draw. 
    '''

    circles[0].center = (100, 100) # outside of plot
    circles[1].center = (100, 100)

    return circles

    
  #------------------
  def update(i_time):
  #------------------

    '''
    This function is being called by FuncAnimation() each frame.
    It basically updates the positions of the objects.

    i_time: the current frame number.

    Returns a list of the objects to draw. 
    '''

    # Calculate new position.
    angle = i_time *0.01

    x1  =  cos(angle)
    y1  =  sin(angle)
    x2  =  cos(angle+pi)
    y2  =  sin(angle+pi)


    # update circle positions
    circles[0].center = (x1, y1)
    circles[1].center = (x2, y2)

    return circles



  # canvas for the animation, figsize is the resolution of the canvas. 
  fig = plt.figure(figsize=(6, 6))
  ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

  x  = 1.0
  y  = 0.0

  r = radius_balls

  

  '''
  The objects that you will draw have to be defined here, before you call
  FuncAnimation.
  '''

  circles = []
  circles.append(plt.Circle((x, y), radius = r, fc ='red')) # Circle object
  circles.append(plt.Circle((x, y), radius = r, fc ='blue')) 
  ax.add_patch(circles[0]) # adds the object to the canvas.
  ax.add_patch(circles[1])


  '''
  Finally, the call to the function FuncAnimation:
  Input parameters:
     - fig:       the area to draw on
     - update:    function name of the function that updates the positions
     - init_func: function name of the function that initialize
     - frames:    the amount of frames the animation has to do
     - interval:  the interval between the frames in milliseconds
     - blit:      (see above) technique for faster animations.
     - repeat:    repeat the animation (True or False)    
  '''

  anim = animation.FuncAnimation(fig, update, init_func=init,
                            
                            frames=2000, interval=2, blit=True, repeat = False)
  plt.show()





# ==============================
#  The main call to the function
# ==============================
example_animate_moving_circles(radius_balls)





# ============================
# SOME BASIC QUESTIONS/ANSWERS
# ============================
'''
Q: WHAAAT? Functions defined inside functions??? Whats happening?

A: Normally we don't do this but for once we allow this. (Because FuncAnimation requires this)


Q: What is plt.Circle?

A: It is a Circe class, something which you didn't learn yet. A class is
   basically a collection of functions, somehow similar to how a module works.
   ( like math.sin() you can do Circle.center() )


Q: How can I add more objects?

A: Add more to the list. (in this case the list 'circles')
'''







    



