from pathlib import Path

path = Path("./DataStore")
print(path.exists())

path = Path("./DataStore1")
print(path.exists())

if(not path.exists()):
    path.mkdir()

if(path.exists()):
    path.rmdir()

path = Path("./DataStore")
for item in path.glob('*'):
    print(type(item))
    print(item)