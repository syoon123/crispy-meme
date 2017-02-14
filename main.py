from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(screen, 50, 50, 450, 100, color)

draw_line(screen, 50, 50, 100, 450, color)

draw_line(screen, 50, 250, 450, 100, color)

display(screen)
save_extension(screen, 'img.png')
