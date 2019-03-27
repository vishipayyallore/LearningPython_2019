
def banner(message, length, header='=', footer='-'):
    print()
    print(header * length)
    print((' ' * (length//2 - len(message)//2)), message)
    print(footer * length)


def banner_v2(length, footer='*'):
    print(footer * length)
    print()
