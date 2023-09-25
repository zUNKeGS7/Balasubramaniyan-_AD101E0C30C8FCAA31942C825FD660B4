class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Amernath","CS01",6.5),
    Student("Aravind S","CS02",8.9),
    Student("Bala Murugan", "CS03", 7.8),
    Student("BALASUBRAMANIYAN M", "CS04", 7.7),
    Student("GOKULAN V", "CS05", 8.7),
    Student("GOWRI SHANKAR T", "CS06", 9.7),
    Student("G. HARIKARISHNAN", "CS07", 7.5),
    Student("KAVIDASS P", "CS08", 7.3),
    Student("KESAVAN J", "CS09", 5.3),
    Student("MOHAMED YUSUF J", "CS010", 6.3),
    Student("MUTHU V", "CS011", 8.3),
    Student("MUTHUKUMAR P", "CS012", 8.4),
    Student("NAVEEN KUMAR. G", "CS014", 7.4),
    Student("R. SANTHOSH ", "CS015", 7.1),
    Student("SURESHKUMAR R ", "CS016", 7.7),
    Student("VARUNKUMAR  ", "CS018", 5.7),
    Student("VETTAI R", "CS019", 8.7),
    Student("VIJAYAN S", "CS020", 8.2),
    Student("YOGESHWARAN V", "CS021", 7.2),
    Student("JEEVAJOTHI A", "CS022", 7.8),
    Student("KALAIVANI.M", "CS023", 8.8),
    Student("KAVITHA R ", "CS024", 9.8),
    Student("PRITHEESHA M ", "CS026", 8.2),
    Student("SELVAPRIYA V ", "CS027", 8.0),
    Student("SUBIKSHA M ", "CS029", 8.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))