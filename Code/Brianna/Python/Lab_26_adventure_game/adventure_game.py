"""
Main module for adventure game.

"""

import pygame
import constants
import areas
from player import Player

def main():
""" Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Escape to Code Mountain")

    # Create the player
    player = Player()

    # Create all the areas -- World list? Not really areas.
    area_list = []
    area_list.append(areas.Area_01(player))
    area_list.append(areas.Area_02(player))

    # Set the current area
    current_area_no = 0
    current_area = area_list[current_area_no]

    active_sprite_list = pygame.sprite.Group()
    player.area = current_area

    player.rect.x = 340 ### ???
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height  ###????
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the area
        current_area.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_area.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_area.shift_world(diff)

        # If the player gets to the end of the area, go to the next area
        current_position = player.rect.x + current_area.world_shift
        if current_position < current_area.area_limit:
            player.rect.x = 120
            if current_area_no < len(area_list)-1:
                current_area_no += 1
                current_area = area_list[current_area_no]
                player.area = current_area

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_area.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()









i"""mport pygame
import constants
import areas
from player import Player



def Main():
    # initialize pygame and set up the window.
    pygame.init()
    # Set width and height of the screen. First number is width, second is height.
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Programmer's Escape to Hidden Mountain")
    # Hide the mouse cursor
    pygame.mouse.set_visible(0)

    # Loop until the user clicks the close button.
    done = False  # Loop control
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()  # Controls how fast the game runs
    game = Game()

    while not done:
        # Process events mouse clicks, etc.
        done = game.process_events()
        # Update object positions, check for colissions.
        game.run_logic()
        # draw the current frame
        game.display_frame(screen)
        #pausing for next frame
        clock.tick(60)
    pygame.quit()"""
