import numpy as np
from scipy.stats import norm
from scipy.optimize import bisect

def calculate_option_price(P, S, T_days, r, sigma, option_type, q=0):
    """
    Calcula el precio de una opción usando Black-Scholes con dividendos.
    """
    return black_scholes_price(P, S, T_days, r, sigma, option_type, q)
    


def black_scholes_price(P, S, T_days, r, sigma, option_type, q=0):
    """
    Calcula el precio de una opción usando el modelo de Black-Scholes con dividendos.

    :param P: Precio actual del subyacente
    :param S: Precio de ejercicio
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (decimal)
    :param sigma: Volatilidad del subyacente (decimal)
    :param option_type: "call" o "put"
    :param q: Tasa de dividendos (decimal)
    :return: Precio de la opción
    """
    T = T_days / 365  # Convertimos días a años
    d1 = (np.log(P / S) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        return P * np.exp(-q * T) * norm.cdf(d1) - S * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return S * np.exp(-r * T) * norm.cdf(-d2) - P * np.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("El parámetro 'option_type' debe ser 'call' o 'put'.")

