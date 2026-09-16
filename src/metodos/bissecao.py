def bissecao(f, a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("O intervalo não possui mudança de sinal.")

    for i in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)

        if abs(fm) < tol:
            return m, i

        if f(a) * fm < 0:
            b = m
        else:
            a = m

    return m, max_iter