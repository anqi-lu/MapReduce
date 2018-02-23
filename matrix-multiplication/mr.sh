cat matrix_m.txt matrix_n.txt | ./mapper.py | sort -k1,2 | ./reducer.py > output.txt

