from setuptools import setup,find_packages
from typing import List


PROJECT_NAME = 'Housing Price Prediction System'
VERSION = "0.0.1"
AUTHOR = "Tanish Parmar"
DESCRIPTION = "Housing Price Prediction System made using regression machine learning models"
# PACKAGES = find_packages()
REQUIREMENTS_FILE_NAME = "requirements.txt"



def get_requirements_list() -> List[str]:
    """
    This function is going to return list of requirements mentioned in requirements.txt file ,this function returns list.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

# if __name__ == "__main__":
#     print(get_requirements_list())