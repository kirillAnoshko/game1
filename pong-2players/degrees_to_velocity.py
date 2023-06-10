import math

def degrees_to_velocity(degrees, speed) -> tuple:
    """
        Получает угол в градусах и скорость.
        Оба аргумента могут быть целыми или вещественными.
        0° — верх, 90° — право, 180° — низ, 270° — лево.
        Возвращает кортеж (скорость по X, скорость по Y).
    """
    radians = math.radians(degrees)
    velocity_x = (math.sin(radians) * speed)
    velocity_y = (math.cos(radians) * speed) * -1 # в pygame Y растет вниз
    return(velocity_x, velocity_y)
