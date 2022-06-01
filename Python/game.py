import pygame
import sys
from random import choice

class Player(pygame.sprite.Sprite):
    def __init__(self, position, constraint, velocity):
        super().__init__()
        self.image = pygame.image.load('./Assets/player.png')
        self.rect = self.image.get_rect(midbottom=position)
        self.velocity = velocity
        self.xconstraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound('./Assets/laser.wav')
        self.laser_sound.set_volume(0)

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
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom, 'pink'))

    def update(self):
        self.gerak_player()
        self.batas_player()
        self.recharge_laser()
        self.lasers.update()


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = color + '.png'
        self.image = pygame.image.load('./Assets/' + file_path).convert_alpha()
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
    def __init__(self, pos, velocity, screen_height, color):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.velocity = velocity
        self.Y_constraint = screen_height

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y <= -50 or self.rect.y >= self.Y_constraint + 50:
            self.kill()


class SpaceInvaders:
    def __init__(self):
        # window setup
        self.screen_width = 600
        self.screen_height = 700
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.ENEMYLASER = pygame.USEREVENT + 1
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('./Assets/background.jpeg').convert_alpha()
        pygame.time.set_timer(self.ENEMYLASER, 800)

        # Player setup
        player_sprite = Player(
            (self.screen_width / 2, self.screen_height), self.screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load('./Assets/lives.png').convert_alpha()
        self.live_x_start_pos = self.screen_width - \
            (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('./Assets/m04.TTF', 20)

        # Enemy setup
        self.enemys = pygame.sprite.Group()
        self.enemy_lasers = pygame.sprite.Group()
        self.enemy_setup(rows=7, cols=7)
        self.enemy_direction = 1

        # Audio setup
        music = pygame.mixer.Sound('./Assets/music.wav')
        music.set_volume(0.5)
        music.play(loops=-1)
        self.laser_sound = pygame.mixer.Sound('./Assets/laser.wav')
        self.laser_sound.set_volume(0.5)
        self.explosion_sound = pygame.mixer.Sound('./Assets/explosion.wav')
        self.explosion_sound.set_volume(0.5)

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
            if enemy.rect.right >= self.screen_width:
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
            laser_sprite = Laser(random_enemy.rect.center,
                                 10, self.screen_height, 'green')
            self.enemy_lasers.add(laser_sprite)
            self.laser_sound.play()

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

        # enemy
        if self.enemys:
            for enemy in self.enemys:
                if pygame.sprite.spritecollide(enemy, self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives):
            x = self.live_x_start_pos + \
                ((live-1) * (self.live_surf.get_size()[0] + 10))
            self.screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft=(10, 10))
        self.screen.blit(score_surf, score_rect)

    def menu_retry_kalah(self):
        retry_img = pygame.image.load('./Assets/retry.png').convert_alpha()
        exit_img = pygame.image.load('./Assets/exit.png').convert_alpha()
        resume_img = pygame.image.load('./Assets/resume.png').convert_alpha()

        retry_button = Button((self.screen_width/2), 590, retry_img, 0.8)
        resume_button = Button((self.screen_width/2), 530, resume_img, 0.8)
        exit_button = Button((self.screen_width/2), 650, exit_img, 0.8)

        if retry_button.draw(self.screen):
            player_sprite = Player(
                (self.screen_width / 2, self.screen_height), self.screen_width, 5)
            self.player = pygame.sprite.GroupSingle(player_sprite)
            self.enemy_lasers = pygame.sprite.Group()
            self.player.update()
            self.lives = 3
            self.score = 0
            self.enemys = pygame.sprite.Group()
            self.enemy_setup(6, 6)
            self.enemy_direction = 1
            self.start_game()

        if resume_button.draw(self.screen):
            pygame.display.flip()
            pygame.display.update()
            self.lives = 3
            self.score = self.score - 500
            self.start_game()

        if exit_button.draw(self.screen):
            pygame.quit()

    def menu_retry_menang(self):
        retry_img = pygame.image.load('./Assets/retry.png').convert_alpha()
        exit_img = pygame.image.load('./Assets/exit.png').convert_alpha()

        retry_button = Button((self.screen_width/2), 590, retry_img, 0.8)
        exit_button = Button((self.screen_width/2), 650, exit_img, 0.8)

        if retry_button.draw(self.screen):
            player_sprite = Player(
                (self.screen_width / 2, self.screen_height), self.screen_width, 5)
            self.player = pygame.sprite.GroupSingle(player_sprite)
            self.enemy_lasers = pygame.sprite.Group()
            self.player.update()
            self.lives = 3
            self.score = 0
            self.enemys = pygame.sprite.Group()
            self.enemy_setup(6, 6)
            self.enemy_direction = 1
            self.start_game()

        if exit_button.draw(self.screen):
            pygame.quit()

    def game_result(self):

        if not self.enemys.sprites():
            victory_surf = self.font.render(
                'SELAMAT! Anda Menang', False, 'white')
            victory_rect = victory_surf.get_rect(
                center=(self.screen_width / 2, self.screen_height / 2))
            self.screen.blit(victory_surf, victory_rect)
            self.menu_retry_menang()
            pygame.display.update()

        # menu kalah
        if self.lives <= 0:
            run = True
            while run:
                self.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                self.screen.blit(self.background, (0, 0))
                lose_surf = self.font.render('Anda Kalah!', False, 'white')
                lose_rect = lose_surf.get_rect(
                    center=(self.screen_width / 2, self.screen_height / 2))
                self.screen.blit(lose_surf, lose_rect)
                self.menu_retry_kalah()

                pygame.display.update()

    def run(self):
        self.player.update()
        self.enemy_lasers.update()

        self.enemys.update(self.enemy_direction)
        self.enemy_pos_check()
        self.collision()

        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.enemys.draw(self.screen)
        self.enemy_lasers.draw(self.screen)
        self.display_lives()
        self.display_score()
        self.game_result()

    def start_game(self):
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.ENEMYLASER:
                    self.enemy_tembak_laser()

            self.screen.blit(self.background, (0, 0))
            self.run()

            if keys[pygame.K_1]:
                self.enemys.empty()
                self.game_result()
                self.menu_retry_menang()

            if keys[pygame.K_2]:
                self.lives = 0
                self.menu_retry_kalah()

            pygame.display.flip()
            self.clock.tick(60)
