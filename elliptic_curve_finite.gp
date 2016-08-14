#
# generate data file with python elliptic_curve_finite.py > elliptic_curve_finite.out
#
# plot using 
# gunplot elliptic_curve_finite.gp
#
##set term png
##set output "elliptic_curve_finite.png"
#
#  Fields in each record are separated by commas.
#
set datafile separator ","

set title "solutions to elliptic curve at 67"
set xlabel "x"
set xrange [0:66]
set yrange [0:66]
set ylabel "y"
set grid
set timestamp
#
# lines connecting (2,22) and (6,25)
# rc = 3/4
#
plot    (x - ( 2      ) )*3/4 + 22      lc 'black', \
	(x - ( 2      ) )*3/4 + 22 - 67 lc 'black', \
	(x - ( 2 - 67 ) )*3/4 + 22 - 67 lc 'black', \
	(x - ( 2 + 67 ) )*3/4 + 22      lc 'red', \
	(x - ( 2 + 67 ) )*3/4 + 22 + 67 lc 'red', \
'elliptic_curve_finite.out' lc 'red'

pause -1
