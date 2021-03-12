# Optimize the number of square dies that can be fit on a circular wafer
# By Sevan Brodjian || ICORLAB @ UIUC - Dr. Can Bayram || March 10, 2021


# import necessary libraries
import pygame
from tqdm import tqdm
import math
import sys
import os
import time

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')
print('Loading...')

# Window sizes for pygame
Screen_Width = 500
Screen_Height = 500

# FUNCTION: Calculate the distance between two points


def dist(loc1, loc2=[Screen_Width / 2, Screen_Height / 2]):
    return math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1]))


# Start our program
while(True):
    # Initialize pygame
    pygame.init()
    icon = pygame.image.load('iconSmall.jpg')
    pygame.display.set_icon(icon)

    # Print opening message
    os.system('cls' if os.name == 'nt' else 'clear')
    print("©ICORLAB @ UIUC 2021 - Dr. Can Bayram || By Sevan Brodjian")
    print("###########################################################")
    print("#       *~ DIES ON WAFER OPTIMIZATION CALCULATOR ~*       #")
    print("###########################################################")
    print("\n")

    # Setup user-input values
    WaferDiaInMM = input("Enter Wafer Diameter (mm): ")
    if(WaferDiaInMM == ""):
        WaferDiaInMM = 200
    try:
        WaferDiaInMM = float(WaferDiaInMM)
    except ValueError:
        print("Not a float")
        sys.exit()
    if(WaferDiaInMM <= 0):
        print("Invalid value (must be > 0)")
        sys.exit()

    DieSideLengthInMM = input("Enter Square Die Side Length (mm): ")
    if(DieSideLengthInMM == ""):
        DieSideLengthInMM = 11.8
    try:
        DieSideLengthInMM = float(DieSideLengthInMM)
    except ValueError:
        print("Not a float")
        sys.exit()
    if(DieSideLengthInMM <= 0):
        print("Invalid value (must be > 0)")
        sys.exit()

    SpacingInMM = input("Enter Spacing Between Dies (mm): ")
    if(SpacingInMM == ""):
        SpacingInMM = 0.2
    try:
        SpacingInMM = float(SpacingInMM)
    except ValueError:
        print("Not a float")
        sys.exit()
    if(WaferDiaInMM < 0):
        print("Invalid value (must be >= 0)")
        sys.exit()

    SteppingInMM = input("Enter Stepping Size (mm): ")
    if(SteppingInMM == ""):
        SteppingInMM = 0.5
    try:
        SteppingInMM = float(SteppingInMM)
    except ValueError:
        print("Not a float")
        sys.exit()
    if(SteppingInMM <= 0):
        print("Invalid value (must be > 0)")
        sys.exit()

    EdgeClearenceInMM = input("Enter Edge Clearance (mm): ")
    if(EdgeClearenceInMM == ""):
        EdgeClearenceInMM = 5
    try:
        EdgeClearenceInMM = float(EdgeClearenceInMM)
    except ValueError:
        print("Not a float")
        sys.exit()
    if(WaferDiaInMM < 0):
        print("Invalid value (must be >= 0)")
        sys.exit()
    WaferDiaInMM -= 2 * EdgeClearenceInMM

    # Define constants for use in this program
    Hiter = 0
    Witer = 0
    Center = [Screen_Width / 2, Screen_Height / 2]
    Radius = 200
    pixelsPermm = Radius / (WaferDiaInMM / 2)

    s = DieSideLengthInMM * pixelsPermm
    spacing = SpacingInMM * pixelsPermm
    stepping = SteppingInMM * pixelsPermm

    maxCount = 0
    calculating = True
    bestW = 0
    bestH = 0

    # Set up the drawing window
    screen = pygame.display.set_mode([Screen_Width, Screen_Height])
    pygame.display.set_caption("ICORLAB Dies-on-Wafer Calculator")

    # Calculate total number of steps for progress bar
    numSteps = round((s + spacing) / stepping * (s + spacing) / stepping)

    # Calculate the max dies on this wafer
    for tracker in tqdm(range(numSteps), desc="CALCULATING"):

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("\n EXITING ABNORMALLY...")
                sys.exit()

        # Set the background to white
        screen.fill([0, 0, 0])

        # Draw a solid white circle in the center (wafer)
        pygame.draw.circle(screen, [255, 255, 255], Center, Radius)

        # Print off all dies
        count = 0
        partial = 0
        i = 0
        j = 0
        while(i < Screen_Width - s):
            j = 0
            while(j < Screen_Height - s):
                # Did the user click the window close button?
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        print("\n EXITING ABNORMALLY...")
                        sys.exit()

                # Define a rectangle at this location
                surf = pygame.Surface([s - 2, s - 2])
                loc = [i + Hiter, j + Witer]

                # Calculate whether it is in the wafer fully or partially and color accordingly, then draw it
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

        # Iterate through all combinations
        if(calculating):
            Hiter += stepping
            if(Hiter >= s + spacing):
                Hiter = 0
                Witer += stepping
            if(Witer >= s + spacing):
                Hiter = bestH
                Witer = bestW
                calculating = False
                tracker = numSteps

        # Update the display
        if(calculating):
            pygame.display.flip()

    # DONE CALCULATING
    print("DONE")

    # Print off all dies one last time
    count = 0
    partial = 0
    i = 0
    j = 0
    while(i < Screen_Width - s):
        j = 0
        while(j < Screen_Height - s):
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("\n EXITING ABNORMALLY...")
                    sys.exit()

            # Define a rectangle at this location
            surf = pygame.Surface([s - 2, s - 2])
            loc = [i + Hiter, j + Witer]

            # Calculate whether it is in the wafer fully or partially and color accordingly, then draw it
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

    print('\n ~~~ MAXIMUM DIES FIT ON WAFER: ' + str(maxCount) + ' ~~~')
    again = input("Run new calculation? (Y/N): ")
    pygame.quit()
    if(again != "Y"):
        sys.exit()
