add=lambda *a:sum(a)
sub=lambda a,b:a-b
mul=lambda *a:eval('*'.join(map(str,a)))
div=lambda a,b:a/b
fact=lambda n:1 if n==0 else n*fact(n-1)

if __name__ == "__main__":
    print("This only runs if you execute tools.py directly!")
