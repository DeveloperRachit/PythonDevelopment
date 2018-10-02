def areaTriangle(base,height):
  
    return ((base*height)/2)

def main():
    
    base = int(input('Enter the base : '))
    height = int(input('Enter the height : '))
    print('The area is : ',areaTriangle(base,height))

if __name__ == '__main__':
    main()