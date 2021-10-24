from is_even import is_even


class TestIsEven:
    def test_success(self):
        assert is_even(2) is True
        assert is_even(3) is False
        assert is_even(4) is True
        assert is_even(1315523) is False
        assert is_even(1315524) is True
