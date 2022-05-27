import pygame
from game import SpaceInvaders, Button

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    game = SpaceInvaders()
    pygame.display.set_caption("Space Invaders")

    enemy_imageblue = pygame.image.load('./Assets/blue.png').convert_alpha()
    enemy_imageorange = pygame.image.load('./Assets/orange.png').convert_alpha()
    enemy_imagegreen = pygame.image.load('./Assets/green.png').convert_alpha()
    scoreo = game.font.render('100', True, 'white')
    scoreg = game.font.render('200', True, 'white')
    scoreb = game.font.render('300', True, 'white')
    scoreoRect = scoreo.get_rect()
    scoregRect = scoreg.get_rect()
    scorebRect = scoreb.get_rect()

    scoreE = game.font.render('Score Enemy', True, 'white')
    scoreERect = scoreE.get_rect()

    logo_img = pygame.image.load('./Assets/mainlogo.png').convert_alpha()
    start_img = pygame.image.load('./Assets/start.png').convert_alpha()
    exit_img = pygame.image.load('./Assets/exit.png').convert_alpha()
    
    run = True
    while run:

        start_button = Button((game.screen_width/2), 590, start_img, 0.8)
        exit_button = Button((game.screen_width/2), 650, exit_img, 0.8)

        game.screen.blit(game.background,(0,0))

        game.screen.blit(logo_img,(50,10))

        game.screen.blit(enemy_imageorange,((game.screen_width/2)+50,game.screen_height/2))
        game.screen.blit(enemy_imagegreen,((game.screen_width/2)+50,(game.screen_height/2)+50))
        game.screen.blit(enemy_imageblue,((game.screen_width/2)+50,(game.screen_height/2)+100))
        game.screen.blit(scoreo,((game.screen_width/2)-90, (game.screen_height/2)+10))
        game.screen.blit(scoreg,((game.screen_width/2)-90,(game.screen_height/2)+60))
        game.screen.blit(scoreb,((game.screen_width/2)-90,(game.screen_height/2)+110))
        game.screen.blit(scoreE,((game.screen_width/2)-90, (game.screen_height/2)-30))

        if start_button.draw(game.screen):
            game.start_game()
        if exit_button.draw(game.screen):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False

        pygame.display.update()

    pygame.quit