import math

def calculate_trajectory(input_data):
    # ������ ������� ������
    x1, y1, x2, y2 = map(float, input_data[0].strip().split())
    w = float(input_data[1].strip())  # ������ �����
    xf, yf = map(float, input_data[2].strip().split())  # �������� ����������
    n = int(input_data[3].strip())  # ���������� ���������
    
    turns = []
    for i in range(n):
        x, y, r = map(float, input_data[4 + i].strip().split())
        turns.append((x, y, r))
    
    # �������� ������������
    if w <= 0 or n < 0:
        return "-1"
    
    total_length = 0.0
    angles = []
    
    # ��������� ����� (����� ����������)
    current_x = (x1 + x2) / 2
    current_y = (y1 + y2) / 2

    # ������ ������� �� ������� ��������, ���� ���� ��������
    if n > 0:
        first_turn = turns[0]
        distance_to_first_turn = math.sqrt((first_turn[0] - current_x) ** 2 + (first_turn[1] - current_y) ** 2)
        total_length += distance_to_first_turn
        current_x, current_y = first_turn[0], first_turn[1]  # ��������� ���������� �� ������ ����� ��������

    for i in range(n):
        x, y, r = turns[i]
        
        # ���������� ������
        R_out = r   # ������� ������
        R_in = R_out - w  # ���������� ������ ����������� �������

        # �������� �� ����������� ��������
        if R_in <= 0 or R_out <= 0:
            return "-1"  # ���� ������� ����������

        # ����� ���� ��� ��������
        angle = math.radians(90)  # ���������� 90 �������� ��� ������� (����� ������������ �����)
        arc_length = angle * R_in  # ����� ���� ��� ����������� �������
        total_length += arc_length

        # ���� �������� ��������� ������ ������
        alpha_left = angle * (R_in / R_out)  # ���� �������� ��� ������ ������
        angles.append(alpha_left)  # ���� �������� � ��������

        # ��������� ������� ���������� (����� ����������) ����� ��������
        current_x = x + (R_in * math.cos(math.radians(90)))  # ���������� �� X
        current_y = y + (R_in * math.sin(math.radians(90)))  # ���������� �� Y

    # ������ ������� �� ������
    distance_to_finish = math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    total_length += distance_to_finish  # ��������� ����� �� ������

    # �������������� ������
    output = []
    output.append(f"{total_length:.5f}")  # ����� ����� ����������
    if angles:  # ���������, ���� �� ����
        for angle in angles:
            output.append(f"{angle:.5f}")  # ���� �������� ��������� ������ ������ � ��������
    
    return "\n".join(output)

# ������ ������� ������ �� �����
with open('input.txt', 'r') as file:
    input_data = file.readlines()

# ���������� ����� ���������� � ����� ��������
result = calculate_trajectory(input_data)

# ������ ����������� � ����
with open('output.txt', 'w') as file:
    file.write(result + "\n" if result != "-1" else "-1\n")

# �����������: ������� ��������� �� �����
print(result)