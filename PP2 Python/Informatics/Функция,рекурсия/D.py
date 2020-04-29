def pad(x, y):
    if abs(x) < 1 and abs(y) < 1:
        return True
    return False
def IsPointInSquare(x,y):
    if pad(x, y):
        return 'YES'
    return'NO'
x = float(input())
y = float(input())
print( IsPointInSquare(x,y) )
