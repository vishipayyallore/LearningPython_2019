vars = locals()
print(f'Locals -> {vars}')

details = dict(vars)
for local in details:
    print(f'{local} == {details[local]}  ')