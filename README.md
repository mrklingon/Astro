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
Rouuah:7, 9
Reeei:6, 9
Ahaie:7, 0
Zooof:5, 1
Ahiah:2, 2
Paafnk:8, 1
Rouuas:6, 0
Reuof:2, 5
......**..
.....*..*.
..*.......
..........
..........
..*.......
..........
..........
..........
......**..
```
A list of stars and their x,y coordinates in a 10x10 grid, then a map of the stars.
