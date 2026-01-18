# setup.py is a Python file used to package and distribute Python projects. It tells Python and tools like pip how to install your project and what information it contains.
# Think of it like a blueprint for your Python package.

#used to make my ML project aspacckage

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        # Remove -e . if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Arshdeep",
    author_email="arshdeepgtbit@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
