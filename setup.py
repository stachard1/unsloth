from setuptools import setup, find_packages
import os

# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements from requirements.txt if it exists
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_path):
        with open(req_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="unsloth",
    version="2024.12.0",
    author="Unsloth AI",
    author_email="danielhanchen@gmail.com",
    description="2-5x faster, 70% less memory LLM finetuning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://docs.unsloth.ai",
        "Source": "https://github.com/unslothai/unsloth",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.2",
        "tyro>=0.7.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
        ],
        "triton": [
            "triton>=2.1.0",
        ],
        "huggingface": [
            "huggingface_hub>=0.20.0",
            "peft>=0.7.0",
            "trl>=0.7.4",
            "accelerate>=0.26.0",
            "bitsandbytes>=0.41.3",
            "xformers",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "llm",
        "finetuning",
        "lora",
        "qlora",
        "transformers",
        "machine learning",
        "deep learning",
        "nlp",
    ],
    license="Apache 2.0",
    include_package_data=True,
    zip_safe=False,
)
