import pytest
from src.calculations.optionPrice import *

def test_call_option():
    price = calculate_option_price(P=100, S=100, T_days=30, r=0.05, sigma=0.233, option_type="call")
    assert price == pytest.approx(2.869, rel=1e-3)

def test_put_option():
    price = calculate_option_price(P=100, S=100, T_days=30, r=0.05, sigma=0.233, option_type="put")
    assert price == pytest.approx(2.459, rel=1e-3)

def test_call_option_dividends():
    price = calculate_option_price(P=100, S=100, T_days=30, r=0.05, sigma=0.233, option_type="call", q=0.08)
    assert price == pytest.approx(2.529, rel=1e-3)

def test_put_option_dividends():
    price = calculate_option_price(P=100, S=100, T_days=30, r=0.05, sigma=0.233, option_type="put", q=0.08)
    assert price == pytest.approx(2.775, rel=1e-3)

def test_itm_call():
    price = calculate_option_price(P=120, S=100, T_days=30, r=0.05, sigma=0.233, option_type="call")
    assert price == pytest.approx(20.416, rel=1e-3)

def test_itm_put():
    price = calculate_option_price(P=80, S=100, T_days=30, r=0.05, sigma=0.233, option_type="put")
    assert price == pytest.approx(19.591, rel=1e-3)

def test_deep_otm_call():
    price = calculate_option_price(P=50, S=100, T_days=30, r=0.05, sigma=0.233, option_type="call")
    assert price == pytest.approx(0.0, rel=1e-3)

def test_deep_otm_put():
    price = calculate_option_price(P=150, S=100, T_days=30, r=0.05, sigma=0.233, option_type="put")
    assert price == pytest.approx(0.000, abs=0.001)