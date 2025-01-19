import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def arc_length(radius, angle):
  return radius * angle

x1, y1, x2, y2 = map(float, input().split())
w = float(input())
xf, yf = map(float, input().split())
n = int(input())

points = []
for i in range(n):
    points.append(list(map(float, input().split())))

# ѕриблизительный расчет центра автомобил€ (нужны более точные данные дл€ точности!)
start_x = (x1 + x2) / 2
start_y = (y1 + y2) / 2
print(start_x, start_y)
total_length = 0
prev_x, prev_y = start_x, start_y

for i in range(n):
    x_curr, y_curr, R = points[i]
    print(x_curr, y_curr, R)
    total_length += distance(prev_x, prev_y, x_curr, y_curr)  # –ассто€ние до начала поворота
    print(total_length)
    # ƒобавление длины дуги поворота (приблизительное)
    inner_radius = R - w
    angle = w / inner_radius # ѕриблизительное вычисление угла -  нужно улучшение!
    total_length += arc_length(inner_radius, angle)
    print(inner_radius, angle, total_length)
    prev_x, prev_y = x_curr, y_curr
    print(prev_x, prev_y)
total_length += distance(prev_x, prev_y, xf, yf)
print(total_length)
#ѕроверка возможности построени€ траектории
if n > 0 and any(R <= w for _, _, R in points):
    print("-1")
else:
    angles = []
    for x, y, R in points:
        inner_radius = R - w
        # ѕриблизительное вычисление угла - нужно улучшение!
        angle = w / inner_radius
        print(angle)
        angles.append(angle)

    print(f"{total_length:.5f}")
    for angle in angles:
        print(f"{angle:.5f}")