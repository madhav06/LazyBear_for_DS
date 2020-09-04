# Interview Question:

# Balanced Parentheses Check:
#
# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced.
# We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
# Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
# As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
# For example ‘([])’ is balanced but ‘([)]’ is not.
#
# You can assume the input string has no spaces.

def balanced_check(s):

    # Check is even numbers of brackets
    if len(s)%2 != 0:
        return False


    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])

    # Using list as stack
    stack = []

    # Checking  every parenthesis in string
    for paren in s:

        #
        # if its opening, append it
        if paren in opening:
            stack.append(paren)

        else:
            # checking that if there is any parenthesis in stack or # NOTE:
            if len(stack) == 0:
                return False

            # Checking the last open parenthesis
            last_open = stack.pop()

            # if it has any matches
            if (last_open,paren) not in matches:
                return False

        print (len(stack) == 0)


balanced_check( '[]' )
#balanced_check( '()(){]}' )
# balanced_check( '[](){([[[]]])}' )




"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):

    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')

# Run Tests

t = TestBalanceCheck()
t.test(balanced_check)

# balanced parenthesis checks that for every opening parenthesis there will be closing parenthesis  in the reverse order opened.
# For example ‘([])’ is balanced but ‘([)]’ is not.