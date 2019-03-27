def inventory(category, *items):
    print("%s [items=%d]:" % (category, len(items)), items)
    for item in items:
        print("-", item)
    return

inventory('Electronics', 'tv', 'lcd', 'ac', 'refrigerator', 'heater')
inventory('Books', 'python', 'java', 'c', 'c++')

inventory('Books', ['python', 'java', 'c', 'c++'], ('python', 'java', 'c', 'c++'), 10, 'Azim')
