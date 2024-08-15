import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length = 200
point = sd.get_point(300, 300)

v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
v1.draw()
v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
v2.draw()
v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
v3.draw()

sd.pause()
