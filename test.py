from string import Formatter

mystr = "how do {you} true this {on}"
fieldnames = [fname for _, fname, _, _ in Formatter().parse(mystr) if fname]
fieldvalues = ["replace_you", "replace_on"]
d = dict(zip(fieldnames, fieldvalues))
print(mystr.format(**d))
