def genTriangle(s):
   
    print('     ',s)
    print('    ',s,s)
    print('   ',s,s,s)
    print('  ',s,s,s,s)
    print(' ',s,s,s,s,s)
    print('',s,s,s,s,s,s)


def main():
   

    s = input("Input a symbol : ")
    genTriangle(s)


if __name__ == "__main__":
    main()