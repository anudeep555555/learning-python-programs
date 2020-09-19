I wrote a function which takes list as a parameter . This method only allows two digit numbers in such a way that it starts from a bigger number and ends with lower number and concatenates them and returns the largest number formed from the list.

    import pytest
    values=[([22,34,55],553422),([23,34,43,64],64433423)]
    @pytest.mark.parametrize("number_list,expected_value", values)
    def test_largest_number_from_list(number_list,expected_value):
            result=largest_number_from_list(number_list)
            assert result==expected_value
    
    def largest_number_from_list(number_list):
        number_list.sort()
        new = ''
        for i in (number_list[::-1]):
            if len(str(i)) == 2:
                new += str(i)
        new = int(new)
        return new

I am asserting input as list which checks by passing the list as input and I am also asserting the output which checks the return value of function is matching with asserting value.

