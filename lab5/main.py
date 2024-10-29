class Matrix:
    def __init__(self, array):
        self.array = array

    def inverse(self):
        n = len(self.array)
        inverse = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        augmented = [self.array[i] + inverse[i] for i in range(n)]

        for i in range(n):
            if augmented[i][i] == 0:
                for j in range(i + 1, n):
                    if augmented[j][i] != 0:
                        augmented[i], augmented[j] = augmented[j], augmented[i]
                        break
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot
            for j in range(n):
                if i != j:
                    factor = augmented[j][i]
                    for k in range(2 * n):
                        augmented[j][k] -= factor * augmented[i][k]

        inverse_matrix = [row[n:] for row in augmented]
        return Matrix(inverse_matrix)

    def __add__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Dimensions are wrong!")
        return Matrix(
            [[self.array[i][j] + other.array[i][j] for j in range(len(self.array[0]))] for i in range(len(self.array))]
        )

    def __sub__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Dimensions are wrong!")
        return Matrix(
            [[self.array[i][j] - other.array[i][j] for j in range(len(self.array[0]))] for i in range(len(self.array))]
        )

    def __mul__(self, other):
        if len(self.array[0]) != len(other.array):
            raise ValueError("Dimensions are wrong!")
        result = [[0] * len(other.array[0]) for _ in range(len(self.array))]
        for i in range(len(self.array)):
            for j in range(len(other.array[0])):
                for k in range(len(other.array)):
                    result[i][j] += self.array[i][k] * other.array[k][j]
        return Matrix(result)

    def LUP(self):
        n = len(self.array)
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]
        P = list(range(n))

        for i in range(n):
            max_index = i
            max_value = abs(self.array[i][i])
            for k in range(i + 1, n):
                if abs(self.array[k][i]) > max_value:
                    max_value = abs(self.array[k][i])
                    max_index = k

            if max_index != i:
                P[i], P[max_index] = P[max_index], P[i]
                self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

        for i in range(n):
            for j in range(i, n):
                U[i][j] = self.array[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            for j in range(i + 1, n):
                if U[i][i] == 0:
                    raise ValueError()
                L[j][i] = (self.array[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
            L[i][i] = 1.0

        return L, U, P


def lup_solve(matrix, b):
    L, U, P = matrix.LUP()
    n = len(L)
    P = [[1 if j == P[i] else 0 for j in range(n)] for i in range(n)]
    P = Matrix(P)
    L = Matrix(L)
    U = Matrix(U)
    b = Matrix([[value] for value in b])

    y = L.inverse() * (P * b)
    x = U.inverse() * y

    x_flat = [int(round(row[0], 10)) for row in x.array]
    return x_flat


m = [
    [4, -5, 2],
    [3, -3, 2],
    [2, -3, 1],
]

b = [1, 2, 3]

mat = Matrix(m)
l = lup_solve(mat, b)
print(l)