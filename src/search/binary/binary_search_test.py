from binary_search import binary_search


class TestBinarySearch:
    def test_success(self):
        assert binary_search([1, 9, 63, 143, 37, 9, 2, 6, 5], 37) == 4
        assert binary_search([8, 90, 331, 32, 4, 6, 2], 2) == 6
        assert binary_search([8, 90, 331, 32, 4, 6, 2], 3232) == -1
