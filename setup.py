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
