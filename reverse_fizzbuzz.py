def reverse_fizzbuzz(string):
    words_num = {
        'Fizz': [3],
        'Buzz': [5],
        'FizzBuzz': [15],
        'Fizz Buzz': [9, 10],
        'Buzz Fizz': [5, 6]
    }

    if string in words_num.keys():
        return words_num[string]
    else:
        num_array = string.split()
        for index, num in enumerate(num_array, start=0):
            if num.isdigit():
                return list(range(int(num) - index, int(num) + len(num_array[index::])))
