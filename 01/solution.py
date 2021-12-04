# part 1
with open("input.txt") as f:
    lines = f.readlines()
l = list(map(lambda l:int(l.rstrip()), lines))
print(sum(map(lambda i:1 if l[i] > l[i-1] else 0, range(1, len(l)))))

# part 2
l_windows = list(map(lambda i:l[i-2] + l[i-1] + l[i], range(2, len(l))))
greater_than_previous= map(lambda i:1 if l_windows[i] > l_windows[i-1] else 0, range(1, len(l_windows)))
print(sum(greater_than_previous))
