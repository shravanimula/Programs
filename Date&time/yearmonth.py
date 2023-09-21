from datetime import *
x=datetime.now()
print(x)
print(x.strftime('%A')) #day full version
print(x.strftime('%a')) #day short version

print(x.strftime('%Y')) #year full version
print(x.strftime('%y')) #year short version

print(x.strftime('%B')) #month full version
print(x.strftime('%b')) #month short version
