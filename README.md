# SWIG tutorial.

## Install SWIG in Linux

```bash
$ sudo apt-get install swig
```
## Create C file.


**example.c**

```c
 /* File : example.c */
 
 #include <time.h>
 double My_variable = 3.0;


 int fact(int n) {
     if (n <= 1) return 1;
     else return n*fact(n-1);
 }
 

 int my_mod(int x, int y) {
     return (x%y);
 }
 	

 char *get_time()
 {
     time_t ltime;
     time(&ltime);
     return ctime(&ltime);
 }
 
 
```

## Create SWIG interface file.

```SWIG
/* example.i */
 %module example
 %{
 /* 헤더파일과 함수들을 이곳에 넣어주도록 하자. */
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();
 %}
 
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();
```
## Create python module.

### Using setup.py.

#### Step 1. wrap C file with swig command

```bash
$swig -python example.i
```


   
#### Step 2. Create setup.py


```python
#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

# Extension 안에 argument로 output파일 이름과, 우리들의 c 파일을 넣어주면 된다. 
example_module = Extension('_example',
                           sources=['example_wrap.c', 'example.c'],
                           )

                           
# setup 안에는 정보와 모듈의 이름이 들어간다. 맞춰주도록 하자. 
setup (name = 'example',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
```


```
$ python setup.py build_ext --inplace
```


# Result comparsion with pure python module.

## example_py.py

```python
def fact(x):
  if x == 1:
    return x
  else:
    return x * fact(x-1) 
```



## test.py

```python
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
```

