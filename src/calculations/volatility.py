import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
from calculations.optionPrice import *

def implied_volatility(market_price, P, S, T_days, r, option_type, american=False):
    """
    Calcula la volatilidad implícita de una opción usando búsqueda numérica.

    :param market_price: Precio de mercado de la opción
    :param P: Precio actual del subyacente
    :param S: Precio de ejercicio
    :param T_days: Tiempo hasta la expiración en días
    :param r: Tasa libre de riesgo (decimal)
    :param option_type: "call" o "put"
    :param american: Booleano que indica si la opción es americana
    :return: Volatilidad implícita (decimal)
    """

    def objective_function(sigma):
        """Función que calcula la diferencia entre el precio teórico y el precio de mercado."""
        if american:
            return binomial_tree_price(P, S, T_days, r, sigma, option_type) - market_price
        else:
            return black_scholes_price(P, S, T_days, r, sigma, option_type) - market_price

    try:
        # Buscamos la raíz de la función (donde el precio teórico coincide con el precio de mercado)
        implied_vol = brentq(objective_function, 0.0001, 5.0, xtol=1e-6)
        return round(implied_vol, 5)
    except ValueError:
        # Si ocurre un error, devolvemos 0.00% de volatilidad
        print("Error al calcular la volatilidad implícita. Devolviendo 0.00%.")
        return 0.00