from factorial import factorial_iterative, factorial_recursive


class TestFactorial:
    def test_iterative(self):
        assert factorial_iterative(1) == 1
        assert factorial_iterative(2) == 2
        assert factorial_iterative(3) == 6
        assert factorial_iterative(4) == 24
        assert factorial_iterative(5) == 120

    def test_recursive(self):
        assert factorial_recursive(1) == 1
        assert factorial_recursive(2) == 2
        assert factorial_recursive(3) == 6
        assert factorial_recursive(4) == 24
        assert factorial_recursive(5) == 120
