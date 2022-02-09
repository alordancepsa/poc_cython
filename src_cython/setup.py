from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
extensions = [
  Extension("lib.fibo", ["lib/fibo.py"]),
  Extension("lib.primes", ["lib/primes.py"])
]
setup(
    name='Packing',
    ext_modules=cythonize(extensions),    
    zip_safe=False,
)
