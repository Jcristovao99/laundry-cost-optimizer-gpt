# optimizer.py
def optimize_order(items, delivery_location="default"):
    if not isinstance(items, dict):
        raise ValueError("O campo 'items' deve ser um dicionário.")

    total = 0
    detalhes = []

    precos = {
        "peca_variada": 0.80,
        "camisa": 0.75,
        "vestido_simples": 7.0,
        "vestido_frisado": 12.5,
        "fato": 5.5,
        "casaco": 3.5,
        "toalha": 3.5,
        "lencol": 1.0
    }

    for tipo, qtd in items.items():
        if not isinstance(qtd, (int, float)):
            continue  # ignora entradas inválidas
        preco_unit = precos.get(tipo, 0)
        subtotal = preco_unit * qtd
        total += subtotal
        detalhes.append({
            "tipo": tipo,
            "quantidade": qtd,
            "preco_unitario": preco_unit,
            "subtotal": round(subtotal, 2)
        })

    if isinstance(delivery_location, str) and delivery_location.lower() == "montijo":
        total += 5

    return {
        "total_cost": round(total, 2),
        "entrega": delivery_location,
        "detalhes": detalhes
    }
