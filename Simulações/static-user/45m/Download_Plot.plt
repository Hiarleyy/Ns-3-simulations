set terminal pdf
set output "Data_Download.pdf"
set title "Taxa de Sinal"
set xlabel "time"
set ylabel "db"
plot "RxPacketTrace100Ghz.txt" using 2:14 with linespoint title "Sinr" lw 0.2 lc "red"

