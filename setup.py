"""
    Setup file for cython_template.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.4.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup, Extension, find_packages

import numpy

from Cython.Build import cythonize

extensions = [
    Extension(
        name="UtilsModule.dependencies.hello_world",
        sources=["src/UtilsModule/dependencies/hello_world.pyx"], 
        include_dirs=[numpy.get_include()]
    ),
]


#setup(
#    ext_modules=cythonize(extensions)
#)

if __name__ == "__main__":
    try:
        setup(use_scm_version={"version_scheme": "no-guess-dev"},
              ext_modules=cythonize(extensions))
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
