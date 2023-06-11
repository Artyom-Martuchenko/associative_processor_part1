class Memory:
    memory = []
    def __init__(self, numbers):
        self.memory = []
        for i in range(len(numbers)):
            self.memory.append(self.toBinary(numbers[i]))


    def sort1(self, number, kind):
        number = self.toBinary(number)
        if kind == 'up':
            result = ['1'] * 16
            for i in range(len(self.memory)):
                if self.comparison(self.memory[i], number) == 'similiar':
                    return self.memory[i]
                elif self.comparison(self.memory[i], number) and self.comparison(result, self.memory[i]):
                    result = self.memory[i]
        else:
            result = ['0'] * 16
            for i in range(len(self.memory)):
                if self.comparison(self.memory[i], number) == 'similiar':
                    return self.memory[i]
                if self.comparison(number, self.memory[i]) and self.comparison(self.memory[i], result):
                    result = self.memory[i]
        return result

    def sort2(self, number):
        number = self.toBinary(number)
        result = 0
        res_counter = 0
        for i in range(len(self.memory)):
            counter = 0
            for j in range(len(number)):
                if self.memory[i][j] == number[j]:
                    counter += 1
            if counter >= res_counter:
                result = self.memory[i]
                res_counter = counter
        return result

    def comparison(self, A, B):
        result = 'similiar'
        for i in range(len(A)):
            if A[i] == '1' and B[i] == '0':
                return True
            elif A[i] == '0' and B[i] == '1':
                return False
        return result

    def toBinary(self, number):
        result = list(bin(number))
        del result[1]
        del result[0]
        while len(result) < 16:
            result.insert(0, '0')
        return result

    def getMatrix(self):
        for i in range(len(self.memory)):
            string = ''.join(self.memory[i])
            for j in range(len(string)):
                print(string[j], end=' ')
            print('')





if __name__ == '__main__':
    # Мартюченко Артем 121701
    res = Memory([255, 6212, 2341, 23421, 7593, 20, 1234, 8139, 50000, 1, 42690, 15278, 32190, 1313, 24458, 36423])
    enter1 = 8000
    result1 = ''.join(res.sort1(enter1, 'up'))
    print(f'Ввод для поиска по ближайшему сверху: {enter1}')
    enter1 = ''.join(res.toBinary(enter1))
    print(f'Ввод для поиска по ближайшему сверху: {enter1}')
    print(f'Результат поиска по ближайшему сверху: {result1} или {int(result1, 2)}')

    print('-'*100)

    enter2 = 8000
    result2 = ''.join(res.sort1(enter2, 'down'))
    print(f'Ввод для поиска по ближайшему снизу: {enter2}')
    enter2 = ''.join(res.toBinary(enter2))
    print(f'Ввод для поиска по ближайшему снизу: {enter2}')
    print(f'Результат поиска по ближайшему снизу: {result2} или {int(result2, 2)}')

    print('-' * 100)

    enter3 = 15000
    result3 = ''.join(res.sort2(enter3))
    print(f'Ввод для поиска по соответствию: {enter3}')
    enter3 = ''.join(res.toBinary(enter3))
    print(f'Ввод для поиска по соответствию: {enter3}')
    print(f'Результат поиска по соответствию: {result3} или {int(result3, 2)}')
    print('Matrix:')
    res.getMatrix()