BMI Calculator
================
This project can be used to finding the count of overweight people based on the input JSON data passed.
The below table is referred for doing the calculations.
Table 1 - BMI Category and the Health Risk.
BMI Category BMI Range (kg/m2) Health risk
Underweight 18.4 and below Malnutrition risk
Normal weight 18.5 - 24.9 Low risk
Overweight 25 - 29.9 Enhanced risk
Moderately obese 30 - 34.9 Medium risk
Severely obese 35 - 39.9 High risk
Very severely obese 40 and above Very high risk

``This has been written using Python 3.x``

Usage 
==========
1. Install python 3.x in your system. More details on how to install is provided in the link https://docs.python.org/3/using/index.html
2. After installing, we will use python interpreter to run the code
3. To open the command-line interpreter:
   1. On **Windows**, the command-line is called the command prompt or MS-DOS console. A quicker way to access it is to go to *Start menu → Run* and type **cmd**. 
   2. On **GNU/Linux**, the command-line can be accessed by several applications like xterm, Gnome Terminal or Konsole. 
   3. On **MAC OS X**, the system terminal is accessed through *Applications → Utilities → Terminal*.
4. Execute the code by typing the word python followed by the path to your python script file, like this:
    ```
    python C:\Downloads\bmi-calculator\src\bmi\calculator.py "[{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96 },{ 'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85 },{ 'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77 },{ 'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62},{'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70},{'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82}]"
    ```
5. The count of overweight people will be printed in the console