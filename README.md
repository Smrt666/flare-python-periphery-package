# flare-python-periphery-package
TODO:
* create LICENSE
* update pyproject.toml
* update readme

Need account on TestPyPI/PyPI, API token (https://test.pypi.org/manage/account/#api-tokens)
deploy (replace testpypi with pypi):
```bash
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```