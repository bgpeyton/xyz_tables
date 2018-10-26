A script for converting simple `.xyz` coordinate files to simple LaTeX tables.

`.xyz` file must contain name of molecule on first line, as in `h2o.xyz` included. Names may be multi-word. 

To run,
```python
python xyz2tbl.py mol.xyz
```

Resulting LaTeX code will be stored in `out.txt`.

`out.txt` will be appended, not overwritten, so feel free to make all of your tables at once, then copy them into your document!

Note that all coordinates will be printed to 6 decimal places. Make adjustments if needed. 
