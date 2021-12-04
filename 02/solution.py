with open("input.txt") as f:
    lines = f.readlines()

# part 1
from functools import reduce
from operator import add
print(-1 * reduce(lambda e1, e2: e1*e2, reduce(lambda l1, l2: list(map(add, l1, l2)), map(lambda words: [(words[0]=="forward") * int(words[1]), ((words[0]=="up") + (-1 * (words[0]=="down"))) * int(words[1])], map(lambda line: line.split(), lines)))))

# part 2
## cant be solved with one liner
