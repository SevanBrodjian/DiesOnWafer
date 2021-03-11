# Optimize the number of square dies that can be fit on a circular wafer
# By Sevan Brodjian || ICORLAB @ UIUC - Dr. Can Bayram || March 10, 2021

# import necessary libraries
import math

# Import and initialize the pygame library
import pygame
pygame.init()

# Define constants for use in this program
pixelValInmm = 0.1
Screen_Width = 450
Screen_Height = 450
Hiter = 0
Witer = 0
Center = [Screen_Width / 2, Screen_Height / 2]
Radius = 190
s = 20
spacing = 0.4
maxCount = 0
calculating = True
bestW = 0
bestH = 0

# Set up the drawing window
screen = pygame.display.set_mode([Screen_Width, Screen_Height])
pygame.display.set_caption("ICORLAB Dies-on-Wafer Calculator")

# Calculate the distance between two points


def dist(loc1, loc2=[Screen_Width / 2, Screen_Height / 2]):
    return math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1]))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set the background to white
    screen.fill([0, 0, 0])

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, [255, 255, 255], Center, Radius)

    count = 0
    partial = 0
    i = 0
    j = 0
    while(i < Screen_Width - s):
        j = 0
        while(j < Screen_Height - s):
            surf = pygame.Surface([s - 2, s - 2])
            loc = [i + Hiter, j + Witer]
            MAX = max(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
            MIN = min(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
            if(MAX < Radius):
                surf.fill([25, 255, 25])
                count += 1
            elif(MIN < Radius):
                surf.fill([25, 25, 255])
                partial += 1
            else:
                surf.fill([255, 25, 25])
            surf2 = pygame.Surface([s - 1, s - 1])
            surf2.fill([0, 0, 0])
            screen.blit(surf2, loc)
            screen.blit(surf, [loc[0] + 1, loc[1] + 1])
            if(count > maxCount):
                maxCount = count
                bestH = Hiter
                bestW = Witer
            j += s + spacing
        i += s + spacing

    if(calculating):
        Hiter += 1
        if(Hiter >= s + spacing):
            Hiter = 0
            Witer += 1
        if(Witer >= s + spacing):
            print(maxCount)
            Hiter = bestH
            Witer = bestW
            calculating = False

    # Update the display
    if(calculating):
        pygame.display.flip()
# Done! Time to quit.
pygame.quit()
