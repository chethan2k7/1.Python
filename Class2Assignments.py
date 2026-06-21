class AllFunctions():
    def Subfields():            
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")

    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print("is Even number")
            message="is Even number"
        else:
            print("is Odd number")
            message="is Odd number"


    def Eligible():

        gender = input("Enter Gender (Male/Female): ")
        age = int(input("Enter Age: "))
        if gender == "Male":
            if age >= 21:
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")
            
        elif gender == "Female":
            if age >= 18:
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")
    
        else:
            print("Invalid Gender")

    
    def percentage(Subj1,Subj2,Subj3,Subj4,Subj5):
        Total=(Subj1+Subj2+Subj3+Subj4+Subj5)
        print("Total:",Total)
        percentage=(Subj1+Subj2+Subj3+Subj4+Subj5)/5
        print ("Percentage:", percentage)

    
    def trianglePerimeter(Height1,Height2,Breadth):
        perimeter=Height1+Height2+Breadth
        return perimeter

    def triangleArea(Height,Breadth):
        Area=(Height*Breadth)/2
        return Area
    
     