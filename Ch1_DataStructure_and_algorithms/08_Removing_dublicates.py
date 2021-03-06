"""
    Задача: мы хотим удалить дублирующиеся значения из последовательности, но при этом сохранить порядок следования
    оставшихся элементов.
"""


def dedupe(items):
    """Элементы последовательности должны быть хешируемыми"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
for i in dedupe(a):
    print(i)
print(list(dedupe(a)))


def unhashable_dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
]
print(list(unhashable_dedupe(b, key=lambda d: (d['x'], d['y']))))
print(list(unhashable_dedupe(b, key=lambda d: d['x'])))
