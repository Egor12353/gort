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

    # Прямой участок до первого поворота, если есть повороты
    if n > 0:
        first_turn = turns[0]
        distance_to_first_turn = math.sqrt((first_turn[0] - current_x) ** 2 + (first_turn[1] - current_y) ** 2)
        total_length += distance_to_first_turn
        total_length -= r
        current_x, current_y = first_turn[0], first_turn[1]  # Обновляем координаты до первой точки поворота

    for i in range(n):
        x, y, r = turns[i]
        
        # Внутренний радиус
        R_in = r - w
        
        # Проверка на возможность поворота
        if R_in <= 0:
            return "-1"  # Если поворот невозможен

        # Длина дуги для поворота (угол поворота в радианах)
        angle = math.pi / 73,5  # Поворот на 90 градусов (можно заменить на другой угол)
        arc_length = angle *  R_in # Длина дуги
        total_length += arc_length
        
        angles.append(angle)  # Угол поворота в радианах
        
        # Обновляем текущие координаты (центр автомобиля) после поворота
        # Здесь мы предположим, что поворот происходит вокруг точки (x, y)
        # Используем координаты поворота для расчета новых координат
        current_x = x + (r * math.cos(angle))  # Обновление по X
        current_y = y + (r * math.sin(angle))  # Обновление по Y
        print(current_x, current_y)
    # Прямой участок до финиша
    distance_to_finish = math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    total_length += distance_to_finish
    print(total_length)
    total_length -= r
    # Форматирование вывода
    output = []
    output.append(f"{total_length:.5f}")
    for angle in angles:
        output.append(f"{angle:.5f}")
    
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