from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
extensions = [
  Extension("functions.fibo", ["functions/fibo.py"]),
  Extension("functions.primes", ["functions/primes.py"])
]
setup(
    name='Packing',
    ext_modules=cythonize(extensions),    
    zip_safe=False,
)
