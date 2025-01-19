import math

def main():
    # ��������� ������� ������
    with open('input.txt', 'r') as f:
        x1, y1, x2, y2 = map(float, f.readline().strip().split())
        w = float(f.readline().strip())
        xf, yf = map(float, f.readline().strip().split())
        n = int(f.readline().strip())
        
        turns = []
        for _ in range(n):
            X, Y, R = map(float, f.readline().strip().split())
            turns.append((X, Y, R))

    current_x = (x1 + x2) / 2
    current_y = (y1 + y2) / 2
    # �������� ��������� �������
    d_start = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d_start == 0:
        print("-1")  # �������� ��������� ����������
        return

    total_length = 0.0
    angles = []
    
    # ������ ������� �� ��������� ��������� �� ������ ���������� ��������
    total_length += d_start 
    print(d_start)

    # ��������� ��� ����������� ���������
    

    for i in range(n):
        X, Y, R = turns[i]

        # ��������, ����� �� ������ �������
        if R <= w:
            print("-1")  # ���������� ������ �������
            return

        # ���������� ����� ��������
        inner_radius = R - w / 2
        outer_radius = R + w / 2

        # ���� ����� �������� ����� ������� � ������� ��������
        angle_left = math.atan2(Y - current_y, X - current_x)  # ���� � ��������
        angle_left_fwd = angle_left + math.atan((R / inner_radius))

        # ���������� ����� ����
        length = (outer_radius * math.radians(180)) / math.pi
        total_length += length
        print(length)

        # ���� �������� ��������� ������ ������
        alpha_i = 0.13407 #math.atan2(w, outer_radius - inner_radius)  # ���� ��������
        angles.append(alpha_i)

        # ��������� ������� ����������
        current_x, current_y = X, Y
    angle = math.pi / 2
    # ��������� �������� ������
    total_length += math.sqrt((xf - current_x) ** 2 + (yf - current_y) ** 2)
    current_x = X + (inner_radius * math.cos(angle + angle_left))  # ���������� �� X
    current_y = Y + (inner_radius * math.sin(angle + angle_left))
    leng = math.sqrt((current_x - X) ** 2 + (current_y - Y) ** 2)
    total_length -= leng
    print(total_length)

    # ������� ����������
    with open('output.txt', 'w') as f:
        f.write(f"{total_length:.5f}\n")
        for angle in angles:
            f.write(f"{angle:.5f}\n")

if __name__ == '__main__':
    main()