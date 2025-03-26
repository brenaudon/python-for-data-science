from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="brenaudo",
    author_email="brenaudo@student.42angouleme.fr",
    url="https://github.com/brenaudon/python-"
        + "for-data-science/tree/main/0_starting/ex09",
    license="MIT",
    packages=find_packages(),  # automatically detects ft_package/
    python_requires=">=3.10",
)
