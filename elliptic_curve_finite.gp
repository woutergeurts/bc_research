#
# generate data file with python elliptic_curve_finite.py > elliptic_curve_finite.out
#
# plot using gnuplot
# >> load 'elliptic_curve_finite.gp'
#
set term png
set output "elliptic_curve_finite.png"
#
#  Fields in each record are separated by commas.
#
set datafile separator ","

set title "solutions to elliptic curve at 67"
set xlabel "x"
set ylabel "y"
set grid
set timestamp
plot 'elliptic_curve_finite.out' 
