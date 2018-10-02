def areaRectangle(length,breadth):
    
    return (length * breadth)

def main():
   
    length = int(input("Enter the length : "))
    breadth = int(input("Enter the breadth : "))
    area = areaRectangle(length,breadth)
    print('The area is : ',area)

if __name__ == '__main__':
    main()