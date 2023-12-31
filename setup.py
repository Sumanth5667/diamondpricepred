from setuptools import find_packages,setup
from typing import List
costant='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if costant in requirements:
            requirements.remove(costant)
        return requirements
    

setup(

    name='diamondpriceprediction',
    version='0.0.1',
    author='sumanthnimmagadda',
    author_email='sumanthnimmagadda5667@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)