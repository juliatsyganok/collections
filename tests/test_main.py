import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import random
from main import run

class TestMain:
    def test_run_no_seed(self):
        try:
            run(steps=5)
        except Exception as e:
            pytest.fail(f"Ошибка: {e}")

    def test_run_with_seed(self):
        try:
            run(steps=5, seed=42)
        except Exception as e:
            pytest.fail(f"Ошибка: {e}")

    def test_seed_reproduce(self):
        random.seed(42)
        r1 = random.randint(1, 100)
        random.seed(42)
        r2 = random.randint(1, 100)
        assert r1 == r2

    def test_steps(self):
        try:
            run(steps=10)
        except Exception as e:
            pytest.fail(f"Ошибка: {e}")

    def test_zero_steps(self):
        try:
            run(steps=0)
        except Exception as e:
            pytest.fail(f"Ошибка: {e}")