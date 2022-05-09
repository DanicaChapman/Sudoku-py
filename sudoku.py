import pygame #setup
import requests

aqua = (3,168,158)

values = requests.get("https://sugoku.herokuapp.com/board?difficulty=random")
grid = values.json()['board']
og_grid = [[grid[x][y] for y in range(len(grid[0]))] for x in range (len(grid))] #separate grid for comparison

width = 550 #width of grid
buf = 5 #small buffer for individual squares

def input(window, pos): #function for handling user input
    font = pygame.font.SysFont('impact', 40)
    i,j = pos[1], pos[0]

    while True: #whenever theres a click
        for move in pygame.event.get():
            if move.type == pygame.QUIT:
                return
            if move.type == pygame.KEYDOWN:
                if (og_grid[i-1][j-1] != 0):
                    return
                if (move.key == 48): #user inputs zero
                    grid[i-1][j-1] = move.key - 48
                    pygame.draw.rect(window, "black", (pos[0]*50 + buf, pos[1]*50 +buf, 50 - 1.5*buf, 50 - 1.5*buf))
                    pygame.display.update()
                if (0 < (move.key - 48) <10): #if user input is valid, -48 to conver input to ASCII
                    pygame.draw.rect(window, "black", (pos[0]*50 + buf, pos[1]*50 +buf, 50 - 1.5*buf, 50 - 1.5*buf))
                    number = font.render(str(move.key-48), True, aqua)
                    window.blit(number, (pos[0]*50 + 15, pos[1]*50))
                    grid[i-1][j-1] = move.key - 48
                    pygame.display.update()
                return
    return




def main(): #main
    pygame.init()
    window = pygame.display.set_mode((width,width))
    pygame.display.set_caption("Let's Play Sudoku") #title
    window.fill("black") #background
    font = pygame.font.SysFont('impact', 40)

    for i in range(0,10):
        if(i%3 == 0): #wider lines
            pygame.draw.line(window, ("white"), (50 + 50*i, 50), (50 + 50*i ,500 ), 6 )
            pygame.draw.line(window, ("white"), (50, 50 + 50*i), (500, 50 + 50*i), 6 )
        #smaller lines
        pygame.draw.line(window, ("white"), (50 + 50*i, 50), (50 + 50*i ,500 ), 3 )
        pygame.draw.line(window, ("white"), (50, 50 + 50*i), (500, 50 + 50*i), 3 )
    pygame.display.update()

    for i in range (0, len(grid[0])):
        for j in range (0, len(grid[0])):
            if (0<grid[i][j]<10): 
                number = font.render(str(grid[i][j]), True, aqua)
                window.blit(number, ((j+1)*50 +15, (i+1)*50))
    pygame.display.update()
        

    while True: #keeps game running until user quits
        for move in pygame.event.get():
            if move.type == pygame.MOUSEBUTTONUP and move.button == 1: #leftclick
               position = pygame.mouse.get_pos() 
               input(window, (position[0]//50, position[1]//50))
            if move.type == pygame.QUIT:
                pygame.quit()
                return

main()





