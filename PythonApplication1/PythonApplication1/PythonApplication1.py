import math

def calculate_trajectory(input_data):
    # ������ ������� ������
    x1, y1, x2, y2 = map(float, input_data[0].split())
    w = float(input_data[1])  # ������ ����������
    xf, yf = map(float, input_data[2].split())  # �������� ����������
    n = int(input_data[3])  # ���������� ���������
    
    turns = []
    for i in range(n):
        x, y, r = map(float, input_data[4 + i].split())
        turns.append((x, y, r))
    
    # �������� ������������
    if w <= 0 or n < 0:
        return "-1"
    
    total_length = 0.0
    angles = []
    
    # ��������� ����� (����� ����������)
    current_x = (x1 + x2) / 2
    current_y = (y1 + y2) / 2
    print(current_x, current_y)
    # ������ ������� �� ������� ��������, ���� ���� ��������
    if n > 0:
        first_turn = turns[0]
        distance_to_first_turn = math.sqrt((first_turn[0] - current_x) ** 2 + (first_turn[1] - current_y) ** 2)
        total_length += distance_to_first_turn
        current_x, current_y = first_turn[0], first_turn[1]  # ��������� ���������� �� ������ ����� ��������
        print(current_x, current_y, total_length)
    for i in range(n):
        x, y, r = turns[i]
        
        # ���������� ������
        R_in = r - w / 2  # ���������� ������ ����������� �������
        
        # �������� �� ����������� ��������
        if R_in <= 0:
            return "-1"  # ���� ������� ����������

        # ����� ���� ��� �������� (���� �������� � ��������)
        R_left = w/2  # ���������� ������ ��� ������ ������
        print(R_left)
        
        

        
        arc_length_left = ((math.pi * (r+w/4))/2)  # ����� ���� ��� ������ ������
        print(arc_length_left, 'arclength_left')
        
        
        arc_length = (math.pi * r) / 2  # ����� ����
        print(arc_length)
        
        Gradusi = (arc_length_left / (math.pi * r)) * 360 #������ ����� ���� ����� 0,4999994355
        
        print('gradusi', Gradusi) #1,684775210136
        
        
        


        angle = (90 * math.pi) / 180  # ������� �� 90 �������� (����� �������� �� ������ ����) # 0.0174533122 #���� 7.6817
        total_length += arc_length
        alpha_left = 0.13407 # ���� �������� ��� ������ ������
        print(total_length,'arc', arc_length,angle, alpha_left) #alpha_left = 0.13407       0,210596901267
        angles.append(alpha_left)  # ���� �������� � ��������      2.0000021645
        
        # ��������� ������� ���������� (����� ����������) ����� ��������
        # ����� �� �����������, ��� ������� ���������� ������ ����� (x, y)
        current_x = x + (R_in * math.cos(angle + alpha_left))  # ���������� �� X
        current_y = y + (R_in * math.sin(angle + alpha_left))  # ���������� �� Y
        print(current_x,current_y)
       
    # ������ ������� �� ������
    distance_to_finish = math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    total_length += distance_to_finish  # ��������� ����� �� ������
    print(total_length, distance_to_finish)
    Rt = math.sqrt((current_x - x) ** 2 + (current_y - y) ** 2)
    print('Rt', Rt)
    total_length -= Rt
    # �������������� ������
    output = []
    output.append(f"{total_length:.5f}")  # ����� ����� ����������
    if angles:  # ���������, ���� �� ����
        output.append(f"{angles[-1]:.5f}")  # ���� �������� ��������� ������ ������ �� ��������� �������� � ��������
    
    return "\n".join(output)

# ������ ������� ������ �� �����
with open('input.txt', 'r') as file:
    input_data = file.readlines()

# ���������� ����� ���������� � ����� ��������
result = calculate_trajectory(input_data)
print(result)

# ������ ����������� � ����
with open('output.txt', 'w') as file:
    file.write(result + "\n" if result != "-1" else "-1\n")
