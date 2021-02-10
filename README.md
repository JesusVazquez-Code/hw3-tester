# hw3-tester

Tests for CS540 Spring 2021 HW3: Principal Component Analysis 

## Usage

Download [test.py](test.py) and move it into the directory that contains `pca.py` and `YaleB_32x32.npy`

The contents of your directory should look like this:

```shell
$ tree
.
├── YaleB_32x32.npy
├── pca.py
└── test.py
```

To run the tests, do

```python
$ python3 test.py
```

It is assumed that `YaleB_32x32.npy` is present in the same directory as `test.py` and `pca.py`. If this is not the case, you can the argument `--yale-path` like this:

```python
$ python3 test.py --yale-path path/to/YaleB_32x32.npy
```

## Disclaimer

These tests are not endorsed or created by anyone working in an official capacity with UW Madison or any staff for CS540. The tests are make by students, for students.

By running `test.py`, you are executing code you downloaded from the internet. Back up your files and take a look at what you are running first.

If you have comments or questions, create an issue at [https://github.com/CS540-testers-SP21/hw3-tester/issues](https://github.com/CS540-testers-SP21/hw3-tester/issues) or ask in our discord at [https://discord.gg/RDFNsAxgCQ](https://discord.gg/RDFNsAxgCQ).