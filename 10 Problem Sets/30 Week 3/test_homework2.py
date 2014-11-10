# Template for Homework 2 Tests
#
# Name:
# Student number:

#
# This part sets up your tests. Please add tests in the next section. Do not
# change this section.
#

from homework2 import *

import sys

class ansi_colors:
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def assert_equal(have, want):
    try:
        result = eval(have)
        if str(result) == str(want):
            print ansi_colors.GREEN + ":)", have, "yields", str(want) + ansi_colors.ENDC
        else:
            print ansi_colors.FAIL + ":(", have + ansi_colors.ENDC
            print "   \\ expected " + str(want) + ", but returned " + str(result)
    except:
        print ansi_colors.FAIL + ":(", have + ansi_colors.ENDC
        print "   \\ evaluating the expression `" + str(have) + "` fails with error:"
        print "     " + str(sys.exc_info()[1])

#
# Here is your first example test. Write your own tests in a similar fashion!
#

def test_is_divisible():
    assert_equal("is_divisible(10, 5)", True)
    assert_equal("is_divisible(18, 7)", False)
    assert_equal("is_divisible(42, 0)", False)

test_is_divisible()
