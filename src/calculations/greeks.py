import yfinance as yf
import numpy as np
from scipy.stats import norm
from datetime import datetime

# Calcular Delta usando el modelo de Black-Scholes
def calculate_delta(P, S, T, r, sigma, option_type):
    """
    Calcula el Delta de una opción usando el modelo de Black-Scholes.
    
    Parámetros:
    - P: Precio del activo subyacente
    - S: Precio de ejercicio
    - T: Tiempo hasta el vencimiento (en días)
    - r: Tasa de interés libre de riesgo
    - sigma: Volatilidad implícita
    - option_type: Tipo de opción ("call" o "put")

    """
    # Convertir el tiempo hasta el vencimiento en años
    T = T / 365.0
    
    # Calcular d1 usando la fórmula de Black-Scholes
    d1 = (np.log(P / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    # Calcular Delta dependiendo del tipo de opción
    if option_type == "call":
        delta = norm.cdf(d1)  # Delta para opciones call
    elif option_type == "put":
        delta = norm.cdf(d1) - 1  # Delta para opciones put
    else:
        raise ValueError("El tipo de opción debe ser 'call' o 'put'.")
    
    return round(delta, 4)