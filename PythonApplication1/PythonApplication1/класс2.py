import math

def calculate_trajectory(input_data):
    # Чтение входных данных
    x1, y1, x2, y2 = map(float, input_data[0].strip().split())
    w = float(input_data[1].strip())  # Ширина трека
    xf, yf = map(float, input_data[2].strip().split())  # Конечные координаты
    n = int(input_data[3].strip())  # Количество поворотов
    
    turns = []
    for i in range(n):
        x, y, r = map(float, input_data[4 + i].strip().split())
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
        current_x, current_y = first_turn[0], first_turn[1]  # Обновляем координаты до первой точки поворота

    for i in range(n):
        x, y, r = turns[i]
        
        # Внутренний радиус
        R_out = r   # Внешний радиус
        R_in = R_out - w  # Корректный расчет внутреннего радиуса

        # Проверка на возможность поворота
        if R_in <= 0 or R_out <= 0:
            return "-1"  # Если поворот невозможен

        # Длина дуги для поворота
        angle = math.radians(90)  # Используем 90 градусов для примера (можно использовать любое)
        arc_length = angle * R_in  # Длина дуги для внутреннего радиуса
        total_length += arc_length

        # Угол поворота переднего левого колеса
        alpha_left = angle * (R_in / R_out)  # Угол поворота для левого колеса
        angles.append(alpha_left)  # Угол поворота в радианах

        # Обновляем текущие координаты (центр автомобиля) после поворота
        current_x = x + (R_in * math.cos(math.radians(90)))  # Обновление по X
        current_y = y + (R_in * math.sin(math.radians(90)))  # Обновление по Y

    # Прямой участок до финиша
    distance_to_finish = math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    total_length += distance_to_finish  # Добавляем длину до финиша

    # Форматирование вывода
    output = []
    output.append(f"{total_length:.5f}")  # Общая длина траектории
    if angles:  # Проверяем, есть ли углы
        for angle in angles:
            output.append(f"{angle:.5f}")  # Угол поворота переднего левого колеса в радианах
    
    return "\n".join(output)

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    input_data = file.readlines()

# Вычисление длины траектории и углов поворота
result = calculate_trajectory(input_data)

# Запись результатов в файл
with open('output.txt', 'w') as file:
    file.write(result + "\n" if result != "-1" else "-1\n")

# Опционально: выводим результат на экран
print(result)