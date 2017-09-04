a = {"cars": 1, "houses": 2, "schools": 3, "stores": 4}
b = {"Pens": 1, "Pencils": 2, "Paper": 3}

a.update(b)
print(a)

subkeys = ["cars", "Pencils"]
subdict = {x: a[x] for x in a if x in subkeys}

print(subdict)

