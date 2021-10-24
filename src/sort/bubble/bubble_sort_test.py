from bubble_sort import bubble_sort


class TestBubbleSort:
    def test_success(self):
        assert bubble_sort([6, 1, 8, 3]) == [1, 3, 6, 8]
        assert bubble_sort([9, 1, 4, 2, 5, 1, 0, -10]) == [-10, 0, 1, 1, 2, 4, 5, 9]
