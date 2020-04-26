# Map-Visualiser
A way to visualise the FLL Map and plan a route


## Instructions for use 
- First downoad this repo
- Then find an image of the FLL Board you need and convert it to a GIF.
   - Use an online converter of open it in MS paint and exort as a .gif file
- Add the map into the same directory 
- Open the visualplanner.py and add a new variable after line 9 equal to the new mat or edit an existing one
- Then add this variable to line twelve instead of the existing one.

For Example:
If my new map is called olympics.gif I will change line 9 to:
```python
newMap = "olympics.gif"
# and I will change line 12 to:
wn.bgpic(newMap)
```

- Now your done, run the program and either use the number pad or drag the robot
