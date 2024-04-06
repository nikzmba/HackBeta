import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "HackBeta"
AUTHOUR_USERNAME = "nikzmba"
SRC_REPO = "hackbeta"
AUTHOUR_EMAIL = "mbabeykoon@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOUR_USERNAME,
    author_email=AUTHOUR_EMAIL,
    description="News data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOUR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOUR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
 
)