# Optimize the number of square dies that can be fit on a circular wafer
# By Sevan Brodjian || ICORLAB @ UIUC - Dr. Can Bayram || March 10, 2021

# This program draws square dies on a circular wafer. It then iterates
# by stepping the dies one step to the right until they have shifted
# horizontally by one side length + one spacing. Then, they shift back
# to the left and down by one step. We repeat until we have iterated horizontally
# and vertically by one side length + one spacing on both directions. Thus,
# we have tried all possible configurations (within our stepping size limitations)
# and can display for the user the maximum number of dies that we were able to fit.

# Import necessary libraries

# Used to clear the screen
import os

# Used for closing our program
import sys

# Used for simplifying some calculations
import math

# Used for progress bars
from tqdm import tqdm

# Graphics library for displaying results and calculations
import pygame

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')
print('Loading...')

# Window sizes for our display
Screen_Width = 500
Screen_Height = 500

# FUNCTION: Calculate the distance between two points
def dist(loc1, loc2=[Screen_Width / 2, Screen_Height / 2]):
    return math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1]))


# Start our program - main loop
while(True):

    # Initialize pygame, set our icon to big I
    pygame.init()
    icon = pygame.image.load('iconSmall.jpg')
    pygame.display.set_icon(icon)

    # Clear the screen and print license message
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Developed by ICORLAB at the University of Illinois at Urbana-Champaign, 2021")
    print("Professor Can Bayram, cbayram@illinois.edu, https://icorlab.ece.illinois.edu")
    print("Department of Electrical and Computer Engineering")
    print("By Sevan Brodjian, sevanpb2@illinois.edu")
    print("Please read the README.md or README.txt for instructions.\n\n")
    print("#############################################################################")
    print("#                *~ DIES ON WAFER OPTIMIZATION CALCULATOR ~*                #")
    print("#############################################################################")
    print("\n")


    # Setup user-input values

    # Get the diameter of the wafer in mm, defaults to 200 if nothing entered
    # Values must be a float greater than 0
    WaferDiaInMM = input("Enter Wafer Diameter (mm)[200]: ")
    if(WaferDiaInMM == ""):
        WaferDiaInMM = 200
    try:
        WaferDiaInMM = float(WaferDiaInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(WaferDiaInMM <= 0):
        print("Invalid value (must be > 0) - EXITING ABNORMALLY")
        sys.exit()

    # Get the dies dimensions in mm, defaults to 10 if nothing entered
    # Values must be a float greater than 0
    DieSideLengthInMM = input("Enter Square Die Side Length (mm)[10]: ")
    if(DieSideLengthInMM == ""):
        DieSideLengthInMM = 10
    try:
        DieSideLengthInMM = float(DieSideLengthInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(DieSideLengthInMM <= 0):
        print("Invalid value (must be > 0) - EXITING ABNORMALLY")
        sys.exit()

    # Get the spacing between dies in mm, defaults to 0.2 if nothing entered
    # Values must be a float greater than or equal to 0
    SpacingInMM = input("Enter Spacing Between Dies (mm)[0.2]: ")
    if(SpacingInMM == ""):
        SpacingInMM = 0.2
    try:
        SpacingInMM = float(SpacingInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(WaferDiaInMM < 0):
        print("Invalid value (must be >= 0) - EXITING ABNORMALLY")
        sys.exit()

    # Get the edge clearance of the wafer in mm, defaults to 5 if nothing entered
    # Values must be a float greater than or equal to 0
    EdgeClearenceInMM = input("Enter Edge Clearance (mm)[5]: ")
    if(EdgeClearenceInMM == ""):
        EdgeClearenceInMM = 5
    try:
        EdgeClearenceInMM = float(EdgeClearenceInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(WaferDiaInMM < 0):
        print("Invalid value (must be >= 0) - EXITING ABNORMALLY")
        sys.exit()

    # Get the height of our CMOS flat in mm, defaults to 0 if nothing entered
    # Values must be a float greater than or equal to 0
    NotchHeightInMM = input("Enter Notch/Flat Height (mm)[0]: ")
    if(NotchHeightInMM == ""):
        NotchHeightInMM = 0
    try:
        NotchHeightInMM = float(NotchHeightInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(NotchHeightInMM < 0):
        print("Invalid value (must be >= 0) - EXITING ABNORMALLY")
        sys.exit()

    # Get the stepping size for our calculations in mm, defaults to 0.5 if nothing entered
    # Values must be a float greater than 0
    SteppingInMM = input("Enter Stepping Size (mm)[0.5]: ")
    if(SteppingInMM == ""):
        SteppingInMM = 0.5
    try:
        SteppingInMM = float(SteppingInMM)
    except ValueError:
        print("Not a number - EXITING ABNORMALLY")
        sys.exit()
    if(SteppingInMM <= 0):
        print("Invalid value (must be > 0) - EXITING ABNORMALLY")
        sys.exit()

    # Subtracts our edge clearance from the height of our notch (this area is already unusable)
    NotchHeightInMM -= EdgeClearenceInMM

    # Save the original of our entire wafer (including edges)
    origDiaInMM = WaferDiaInMM

    # Subtract the edge clearance * 2 to get the usable radius of our wafer
    WaferDiaInMM -= 2 * EdgeClearenceInMM

    # Define constants for use in this program
    # Vertical/Height iterator
    Hiter = 0
    # Horizontal/Width itertor
    Witer = 0
    # A tuple for the center location of our program
    Center = [Screen_Width / 2, Screen_Height / 2]
    # Radius of our entire wafer in pixels
    backRadius = 200
    # Using our entire wafer as a reference, calculate the  number of pixels that equals one mm
    pixelsPermm = backRadius / (origDiaInMM / 2)

    # Convert all our user input values from mm dimensions to pixels
    # Radius for our usable wafer
    Radius = WaferDiaInMM * pixelsPermm / 2
    # Side length of our square dies
    s = DieSideLengthInMM * pixelsPermm
    # Spacing between dies
    spacing = SpacingInMM * pixelsPermm
    # Stepping size for our iterations
    stepping = SteppingInMM * pixelsPermm
    # Height of our notch relative to the bottom of our usable wafer
    notch = NotchHeightInMM * pixelsPermm

    # The maximum number of complete dies we could fit on this wafer
    maxCount = 0
    # The maximum number of partial dies we could fit on this wafer
    maxPartial = 0
    # True while we are iterating, otherwise false
    calculating = True
    # The Hiter value of our maximum die configuration
    bestW = 0
    # The Witer value of our maximum die configuration
    bestH = 0

    # Set up the drawing window
    screen = pygame.display.set_mode([Screen_Width, Screen_Height])
    pygame.display.set_caption("ICORLAB Dies-on-Wafer Calculator - CALCULATING...")

    # Calculate total number of steps (for progress bar)
    numSteps = round((s + spacing) / stepping * (s + spacing) / stepping)


    # CALCULATE THE MAXIMUM DIES ON THIS WAFER
    # Iterate a total of numSteps times
    for tracker in tqdm(range(numSteps), desc="CALCULATING"):

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("\n EXITING ABNORMALLY...")
                sys.exit()

        # Set the background to white
        screen.fill([0, 0, 0])

        # Draw a solid orange circle in the center (wafer)
        pygame.draw.circle(screen, [252, 186, 3], Center, backRadius)
        # Draw a solid white circle in the center (usable wafer)
        pygame.draw.circle(screen, [255, 255, 255], Center, Radius)

        # Cut off the notch from our wafer with a black rectangle
        flat = pygame.Surface([Screen_Width, Screen_Height - (Center[1]+Radius-notch)])
        flat.fill([0, 0, 0])
        screen.blit(flat, [0, Center[1]+Radius-notch])

        # Print off all dies

        # The number of complete dies we fit on the wafer with this configuration
        count = 0
        # The number of partial dies we fit on the wafer with this configuration
        partial = 0
        # Temporary horizontal drawing iterator
        i = 0
        # Temporary Veritcal drawing iterator
        j = 0
        # Draw dies from left to right in columns
        while(i < Screen_Width - s):
            # reset j
            j = 0
            # Draw a column of dies
            while(j < Screen_Height - s):
                # Did the user click the window close button?
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        print("\n EXITING ABNORMALLY...")
                        sys.exit()

                # Aesthetic black border size around our dies
                border = min(1, s / 5)
                # Define a rectangular surface (die) at (i, j) offset by (Hiter, Witer)
                surf = pygame.Surface([s - 2 * border, s - 2 * border])
                loc = [i + Hiter, j + Witer]

                # Calculate the maximum distance from our wafer center of all four corners
                MAX = max(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
                # Calculate the minimum distance from our wafer center of all four corners
                MIN = min(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
                # Calculate how far vertically below our wafer center the lower die edge is
                lowerUnder = loc[1] + s - Center[1]
                # Calculate how far vertically below our wafer center the upper die edge is
                upperUnder = loc[1] - Center[1]
                # Generate a surface for our black border
                surf2 = pygame.Surface([s, s])

                # Check if this wafer is fully within our radius and above our notch
                # If so, color it green and increment count
                if(MAX < Radius and lowerUnder < Radius - notch):
                    surf.fill([25, 255, 25])
                    count += 1
                # Check if this wafer is partially within our radius or in our notch
                # If so, color it blue, remove the border, increment partial, and make it partly transparent
                elif(MIN < Radius and upperUnder < Radius - notch):
                    surf.fill([25, 25, 255])
                    partial += 1
                    surf.set_alpha(175)
                    surf2.set_alpha(0)
                # Otherwise, this die does not fit on our wafer. Color it red and partly transparent.
                else:
                    surf.fill([255, 25, 25])
                    surf.set_alpha(175)
                    surf2.set_alpha(0)
                # Color our border black and draw it
                surf2.fill([0, 0, 0])
                screen.blit(surf2, loc)
                # Draw our die!
                screen.blit(surf, [loc[0] + border, loc[1] + border])

                # Done with this die, increment vertically to the next die
                j += s + spacing
            # Done with this column, increment horizontally to the next column of dies
            i += s + spacing

        # Check if we have fit a new maximum number of dies on the wafer
        if(count > maxCount):
            maxPartial = partial
            maxCount = count
            bestH = Hiter
            bestW = Witer

        # Iterate through all combinations
        if(calculating):
            Hiter += stepping
            if(Hiter >= s + spacing):
                Hiter = 0
                Witer += stepping
            # Check if we have returned to our original configuration
            # If so, we are done calculating!
            if(Witer >= s + spacing):
                calculating = False
                tracker = numSteps

        # Update the display
        if(calculating):
            pygame.display.flip()


    # DONE CALCULATING
    print("DONE")

    # Print off all dies one last time in the best configuration
    # Set the background to white
    screen.fill([0, 0, 0])

    # Draw a solid orange circle in the center (wafer)
    pygame.draw.circle(screen, [252, 186, 3], Center, backRadius)
    # Draw a solid white circle in the center (usable wafer)
    pygame.draw.circle(screen, [255, 255, 255], Center, Radius)

    # Cut off the notch from our wafer with a black rectangle
    flat = pygame.Surface([Screen_Width, Screen_Height - (Center[1]+Radius-notch)])
    flat.fill([0, 0, 0])
    screen.blit(flat, [0, Center[1]+Radius-notch])

    # Print off all dies

    # Set Hiter and Witer to their values at the best configuration
    Hiter = bestH
    Witer = bestW
    # Temporary horizontal drawing iterator
    i = 0
    # Temporary Veritcal drawing iterator
    j = 0
    # Draw dies from left to right in columns
    while(i < Screen_Width - s):
        # reset j
        j = 0
        # Draw a column of dies
        while(j < Screen_Height - s):
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("\n EXITING ABNORMALLY...")
                    sys.exit()

            # Aesthetic black border size around our dies
            border = min(1, s / 5)
            # Define a rectangular surface (die) at (i, j) offset by (Hiter, Witer)
            surf = pygame.Surface([s - 2 * border, s - 2 * border])
            loc = [i + Hiter, j + Witer]

            # Calculate the maximum distance from our wafer center of all four corners
            MAX = max(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
            # Calculate the minimum distance from our wafer center of all four corners
            MIN = min(dist(loc), dist([loc[0] + s, loc[1]]), dist([loc[0], loc[1] + s]), dist([loc[0] + s, loc[1] + s]))
            # Calculate how far vertically below our wafer center the lower die edge is
            lowerUnder = loc[1] + s - Center[1]
            # Calculate how far vertically below our wafer center the upper die edge is
            upperUnder = loc[1] - Center[1]
            # Generate a surface for our black border
            surf2 = pygame.Surface([s, s])

            # Check if this wafer is fully within our radius and above our notch
            # If so, color it green
            if(MAX < Radius and lowerUnder < Radius - notch):
                surf.fill([25, 255, 25])
            # Check if this wafer is partially within our radius or in our notch
            # If so, color it blue, remove the border and make it partly transparent
            elif(MIN < Radius and upperUnder < Radius - notch):
                surf.fill([25, 25, 255])
                surf.set_alpha(175)
                surf2.set_alpha(0)
            # Otherwise, this die does not fit on our wafer. Don't display it.
            else:
                surf.set_alpha(0)
                surf2.set_alpha(0)
            # Color our border black and draw it
            surf2.fill([0, 0, 0])
            screen.blit(surf2, loc)
            # Draw our die!
            screen.blit(surf, [loc[0] + border, loc[1] + border])

            # Done with this die, increment vertically to the next die
            j += s + spacing
        # Done with this column, increment horizontally to the next column of dies
        i += s + spacing

    # Display our results
    # Update the display
    pygame.display.flip()
    # Change our program title
    pygame.display.set_caption("ICORLAB Dies-on-Wafer Calculator - DONE")
    # Print the calculated values in the terminal
    print('\n ~~~ MAXIMUM DIES FIT ON WAFER: ' + str(maxCount) + ' ~~~')
    print(' ~~~ PARTIAL DIES FIT ON WAFER: ' + str(maxPartial) + ' ~~~')
    print("\nRun new calculation? (y/n) [ENTER IN OTHER WINDOW]")

    # Check if we run again
    waiting = True
    done = True
    while(waiting):
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                pygame.quit()
                print("\n EXITING ABNORMALLY...")
                sys.exit()
            # Did the user press a key?
            if event.type == pygame.KEYDOWN:
                # Was the key pressed 'y'?
                if event.key == pygame.K_y:
                    done = False
                waiting = False

    # Close our pygame window
    pygame.quit()
    # If the user didn't press 'y' then exit. Otherwise loop again
    if(done):
        sys.exit()