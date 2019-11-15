from easygui import msgbox, multenterbox

fieldNames = ["firstAngle", "secondAngle", "thirdAngle"]

tnum= int(input("Enter the number of triangles will be shown: "))
i=0
while i<tnum:

    fieldValues = list(multenterbox(msg='Fill in values for the fields.', title='Enter', fields=(fieldNames)))
    if(int(fieldValues[0]) + int(fieldValues[1]) + int(fieldValues[2]) != 180):
        result="Not a valid input"
    elif(fieldValues[0]==fieldValues[1] and fieldValues[1]==fieldValues[2]):
        result="equilateral"
    elif(fieldValues[0]==fieldValues[1] or fieldValues[1]==fieldValues[2] or fieldValues[0]==fieldValues[2]):
        result="isosceles"
    else:
        result="scalene"
 
    msgbox(msg=(result), title = "Results")
    print(str(i+1)+". triangle succesfully shown")
    i+=1


