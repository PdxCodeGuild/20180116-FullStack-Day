# Minimum number of calls to display text in pygame window
import pygame, sys
import l26_settings as settings

# to run anything in this module, pygame must be initialized
sample_text = 'This is a text test \n this is only a text test.'

#create a screen
def init_screen(title_bar_text, icon_img, win_dimensions):
    # win_bg_rgb = (0, 0, 0)
    surface_window = pygame.display.set_mode(win_dimensions) #init window
    pygame.display.set_caption(title_bar_text) # set caption
    pygame.display.set_icon(icon_img)  # set icon
    # surface_window.fill(win_bg_rgb)
    return surface_window


def display_text(surface_win, text_lines, coordinates, text_color=settings.WHITE):
    font_size = 32
    text_font = pygame.font.SysFont('couriernew', font_size, bold=False)
    antialias = False
    bg_color = settings.BLACK
    text_lines = list(text_lines)
    for line in text_lines:
        rendered_text = text_font.render(line, antialias, text_color, bg_color)
        surface_win.blit(rendered_text, coordinates)
        coordinates[1] += text_font.get_height()
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


