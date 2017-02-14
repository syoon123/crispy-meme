from display import *
def draw_line( screen, x0, y0, x1, y1, color ):    
    A=y1-y0
    B= -(x1-x0)
    #Octant 1
    if (A<=-B and A>=0 and B<0):
        x=x0
        y=y0
        d=2*A+B 
        while (x<=x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*B 
            x+=1
            d+=2*A
    #Octant 2
    if (A>-B and A>0 and B<=0):
        x=y0
        y=x0
        d=2*B+A 
        while (x<=x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*A 
            x+=1
            d+=2*B
    #Octant 8
    if (A<B and A<0 and B<0):
        x=x0
        y=y0
        d=2*A-B 
        while (x<=x1):
            plot(screen,color,x,y)
            if (d>0):
                y-=1
                d-=2*B 
            x+=1
            d+=2*A

