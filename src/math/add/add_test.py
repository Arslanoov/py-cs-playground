from add import add


class TestAdd:
    def test_success(self):
        assert add(2, 2) == 4
