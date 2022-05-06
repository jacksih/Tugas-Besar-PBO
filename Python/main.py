import pygame
import sys
from random import choice


class Player(pygame.sprite.Sprite):
    def __init__(self, position, constraint, velocity):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect(midbottom=position)
        self.velocity = velocity
        self.xconstraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound('laser.wav')
        self.laser_sound.set_volume(0.5)

    def gerak_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity

        if keys[pygame.K_SPACE] and self.ready:
            self.tembak_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def recharge_laser(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def batas_player(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.xconstraint:
            self.rect.right = self.xconstraint

    def tembak_laser(self):
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))

    def update(self):
        self.gerak_player()
        self.batas_player()
        self.recharge_laser()
        self.lasers.update()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        if color == 'orange':
            self.value = 100
        elif color == 'green':
            self.value = 200
        else:
            self.value = 300

    def update(self, direction):
        self.rect.x += direction


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('pink')
        self.rect = self.image.get_rect(center=pos)
        self.velocity = velocity
        self.Y_constraint = screen_height

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y <= -50 or self.rect.y >= self.Y_constraint + 50:
            self.kill()


class SpaceInvaders:
    def __init__(self):
        # Player setup
        player_sprite = Player(
            (screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load('lives.png').convert_alpha()
        self.live_x_start_pos = screen_width - \
            (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('m04.ttf', 20)

        # Enemy setup
        self.enemys = pygame.sprite.Group()
        self.enemy_lasers = pygame.sprite.Group()
        self.enemy_setup(rows=6, cols=8)
        self.enemy_direction = 1

        # Audio setup
        music = pygame.mixer.Sound('music.wav')
        music.set_volume(0.5)
        music.play(loops=-1)
        self.laser_sound = pygame.mixer.Sound('laser.wav')
        self.laser_sound.set_volume(0.3)
        self.explosion_sound = pygame.mixer.Sound('explosion.wav')
        self.explosion_sound.set_volume(0.3)

    def enemy_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=120):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if 0 <= row_index <= 1:
                    enemy_sprite = Enemy('blue', x, y)
                elif 2 <= row_index <= 4:
                    enemy_sprite = Enemy('green', x, y)
                else:
                    enemy_sprite = Enemy('orange', x, y)
                self.enemys.add(enemy_sprite)

    def enemy_pos_check(self):
        all_enemys = self.enemys.sprites()
        for enemy in all_enemys:
            if enemy.rect.right >= screen_width:
                self.enemy_direction = -1
                self.enemy_move_down(2)
            elif enemy.rect.left <= 0:
                self.enemy_direction = 1
                self.enemy_move_down(2)

    def enemy_move_down(self, distance):
        if self.enemys:
            for enemy in self.enemys.sprites():
                enemy.rect.y += distance

    def enemy_tembak_laser(self):
        if self.enemys.sprites():
            random_enemy = choice(self.enemys.sprites())
            laser_sprite = Laser(random_enemy.rect.center, 10, screen_height)
            self.enemy_lasers.add(laser_sprite)
            self.laser_sound.play()

    def menu_kalah(self):
        screen.blit(background, (0, 0))
        lose_surf = self.font.render('Anda Kalah!', False, 'white')
        lose_rect = lose_surf.get_rect(
            center=(screen_width / 2, screen_height / 2))
        screen.blit(lose_surf, lose_rect)
        pygame.display.flip()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def collision(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # enemy collisions
                enemys_hit = pygame.sprite.spritecollide(
                    laser, self.enemys, True)
                if enemys_hit:
                    for enemy in enemys_hit:
                        self.score += enemy.value
                        laser.kill()
                        self.explosion_sound.play()

                # enemy lasers
        if self.enemy_lasers:
            for laser in self.enemy_lasers:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.menu_kalah()

        # enemy
        if self.enemys:
            for alien in self.enemys:
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives):
            x = self.live_x_start_pos + \
                ((live-1) * (self.live_surf.get_size()[0] + 10))
            screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)

    def game_result(self):
        if not self.enemys.sprites():
            victory_surf = self.font.render(
                'SELAMAT! Anda Menang', False, 'white')
            victory_rect = victory_surf.get_rect(
                center=(screen_width / 2, screen_height / 2))
            screen.blit(victory_surf, victory_rect)

    def main_menu(self):
        # high score
        # jumlah poin yg diberikan tiap jenis enemy
        # button play dan exit
        pass

    def run(self):
        self.player.update()
        self.enemy_lasers.update()

        self.enemys.update(self.enemy_direction)
        self.enemy_pos_check()
        self.collision()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.enemys.draw(screen)
        self.enemy_lasers.draw(screen)
        self.display_lives()
        self.display_score()
        self.game_result()


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = SpaceInvaders()

    ENEMYLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMYLASER, 800)

    background = pygame.image.load('background.jpeg').convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ENEMYLASER:
                game.enemy_tembak_laser()

        screen.blit(background, (0, 0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
