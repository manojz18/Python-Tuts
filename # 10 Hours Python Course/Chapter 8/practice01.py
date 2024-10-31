# Find the gratest number among three

def greatest(a, b, c):
    if(a > b and a > c):
        return a
    
    elif(b > a and b > c):
        return b
    
    else:
        return c
    

ans = greatest(10, 15, 20)

print(ans)