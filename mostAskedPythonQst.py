# FizzBuzz challenge
from numpy.ma.core import minimum


def fizzBuzzSol(n):
    for i in range(1, n+1):
        if i % 3 ==0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzzSol(15)

# plaindrome check
def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome('madam'))
print(is_palindrome('racecar'))
print(is_palindrome('python'))

# anagrams check
def anagram_check(str1, str2):
    return sorted(str1) == sorted(str2)

print(anagram_check('silent', 'listen'))
print(anagram_check('hello', 'world'))

# fibonacci series:
# loop method
def fibonacci_series(n):
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print(fibonacci_series(7))

# recursive method:
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print([fibonacci_recursive(i) for i in range(7)])

# factorial
def factorial_check(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_check(n-1)

print(factorial_check(5))

# merge two sorted lists:
def merge_sorted_list(a, b):
    result = []
    i = j =0
    while i < len(a) and j < len(b):
        if(a[i] < b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend((b[j:]))
    return result

print(merge_sorted_list([1,3,5], [2,4,6]))

# find maxandmin without max() and min()
def find_max(lst):
    maximum=lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([3, 10, 5, 6, 12]))

def find_min(lst):
    minimum=lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

print(find_min([2,4,8,9,1,0]))

# count frequency of elements in lst
def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(count_frequency([1,2,3,2,3,4,4,4,5]))

# api call and process JSOn response:
import requests

def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data = response.json()
    for post in data[:5]:
        print(post['title'])

fetch_data()

