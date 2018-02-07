import pygame as pg
import random
from settings import *
from sprites import *
from enemy import *
from bullets import *

pg.init()
pg.mixer.init()


class Game():
    def __init__(self):
        self.background = pg.image.load('img/felt_green.jpg')
        self.background_rect = self.background.get_rect()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.is_running = True
        self.playing = True
        self.points = 0
        # Sprites and Groups
        self.bullets_group = pg.sprite.Group()        # Bullets Group will store all the Bullet CLASSES
        self.all_sprites = pg.sprite.Group()          # Mob Group will store all the enemy CLASSES
        self.mob = pg.sprite.Group()                  # ALL_SPRITE will store bullets, mobs and player
                                                      #            and will update together in the game
                                                      #            update function. This prevents from creating
                                                      #            lists and iterate through them.
    def new(self):
        # Add a player
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create Enemies
        for i in range(15):
            m = Mob((random.randint(1, WIDTH)), 0)
            self.all_sprites.add(m)
            self.mob.add(m)

        self.run()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game - loop - update
        self.all_sprites.update()
        self.bullets_group.update()
        self.mob.update()
        # Here we are checking if two groups collide. if this is the case we will delete
        # both of the objects that touched. If there is more than one object in the groups
        # the computer will check to see which one is the one it needs to delete using this code.
        self.hits = pg.sprite.groupcollide(self.bullets_group, self.mob, True, True)
        for hit in self.hits:
            m = Mob((random.randint(1, WIDTH)), 0)
            self.all_sprites.add(m)
            self.mob.add(m)
            self.points +=1

        # Check to see if a mob group hit the player.
        # if player is in the space of mob it will exit the game
        # in this one we compare a Single sprite with a group.
        self.hits = pg.sprite.spritecollide(self.player, self.mob, False)
        if self.hits:
            self.playing = False
            self.is_running = False

    def events(self):
        # game-loop - events
        for events in pg.event.get():

            if events.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.is_running = False
            elif events.type == pg.KEYDOWN:
                if events.key == pg.K_SPACE:
                    self.player.shoot(self.all_sprites, self.bullets_group)


    def draw(self):
        # game loops - draw
        # self.screen.fill(BLACK)

        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        self.show_points()

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(TITLE,48,WHITE,WIDTH/2,HEIGHT/4)
        self.draw_text("  KILL EVERYONE ", 40, WHITE, WIDTH / 2, HEIGHT / 3)
        self.draw_text("Hit Enter to continue: ",30,WHITE,WIDTH/2,HEIGHT/2)
        pg.display.flip()
        self.wait_for_response()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size )
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


    def wait_for_response(self):

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.is_running = False
                    self.player = False
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False




    def show_points(self):
        self.draw_text('Points: ' + str(self.points),30, BLACK,60,10)
        pg.display.flip()


    def show_go_screen(self):

        # Because of how my waiting_for_response is set up i need leave the game_over function
        # or when i exit i without losing i will go to the game over screeen.
        # if not self.is_running:
        #     return
        self.screen.fill(BLACK)
        self.draw_text("  YOU JUST LOST SON! ", 40, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:  " + str(self.points), 40, WHITE, WIDTH / 2, HEIGHT / 3)
        self.draw_text("Hit Enter to play again: ",30,WHITE,WIDTH/2,HEIGHT/2)
        pg.display.flip()
        self.wait_for_response()



g = Game()
g.show_start_screen()

while g.is_running:
    g.new()
    g.show_go_screen()


pg.quit()
