from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "IRWA_Group"  # Corrected variable usage
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']  # Corrected package name

# Define setup
setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,  # Using variable without quotes
    author_email='it22141606@my.sliit.lk',
    packages=[SRC_REPO],
    python_requires='>=3.12.5',  # Corrected to python_requires
    install_requires=LIST_OF_REQUIREMENTS,  # Corrected list usage
    long_description=long_description,
    long_description_content_type="text/markdown",
)
