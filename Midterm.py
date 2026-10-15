#Goodness Dikeocha

#Problem 1: Course Gradebook (Dictionaries)
class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        if student not in self.grades:
            self.grades[student] = {}

        self.grades[student][assignment] = score

    def student_average(self, student):
        if student not in self.grades:
            return None

        scores = self.grades[student]

        if len(scores) == 0:
            return None

        total = sum(scores.values())
        return total / len(scores)

    def assignment_average(self, assignment):
        scores = []

        for student in self.grades:
            if assignment in self.grades[student]:
                scores.append(self.grades[student][assignment])

        if len(scores) == 0:
            return None

        return sum(scores) / len(scores)

    def top_students(self, n):
        averages = []

        for student in self.grades:
            average = self.student_average(student)

            if average is not None:
                averages.append((student, average))

        averages.sort(key=lambda item: item[1], reverse=True)

        result = []

        for student, average in averages[:n]:
            result.append(student)

        return result

    def missing(self, assignment):
        result = []

        for student in self.grades:
            if assignment not in self.grades[student]:
                result.append(student)

        result.sort()
        return result


# Test cases
gb = Gradebook()
gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75)

print(gb.student_average("Alice"))
print(gb.student_average("Bob"))
print(gb.student_average("Zed"))
print(gb.assignment_average("hw1"))
print(gb.assignment_average("hw9"))
print(gb.top_students(2))
print(gb.missing("hw2"))


#Problem 5: Polynomial Class with Operator Overloading (OOP — Magic Methods)

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        result = ""

        for i in range(len(self.coefficients) - 1, -1, -1):
            n = self.coefficients[i]

            if n == 0:
                continue

            if i == 0:
                term = str(n)
            elif i == 1:
                if n == 1:
                    term = "x"
                elif n == -1:
                    term = "-x"
                else:
                    term = str(n) + "x"
            else:
                if n == 1:
                    term = "x^" + str(i)
                elif n == -1:
                    term = "-x^" + str(i)
                else:
                    term = str(n) + "x^" + str(i)

            if result == "":
                result = term
            elif n > 0:
                result += " + " + term
            else:
                result += " - " + term.lstrip("-")

        return result if result else "0"

    def __repr__(self):
        return "Polynomial(" + str(self.coefficients) + ")"

    def __len__(self):
        return len(self.coefficients)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.coefficients):
            return 0
        return self.coefficients[index]

    def __call__(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)
        return result

    def __add__(self, other):
        result = []
        size = max(len(self), len(other))

        for i in range(size):
            result.append(self[i] + other[i])

        return Polynomial(result)

    def __mul__(self, number):
        result = []
        for coefficient in self.coefficients:
            result.append(coefficient * number)
        return Polynomial(result)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


# Run all test cases below the class
p = Polynomial([1, 2, 3])
q = Polynomial([0, 1])

print(p)
print(q)
print(repr(p))
print(len(p))
print(p[2], p[7])
print(p(2))
print(q(5))

r = p + q
print(r)
print(p * 2)
print(p == Polynomial([5, 0, 1]))
print(q < p)
