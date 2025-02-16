import pytest
from src.calculations.volatility import *

def test_atm_call():
    vol = implied_volatility(market_price=5, P=100, S=100, T_days=30, r=0.05, option_type="call")
    assert vol == pytest.approx(0.4201, abs=0.001)

def test_atm_put():
    vol = implied_volatility(market_price=5, P=100, S=100, T_days=30, r=0.05, option_type="put")
    assert vol == pytest.approx(0.4561, abs=0.001)

def test_atm_call_dividends():
    vol = implied_volatility(market_price=5, P=100, S=100, T_days=30, r=0.05, option_type="call",q=0.08)
    assert vol == pytest.approx(0.4506, abs=0.001)

def test_atm_put_dividends():
    vol = implied_volatility(market_price=5, P=100, S=100, T_days=30, r=0.05, option_type="put",q=0.08)
    assert vol == pytest.approx(0.4289, abs=0.001)

def test_high_price_call():
    vol = implied_volatility(market_price=20, P=100, S=100, T_days=30, r=0.05, option_type="call")
    assert vol == pytest.approx(1.7525, abs=0.001)

def test_high_price_put():
    vol = implied_volatility(market_price=20, P=100, S=100, T_days=30, r=0.05, option_type="put")
    assert vol == pytest.approx(1.7896, abs=0.001)

def test_low_price_call():
    vol = implied_volatility(market_price=0.5, P=100, S=100, T_days=30, r=0.05, option_type="call")
    assert vol == pytest.approx(0.0212, abs=0.001)

def test_low_price_put():
    vol = implied_volatility(market_price=0.5, P=100, S=100, T_days=30, r=0.05, option_type="put")
    assert vol == pytest.approx(0.0601, abs=0.001)