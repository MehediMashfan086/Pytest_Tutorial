class TestCase:
    def test_one(self):
        x = "mehedi"
        assert 'h' in x
        
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')