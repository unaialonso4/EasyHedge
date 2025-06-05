import pytest
from src.calculations.greeks import calculate_delta, calculate_gamma, calculate_vega, calculate_theta, calculate_rho

def test_calculate_delta():
    assert calculate_delta(100, 100, 30, 0.05, 0.2, "call") == pytest.approx(0.53996, rel=1e-2)
    assert calculate_delta(100, 100, 30, 0.05, 0.2, "put") == pytest.approx(-0.46004, rel=1e-2)

def test_calculate_gamma():
    assert calculate_gamma(100, 100, 30, 0.05, 0.2) == pytest.approx(0.06923, rel=1e-2)

def test_calculate_vega():
    assert calculate_vega(100, 100, 30, 0.05, 0.2) == pytest.approx(0.11380, rel=1e-2)

def test_calculate_theta():
    assert calculate_theta(100, 100, 30, 0.05, 0.2, "call") == pytest.approx(-0.04499, rel=1e-2)
    assert calculate_theta(100, 100, 30, 0.05, 0.2, "put") == pytest.approx(-0.03135, rel=1e-2)

def test_calculate_rho():
    assert calculate_rho(100, 100, 30, 0.05, 0.2, "call") == pytest.approx(0.04233, rel=1e-2)
    assert calculate_rho(100, 100, 30, 0.05, 0.2, "put") == pytest.approx(-0.03952, rel=1e-2)

if __name__ == "__main__": 
    pytest.main()