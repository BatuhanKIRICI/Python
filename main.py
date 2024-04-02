student_heights = input().split()
print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

print(round(total_height / (len(student_heights))))
