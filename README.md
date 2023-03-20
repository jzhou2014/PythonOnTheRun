# Move Python

## Goals


The primary goal is to provide **an entry point** for Python newbies who prefer to learn hands-on.
This repository has a collection of standalone modules which can be run in an IDE
like [PyCharm](READMEPycharm.md). A normal terminal will work
with the examples too. Comments are available to guide readers
through what the programs are doing step-by-step. Users are encouraged to modify
source code as long as the `main` routines are not deleted and
[Runner runs successfully](runner.py) after each change.

## Getting started

Feel free to clone the repository once [Git](READMEGit.md) and Python installed on your local machine.

Once the repository is accessible, you are ready to learn from the standalone
modules. To get the most out of each module, read the module code and run it.
There are two ways of running the modules:

1. Run a single module: `python movepython/syntax/variable.py`
2. Run all of the modules: `python runner.py`

## Table of contents

1. **About Python**
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md)
    - Design philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
    - Style guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
    - Data model: [Data model](https://docs.python.org/3/reference/datamodel.html)
    - Standard library: [The Python Standard Library](https://docs.python.org/3/library/)
    - Built-in functions: [Built-in Functions](https://docs.python.org/3/library/functions.html)
2. **Syntax**
    - Variable: [Built-in literals](movepython/syntax/variable.py)
    - Expression: [Numeric operations](movepython/syntax/expression.py)
    - Conditional: [if | if-else | if-elif-else](movepython/syntax/conditional.py)
    - Loop: [for-loop | while-loop](movepython/syntax/loop.py)
    - Function: [def | lambda](movepython/syntax/function.py)
3. **Data Structures**
    - List: [List operations](movepython/data_structures/list.py)
    - Tuple: [Tuple operations](movepython/data_structures/tuple.py)
    - Set: [Set operations](movepython/data_structures/set.py)
    - Dict: [Dictionary operations](movepython/data_structures/dict.py)
    - Comprehension: [list | tuple | set | dict](movepython/data_structures/comprehension.py)
    - String: [String operations](movepython/data_structures/string.py)
    - Deque: [deque](movepython/data_structures/deque.py)
    - Time complexity: [cPython operations](https://wiki.python.org/moin/TimeComplexity)
4. **Classes**
    - Basic class: [Basic definition](movepython/classes/basic_class.py)
    - Abstract class: [Abstract definition](movepython/classes/abstract_class.py)
    - Exception class: [Exception definition](movepython/classes/exception_class.py)
    - Iterator class: [Iterator definition | yield](movepython/classes/iterator_class.py)
5. **Advanced**
    - Decorator: [Decorator definition | wraps](movepython/advanced/decorator.py)
    - Context manager: [Context managers](movepython/advanced/context_manager.py)
    - Method resolution order: [mro](movepython/advanced/mro.py)
    - Mixin: [Mixin definition](movepython/advanced/mixin.py)
    - Metaclass: [Metaclass definition](movepython/advanced/meta_class.py)
    - Thread: [ThreadPoolExecutor](movepython/advanced/thread.py)
    - Asyncio: [async | await](movepython/advanced/async.py)
    - Weak reference: [weakref](movepython/advanced/weak_ref.py)
    - Benchmark: [cProfile | pstats](movepython/advanced/benchmark.py)
    - Mocking: [MagicMock | PropertyMock | patch](movepython/advanced/mocking.py)
    - Regular expression: [search | findall | match | fullmatch](movepython/advanced/regex.py)
    - Data format: [json | xml | csv](movepython/advanced/data_format.py)
    - Datetime: [datetime | timezone](movepython/advanced/date_time.py)

## Additional resources

### GitHub repositories

Keep learning by reading from other well-regarded resources.

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)
- [faif/python-patterns](https://github.com/faif/python-patterns)
- [geekcomputers/Python](https://github.com/geekcomputers/Python)
- [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning)
- [karan/Projects](https://github.com/karan/Projects)
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners)
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience)
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
- [30-seconds/30-seconds-of-python](https://github.com/30-seconds/30-seconds-of-python)
- [ml-tooling/best-of-python](https://github.com/ml-tooling/best-of-python)

### Interactive practice

Keep practicing so that your coding skills don't get rusty.

- [leetcode.com](https://leetcode.com/)
- [hackerrank.com](https://www.hackerrank.com/)
- [kaggle.com](https://www.kaggle.com/)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
- [DevProjects](https://www.codementor.io/projects/python)
- [codewars.com](https://www.codewars.com/)
