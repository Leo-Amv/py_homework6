# Все равны, как на подбор

values = [i for i in range(20) if i % 2 == 0]
qubes = [i**3 for i in range(10) if i % 3 != 0]

print(values)
print(qubes)


def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('defferent')
