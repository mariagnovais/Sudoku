import pygame
import sys
from sudoku_generator import *
import pygame


def start_screen(screen):
  pygame.init()
  font = pygame.font.Font(None, 36)
  screen.fill('light pink')


  # Title text
  title_text = font.render("Welcome to Sudoku", True, 'black')
  screen.blit(title_text, (450 // 2 - title_text.get_width() // 2, 50))


  #Select game mode text
  select_text = font.render("Select Game Mode:", True, "black")
  screen.blit(select_text, (450 // 2 - select_text.get_width() // 2, 150))


  #Make buttons
  easy_button = pygame.Rect(75, 200, 100, 50)
  medium_button = pygame.Rect(175, 200, 100, 50)
  hard_button = pygame.Rect(275, 200, 100, 50)


  #Draw buttons
  pygame.draw.rect(screen, (177, 156, 217), easy_button)
  pygame.draw.rect(screen, (177, 156, 217), medium_button)
  pygame.draw.rect(screen, (177, 156, 217), hard_button)


  #Create text
  easy_font = font.render("Easy", True, 'black')
  medium_font = font.render("Medium", True, 'black')
  hard_font = font.render("Hard", True, 'black')


  #Adds text to button
  screen.blit(easy_font, (450//4-easy_font.get_width()//2, 215))
  screen.blit(medium_font, (450//2-medium_font.get_width()//2, 215))
  screen.blit(hard_font, (450//1.35-hard_font.get_width()//2, 215))


  # Update the display
  pygame.display.flip()


  #Returns difficulty when button is clicked
  while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        # If user clicks on button
        if event.type == pygame.MOUSEBUTTONDOWN:
           if easy_button.collidepoint(event.pos):
              difficulty = 30
              return difficulty
           if medium_button.collidepoint(event.pos):
              difficulty = 40
              return difficulty
           if hard_button.collidepoint(event.pos):
              difficulty = 50
              return difficulty
     pygame.display.update()


def game_over_screen(screen, gameWon):
  # Fill screen
  screen.fill("light pink")

  #Game over text
  game_over_font = pygame.font.Font(None, 40)

  #Retrieve winner text
  if gameWon:
     message = 'You win!'
     game_over_text = game_over_font.render(message, 0, "black")
     screen.blit(game_over_text, (450 // 2 - game_over_text.get_width() // 2, 150))
  else:
     message = "You lost :("
     game_over_text = game_over_font.render(message, 0, "black")
     screen.blit(game_over_text, (450 // 2 - game_over_text.get_width() // 2, 150))

  restart_b = pygame.Rect(175, 465, 100, 25)

  if not gameWon:
      pygame.draw.rect(screen, (177, 156, 217), restart_b)
      restart_t = font.render("Restart", True, 'black')
      screen.blit(restart_t, (185, 465))

  exit_b = pygame.Rect(325, 465, 100, 25)

  if gameWon:
      pygame.draw.rect(screen, (177, 156, 217), exit_b)
      exit_t = font.render("Exit", True, 'black')
      screen.blit(exit_t, (350, 465))

  pygame.display.update()

  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()

          if event.type == pygame.MOUSEBUTTONDOWN:
              if exit_b.collidepoint(event.pos):
                  sys.exit()

              if restart_b.collidepoint(event.pos):
                  screen.fill("light pink")
                  return True


if __name__ == '__main__':
  running = True


  pygame.init()
  pygame.display.set_caption('Sudoku')
  screen = pygame.display.set_mode((450, 500))
  #start_screen(screen)


  #Game Loop
  while running:
     #start_screen(screen)
     gameOver = False
     full_board = False
     difficulty = start_screen(screen)


     #Create instance and draw board
     b = Board(450, 500, screen, difficulty)
     screen.fill("light pink")
     b.draw()


     #Create an OG variable for "reset to original"
     og_board = b


     font = pygame.font.Font(None, 36)
     #Make buttons
     reset_button = pygame.Rect(35, 465, 100, 25)
     restart_button = pygame.Rect(175, 465, 100, 25)
     exit_button = pygame.Rect(325, 465, 100, 25)


     #Draw buttons
     pygame.draw.rect(screen, (177, 156, 217), reset_button)
     pygame.draw.rect(screen, (177, 156, 217), restart_button)
     pygame.draw.rect(screen, (177, 156, 217), exit_button)


     #Create button text
     reset_text = font.render("Reset", True, 'black')
     restart_text = font.render("Restart", True, 'black')
     exit_text = font.render("Exit", True, 'black')


     #Add text to buttons
     screen.blit(reset_text, (50, 465))
     screen.blit(restart_text, (185, 465))
     screen.blit(exit_text, (350, 465))


     #Events
     while gameOver is False:
        for event in pygame.event.get():
           #X out button pressed
           if event.type == pygame.QUIT:
              sys.exit()


           #Clicks
           if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
              x, y = pygame.mouse.get_pos()


              #Quit
              if exit_button.collidepoint(event.pos):
                 gameOver = True
                 sys.exit()


              #Reset
              if reset_button.collidepoint(event.pos):
                 screen.fill('light pink')
                 b.reset_to_original()
                 b.draw()
                 font = pygame.font.Font(None, 36)
                 # Make buttons
                 reset_button = pygame.Rect(35, 465, 100, 25)
                 restart_button = pygame.Rect(175, 465, 100, 25)
                 exit_button = pygame.Rect(325, 465, 100, 25)

                 # Draw buttons
                 pygame.draw.rect(screen, (177, 156, 217), reset_button)
                 pygame.draw.rect(screen, (177, 156, 217), restart_button)
                 pygame.draw.rect(screen, (177, 156, 217), exit_button)

                 # Create button text
                 reset_text = font.render("Reset", True, 'black')
                 restart_text = font.render("Restart", True, 'black')
                 exit_text = font.render("Exit", True, 'black')

                 # Add text to buttons
                 screen.blit(reset_text, (50, 465))
                 screen.blit(restart_text, (185, 465))
                 screen.blit(exit_text, (350, 465))

              #Restart
              if restart_button.collidepoint(event.pos):
                 screen.fill("light pink")
                 gameOver = True
                 break


              #Board is clicked
              board_pos = b.click(x, y)
              try:
                if board_pos is not None:
                    x, y = board_pos
                    b.select(x, y)
              except TypeError:
                  print()


           #User enters valid keyboard input
           if event.type == pygame.KEYDOWN:


              if (event.key == pygame.K_1 or
                      event.key == pygame.K_2 or
                      event.key == pygame.K_3 or
                      event.key == pygame.K_4 or
                      event.key == pygame.K_5 or
                      event.key == pygame.K_6 or
                      event.key == pygame.K_7 or
                      event.key == pygame.K_8 or
                      event.key == pygame.K_9):
                 sketched_value = event.key - 48
                 b.sketch(sketched_value)
                 b.place_number(sketched_value)
                 b.update_board()
                 sketched_value = 0


              #Clears spot on board if delete
              if event.key == pygame.K_BACKSPACE:
                 b.clear()


              #User hits enter -> place sketched value
              if event.key == pygame.K_RETURN and sketched_value != 0:
                 b.place_number(sketched_value)
                 b.update_board()
                 sketched_value = 0


              if b.is_full():
                 gameOver = True
                 full_board = True

           pygame.display.flip()


           #Game == over and there is a winner. Game is finished
        if gameOver and full_board:
           pygame.display.update()
           gameWon = b.check_board()
           #pygame.time.delay(1000)
           gameOver = game_over_screen(screen, gameWon)
           if gameOver:
               break
               # exit button on lose end game
               # exit_button = pygame.Rect(325, 465, 100, 25)
               # pygame.draw.rect(screen, (177, 156, 217), exit_button)
               # exit_text = font.render("Exit", True, 'black')
               # screen.blit(exit_text, (350, 465))

               # collide point


           # else:
           #     # restart button on win end game
           #     restart_button = pygame.Rect(175, 465, 100, 25)
           #     pygame.draw.rect(screen, (177, 156, 217), restart_button)
           #     restart_text = font.render("Restart", True, 'black')
           #     screen.blit(restart_text, (185, 465))

               # collide point
               # b.draw()
               # font = pygame.font.Font(None, 36)
               # # Make buttons
               # reset_button = pygame.Rect(35, 465, 100, 25)
               # restart_button = pygame.Rect(175, 465, 100, 25)
               # exit_button = pygame.Rect(325, 465, 100, 25)
               #
               # # Draw buttons
               # pygame.draw.rect(screen, (177, 156, 217), reset_button)
               # pygame.draw.rect(screen, (177, 156, 217), restart_button)
               # pygame.draw.rect(screen, (177, 156, 217), exit_button)
               #
               # # Create button text
               # reset_text = font.render("Reset", True, 'black')
               # restart_text = font.render("Restart", True, 'black')
               # exit_text = font.render("Exit", True, 'black')

        pygame.display.update()


