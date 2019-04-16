
def string_strip(stringvalue: str):
    return "".join(stringvalue.split())


def string_mask(stringvalue: str):
    for char in stringvalue:
        print(ord(char), end=' | ')
