import sys
import pygame

pygame.init()

# get screen size and screen object
height = pygame.display.Info().current_h - 75
width = pygame.display.Info().current_w - 75
screen = pygame.display.set_mode((width, height))

# get mouse
pygame.mouse.set_visible(True)
mouse = pygame.mouse.get_cursor()

# get object, initial position, color
dragDropPos = {"x": width / 2, "y": height / 2}
dragDropDimension = {"height" : 50, "width" : 50}
dragDropColor = (100,200,100)
dragDropMoving = False 
dragDropRect = pygame.Rect(dragDropPos["x"], dragDropPos["y"], dragDropDimension["width"], dragDropDimension["height"])

# draw initial position
pygame.draw.rect(screen, dragDropColor, dragDropRect)

# main game loop
while True:

    # get mouse position
    mousePos = pygame.mouse.get_pos()

    # check events
    for event in pygame.event.get(pump=True):

        #if exit event, quit
        if event.type == pygame.QUIT:
            sys.exit()
        
        # if the mouse clicks down, move the dragDrop square to its position
        if event.type == pygame.MOUSEBUTTONDOWN and dragDropRect.collidepoint(mousePos) == True:
            dragDropPos["x"] = mousePos[0]
            dragDropPos["y"] = mousePos[1]
            dragDropMoving = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragDropMoving = False

    # move the reactangle if mouse continuing to hold down
    if dragDropMoving == True:
        screen.fill((0,0,0))
        dragDropRect.center = mousePos
        pygame.draw.rect(screen, dragDropColor, dragDropRect)

    pygame.display.flip()