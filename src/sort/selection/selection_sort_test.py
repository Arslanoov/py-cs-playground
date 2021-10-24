from selection_sort import selection_sort


class TestSelectionSort:
    def test_success(self):
        assert selection_sort([6, 1, 8, 3]) == [1, 3, 6, 8]
        assert selection_sort([9, 1, 4, 2, 5, 1, 0, -10]) == [-10, 0, 1, 1, 2, 4, 5, 9]
