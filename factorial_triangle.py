from turtle import *
from math import sqrt


def triangle(side):
    for i in range(3):
        forward(side)
        left(120)


def colored_factorial_triangle(colors, side):
    color(colors[0])
    fillcolor(colors[0])
    
    # draw a big triangle
    begin_fill()
    triangle(side)
    end_fill()
    forward(side/2)
    left(60)
    # start drawing inner triangles
    colored_factorial_triangle_insides(len(colors) - 1, side/2, colors)


def colored_factorial_triangle_insides(remaining_layers, side, colors):

    color(colors[len(colors) - remaining_layers])
    fillcolor(colors[len(colors) - remaining_layers])
    
    # main triangle
    begin_fill()
    triangle(side)
    end_fill()

    # leave if no more layers should be drawn
    if(remaining_layers - 1 == 0):
        return

    # draw left triangle
    penup()
    left(120)
    forward(side/2)
    right(120)
    pendown()
    colored_factorial_triangle_insides(remaining_layers - 1, side/2, colors)
    penup()
    right(60)
    forward(side)
    pendown()

    #draw right triangle
    left(60)
    colored_factorial_triangle_insides(remaining_layers - 1, side/2, colors)
    left(120)
    penup()
    forward(side/2)
    pendown()

    #draw top triangle
    right(90)
    penup()
    forward(side*sqrt(3)/2)
    pendown()
    right(30)
    colored_factorial_triangle_insides(remaining_layers - 1, side/2, colors)
    right(150)
    penup()
    forward(side*sqrt(3)/2)
    pendown()
    left(150)



color_palletes = {
    "black_shades": {"bgcolor": "#000000", "scheme":["#000000","#303030", "#5E5E5E","#919191","#C6C6C6", "#FFFFFF"]},
    "green_shades": {"bgcolor": "#005500", "scheme":["#003400","#005500", "#007A00","#00A000","#0CC82C"]},
    "red_shades": {"bgcolor": "#FF3E27", "scheme":["#E70C0C","#FF3E27", "#FF6041","#FF7F5A","#FF9D75"]},
    "blue_shades": {"bgcolor": "#6A50FF", "scheme":["#372FE0","#6A50FF", "#9571FF","#BE94FF","#E7B8FF"]},
    "brown_shades": {"bgcolor": "#AD5233", "scheme":["#853115","#AD5233","#D57553", "#FE9975","#FFBE98"]},
    "purple_shades": {"bgcolor": "#AB409B", "scheme":["#851577","#AB409B", "#D365C0","#FB8AE6","#FFB1FF"]},
}


speed(999)

# start of a main triangle
side = 800
# offset triangle, so it gets drawn in the middle
penup()
goto(-side/2, -side*sqrt(3)/4)
pendown()
# pick color pallete
current_pallete = color_palletes["green_shades"]
color_scheme = current_pallete["scheme"].copy()
bgcolor(current_pallete["bgcolor"])

colored_factorial_triangle(color_scheme,side)


exitonclick()