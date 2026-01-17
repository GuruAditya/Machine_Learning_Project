from setuptools import setup,find_packages
from typing import List

a="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if a in requirements:
            requirements.remove(a)
    return requirements

setup(
    name="ML project",
    author="Aditya",
    author_email="adityagururani120230@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
