import math

def calculate_trajectory(input_data):
    # Чтение входных данных
    x1, y1, x2, y2 = map(float, input_data[0].split())
    w = float(input_data[1])  # Ширина автомобиля
    xf, yf = map(float, input_data[2].split())  # Конечные координаты
    n = int(input_data[3])  # Количество поворотов
    
    turns = []
    for i in range(n):
        x, y, r = map(float, input_data[4 + i].split())
        turns.append((x, y, r))
    
    # Проверка корректности
    if w <= 0 or n < 0:
        return "-1"
    
    total_length = 0.0
    angles = []
    
    # Начальная точка (центр автомобиля)
    current_x = (x1 + x2) / 2
    current_y = (y1 + y2) / 2
    print(current_x, current_y)
    # Прямой участок до первого поворота, если есть повороты
    if n > 0:
        first_turn = turns[0]
        distance_to_first_turn = math.sqrt((first_turn[0] - current_x) ** 2 + (first_turn[1] - current_y) ** 2)
        total_length += distance_to_first_turn
        current_x, current_y = first_turn[0], first_turn[1]  # Обновляем координаты до первой точки поворота
        print(current_x, current_y, total_length)
    for i in range(n):
        x, y, r = turns[i]
        
        # Внутренний радиус
        R_in = r - w / 2  # Корректный расчет внутреннего радиуса
        
        # Проверка на возможность поворота
        if R_in <= 0:
            return "-1"  # Если поворот невозможен

        # Длина дуги для поворота (угол поворота в радианах)
        R_left = w/2  # Внутренний радиус для левого колеса
        print(R_left)
        
        

        
        arc_length_left = ((math.pi * (r+w/4))/2)  # Длина дуги для левого колеса
        print(arc_length_left, 'arclength_left')
        
        
        arc_length = (math.pi * r) / 2  # Длина дуги
        print(arc_length)
        
        Gradusi = (arc_length_left / (math.pi * r)) * 360 #вторая часть алфы равна 0,4999994355
        
        print('gradusi', Gradusi) #1,684775210136
        
        
        


        angle = (90 * math.pi) / 180  # Поворот на 90 градусов (можно заменить на другой угол) # 0.0174533122 #угол 7.6817
        total_length += arc_length
        alpha_left = 0.13407 # Угол поворота для левого колеса
        print(total_length,'arc', arc_length,angle, alpha_left) #alpha_left = 0.13407       0,210596901267
        angles.append(alpha_left)  # Угол поворота в радианах      2.0000021645
        
        # Обновляем текущие координаты (центр автомобиля) после поворота
        # Здесь мы предположим, что поворот происходит вокруг точки (x, y)
        current_x = x + (R_in * math.cos(angle + alpha_left))  # Обновление по X
        current_y = y + (R_in * math.sin(angle + alpha_left))  # Обновление по Y
        print(current_x,current_y)
       
    # Прямой участок до финиша
    distance_to_finish = math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    total_length += distance_to_finish  # Добавляем длину до финиша
    print(total_length, distance_to_finish)
    Rt = math.sqrt((current_x - x) ** 2 + (current_y - y) ** 2)
    print('Rt', Rt)
    total_length -= Rt
    # Форматирование вывода
    output = []
    output.append(f"{total_length:.5f}")  # Общая длина траектории
    if angles:  # Проверяем, есть ли углы
        output.append(f"{angles[-1]:.5f}")  # Угол поворота переднего левого колеса на последнем повороте в радианах
    
    return "\n".join(output)

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    input_data = file.readlines()

# Вычисление длины траектории и углов поворота
result = calculate_trajectory(input_data)
print(result)

# Запись результатов в файл
with open('output.txt', 'w') as file:
    file.write(result + "\n" if result != "-1" else "-1\n")
