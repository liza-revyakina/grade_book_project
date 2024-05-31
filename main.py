# Были добавлены методы, которых не было в задании. Они нужны для работы требуемых методов.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Перегрузка метода
    def __str__(self):
        output = (f"Имя: {self.name}\n"
                  f"Фамилия: {self.surname}\n"
                  f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                  f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                  f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return output

    # Методы добавления курсов (в процессе и завершенных)
    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Метод для оценки лектора
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached and grade in range(1, 11)):
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'

    # Метод, определяющий среднюю оценку студента по всем курсам
    def average_grade(self):
        for keys, values in self.grades.items():
            return sum(values) / len(values)

    # Метод, определяющий среднюю оценку студента для конкретного курса (нужен для определения балла всех студентов)
    def average_course_grade(self, course):
        values = []
        for value in self.grades.get(course):
            values.append(value)
        return sum(values) / len(values)

    # Методы для сравнения экземпляра класса (студента) с другим экземпляром класса (студентом)
    def __gt__(self, student2):
        return self.average_grade() > student2.average_grade()

    def __lt__(self, student2):
        return self.average_grade() < student2.average_grade()

    def __eq__(self, student2):
        return self.average_grade() == student2.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Метод для добавления закрепленных курсов, наследуемый всеми подклассами
    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Перегрузка метода
    def __str__(self):
        output = (f"Имя: {self.name}\n"
                  f"Фамилия: {self.surname}")
        return output

    # Метод для оценки домашней работы
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress and grade in range(1, 11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    # Перегрузка метода
    def __str__(self):
        output = (f"Имя: {self.name}\n"
                  f"Фамилия: {self.surname}\n"
                  f"Средняя оценка за лекции: {self.average_grade()}")
        return output

    # Метод, определяющий среднюю оценку лектора по всем курсам
    def average_grade(self):
        for keys, values in self.grades_for_lectures.items():
            return sum(values) / len(values)

    # Метод, определяющий среднюю оценку лектора для конкретного курса (нужен для определения балла всех студентов)
    def average_course_grade(self, course):
        values = []
        for value in self.grades_for_lectures.get(course):
            values.append(value)
        return sum(values) / len(values)

    # Методы для сравнения экземпляра класса (лектора) с другим экземпляром класса (лектором)
    def __gt__(self, lecturer2):
        return self.average_grade() > lecturer2.average_grade()

    def __lt__(self, lecturer2):
        return self.average_grade() < lecturer2.average_grade()

    def __eq__(self, lecturer2):
        return self.average_grade() == lecturer2.average_grade()


# Функция для определения среднего балла всех лекторов за конкретный курс
def average_lectors_grade(all_lecturers, course):
    all_grades = []
    for lecture in all_lecturers:
        all_grades.append(lecture.average_course_grade(course))
    return sum(all_grades) / len(all_grades)


# Функция для определения среднего балла всех студентов за конкретный курс
def average_students_grade(all_students, course):
    all_students_grades = []
    for student in all_students:
        all_students_grades.append(student.average_course_grade(course))
    return sum(all_students_grades) / len(all_students_grades)

# Тесты

# Создание экземпляров
some_reviewer = Reviewer("Some", "Buddy")
other_reviewer = Reviewer("Another", "Reviewer")

some_lecturer = Lecturer("One", "Lecturer")
other_lecturer = Lecturer("Other", "Person")

some_student = Student("Ruoy", "Eman", "your_gender")
other_student = Student("Liza", "Revyakina", "female")

# Добавление курсов в списки
some_lecturer.add_courses("Математика")
other_lecturer.add_courses("Математика")
some_student.add_courses("Математика")
other_student.add_courses("Математика")
some_student.add_finished_courses("Литература")
other_student.add_finished_courses("Биология")
some_reviewer.add_courses("Математика")
other_reviewer.add_courses("Математика")

# Проверка списков
print(f"\nСписки курсов")
print(f"Закрепленные курсы лектора: {some_lecturer.courses_attached}")
print(f"Курсы студента в процессе: {some_student.courses_in_progress}")
print(f"Завершенные курсы студента: {some_student.finished_courses}")
print(f"Закрепленные курсы проверяющего: {some_reviewer.courses_attached}")

# Добавление оценок лекторам
some_student.rate_lecture(some_lecturer, "Математика", 10)
some_student.rate_lecture(some_lecturer, "Математика", 8)
other_student.rate_lecture(other_lecturer, "Математика", 8)
other_student.rate_lecture(other_lecturer, "Математика", 8)

# Проверка оценок
print(f"\nСписки оценок лекторов")
print(f"Оценки лектора {some_lecturer.name} {some_lecturer.surname}: {some_lecturer.grades_for_lectures}")
print(f"Оценки лектора {other_lecturer.name} {other_lecturer.surname}: {other_lecturer.grades_for_lectures}")

# Добавление оценок студентам
some_reviewer.rate_hw(some_student, "Математика", 8)
some_reviewer.rate_hw(some_student, "Математика", 6)
other_reviewer.rate_hw(other_student, "Математика", 7)
other_reviewer.rate_hw(other_student, "Математика", 9)

# Проверка оценок
print(f"\nСписки оценок студентов")
print(f"Оценки студента {some_student.name} {some_student.surname}: {some_student.grades}")
print(f"Оценки студента {other_student.name} {other_student.surname}: {other_student.grades}")

# Переменная для тестирования на основе одного добавленного курса
current_course = "Математика"

# Проверка метода, выводящего средний балл
print(f"\nСредний балл студентов")
print(f"Средний балл студента {some_student.name} {some_student.surname} "
      f"за курс {current_course}: {some_student.average_course_grade(current_course)}")
print(f"Средний балл студента {other_student.name} {other_student.surname} "
      f"за курс {current_course}: {other_student.average_course_grade(current_course)}")

print(f"\nСредний балл лекторов")
print(f"Средний балл лектора {some_lecturer.name} {some_lecturer.surname} "
      f"за курс {current_course}: {some_lecturer.average_course_grade(current_course)}")
print(f"Средний балл лектора {other_lecturer.name} {other_lecturer.surname} "
      f"за курс {current_course}: {other_lecturer.average_course_grade(current_course)}")


# Проверка функции для подсчета среднего балла в рамках курса
lecturers = [some_lecturer, other_lecturer]
print(f"\nСредние баллы за курс")
print(f"Средний балл всех лекторов на курсе {current_course}: {average_lectors_grade(lecturers, current_course)}")

students = [some_student, other_student]
print(f"Средний балл всех студентов на курсе {current_course}: {average_students_grade(students, current_course)}")

# Проверка перегруженного метода __str__
print(f"\nИнформация о студентах")
print(f"\n{some_student}")
print(f"\n{other_student}")
print(f"\nИнформация о лекторах")
print(f"\n{some_lecturer}")
print(f"\n{other_lecturer}")
print(f"\nИнформация о проверяющих")
print(f"\n{some_reviewer}")
print(f"\n{other_reviewer}")

# Проверка перегруженных методов сравнение
print(f"\nУ {some_student.name} {some_student.surname} средний балл выше, "
      f"чем у {other_student.name} {other_student.surname}?")
print(some_student > other_student)
print(f"\nУ {some_lecturer.name} {some_lecturer.surname} средний балл выше, "
      f"чем у {other_lecturer.name} {other_lecturer.surname}?")
print(some_lecturer > other_lecturer)
print(f"\nУ {some_student.name} {some_student.surname} средний балл ниже, "
      f"чем у {other_student.name} {other_student.surname}?")
print(some_student < other_student)
print(f"\nУ {some_lecturer.name} {some_lecturer.surname} средний балл ниже, "
      f"чем у {other_lecturer.name} {other_lecturer.surname}?")
print(some_lecturer < other_lecturer)
print(f"\nУ {some_student.name} {some_student.surname} средний балл равен "
      f"{other_student.name} {other_student.surname}?")
print(some_student == other_student)
print(f"\nУ {some_lecturer.name} {some_lecturer.surname} средний балл равен "
      f"{other_lecturer.name} {other_lecturer.surname}?")
print(some_lecturer == other_lecturer)
