from learning_python.Lesson01_Basics.Section01_Basic_syntax.src.test_demo.MySum import my_sum


def test_my_sum_of_list():
    assert my_sum([1, 2, 3]) == 6, "Should be 6"


def test_my_sum_of_tuple():
    assert my_sum((1, 2, 2)) == 5, "Should be 5"


def test_my_sum_of_set():
    assert my_sum({1, 2, 3}) == 6, "should be 6"


def test_my_sum_wrong():
    assert my_sum([1, 2, 3]) == 5, "should be 6"


def test_my_sum_explain():
    # arrange: set up test conditions
    expected_value = 6
    input_param = [1, 2, 3]
    # act: call the function that need to be tested
    actual_value = my_sum(input_param)
    # assert: check if the function returns the expected value
    assert expected_value == actual_value
