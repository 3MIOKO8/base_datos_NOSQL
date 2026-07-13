import os

def limpiar_pantalla():
    """Limpia la consola o terminal (funciona en Windows y en sistemas basados en Unix/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")
