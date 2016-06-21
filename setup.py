from setuptools import setup, find_packages

with open('README.md') as f:
        readme = f.read()

with open('LICENSE') as f:
        license = f.read()

setup(
        name='markov-text-generator',
        version='0.0.1',
        description='yet another markov text generator',
        long_description=readme,
        author='Steven Samson',
        author_email='steven.a.samson@gmail.com',
        url='https://github.com/steven-s/markov-text-generator',
        license=license,
        packages=find_packages(exclude=('tests'))
)

