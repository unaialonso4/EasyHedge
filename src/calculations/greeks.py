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


def calculate_gamma(S, K, T_days, r, sigma):
    """
    Calcula la Gamma de una opción utilizando el modelo de Black-Scholes.

    Parámetros:
    - S: Precio actual del activo subyacente.
    - K: Precio de ejercicio de la opción.
    - T_days: Tiempo hasta la expiración en días.
    - r: Tasa de interés libre de riesgo (en decimal).
    - sigma: Volatilidad del activo subyacente (en decimal).

    """
    if T_days <= 0 or sigma <= 0 or S <= 0:
        raise ValueError("Tiempo a vencimiento, volatilidad y precio del activo deben ser mayores que cero.")

    # Convertir días a años
    T = T_days / 365.0  

    # Cálculo de d1 (Black-Scholes)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    # Cálculo de Gamma
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    return gamma

def calculate_vega(P, S, T_days, r, sigma):
    """
    Calcula la Vega de una opción utilizando el modelo de Black-Scholes.

    Parámetros:
    - S: Precio actual del activo subyacente.
    - K: Precio de ejercicio de la opción.
    - T_days: Tiempo hasta la expiración en días.
    - r: Tasa de interés libre de riesgo (en decimal).
    - sigma: Volatilidad del activo subyacente (en decimal).

    """
    if T_days <= 0 or sigma <= 0 or S <= 0:
        raise ValueError("Tiempo a vencimiento, volatilidad y precio del activo deben ser mayores que cero.")

    # Convertir días a años
    T = T_days / 365.0  

    # Cálculo de d1 (Black-Scholes)
    d1 = (np.log(P / S) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    # Cálculo de Vega
    vega = P * np.sqrt(T) * norm.pdf(d1)

    return vega/100

def calculate_theta(P, S, T_days, r, sigma, option_type="call"):
    """
    Calcula la Theta de una opción usando el modelo de Black-Scholes.

    :param P: Precio actual del subyacente
    :param S: Precio de ejercicio de la opción
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (en decimal, no en porcentaje)
    :param sigma: Volatilidad del subyacente (en decimal, no en porcentaje)
    :param option_type: "call" o "put"
    """
    T = T_days / 365  # Convertimos días a años
    if T <= 0:
        return 0

    d1 = (np.log(P / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    pdf_d1 = norm.pdf(d1)
    cdf_d1 = norm.cdf(d1)
    cdf_d2 = norm.cdf(d2)

    term1 = (-P * pdf_d1 * sigma) / (2 * np.sqrt(T))  # Decadencia del tiempo
    
    if option_type == "call":
        term2 = -r * S * np.exp(-r * T) * cdf_d2  # Ajuste por tasa de interés
        theta = term1 + term2
    else: 
        term2 = -r * S * np.exp(-r * T) * norm.cdf(-d2)
        theta = term1 - term2 

    return theta / 365 

def calculate_rho(P, S, T_days, r, sigma, option_type):
    """
    Calcula la Rho de una opción usando el modelo de Black-Scholes.
    
    :param S: Precio actual del subyacente
    :param K: Precio de ejercicio de la opción
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (en decimal, no en porcentaje)
    :param sigma: Volatilidad del subyacente (en decimal, no en porcentaje)
    :param option_type: "call" o "put"
    """
    T = T_days / 365  # Convertimos días a años
    if T <= 0:
        return 0

    d1 = (np.log(P / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    cdf_d2 = norm.cdf(d2)
    
    if option_type == "call":
        rho = S * T * np.exp(-r * T) * cdf_d2
    else:  # Opción put
        rho = -S * T * np.exp(-r * T) * norm.cdf(-d2)

    return rho / 100  # Ajustamos para que refleje cambio por 1% de tasa de interés