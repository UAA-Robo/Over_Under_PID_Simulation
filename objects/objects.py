import pygame as pygame
import math as math
import os
import random as random

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, height: int, width: int, x: int, y: int,\
                  r: float, id: int, file_name: str, name: str):
        """
        @brief    Base class Object used to store basic data for elements loaded to the screen or
                  running in the background.
        @param height    The height of the sprite to draw.
        @param width    The width of the sprite to draw.
        @param x    The x-position on the screen of the object.
        @param y    The y-position on the screen of the object (top-down).
        @param r    The rotational value of the object.
        @param id    The ID of the object.
        @param file_name    The file name of the sprite image.
        @param name    The display name of the object.
        """
        super().__init__()


        self.default_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join("media", file_name)).convert_alpha(), (width, height))
        self.surface = self.default_surface
        self.image = self.surface

        self.set_display_x(x)
        self.set_display_y(y)
        self.width = width
        self.height = height
        self.set_rotation(r)
        self.ID = id
        self.name = name

        self.rect = self.surface.get_rect()

        self.update_sprite(self.X, self.Y)

    def set_display_x(self, x: float): self.X = round(x)
    def set_display_y(self, y: float): self.Y = round(y)
    def set_rotation(self, r: float):
        self.R = r
        self.surface = pygame.transform.rotate(self.default_surface, self.R)
        self.rect = self.surface.get_rect()
        self.image = self.surface

    def display_x(self): return self.X
    def display_y(self): return self.Y
    def get_rotation(self): return self.R

    def update_sprite(self, x: float, y: float):
        """
        @brief    Updates the sprite information using the data in the Sprite instance.
        @param x    The actual x-position of the object.
        @param y    The actual y-position of the object.
        """
        self.set_display_x(x)
        self.set_display_y(y)
        self.rect.x = self.display_x() - (self.width // 2)
        self.rect.y = self.display_y() - (self.height // 2)

class Text:
    def __init__(self, text: str, x_pos: int, y_pos: int):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

class Robot(Sprite):
    def __init__(self, height: int, width: int, x: int, y: int,\
                  r: float, v: float, id: int, file_name: str, name: str):
        """
        @brief    Robot object child of Object. Simulated robot for the purpose of PID testing.
        @param height    The height of the sprite to draw.
        @param width    The width of the sprite to draw.
        @param x    The x-position on the screen of the robot.
        @param y    The y-position on the screen of the robot (top-down).
        @param r    The rotational value of the robot.
        @param v    The velocity of the robot.
        @param id    The ID of the robot.
        @param file_name    The file name of the sprite image.
        @param name    The display name of the robot.
        """
        super().__init__(height, width, x, y, r, id, file_name, name)
        self.set_velocity(v)
        self.intended_heading = r
        self.horizontal_difference = 0.0
        self.x_raw = float(self.display_x())
        self.y_raw = float(self.display_y())
        self.last_x = self.x_raw
        self.last_y = self.y_raw
        self.moved_distance = 0.0
        self.accumulated_distance = 0.0
        self.left_speed = self.get_velocity()
        self.right_speed = self.get_velocity()
        self.changedSides: bool = False
        self.rand_tick = 0
        self.start_new_path()
    

    def set_velocity(self, v): self.velocity = v

    def get_velocity(self): return self.velocity

    def get_distance(self): return self.accumulated_distance

    def reset_distance(self): self.accumulated_distance = 0.0

    def move(self):
        """
        @brief    Moves the robot by the distance provided by its velocity in one iteration
        """
        # if self.rand_tick == 100:
        #     self.right_speed -= 100.0
        #     self.rand_tick = 0
        self.set_rotation(self.get_rotation() - (self.left_speed - self.right_speed) / 8.0)
        delta_x = float(self.get_velocity() * math.cos(math.radians(self.get_rotation())))
        delta_y = float(self.get_velocity() * math.sin(math.radians(self.get_rotation())))
        self.x_raw += delta_x
        self.y_raw -= delta_y
        self.set_display_x(round(self.x_raw) % 800)
        self.set_display_y(round(self.y_raw) % 800)

        self.moved_distance = math.dist((self.x_raw, self.y_raw), (self.last_x, self.last_y))

        self.accumulated_distance += self.get_velocity()
        self.update_sprite(self.display_x() + int(delta_x), self.display_y() - int(delta_y))

        self.left_speed = self.get_velocity()
        self.right_speed = self.get_velocity()
        self.rand_tick += 1
        self.last_x = self.x_raw
        self.last_y = self.y_raw

    def start_new_path(self):
        self.x_start = self.x_raw
        self.y_start = self.y_raw
        self.angle_start = self.get_rotation()