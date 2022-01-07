import numpy

lst = [
    {"January": 2200},
    {"February": 2350},
    {"March": 2600},
    {"April": 2130},
    {"May": 2190}

]
h = len(lst)
# jan-2200,feb-2350,mar-2600,april-2130,may-2190
print(lst[1]["February"]-lst[0]["January"])
m = []
for i in range(3):
    m += list(lst[i].values())

print(sum(m))
for i in range(h):
    k = lst[i].values()
    if k == 2000:
        print("spent 2000", lst[i])
else:
    print("never spent 2000")
lst.append({"June": 1980})
k = list(lst[3].values())
print(*k)







