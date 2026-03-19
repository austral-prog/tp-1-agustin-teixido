def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    #variables
    impuesto_uno = precio_base * 0.21
    subtotal = impuesto_uno + impuesto_uno
    propina = subtotal * 0.10
    precio_final = subtotal + propina

    #prints
    print(impuesto_uno)
    print(subtotal)
    print(propina)
    print(precio_final)

price()


