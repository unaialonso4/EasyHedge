import yfinance as yf
import numpy as np
import requests
import finnhub
from datetime import datetime

# Obtener el precio del activo subyacente
def get_stock_price(ticker):
    """
    Obtiene el precio actual del activo subyacente usando Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    return price


def get_company_location(ticker):
    """
    Obtiene la ubicación geográfica de la empresa asociada a un ticker.
    
    Parámetros:
    - ticker: El símbolo bursátil de la empresa (ejemplo: "AAPL" para Apple).
    
    Devuelve:
    - Código de la región/ubicación (ej. "US", "EU", "UK", "JP") si está disponible.
    - None si no se puede determinar la ubicación.
    """
    try:
        # Descargar información de la empresa
        stock = yf.Ticker(ticker)
        info = stock.info

        # Extraer la ubicación de la empresa (país)
        country = info.get("country", None)

        if country:
            # Mapeo de países a códigos de región estándar
            country_to_location = {
                "United States": "US",
                "United Kingdom": "UK",
                "Japan": "JP",
                "Germany": "EU",
                "France": "EU",
                "Italy": "EU",
                "Spain": "EU",
                "Netherlands": "EU",
                "Belgium": "EU",
                "Luxembourg": "EU",
                "Switzerland": "EU",
                # Añadir más mapeos si es necesario
            }

            # Devolver la ubicación en formato estándar
            return country_to_location.get(country, "US")  # Predeterminado: "US"

        else:
            raise ValueError("No se encontró información de país para el ticker.")

    except Exception as e:
        print(f"Error al obtener la ubicación de la empresa para el ticker {ticker}: {e}")
        return None


def get_risk_free_rate():
    """
    Obtiene la tasa de interés libre de riesgo de EE.UU. utilizando Alpha Vantage 
    (rendimiento de bonos del Tesoro a 3 meses).
    """
    # API Key para Alpha Vantage
    ALPHA_VANTAGE_API_KEY = "M4VA9A2I0200H96E"  # Reemplaza con tu clave de Alpha Vantage

    try:
        # Usar Alpha Vantage para obtener la tasa de interés libre de riesgo en EE.UU.
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TREASURY_YIELD",
            "interval": "daily",
            "maturity": "3month",  # Bono del Tesoro a 3 meses
            "apikey": ALPHA_VANTAGE_API_KEY,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extraer la última tasa disponible
        yields = data.get("data", [])
        if yields:
            last_yield = float(yields[0]["value"]) / 100  # Convertir a decimal (de %)
            return round(last_yield, 6)
        else:
            raise ValueError("No se encontraron datos de tasas de interés para US.")
    except Exception as e:
        print(f"Error al obtener la tasa de interés libre de riesgo: {e}")
        return None
    
