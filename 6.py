student_number=10
x=[2,-3,0,5,-7,9,-11,0,4,10]
M=5
#Створення нового масиву Y
Y=[element for element in x if abs(element)> M]
#Виведення результатів 
print(f"Число M: {M}")
print(f"заданий масив x: {x}") 
print(f"отриманий масив Y: {Y}")

