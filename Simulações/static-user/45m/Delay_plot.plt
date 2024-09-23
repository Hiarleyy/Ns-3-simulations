set terminal pdf
set output "Data_Delay.pdf"
set title "Taxa de Delay"
set xlabel "time"
set ylabel "db"
plot "DlRlcStats-100Ghz.txt" using 1:12 with linespoint title "Delay" lw 0.2 lc "blue"

