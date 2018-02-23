import random

def generate():
    sz = 10000
    mu = 0.0
    sigma = 1.0
    my_dir = ''  # Change this line to suit your environment
    random.seed(314159)               # Do Not change this line
    with open(my_dir+'matrix_m.txt', 'w') as f:
        with open(my_dir+'matrix_n.txt', 'w') as g:
            for i in range(sz):
                for j in range(sz):
                    x = random.randint(0,500)
                    if x == 0:
                        mval = random.gauss(mu,sigma)
                        f.writelines('\t'.join(['M', str(i), str(j), str(mval)])+'\n')
                    if x == 1:
                        nval = random.gauss(mu,sigma)
                        g.writelines('\t'.join(['N', str(i), str(j), str(nval)])+'\n')

if __name__ == "__main__":
    generate()

