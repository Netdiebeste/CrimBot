# CrimBot
A simple external python script that auto collects allowance from the roblox game Criminality by RVVZ
this simple script locates the "claim allowance" button and auto clicks it. 
you must make sure the click location is set SPECIFICALLY for you (on the claim allowance button).
use an app like https://sourceforge.net/projects/mpos/ to find the coordinates and put the X value and Z value in is appropriate position.   the code will only check for the button every 30 seconds, to change this edit the 30.0 value in the last line of code: print("please wait")time.sleep(30.0) to how many seconds you want before it checks again. 
