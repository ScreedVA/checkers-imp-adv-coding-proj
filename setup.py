from setuptools import setup, find_packages

setup(
    name="checkers-imp-adv-code-proj",
    version="0.1.0",
    author="Christian DY",
    author_email="techscreed@gmail.com",
    description="Checkers implementation in python based on the international draughts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        'mypackage': ['static/*.png', "static/*.ttf"],  # Adjust the pattern to match your static file extensions
    },
    install_requires=[
        "pillow",
        "pygame",
    ],
    entry_points={
        "console_scripts": [
            "run_checkers_round=mypackage:main",
        ]
    }
)


