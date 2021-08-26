classes = []    

course=input('Enter the name of the class: ')
while course:
    classes.append(course)
    course=input('Enter the name of the class: ')

print('list of classes')

for index, subj in enumerate(classes):
    print(index+1, subj)
