from setuptools import setup, find_packages

setup(
    name='tabler-qicon',
    version='0.1.0', 
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        'PyQt5': ['PyQt5'],
        'PyQt6': ['PyQt6'],
        'PySide2': ['PySide2'],
        'PySide6': ['PySide6'],
    }
)
