def bissecao(f, a, b, eps1, eps2, kmax):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a e b devem ser números.")

    if not isinstance(eps1, (int, float)) or not isinstance(eps2, (int, float)):
        raise TypeError("As tolerâncias devem ser números.")

    if not isinstance(kmax, int):
        raise TypeError("kmax deve ser inteiro.")

    if eps1 <= 0 or eps2 <= 0:
        raise ValueError("As tolerâncias devem ser positivas.")

    if kmax <= 0:
        raise ValueError("kmax deve ser positivo.")

    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0

    if fb == 0:
        return b, 0

    if fa * fb > 0:
        raise ValueError("Não há mudança de sinal no intervalo.")

    for k in range(1, kmax + 1):

        m = (a + b) / 2
        fm = f(m)

        if abs(fm) <= eps2 or abs(b - a) <= eps1:
            return m, k

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    return (a + b) / 2, k