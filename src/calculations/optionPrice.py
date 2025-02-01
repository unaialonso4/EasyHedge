import numpy as np
from scipy.stats import norm
from scipy.optimize import bisect

def calculate_option_price(P, S, T_days, r, sigma, option_type, style="european"):
    """
    Calcula el precio de una opción, eligiendo el modelo adecuado según su tipo.

    :param P: Precio actual del subyacente
    :param S: Precio de ejercicio
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (decimal)
    :param sigma: Volatilidad del subyacente (decimal)
    :param option_type: "call" o "put"
    :param style: "european" o "american"
    :return: Precio de la opción
    """
    if style == "european":
        return black_scholes_price(P, S, T_days, r, sigma, option_type)
    elif style == "american":
        return binomial_tree_price(P, S, T_days, r, sigma, option_type)
    else:
        raise ValueError("Estilo de opción no soportado. Usa 'european' o 'american'.")
    
def black_scholes_price(P, S, T_days, r, sigma, option_type):
    """
    Calcula el precio de una opción europea usando el modelo de Black-Scholes.

    :param P: Precio actual del subyacente
    :param S: Precio de ejercicio
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (decimal)
    :param sigma: Volatilidad del subyacente (decimal)
    :param option_type: "call" o "put"
    :return: Precio de la opción
    """
    T = T_days / 365  # Convertimos días a años
    if T <= 0:
        return max(0, P - S) if option_type == "call" else max(0, S - P)

    d1 = (np.log(P / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = P * norm.cdf(d1) - S * np.exp(-r * T) * norm.cdf(d2)
    else:  
        price = S * np.exp(-r * T) * norm.cdf(-d2) - P * norm.cdf(-d1)

    return price

def binomial_tree_price(P, S, T_days, r, sigma, option_type, N=100):
    """
    Calcula el precio de una opción americana usando el modelo de Árbol Binomial.

    :param S: Precio actual del subyacente
    :param K: Precio de ejercicio
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (decimal)
    :param sigma: Volatilidad del subyacente (decimal)
    :param option_type: "call" o "put"
    :param N: Número de pasos en el árbol binomial
    :return: Precio de la opción
    """
    T = T_days / 365  # Convertimos días a años
    dt = T / N  # Tamaño de cada paso
    u = np.exp(sigma * np.sqrt(dt))  # Factor de subida
    d = 1 / u  # Factor de bajada
    p = (np.exp(r * dt) - d) / (u - d)  # Probabilidad de subida ajustada al riesgo

    # Inicializar la matriz de precios del subyacente
    stock_price = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            stock_price[j, i] = P * (u ** (i - j)) * (d ** j)

    # Inicializar valores de la opción en el último nodo
    option_price = np.zeros((N + 1, N + 1))
    for j in range(N + 1):
        if option_type == "call":
            option_price[j, N] = max(0, stock_price[j, N] - S)
        else:  # Put
            option_price[j, N] = max(0, S - stock_price[j, N])

    # Hacer el recorrido inverso en el árbol para calcular el valor en t=0
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            intrinsic_value = max(0, stock_price[j, i] - S) if option_type == "call" else max(0, S - stock_price[j, i])
            expected_value = np.exp(-r * dt) * (p * option_price[j, i + 1] + (1 - p) * option_price[j + 1, i + 1])
            option_price[j, i] = max(intrinsic_value, expected_value)  # Máximo entre ejercicio temprano y hold

    return option_price[0, 0]  # Precio de la opción en t=0