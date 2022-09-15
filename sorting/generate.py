import sys
import random
from typing import final

# generate.py word 15 5 6

if __name__ == "__main__": # generate lists of random numbers
    if len(sys.argv) != 5:
        sys.exit("Usage: %s unit max_num max_len data_size" % sys.argv[0])
    unit = sys.argv[1] # unit
    max_num = int(sys.argv[2]) # maximum number
    max_len = int(sys.argv[3]) # maximum sequence lengh
    min_len = max_len - 1 # minimum sequence length (Ηταν 1)
    data_size = int(sys.argv[4]) # data size
    nums = range(0, max_num + 1)

    if unit == "word":
        z = 0
        pl = dict()
        while True:
            x = tuple(random.sample(nums, random.randint(min_len, max_len)))
            if x in pl:
                continue
            pl[x] = True
            y = sorted(range(len(x)), key = lambda i: x[i])
            final = "%s\t%s" % (" ".join(map(str, x)), " ".join(map(str, y)))
            # write variable contents to a file in the format of "x\ty"
            with open("data.txt", "a") as f:
                # write variable contents to a file
                f.write(final + "\n")
            z += 1
            if z >= data_size:
                break

    if unit == "sent":
        for z0 in range(data_size):
            z1 = random.randint(1, max_len)
            seq = []
            while True:
                x = random.sample(min_len, random.randint(1, max_len))
                if sum(x) in map(sum, seq): # same sums not allowed
                    continue
                seq.append(x)
                if len(seq) == z1:
                    break
            idx = sorted(range(len(seq)), key = lambda x: sum(seq[x]))
            if z0:
                print()
            for x, y in zip(seq, idx):
                print(" ".join(map(str, x)) + "\t%d" % y)
