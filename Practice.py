import enchant
test = input("Ask: ")
d = enchant.Dict("en_Au")
print(d.check(test))
