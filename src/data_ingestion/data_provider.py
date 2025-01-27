import yfinance as yf
import numpy as np
import requests
from datetime import datetime

# Obtener el precio del activo subyacente
def get_stock_price(ticker):
    """
    Obtiene el precio actual del activo subyacente usando Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    return price


# Calcular el tiempo hasta el vencimiento (en días)
def get_time_to_expiry(expiry_date):
    """
    Calcula el tiempo restante hasta el vencimiento en días.
    """
    today = datetime.now()
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
    days_to_expiry = (expiry - today).days
    return max(days_to_expiry, 0)  # Garantiza que no sea negativo


def get_risk_free_rate():
    """
    Obtiene la tasa de interés libre de riesgo utilizando la API de Alpha Vantage.
    Devuelve la última tasa de los bonos del Tesoro a 3 meses como proxy de la tasa libre de riesgo.
    """
    API_KEY = "M4VA9A2I0200H96E"  # Reemplaza con tu clave de Alpha Vantage
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TREASURY_YIELD",
        "interval": "daily",
        "maturity": "3month",  # Bono del Tesoro a 3 meses
        "apikey": API_KEY,
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extraer la última tasa disponible
        yields = data.get("data", [])
        if yields:
            last_yield = float(yields[0]["value"]) / 100  # Convertir a decimal (de %)
            return last_yield
        else:
            raise ValueError("No se encontraron datos de tasas de interés.")
    
    except Exception as e:
        print(f"Error al obtener la tasa de interés libre de riesgo desde la API: {e}")
        return None

