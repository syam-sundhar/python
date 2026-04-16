def main():
    l,b=get_vales()
    area=calculate_area(l,b)
    display(area)
def get_vales():    
    l=int(input("Enter the length: "))
    b=int(input("Enter the breadth: "))
    return l,b
def calculate_area(l,b):
    return l*b
def display(area):
    print("Area of rectangle is: ",area)
main()