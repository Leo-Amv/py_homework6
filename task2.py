# Мимикрия
def transformation(x): return x
# transformation = lambda x : x


values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda x: x, values))
result = list(map(transformation, values))
if values == transformed_values == result:
    print('ok')
else:
    print('fail')
