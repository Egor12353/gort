import math

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    w, h, R, v, k = map(float, data[0].split())
    k = int(k)

    initial_pos = tuple(map(float, data[1].split()))
    initial_dir = tuple(map(float, data[2].split()))

    print(initial_dir, initial_pos)
    frames = []
    for i in range(3, len(data), 2):
        x_pf = list(map(float, data[i].split()))
        x_df = list(map(float, data[i + 1].split()))
        frames.append((x_pf, x_df))

    return w, h, R, v, k, initial_pos, initial_dir, frames

def move_interface(w, h, R, v, k, initial_pos, initial_dir, frames):
    x_ui, y_ui, z_ui = initial_pos

    for (x_pf, x_df) in frames:
        x_df_0, y_df_0, z_df_0 = x_df
        
        # Обновление координат интерфейса с учетом скорости
        x_ui += x_df_0 * v
        y_ui += y_df_0 * v
        z_ui += z_df_0 * v

        # Ограничение по радиусу
        distance = math.sqrt(x_ui**2 + y_ui**2 + z_ui**2)
        if distance > R:
            # Если вышли за пределы радиуса, возвращаемся на границу
            scale = R / distance
            x_ui *= scale
            y_ui *= scale
            z_ui *= scale

    return x_ui, y_ui, z_ui

def format_output(vertices):
    output = ":\n"
    for i, vertex in enumerate(vertices):
        output += f" {i + 1}: X = {vertex[0]:.5f}, Y = {vertex[1]:.5f}, Z = {vertex[2]:.5f}\n"
    return output

def vivod():
    w, h, R, v, k, initial_pos, initial_dir, frames = read_input('input.txt')
    final_pos = move_interface(w, h, R, v, k, initial_pos, initial_dir, frames)

    x_ui, y_ui, z_ui = final_pos
    half_w = w / 2
    half_h = h / 2

    

    vertices = [
        (x_ui - half_w, y_ui + half_h, z_ui),
        (x_ui + half_w, y_ui + half_h, z_ui),
        (x_ui + half_w, y_ui + half_h, z_ui)
        (x_ui + half_w, y_ui + half_h, z_ui)


    ]

    with open('output.txt', 'w') as f:
        f.write(format_output(vertices))

    print(format_output(vertices))

vivod()

