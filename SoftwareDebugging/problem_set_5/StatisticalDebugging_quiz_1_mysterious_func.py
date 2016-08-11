#!/usr/bin/env python
import sys
import math
import numbers, collections
import copy


answer_function = "f3"   # One of f1, f2, f3
answer_bin = -1         # One of 1, 0, -1
answer_value = 0.8165   # precision to 4 decimal places.

###### MYSTERY FUNCTION

def f1(ml):
    if type(ml) is not list:
        return -1
    elif len(ml) <6 :
        return len(ml)
    else:
        return 0

def f2(ms):
    if type(ms) is not str:
        return -1
    elif len(ms) <6 :
        return len(ms)
    else:
        return 0

def f3(mn):
    if type(mn) is not int:
        return -1
    if mn > 10:
        return -100
    else:
        return mn

def mystery(magic):
    assert type(magic) == tuple
    assert len(magic) == 3

    l, s, n = magic

    r1 = f1(l)

    r2 = f2(s)

    r3 = f3(n)

    if -1 in [r1, r2, r3]:
        return "FAIL"
    elif r3 < 0:
        return "FAIL"
    elif not r1 or not r2:
        return "FAIL"
    else:
        return "PASS"



# global variable to keep the coverage data in
coverage = {}
# Tracing function that saves the coverage data
# To track function calls, you will have to check 'if event == "return"', and in
# that case the variable arg will hold the return value of the function,
# and frame.f_code.co_name will hold the function name

def pnz(rv):
    if rv == 0:
        return 0
    elif rv > 0:
        return 1
    else:
        return -1

def categorize(rv):
    if isinstance(rv, numbers.Number):
        return pnz(rv)
    elif isinstance(rv, collections.Iterable):
        return pnz(len(rv))
    else:
        return -1

def traceit(frame, event, arg):
    global coverage

    if event == "return":
        filename = frame.f_code.co_filename
        func_name = frame.f_code.co_name
        return_value = arg
        if not coverage.has_key(filename):
            coverage[filename] = {}
        if func_name != 'mystery':
            if not coverage.has_key(func_name):
                coverage[filename][func_name] = {}
            # coverage[filename][func_name] = categorize(return_value)
            coverage[filename][func_name][categorize(return_value)] = True

    return traceit

# Calculate phi coefficient from given values
def phi(n11, n10, n01, n00):
    return ((n11 * n00 - n10 * n01) /
             math.sqrt((n11 + n10) * (n00 + n01) * (n00 + n10) * (n11 + n01)))

# Print out values of phi, and result of runs for each covered line
def print_tables(tables):
    result = copy.deepcopy(tables)
    max_factor = None
    for filename in tables.keys():
        for func in tables[filename].keys():
            for cate in tables[filename][func].keys():
                (n11, n10, n01, n00) = tables[filename][func][cate]
                print 'func:', func, 'category:', cate
                print 'n:', n11, n10, n01, n00
                try:
                    factor = phi(n11, n10, n01, n00)
                except:
                    factor = 0 # since phi = 0/0 in this case
                if max_factor is None or factor > max_factor:
                    max_factor = factor
                print 'factor = ', factor
                print 'max factor = ', max_factor , '\n'
        #
        # lines = open(filename).readlines()
        # for i in range(23, 40): # lines of the remove_html_markup in this file
        #     if tables[filename].has_key(i + 1):
        #         (n11, n10, n01, n00) = tables[filename][i + 1]
        #         try:
        #             factor = phi(n11, n10, n01, n00)
        #             prefix = "%+.4f%2d%2d%2d%2d" % (factor, n11, n10, n01, n00)
        #         except:
        #             prefix = "       %2d%2d%2d%2d" % (n11, n10, n01, n00)
        #
        #     else:
        #         prefix = "               "
        #
        #     print prefix, lines[i],

# Run the program with each test case and record
# input, outcome and coverage of lines
def run_tests(inputs):
    runs   = []
    for input in inputs:
        global coverage
        coverage = {}
        sys.settrace(traceit)
        # result = remove_html_markup(input)
        outcome = mystery(input)
        sys.settrace(None)

        # if result.find('<') == -1:
        #     outcome = "PASS"
        # else:
        #     outcome = "FAIL"

        runs.append((input, outcome, coverage))
    return runs
cates = [-1, 0, 1]
funcs = ['f1', 'f2', 'f3']
# Create empty tuples for each covered line
def init_tables(runs):
    tables = {}
    for (input, outcome, coverage) in runs:
        for filename in coverage:
            for func in funcs:
                for cate in cates:
                    if not tables.has_key(filename):
                        tables[filename] = {}
                    if not tables[filename].has_key(func):
                        tables[filename][func] = {}
                    if not tables[filename][func].has_key(cate):
                        tables[filename][func][cate] = (0, 0, 0, 0)

    return tables

# Compute n11, n10, etc. for each line
def compute_n(tables):
    for filename in tables.keys():
        for func in tables[filename].keys():
            for cate in tables[filename][func].keys():
                (n11, n10, n01, n00) = tables[filename][func][cate]
                for (input, outcome, coverage) in runs:
                    if coverage[filename][func].has_key(cate):
                        if outcome == "FAIL":
                            n11 += 1
                        else:
                            n10 += 1
                    else:
                        if outcome == "FAIL":
                            n01 += 1
                        else:
                            n00 += 1
                tables[filename][func][cate] = (n11, n10, n01, n00)
    return tables

# These are the input values you should test the mystery function with
inputs = [([1,2],"ab", 10),
          ([1,2],"ab", 2),
          ([1,2],"ab", 12),
          ([1,2],"ab", 21),
          ("a",1, [1]),
          ([1],"a", 1),
          ([1,2],"abcd", 8),
          ([1,2,3,4,5],"abcde", 8),
          ([1,2,3,4,5],"abcdefgijkl", 18),
          ([1,2,3,4,5,6,7],"abcdefghij", 5)]

# Now compute (and report) phi for each line. The higher the value,
# the more likely the line is the cause of the failures.
runs = run_tests(inputs)

tables = init_tables(runs)

tables = compute_n(tables)

print_tables(tables)
# print_tables(tables)
