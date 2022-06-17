import example
import example_py
from time import time

iter_num = 100000

start = time()
for i in range(0,iter_num):
    example.fact(5)
end = time()
print(f'SWIG time {round(end -start, 2)} sec')

swig_time = end - start

python_start = time()
for i in range(0,iter_num):
    example_py.fact(5)
python_end = time()
print(f'Python time {round(python_end - python_start, 2)} sec')

python_time = python_end - python_start

print(f'{round(python_time/swig_time , 2)} times faster')