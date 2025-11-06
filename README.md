# Astro
simple SF starmap creator

I wrote this program for the neotrinkey - but will be merging it into "Traveler" a simple SF game for the Fruit Jam based on my earlier neotrinkey progam ["Adventure-Engine"](https://github.com/mrklingon/Adventure-Engine).

Files:

* astro.py (copy to code.py}
* wise.py
* prt.py (set REPL=True for printing in REPL, False to print via HID)
* ncount.py

When you touch pad #1, produces output like:
```
Ahghie:3, 1
Mieas:7, 1
Syaei:1, 7
Syuuas:1, 4
Giafnk:5, 4
Zoid:7, 6
..........
...*...*..
..........
..........
.*...*....
..........
.......*..
.*........
..........
..........
```
A list of stars and their x,y coordinates in a 10x10 grid, then a map of the stars.

When you touch pad #2, A random star will be picked as your "location" and the list of stars will be displayed AND the distance to each one from your current location:

```
location = Syuuas
Ahghie:3, 1: 3.60555
Mieas:7, 1: 6.7082
Syaei:1, 7: 3.0
Syuuas:1, 4: 0.0
Giafnk:5, 4: 4.0
Zoid:7, 6: 6.32455

location = Zoid
Ahghie:3, 1: 6.40312
Mieas:7, 1: 5.0
Syaei:1, 7: 6.08276
Syuuas:1, 4: 6.32455
Giafnk:5, 4: 2.82843
Zoid:7, 6: 0.0
```
