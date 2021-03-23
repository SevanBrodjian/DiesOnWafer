~~Dies-On-Wafer Calculator~~

This program will calculate the maximum number of square dies that can be cut from a circular wafer. 
Results and calculations will be visually displayed and final values will be printed to the terminal. 
The following parameters can be input for the calculation to take place, please check the How to use? 
section for more details:
    Wafer Diameter
    Die Side Length
    Spacing Between Dies
    Edge Clearance
    CMOS Notch Height
    Stepping Size


~~Motivation~~
There are other similar calculators online, but this calculator was built to prioritize the following functionalities:
    Guaranteed accurate values every time
    Support for wafers of any size, including non-standard
    Support for any die size
    Support for dies lost to a CMOS notch
    Support for edge exclusion caused by limited epitaxy growth
    Tunable accuracy (stepping size)

Other calculators often prioritize speed and efficiency, and use an algorithmic approach. 
Thus, these calculators produce inconsistent values, are not highly flexible, or have no visual display. 
This calculator uses an iterative approach instead, which guarantees the best possible configuration. 
This calculator can also accept any wafer size, die size, notch height, and edge exclusion without affecting accuracy.


~~How to use?~~
This program works in three phases: Input, Calculation, and Display

1. Input:
    When the program is first launched and finished loading, it is in the input stage. 
    Only a terminal will be open with some introductory text at this point. 
    The purpose of this stage is for the user to specify the configuration of their wafer/die setup to be calculated.
    The user can customize the following parameters:

    Wafer Diameter
        The wafer diameter is the total width of the wafer, measured in millimeters, including the edge exclusion. 
        Diameters between 50mm and 500mm work best.
        Default: 200mm
        Restriction: Values must be a number greater than zero.

    Die Side Length
        The Die Side Length is the length, in mm, of each die that will be cut from this wafer. 
        Only square dies are supported, so dies will have an area of DieSideLength*DieSideLength [mm^2]. 
        Side lengths between 1mm and 30mm work best.
        Default: 10mm
        Restriction: Values must be a number greater than zero.

    Spacing Between Dies
        This is a measurement for how much spacing there must be between two dies, typically due to the cut lines, 
        measured in mm. Any positive value may be input, including 0.
        Default: 0.2mm
        Restriction: Values must be a number greater than or equal to zero.

    Edge Clearance
        Edge Clearance is the maximum proximity a die can have to the edge of the wafer, measured in mm. 
        Edge exclusion is typically caused by limited epitaxy near the edges of the wafer making it unsuitable for dies. 
        Any positive value may be input, including 0.
        Default: 5mm
        Restriction: Values must be a number greater than or equal to zero.

    CMOS Notch Height
        For CMOS compatibility, a notch is usually taken off of one side of the die, common in 300mm wafers. 
        This parameter is a measurement for how high from the bottom point of the wafer the notch is, measured in mm.
        Lost area may include edge excluded zones. Any positive value may be input, including 0.
        Default: 0mm
        Restriction: Values must be a number greater than or equal to zero.

    Stepping Size
        This parameter is specific to this software and determines how accurate the simulation will be, but also how long it 
        will take to compute. Read more about how this works in the calculation step. Stepping sizes between 0.1mm and 0.5mm work best.
        Default: 0.5mm
        Restriction: Values must be a number greater than zero.

    Each value must be typed in when prompted, and then the Enter key must be pressed to submit it. If no value was entered, 
    but the Enter key was pressed, the default value for that parameter will be used. If there were any issues with the values 
    provided the program will print the problem and halt. Once the stepping size has been entered and submitted the program will 
    enter the calculation phase.

2. Calculation:
    During this phase the program will calculate what configuration of dies allows for the maximum number to be fit onto the wafer. 
    To start calculating, a second window titled "ICORLAB Dies-on-Wafer Calculator: Calculating..." will open up. This is the graphics 
    window where we can visually see what is happening and what our configuration looks like.

    The user does not interact with the program during this stage. To cancel the program, simply click the exit button in the 
    graphics window. The wafer will be displayed as a large circle (radius 200px) in the center of the window. Any portion of the 
    circle colored white is a valid part of the wafer for a die to reside. Any portion of the circle colored orange is in the edge 
    exclusion zone, and dies cannot be placed here. Any portion colored black is outside of the wafer and invalid. Additionally, 
    there will be a slice taken off of the bottom of our circle corresponding with the CMOS notch height specified.

    Dies will be placed in a uniform grid pattern, this program does not support any other configuration of dies currently. 
    Die sizes are to scale with the wafer size (with a very slight reduction for visual effect). There will also be a to-scale 
    spacing between the dies in all directions to account for die spacing. If a die resides entirely outside of the valid portion 
    of the wafer it will be colored red. If a die lies partially within the valid region, and partially outside, it will be colored 
    blue. If a die lies entirely within the valid region of our wafer, it will be colored green.

    While calculating, the dies will begin in the upper-left-most corner. Then, the dies will all shift to the right by one step, 
    equal to the specified stepping size. At each step, the number of complete and partial dies fit on our wafer is calculated. 
    After moving to the right by one whole die length + die spacing, the dies are shifted back to the left-most configuration. 
    Then, the dies are stepped downwards by one step. This process will repeat until the dies have traversed one entire side 
    length + spacing horizontally and vertically. This process covers every single possible configuration of dies within the limits 
    of our stepping size; 0.1mm to 0.5mm is typically more than sufficient. Once this is done, the calculation phase is complete 
    and the program enters the Displya phase.

3. Display:
    The program has entered the display phase once the calculation is complete. The title of the graphics window will change 
    to "ICORLAB Dies-on-Wafer Calculator: DONE", the best configuration will be displayed in the window, and the maximum number 
    of complete and partial dies in this configuration will be printed to the terminal. The graphics window will also not show 
    any red dies when the best configuration is being displayed.

    To restart the program and input new parameters, simply select the graphics window and press the 'y' key, which sets the 
    program back to the Input phase. If any other key is pressed while this window is selected the program will close. In either 
    case, the terminal will be cleared and the graphics window will close, so ensure that all necessary results are recorded down 
    before proceeding.


~~Built With~~
This software was written by Sevan Brodjian using Python 3.7.4 in March of 2021. The following Python libraries were used:
    Pygame - Used for generating graphics.
    TQDM - Displays the loading bars.
    OS - Allows for the screen to be cleared.
    Sys - Used to exit the program.
    Math - Used to simplify square roots.
    Pyinstaller - Converts the program into a portable EXE.

~~Requirements~~
The following are the minimum requirements needed to run this software:
    Display: 600 x 600
    CPU: Intel Core i3 or equivalent
    GPU: None
    Operating System: Windows 10
    RAM: 4GB
    Storage: 100MB Available

~~License~~
Developed by ICORLAB at the University of Illinois at Urbana-Champaign, 2021
Professor Can Bayram, cbayram@illinois.edu, https://icorlab.ece.illinois.edu
Department of Electrical and Computer Engineering
By Sevan Brodjian, sevanpb2@illinois.edu