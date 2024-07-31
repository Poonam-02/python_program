'''Real FizzBuzz
The problem
Please write code delivering the requirements of the steps that follow. The requirements don’t
mention a command line application, and we are not looking for one. Do write code that you would
be happy delivering to a paying client.
Step 1:
Write a class that produces the following for any contiguous range of integers:
● the number
● ‘fizz’ for numbers that are multiples of 3
● ‘buzz’ for numbers that are multiples of 5
● ‘fizzbuzz’ for numbers that are multiples of 15
Being careful to avoid trailing spaces.
e.g. Running the program with a range from 1-20 should produce the following result:
1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz
Step 2:
Please enhance your existing FizzBuzz solution to perform the following:
● If the number contains a three you must output the text ‘lucky’. This overrides any existing
behaviour
e.g. Running the program with a range from 1-20 should produce the following result:
1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz
Step 3:
Finally, please enhance your existing solution to perform the following:
● Produce a report at the end of the output showing how many times the following were
printed:
○ fizz
○ buzz
○ fizzbuzz
○ lucky
○ an integer
e.g. Running the program with a range from 1-20 should produce the following result:
1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz fizz:
4 buzz: 3 fizzbuzz: 1 lucky: 2 integer: 10'''

class Demo:
    def number_contains_key(self, n , key):
        digits = self.get_digits(n)
        return key in digits

    @staticmethod
    def get_digits(n):
        # n = 1234
        digits = []
        while n > 0:
            remainder = n % 10
            n = n // 10
            digits.append(remainder)
        return digits

    def __init__(self, num):
        # print(id(self))
        self.num = num
        self.series = {"fizz": 0, "buzz": 0, "fizzbuzz": 0, "lucky": 0, "integers": 0}

    def fizzbuzz(self, key):
        for i in range(1, self.num+1):
            if self.number_contains_key(i, key):
                self.series["lucky"] += 1
                print("lucky")
            elif i % 15 == 0:
                self.series["fizzbuzz"] += 1
                print("fizzbuzz")
            elif i % 3 == 0:
                self.series["fizz"] += 1
                print("fizz")
            elif i % 5 == 0:
                self.series["buzz"] += 1
                print("buzz")
            else:
                self.series["integers"] += 1
                print(i)

    def fizzbuzz_report(self):
        print(self.series)


n = int(input("Enter Number:"))
key = int(input("Enter Key:"))
obj = Demo(n)
# print(id(obj))
obj.fizzbuzz(key)
obj.fizzbuzz_report()
