if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        fname = str(sys.argv[1])
    else:
        fname = 'mol.xyz'

xyz = []
with open(fname,'r') as f: 
    first_line = True
    for line in f:
        if first_line:
            mname = str(line)
            first_line = False
        else:
            (A,x,y,z) = line.split()
            xyz.append([str(A),str(x),str(y),str(z)])

with open('out.txt','a') as o:
    o.write("""\\begin{{table}}
    \\centering
    \\caption{{Atomic coordinates of {} (\\AA ngstroms)}}
    \\label{{{}}}
    \\begin{{tabular}}{{ c c c c }}
    \\hline
    \\hline
    Atomic & & & \\\\
    Symbol & X & Y & Z \\\\
    \\hline""".format(mname,fname.strip('.xyz')))

    for atom in range(0,len(xyz)):
        o.write("""\n\t{} & {} & {} & {} \\\\""".format(xyz[atom][0],xyz[atom][1],xyz[atom][2],xyz[atom][3]))

    o.write("""
    \\hline
    \\hline
    \\end{tabular}
\\end{table}\n""")

