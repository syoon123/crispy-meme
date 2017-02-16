from display import *
def draw_line( screen, x0, y0, x1, y1, color ):    
    A=y1-y0
    B= -(x1-x0)
    x=x0
    y=y0
    #Octant 1
    if (A<=-B and A>=0 and B<=0):
        d=2*A+B 
        while (x<x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*B 
            x+=1
            d+=2*A
    #Octant 2
    if (A>=-B and A>=0 and B<=0):
        d=2*B+A 
        while (y<y1):
            plot(screen,color,x,y)
            if (d<0):
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    #Octant 7
    if (A<=B and A<=0 and B<=0):
        d=A-2*B
        while (y>y1):
            plot(screen,color,x,y)
            if(d>0):
                x+=1
                d+=2*A
            y-=1
            d-=2*B
    #Octant 8
    if (A>=B and A<=0 and B<=0):
        d=2*A-B
        while (x<x1):
            plot(screen,color,x,y)
            if (d<0):
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    #The Rest of the Octants
    if (B>0):
        draw_line( screen, x1, y1, x0, y0, color )
