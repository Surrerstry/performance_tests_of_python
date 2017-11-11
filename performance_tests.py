from timeit import timeit
from time import time
from sys import stderr
from sys import platform
from os import remove

"""
Running:

*nix: 
python performance_tests.py > /dev/null

windows:
python performance_tests.py > NUL
"""

start_time = time()

code = """
print('a')
"""
print('1. Print function:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code, number=100000),
	timeit(code, number=1000000),
	timeit(code, number=10000000),
	), file=stderr)


code = """
tmp = 0
for i in range({}):
	tmp+=i
"""
print('2. for loop:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(1000000), number=1),
	timeit(code.format(10000000), number=1),
	timeit(code.format(100000000), number=1),
	), file=stderr)


code = """
from string import ascii_letters
from random import choice
temporary_list = []
for i in range({}):
	temporary_list.append(choice(ascii_letters))
"""
print('3. append to list:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(100000), number=1),
	timeit(code.format(1000000), number=1),
	timeit(code.format(10000000), number=1),
	), file=stderr)



code = """
temporary_array = [1]*{0}
for _ in range({0}):
	temporary_array.remove(1)
"""
print('4. remove from list:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(100000), number=1),
	timeit(code.format(200000), number=1),
	timeit(code.format(300000), number=1),
	), file=stderr)


code = """
a, b = 0, 1
while a<{}:
	a, b = b, a+b
"""
print('5. Fibonacci number:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(2**100000), number=1),
	timeit(code.format(2**400000), number=1),
	timeit(code.format(2**800000), number=1),
	), file=stderr)


windows="['cmd', '/c', 'echo a']"
nix="['echo', 'a']"
code = """
from subprocess import Popen
for _ in range({}):
	Popen({}).communicate()
"""
print('6. Calling shell program:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(100, windows if 'win' in platform else nix), number=1),
	timeit(code.format(1000, windows if 'win' in platform else nix), number=1),
	timeit(code.format(10000, windows if 'win' in platform else nix), number=1)
	), file=stderr)


code = """
with open('tmp.txt', 'w') as file:
	file.write('01234567890')
"""	
print('7. Write to file:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code, number=1000),
	timeit(code, number=10000),
	timeit(code, number=50000),
	), file=stderr)


code = """
with open('tmp.txt') as file:
	file.read()
"""
print('8. Read from file:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code, number=1000),
	timeit(code, number=10000),
	timeit(code, number=100000),
	), file=stderr)
remove('tmp.txt')


code = """
a=[0,1,2,3,4,5,6,7,8,9]*1000000
del a
"""
print('9. Creation and deleting big variable:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code, number=10),
	timeit(code, number=100),
	timeit(code, number=1000),
	), file=stderr)


code = """
class tst_cls(object):
	def __init__(self):
		self.var = '...'

for _ in range({}):
	tmp=tst_cls()
	del tmp
"""
print('10. Creating and removing instance of object:\n{:.3f}\n{:.3f}\n{:.3f}\n'.format(
	timeit(code.format(1000000), number=1),
	timeit(code.format(10000000), number=1),
	timeit(code.format(100000000), number=1),
	), file=stderr)


print("Time of all tests: {:.2f} seconds".format(time()-start_time), file=stderr)



