import math

class UI:
    def __init__(self, w, h, R, v, k):
        self.w = w
        self.h = h
        self.R = R
        self.v = v
        self.k = k
        self.ui_center = None
        self.delay_counter = 0
        self.delay_active = False

    def initialize(self, head_position, look_direction):
        self.ui_center = self.get_intersection_point(head_position, look_direction)

    def get_intersection_point(self, head_position, look_direction):
        x_h, y_h, z_h = head_position
        x_d, y_d, z_d = look_direction
        length = math.sqrt(x_d**2 + y_d**2 + z_d**2)

        if length == 0:
            return None  # Нулевой вектор

        # Нормализуем направление
        x_d /= length
        y_d /= length
        z_d /= length

        # Уравнения для пересечения с окружностью
        a = x_d**2 + z_d**2
        b = 2 * (x_h * x_d + z_h * z_d)
        c = x_h**2 + z_h**2 - self.R**2

        discriminant = b**2 - 4 * a * c
        if discriminant < 0 or a == 0:  # Нет пересечения или нулевой a
            return None  # Нет пересечения

        # Включаем обработку ошибок для квадратного корня
        try:
            t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        except ValueError as e:
            print(f"t1: {e}")
            return None
        
        return (x_h + t1 * x_d, y_h, z_h + t1 * z_d)

    def is_inside_ui(self, point):
        half_w, half_h = self.w / 2, self.h / 2
        return (self.ui_center[0] - half_w <= point[0] <= self.ui_center[0] + half_w and
                self.ui_center[1] - half_h <= point[1] <= self.ui_center[1] + half_h)

    def update(self, head_position, look_direction):
        intersection_point = self.get_intersection_point(head_position, look_direction)

        if intersection_point and self.is_inside_ui(intersection_point):
            self.delay_active = False
            self.delay_counter = 0
        else:
            if not self.delay_active:
                self.delay_active = True
                self.delay_counter = self.k

        if self.delay_active and self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.move_ui(intersection_point)

    def move_ui(self, target_point):
        if target_point is None:
            return

        target_theta, target_phi = self.to_spherical(target_point)
        current_theta, current_phi = self.to_spherical(self.ui_center)

        # Обновление углов
        distance_theta = self.angle_difference(target_theta, current_theta)
        distance_phi = self.angle_difference(target_phi, current_phi)

        move_distance = min(self.v, math.hypot(distance_theta, distance_phi))
        new_theta = current_theta + move_distance * (distance_theta / max(abs(distance_theta), 1))
        new_phi = current_phi + move_distance * (distance_phi / max(abs(distance_phi), 1))

        self.ui_center = self.to_cartesian(new_theta, new_phi)

    def angle_difference(self, angle1, angle2):
        return (angle1 - angle2 + 180) % 360 - 180

    def to_spherical(self, point):
        x, y, z = point
        r = max(math.sqrt(x**2 + y**2 + z**2), 1e-10)
        theta = math.degrees(math.atan2(math.sqrt(x**2 + z**2), y))
        phi = math.degrees(math.atan2(z, x))
        return theta, phi

    def to_cartesian(self, theta, phi):
        theta_rad = math.radians(theta)
        phi_rad = math.radians(phi)
        x = self.R * math.sin(theta_rad) * math.cos(phi_rad)
        y = self.R * math.cos(theta_rad)
        z = self.R * math.sin(theta_rad) * math.sin(phi_rad)
        return (x, y, z)

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        w, h, R, v, k = map(float, lines[0].strip().split())
        head_initial = list(map(float, lines[1].strip().split()))
        look_initial = list(map(float, lines[2].strip().split()))
        frames = [tuple(map(float, lines[i].strip().split())) for i in range(3, len(lines), 2)]
        look_directions = [tuple(map(float, lines[i+1].strip().split())) for i in range(3, len(lines), 2)]
        return w, h, R, v, k, head_initial, look_initial, list(zip(frames, look_directions))
    
def write_output(file_path, ui_corners):
    with open(file_path, 'w') as f:
        for corner in ui_corners:
            f.write(f"{corner[0]:.5f} {corner[1]:.5f} {corner[2]:.5f}\n")

def main():
    w, h, R, v, k, head_initial, look_initial, frames = read_input("input.txt")
    user_interface = UI(w, h, R, v, k)
    user_interface.initialize(head_initial, look_initial)

    for head_position, look_direction in frames:
        user_interface.update(head_position, look_direction)

    half_w, half_h = w / 2, h / 2
    corners = [
        (user_interface.ui_center[0] - half_w, user_interface.ui_center[1] + half_h, user_interface.ui_center[2]),
        (user_interface.ui_center[0] + half_w, user_interface.ui_center[1] + half_h, user_interface.ui_center[2]),
        (user_interface.ui_center[0] + half_w, user_interface.ui_center[1] - half_h, user_interface.ui_center[2]),
        (user_interface.ui_center[0] - half_w, user_interface.ui_center[1] - half_h, user_interface.ui_center[2])
    ]
    write_output("output.txt", corners)

if __name__ == '__main__':
    main()