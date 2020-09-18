#I have created some test cases to check maximum number among the two given numbers.
#I am only passing the values as input in the created test cases itself.I dont need to define them everytime I run the code.
#My compiler is checking whether created test cases are passed or not with the help of returned value from the function
#Finally it displays passed or failed test cases.
#Command to run in terminal:- pytest 'filename'.py

import pytest
values=[(0,-1,0),(1,4,4),(2,8,8),(4,4,4),(1,100,100)]
@pytest.mark.parametrize("first,second,expected_value", values)
def test_boarding(first,second,expected_value):
        result=boarding(first,second)
        assert result==expected_value
#PF-Tryout

#Program to be tested

def boarding(first,second):
    if first>second:
        max=first
    else:
        max=second
    return max
