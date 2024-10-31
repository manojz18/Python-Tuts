def printing(n):
    if(n == 0):
        return
    print(f"*"*(n))
    printing(n-1)


printing(5)