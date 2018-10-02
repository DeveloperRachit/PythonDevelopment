def computePercentage(maxMarks,obtMarks):
    
    #Approach : Divide obtMarks by maxMarks and multiply by 100

    percentage = obtMarks / maxMarks * 100

    return percentage
    

def main():
   

    maxMarks = int(input("Enter Maximum marks : "))
    obtMarks = int(input("Enter marks obtained : "))
    print("Percentage : ",computePercentage(maxMarks,obtMarks))


if __name__ == "__main__":
    main()

    
    