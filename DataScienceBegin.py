import numpy as np
dataType = [('name' , "S15") , ("class" , int) , ("height" , float)]
studentsDetails = [('James' , 5 , 48.5) , ("Nail" , 6 , 52.5) , ("Paul" , 5 , 42.10) , ("pit" , 5 , 40.11)]
students = np.array(studentsDetails , dtype = dataType) 
print("Original array :")
print(students)
print("Sort by height")
print(np.sort(students , order = "height"))
