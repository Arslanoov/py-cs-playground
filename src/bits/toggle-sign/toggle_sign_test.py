from toggle_sign import toggle_sign


class TestToggleSign:
    def test_success(self):
        assert toggle_sign(3) == -3
        assert toggle_sign(2) == -2
        assert toggle_sign(1452) == -1452
        assert toggle_sign(0) == 0
