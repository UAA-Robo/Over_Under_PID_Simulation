import pygame as pygame

class Window:    
    def __init__(self, title: str, background_color, window_width: int, window_height: int):
        """
        @brief    GUI management class that handles rendering only.
        @param    The title of the window.
        @param background_color    A triplet containing RGB values for the background of the window
                                   (0-255).
        @param window_width    The width of the window to display.
        @param window_height    The height of the window to display.
        """
        self.dimensions = (window_width, window_height)
        self.background_color = background_color
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.dimensions, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.tick = pygame.time.Clock()
        self.isRunning = True

    def update(self, sprite_list: pygame.sprite.Group(), text_list: list):
        """
        @brief    Function call to update the display with a list of objects to render.
        @param sprite_list    The list of sprites to render on the screen.
        """
        font = pygame.font.SysFont("Arial", 20)
        sprite_list.update()
        self.screen.fill(self.background_color)
        sprite_list.draw(self.screen) # 'draw' works correctly
        for text in text_list:
            text_surface = font.render(text.text, False, (0, 0, 0))
            self.screen.blit(text_surface, (text.x_pos, text.y_pos))
        pygame.display.flip()

    def quit(self):
        """
        @brief    Terminates the window object and quits pygame.
        """
        pygame.display.quit()
        pygame.quit()

    
