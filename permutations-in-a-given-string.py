import itertools

word = input()

print(" ".join(map(str, ["".join(j) for j in itertools.permutations([i for i in word],len(word))])))

# I really like one-liners

# input:  ABC
# output: ABC ACB BAC BCA CAB CBA
