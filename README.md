<div id="top">
  <h1 style="color:darkslategrey;"><b>Dies-On-Wafer Calculator</b></h1>
</div>

<div id="intro">
  <p>
    This program will calculate the maximum number of square dies that can be cut from a circular wafer. Results and calculations will be visually displayed and final values will be printed to the terminal. The following parameters can be input for the calculation to take place, please check the How to use? section for more details:
    <ul>
      <li>Wafer Diameter</li>
      <li>Die Side Length</li>
      <li>Spacing Between Dies</li>
      <li>Edge Clearance</li>
      <li>CMOS Notch Height</li>
      <li>Stepping Size</li>
    </ul>
  </p>
</div>

<div id="toc">
  <h1 style="color:darkslategrey;">TOC</h1>
  <h2>
    <a href="#motivation">Motivation</a><br>
    <a href="#howtouse">How to use?</a><br>
    <a href="#builtwith">Built With</a><br>
    <a href="#requirements">Requirements</a><br>
    <a href="#license">License</a><br>
  </h2>
</div>

<br>
<div id="motivation">
  <h1 style="color:darkslategrey;">Motivation</h1>
  <p>
    There are other similar calculators online, but this calculator was built to prioritize the following functionalities:
    <ol>
      <li>Guaranteed accurate values every time</li>
      <li>Support for wafers of any size, including non-standard</li>
      <li>Support for any die size</li>
      <li>Support for dies lost to a CMOS notch</li>
      <li>Support for edge exclusion caused by limited epitaxy growth</li>
      <li>Tunable accuracy (stepping size)</li>
    </ol>
    Other calculators often prioritize speed and efficiency, and use an algorithmic approach. Thus, these calculators produce inconsistent values, are not highly flexible, or have no visual display. This calculator uses an iterative approach instead, which guarantees the best possible configuration. This calculator can also accept any wafer size, die size, notch height, and edge exclusion without affecting accuracy.
  </p>
</div>

<br>
<div id="howtouse">
  <h1 style="color:darkslategrey;">How to use?</h1>
  <p>
    This program works in three phases: 
    <b>Input</b>, <b>Calculation</b>, and <b>Display</b>
    <br>
    <h3><b>1. Input:</b></h3>
    When the program is first launched and finished loading, it is in the input stage. Only a terminal will be open with some introductory text at this point. The purpose of this stage is for the user to specify the configuration of their wafer/die setup to be calculated.<br>
    The user can customize the following parameters:
    <br><br>
    <ul>
      <li><b><u>Wafer Diameter</u></b></li>
      The wafer diameter is the total width of the wafer, measured in millimeters, including the edge exclusion. Diameters between 50mm and 500mm work best.<br>
      <u>Default</u>: 200mm<br>
      <u>Restriction</u>: Values must be a number greater than zero.
      <br><br>
      <li><b><u>Die Side Length</u></b></li>
      The Die Side Length is the length, in mm, of each die that will be cut from this wafer. Only square dies are supported, so dies will have an area of DieSideLength*DieSideLength [mm^2]. Side lengths between 1mm and 30mm work best.<br>
      <u>Default</u>: 10mm<br>
      <u>Restriction</u>: Values must be a number greater than zero.
      <br><br>
      <li><b><u>Spacing Between Dies</u></b></li>
      This is a measurement for how much spacing there must be between two dies, typically due to the cut lines, measured in mm. Any positive value may be input, including 0.<br>
      <u>Default</u>: 0.2mm<br>
      <u>Restriction</u>: Values must be a number greater than or equal to zero.
      <br><br>
      <li><b><u>Edge Clearance</u></b></li>
      Edge Clearance is the maximum proximity a die can have to the edge of the wafer, measured in mm. Edge exclusion is typically caused by limited epitaxy near the edges of the wafer making it unsuitable for dies. Any positive value may be input, including 0.<br>
      <u>Default</u>: 5mm<br>
      <u>Restriction</u>: Values must be a number greater than or equal to zero.
      <br><br>
      <li><b><u>CMOS Notch Height</u></b></li>
      For CMOS compatibility, a notch is usually taken off of one side of the die, common in 300mm wafers. This parameter is a measurement for how high from the bottom point of the wafer the notch is, measured in mm. Lost area may include edge excluded zones. Any positive value may be input, including 0.<br>
      <u>Default</u>: 0mm<br>
      <u>Restriction</u>: Values must be a number greater than or equal to zero.
      <br><br>
      <li><b><u>Stepping Size</u></b></li>
      This parameter is specific to this software and determines how accurate the simulation will be, but also how long it will take to compute. Read more about how this works in the calculation step. Stepping sizes between 0.1mm and 0.5mm work best.<br>
      <u>Default</u>: 0.5mm<br>
      <u>Restriction</u>: Values must be a number greater than zero.
    </ul>
    <br>
    Each value must be typed in when prompted, and then the Enter key must be pressed to submit it. If no value was entered, but the Enter key was pressed, the default value for that parameter will be used. If there were any issues with the values provided the program will print the problem and halt. Once the stepping size has been entered and submitted the program will enter the calculation phase.
    <br>
    <br>
    <h3><b>2. Calculation:</b></h3>
    During this phase the program will calculate what configuration of dies allows for the maximum number to be fit onto the wafer. To start calculating, a second window titled "ICORLAB Dies-on-Wafer Calculator: Calculating..." will open up. This is the graphics window where we can visually see what is happening and what our configuration looks like.<br><br>
    The user does not interact with the program during this stage. To cancel the program, simply click the exit button in the graphics window. The wafer will be displayed as a large circle (radius 200px) in the center of the window. Any portion of the circle colored <b><span style="color:palegoldenrod;">white</span></b> is a valid part of the wafer for a die to reside. Any portion of the circle colored <span style="color:orange;">orange</span> is in the edge exclusion zone, and dies cannot be placed here. Any portion colored <b><span style="color:black;">black</span></b> is outside of the wafer and invalid. Additionally, there will be a slice taken off of the bottom of our circle corresponding with the CMOS notch height specified.<br><br>
    Dies will be placed in a uniform grid pattern, this program does not support any other configuration of dies currently. Die sizes are to scale with the wafer size (with a very slight reduction for visual effect). There will also be a to-scale spacing between the dies in all directions to account for die spacing. If a die resides entirely outside of the valid portion of the wafer it will be colored <span style="color:red;">red</span>. If a die lies partially within the valid region, and partially outside, it will be colored <span style="color:blue;">blue</span>. If a die lies entirely within the valid region of our wafer, it will be colored <span style="color:green;">green</span>.<br><br>
    While calculating, the dies will begin in the upper-left-most corner. Then, the dies will all shift to the right by one step, equal to the specified stepping size. At each step, the number of complete and partial dies fit on our wafer is calculated. After moving to the right by one whole die length + die spacing, the dies are shifted back to the left-most configuration. Then, the dies are stepped downwards by one step. This process will repeat until the dies have traversed one entire side length + spacing horizontally and vertically. This process covers every single possible configuration of dies within the limits of our stepping size; 0.1mm to 0.5mm is typically more than sufficient. Once this is done, the calculation phase is complete and the program enters the Displya phase.
    <br>
    <br>
    <h3><b>3. Display:</b></h3>
    The program has entered the display phase once the calculation is complete. The title of the graphics window will change to "ICORLAB Dies-on-Wafer Calculator: DONE", the best configuration will be displayed in the window, and the maximum number of complete and partial dies in this configuration will be printed to the terminal. The graphics window will also not show any red dies when the best configuration is being displayed.<br><br>
    To restart the program and input new parameters, simply select the graphics window and press the 'y' key, which sets the program back to the Input phase. If <u>any</u> other key is pressed while this window is selected the program will close. In either case, the terminal will be cleared and the graphics window will close, so ensure that all necessary results are recorded down before proceeding.
  </p>
</div>

<br>
<br>
<div id="builtwith">
  <h1 style="color:darkslategrey;">Built With</h1>
  <p>
    This software was written by Sevan Brodjian using Python 3.7.4 in March of 2021. The following Python libraries were used:
    <ul>
      <li><b>Pygame</b> - Used for generating graphics.</li>
      <li><b>TQDM</b> - Displays the loading bars.</li>
      <li><b>OS</b> - Allows for the screen to be cleared.</li>
      <li><b>Sys</b> - Used to exit the program.</li>
      <li><b>Math</b> - Used to simplify square roots.</li>
      <li><b>Pyinstaller</b> - Converts the program into a portable EXE.</li>
    </ul>
  </p>
</div>

<br>
<div id="requirements">
  <h1 style="color:darkslategrey;">Requirements</h1>
  <footer>
    <p>
      The following are the minimum requirements needed to run this software:
      <ul>
      <li><b>Display</b>: 600 x 600</li>
      <li><b>CPU</b>: Intel Core i3 or equivalent</li>
      <li><b>GPU</b>: None</li>
      <li><b>Operating System</b>: Windows 10</li>
      <li><b>RAM</b>: 4GB</li>
      <li><b>Storage</b>: 100MB Available</li>
    </ul>
    </p>
  </footer>
</div>

<br>
<div id="license">
  <h1 style="color:darkslategrey;">License</h1>
  <footer>
    <p>
      Developed by ICORLAB at the University of Illinois at Urbana-Champaign, 2021 <br> 
      Professor Can Bayram, 
      <a href="mailto:cbayram@illinois.edu?Subject=Dies On Wafer Program">cbayram@illinois.edu</a>, 
      <a href="https://icorlab.ece.illinois.edu">https://icorlab.ece.illinois.edu</a> <br>
      Department of Electrical and Computer Engineering <br>
      By Sevan Brodjian, <a href="mailto:sevanpb2@illinois.edu?Subject=Dies On Wafer Program">sevanpb2@illinois.edu</a> <br><br>
    </p>
  </footer>
</div>

<a href="#top">Back to top</a>
