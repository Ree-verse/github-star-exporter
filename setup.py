import re

from setuptools import find_packages, setup

# Find version info from module (without importing the module):
with open("src/github_star_exporter/__init__.py", "r") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="github-star-exporter",
    version=version,
    author="Ree-verse",
    author_email="reeversesoft@gmail.com",
    python_requires=">=3.6",
    url="https://github.com/ree-verse/github-star-exporter",
    description="Export (your) GitHub starred repositories to a JSON file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    license_files = ["LICENSE"],
    keywords='backup, cli, exporter, github, json, python, repositories, stars',
    project_urls={
    "Source": "https://github.com/ree-verse/github-star-exporter",
    "Issues": "https://github.com/ree-verse/github-star-exporter/issues",
    "Docs": "https://github.com/ree-verse/github-star-exporter/blob/main/README.md",
},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # test_suite="tests",
    install_requires=["colorama", "requests"],
    entry_points={
        "console_scripts": [
            "github-star-exporter = github_star_exporter.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: File Formats :: JSON",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
