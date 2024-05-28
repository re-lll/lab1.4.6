class Polynom:
    def __init__(self, coefficients=None):
        if coefficients is None:
            coefficients = {}
        self.coefficients = coefficients

    @classmethod
    def from_input(cls):
        coefficients = {}
        while True:
            try:
                line = input("введіть степінь та коефіцієнт (або '0' для завершення): ")
                if line.strip().lower() == '0':
                    break
                degree, coefficient = map(int, line.split())
                coefficients[degree] = coefficient
            except ValueError:
                print("введіть степінь та коефіцієнт розділені пробілом.")
        return cls(coefficients)

    @classmethod
    def from_file(cls, filename):
        coefficients = {}
        with open(filename, 'r') as file:
            for line in file:
                try:
                    parts = line.split()
                    degree = int(parts[0])
                    coefficient = int(parts[1])
                    coefficients[degree] = coefficient
                except:
                    print("некоректний рядок", line.strip())
        return cls(coefficients)

    def __string__(self):
        terms = []
        for degree in sorted(self.coefficients.keys(), reverse=True):
            coefficient = self.coefficients[degree]
            if coefficient != 0:
                if degree == 0:
                    terms.append(str(coefficient))
                elif degree == 1:
                    terms.append(f"{coefficient}x")
                else:
                    terms.append(f"{coefficient}x^{degree}")
        return " + ".join(terms).replace("+ -", "- ")

    def evaluate(self, x):
        result = 0
        for degree in self.coefficients:
            coefficient = self.coefficients[degree]
            result += coefficient * (x ** degree)
        return result

    def add(self, other):
        result_coeffs = self.coefficients.copy()
        for degree in other.coefficients:
            if degree in result_coeffs:
                result_coeffs[degree] += other.coefficients[degree]
            else:
                result_coeffs[degree] = other.coefficients[degree]
        return Polynom(result_coeffs)

    def subtract(self, other):
        result_coeffs = self.coefficients.copy()
        for degree in other.coefficients:
            if degree in result_coeffs:
                result_coeffs[degree] -= other.coefficients[degree]
            else:
                result_coeffs[degree] = -other.coefficients[degree]
        return Polynom(result_coeffs)

    def multiply(self, other):
        result_coeffs = {}
        for degree1 in self.coefficients:
            for degree2 in other.coefficients:
                degree = degree1 + degree2
                coefficient = self.coefficients[degree1] * other.coefficients[degree2]
                if degree in result_coeffs:
                    result_coeffs[degree] += coefficient
                else:
                    result_coeffs[degree] = coefficient
        return Polynom(result_coeffs)

def main():

    P1 = Polynom.from_file('input01.txt')
    P2 = Polynom.from_file('input02.txt')

    q = P1.add(P2.multiply(P1)).subtract(P2)
    h = P2.multiply(P1.subtract(P2).multiply(P1.subtract(P2)))

    while True:
        try:
            x = float(input("введіть значення x: "))
            break
        except ValueError:
            print("невірний ввід, введіть числове значення.")

    q_value = q.evaluate(x)
    h_value = h.evaluate(x)

    print(f"q({x}) = {q_value}")
    print(f"h({x}) = {h_value}")

    with open('output.txt', 'w') as file:
        file.write(f"{q_value}\n")
        file.write(f"{h_value}\n")

if __name__ == "__main__":
    main()
