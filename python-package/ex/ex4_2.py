# -*- coding: cp949 -*-
python_is = """
Python logo and wordmark.svg
Paradigm	Object-oriented, imperative, functional, procedural, reflective
Designed by	Guido van Rossum
Developer	Python Software Foundation
First appeared	1990[1]
Stable release	
3.7.0 / 27 June 2018; 14 days ago[2]
2.7.15 / 1 May 2018; 2 months ago[3]
Typing discipline	
Duck, dynamic, strong since version 3.5:

Gradual[4]
License	Python Software Foundation License
Filename extensions	.py, .pyc, .pyd, .pyo (prior to 3.5),[5] .pyw, .pyz (since 3.5)[6]
Website	www.python.org
Major implementations
CPython, IronPython, Jython, MicroPython, Numba, PyPy, Stackless Python
Dialects
Cython, RPython
Influenced by
ABC,[7] ALGOL 68,[8] C,[9] C++,[10] CLU,[11] Dylan,[12] Haskell,[13] Icon,[14] Java,[15] Lisp,[16] Modula-3,[10] Perl
Influenced
Boo, Cobra, Coconut,[17] CoffeeScript,[18] D, F#, Falcon, Genie,[19] Go, Groovy, JavaScript,[20][21] Julia,[22] Nim, Ring,[23] Ruby,[24] Swift[25]
 Python Programming at Wikibooks
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[26]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[27]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.
"""


# python 이라는 글자를 3개 찾자
    # 긴 장문 중에
    # 첫번째 python 글자를 찾고
    # 두번째 python 글자는 첫번째 글자 (바로직후) 이후에  처음발견되는 단어야 된다
    # 해당 단어가 몇번째인지 출력하고, 찾은 위치에 있는 python단어를 출력하자
##is_word='Python'
##
##first = python_is.index(is_word)
##print first, python_is[first:first+20]+'...'
##
##second = python_is.index(is_word, first+1)
##print second, python_is[second:second+25]+'...'
##
##thrid = python_is.index(is_word, second+1)
##print thrid, python_is[thrid:thrid+25]+'...'

"""
index(...)
    S.index(sub[,start[,end]])   -> start에 아무것도 없으면 자동으로 0이 들어간다
"""


