from setuptools import setup, find_packages

setup(
    name='tabler-qicon',
    version='0.1.0',
    description='Python package that provides easy access to Tabler Icons for PyQt and PySide applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Charin Rungchaowarat',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT',
    extras_require={
        'PyQt5': ['PyQt5'],
        'PyQt6': ['PyQt6'],
        'PySide2': ['PySide2'],
        'PySide6': ['PySide6'],
    }
)
