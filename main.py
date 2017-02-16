from display import *
from draw import *

screen = new_screen()
color1 = [ 0, 255, 0 ]
color2 = [ 0, 0, 255 ]

#Axes
draw_line(screen, 0, 250, 500, 250, color1)
draw_line(screen, 250, 0, 250, 500, color1)

#y=x, y=-x
draw_line(screen, 0, 0, 500, 500, color1)
draw_line(screen, 0, 500, 500, 0, color1)

draw_line(screen, 250, 250, 500, 350, color2)
draw_line(screen, 250, 250, 300, 500, color2)

draw_line(screen, 250, 250, 500, 160, color2)
draw_line(screen, 250, 250, 350, 0, color2)

draw_line(screen, 250, 250, 170, 500, color2)
draw_line(screen, 250, 250, 0, 300, color2)

draw_line(screen, 250, 250, 0, 175, color2)
draw_line(screen, 250, 250, 120, 0, color2)

display(screen)
save_extension(screen, 'img.png')
