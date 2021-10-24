from double import double


class TestDouble:
    def test_success(self):
        assert double(2) == 4
        assert double(8) == 16
        assert double(9) == 18
        assert double(4242) == 8484
