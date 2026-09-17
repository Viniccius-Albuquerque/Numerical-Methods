def newton_raphson(f, df, x0, eps1, eps2, kmax):

    if not isinstance(x0, (int, float)):
        raise TypeError("x0 deve ser um número.")

    if not isinstance(eps1, (int, float)) or not isinstance(eps2, (int, float)):
        raise TypeError("as tolerâncias devem ser números.")

    if not isinstance(kmax, int):
        raise TypeError("kmax deve ser inteiro.")

    if eps1 <= 0 or eps2 <= 0:
        raise ValueError("as tolerâncias devem ser positivas.")

    if kmax <= 0:
        raise ValueError("kmax deve ser positivo.")

    x = x0
    fx = f(x)

    if abs(fx) <= eps2:
        return x, 0

    for k in range(1, kmax + 1):

        dfx = df(x)

        if dfx == 0:
            raise ValueError("a derivada é zero. não é possível continuar.")

        x_novo = x - fx / dfx
        fx_novo = f(x_novo)

        if abs(x_novo - x) <= eps1 or abs(fx_novo) <= eps2:
            return x_novo, k

        x = x_novo
        fx = fx_novo

    return x, kmax