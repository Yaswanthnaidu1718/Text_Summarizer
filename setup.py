import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "TEXT-SUMMARIZER"
AUTHOR_USER_NAME = "yaswanth1718"   
AUTHOR_EMAIL = "yaswanthnaiduakula05@gmail.com"
SRC_REPO = "TEXT-SUMMARIZER"
setuptools.setup(
    name=SRC_REPO,      
    version=__version__,
    author=AUTHOR_USER_NAME,        
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization using transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)
