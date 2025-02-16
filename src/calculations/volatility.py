import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.calculations.optionPrice import *

def implied_volatility(market_price, P, S, T_days, r, option_type, q=0):
    """
    Calcula la volatilidad implícita de una opción usando Black-Scholes con dividendos.
    """
    def objective_function(sigma):
        return black_scholes_price(P, S, T_days, r, sigma, option_type, q) - market_price
    
    try:
        implied_vol = brentq(objective_function, 0.0001, 5.0, xtol=1e-6)
        return round(implied_vol, 5)
    except ValueError:
        print("Error al calcular la volatilidad implícita. Devolviendo 0.00%.")
        return 0.00