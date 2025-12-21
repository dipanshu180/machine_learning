# Building application as a package
from setuptools import find_packages, setup
from typing import List


e = '-e .'

def get_requirements(file_path:str )->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    '''


    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if e in requirements:
            requirements.remove(e)

    return requirements

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Deep",
    email = "deep011102@gmail.com",
    install_requires = get_requirements("requirements.txt"), 
    packages = find_packages()
) 