
def banner(message, length, header='=', footer='-'):
    print()
    print(header * length)
    print(message)
    print(footer * length)


def banner_v2(length, footer='*'):
    print(footer * length)
    print()
