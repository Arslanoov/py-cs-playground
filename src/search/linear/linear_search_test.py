from linear_search import linear_search


class TestLinearSearch:
    def test_success(self):
        assert linear_search([1, 9, 63, 143, 37, 9, 2, 6, 5], 37) == 4
        assert linear_search([8, 90, 1, 32, 4, 6, 2], 90) == 1
        assert linear_search([8, 90, 1, 32, 4, 6, 2], 31131) == -1
