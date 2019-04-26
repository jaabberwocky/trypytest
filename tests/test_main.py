from apple.main import myfunc

class TestCaseOne():
    def test_funcone(self):
        assert myfunc(4) == 5

    def test_two(self):
        assert myfunc(5) == 6

class TestCaseTwo():
    def test_3(self):
        assert myfunc(2) == 5

    def test_4(self):
        assert myfunc(50) == 51