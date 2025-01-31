import yfinance as yf
import numpy as np
import requests
import finnhub
from datetime import datetime

def get_time_to_expiry(expiry_date):
    """
    Calcula el tiempo restante hasta el vencimiento en días, asegurando que el cálculo sea preciso.
    """
    today = datetime.now().date() 
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()
    days_to_expiry = (expiry - today).days
    return max(days_to_expiry, 0)  # Garantiza que no sea negativo
