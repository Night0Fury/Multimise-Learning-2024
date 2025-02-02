#   1:
eng_marks = {}
eng_marks.update({'Harsh': 99, 'Aadhi': 50, 'Karunesh': 15, 'Sam': 19})

print("eng_marks =", eng_marks)

#   2: 
lang_marks = {'Harsh': 100,'Aadhi': 50,'Karunesh': 90,'Sam': 50}
print("\nlang_marks =", lang_marks)

#   3:
actual_marks = []
actual_marks.append(eng_marks)
actual_marks.append(lang_marks)

print("\nactual_marks =", actual_marks)

#   4:
totalMarks = [eng_marks[name] + lang_marks[name] for name in eng_marks]
print("\ntotalMarks =", totalMarks)

#   5:
names = list(eng_marks.keys())  # Extract names from eng_marks
subjects = ['Eng', 'Lang', 'Total']
list_of_name_sub_tot = [(name, subjects[0], subjects[1], subjects[2]) for name in names]
print("\nlist_of_name_sub_tot =", list_of_name_sub_tot)

#   6: 
class_marks = {
    list_of_name_sub_tot[i]: [eng_marks[names[i]], lang_marks[names[i]], totalMarks[i]]
    for i in range(len(names))
}

print("\nclass_marks =", class_marks)

#   7: 
for key in class_marks:
    total = class_marks[key][2]
    if total > 120:
        feedback = "Kutty Pattas"
    elif total > 100:
        feedback = "Good Student"
    else:
        feedback = "Slow Bloomer"
    class_marks[key].append(feedback)

print("\nclass_marks =", class_marks)
