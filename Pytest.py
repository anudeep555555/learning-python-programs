#Firstly I used Eclipse IDE but its a headache so I shifted to Pycharm
#In pycharm firstly I got an error on firstline itself 'import pytest'
#Then i hovered on pytest then I was asked to install it .Then I installed it.
#Now I am able to use pytest module sucessfully
#I used the format to write test cases. which you can see below
#Now in terminal of pycharm type 'pytest filename.py'
#Now we can see no of testcases passed successfully and also which test case failed
#By using this we can clearly understand how test cases are assigned previously to any code
#and also how to create them in advance
#We are not even calling a function with value in parentheses instead we are defining them previosly
#Our pytest module itself is checking by keeping th evalues defines previously and checking whether they are correct or not.
import pytest
values=[(0,-1),(1,1), (2,1),(24,1),(25,1), (26,2),(27,2),
        (99,2),(100,2), (101,3),(102,3),(199,3),(200,3), (201,-1)]
@pytest.mark.parametrize("seat_number,expected_value", values)
def test_boarding(seat_number,expected_value):
        result=boarding(seat_number)
        assert result==expected_value
#PF-Tryout

#Program to be tested

def boarding(seat_number):
    if(seat_number>=1 and seat_number<=25):
        batch_no=1
    elif(seat_number>=26 and seat_number<=100):
        batch_no=2
    elif(seat_number>=101 and seat_number < 200):
        batch_no=3
    else:
        batch_no=-1
    return batch_no
