# Minimum number of calls to display text in pygame window
import pygame
from l26_settings import *

# to run anything in this module, pygame must be initialized

#create a screen
pygame.display.init()
pygame.font.init()
def init_modules():
    pygame.display.init()
    pygame.font.init()  # consider using this instead

def init_screen():
    win_bg_rgb = (0, 0, 0)
    surface_window = pygame.display.set_mode(SCREEN_SIZE) #init window
    pygame.display.set_caption(BAR_CAPTION) # set caption
    pygame.display.set_icon(pi_img)  # set icon
    surface_window.fill(win_bg_rgb)
    return surface_window


def set_text(surface_win, text_lines, coordinates, text_color=WHITE):
    font_size = 24
    antialias = False
    bg_color = BLACK
    text_lines = list(text_lines)
    coordinates[1] += TEXT_FONT.get_height()
    for line in text_lines:
        rendered_text = TEXT_FONT.render(line, antialias, text_color, bg_color)
        surface_win.blit(rendered_text, coordinates)
        coordinates[1] += TEXT_FONT.get_height()

def get_font_height():
    return TEXT_FONT.get_height()

def render_text_surface(self, text_string, color=WHITE):
    output_surface = self.font.render(text_string, self.antialias, color)
    return output_surface

def blit_text_list(self, main_screen, text_list, origin_coordinates, color=WHITE):
    coordinates = list(origin_coordinates)
    # coordinates[1] += get_font_height()  #starts on line 2
    for text_string in text_list:
        text_surface = self.font.render(text_string, self.antialias, color, self.bg_color)
        main_screen.blit(text_surface, origin_coordinates)
        coordinates[1] += self.get_font_height()

def render_and_blit_char(self, main_screen, character, coordinates, color=WHITE):
    coordinates = list(coordinates)
    text_surface = self.font.render(character, self.antialias, color, self.bg_color)
    main_screen.blit(text_surface, coordinates)

def blit_onto_surface(self, main_screen, surface, coordinates):
    main_screen.blit(surface, coordinates)

def clear_screen(main_screen):
    main_screen.fill(SCREEN_BG_COLOR)

class MessageBox:  #holds messages, displays current
    messages = []
    text_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE, BOLD)
    antialias = False
    bg_color = BLACK

    def __init__(self, surface):
        self.surface = surface

    def display_message(self):
        coordinates = [0, 0]
        text_color = WHITE
        rendered_text = self.text_font.render(self.messages[-1], ANTIALIAS, text_color, self.bg_color)
        self.surface.blit(rendered_text, coordinates)

class StatusBox(MessageBox):  #holds messages, displays current
    messages = []
    font_size = 24
    text_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE, BOLD)
    antialias = False
    bg_color = BLACK

    def __init__(self, surface):
        self.surface = surface

    def display_message(self):
        coordinates = [0, 450]
        text_color = WHITE
        rendered_text = self.text_font.render(self.messages[-1], self.antialias, text_color, self.bg_color)
        self.surface.blit(rendered_text, coordinates)


def next_line(y_value, font):
    return y_value + font.get_height()

def next_letter(x_value, font_size):
    return x_value + font_size

def display_screen():
    pygame.display.update()

# just a test script for the text/graphics module
#
# surface_coordinates = [100, 100]
# text_lines = 'Testing testing testing testing', 'testing'
#
# icon = pygame.image.load ('heart.png')  # icon file in game directory
# pygame.display.init()
# pygame.font.init()
# main_win = init_screen('hello', icon, (600, 480))
# display_text(main_win, text_lines, surface_coordinates)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

def display_map():
