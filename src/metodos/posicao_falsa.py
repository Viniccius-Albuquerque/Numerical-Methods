def posicao_falsa(f, a, b, eps1, eps2, kmax):

#========================CONDICOES DE ERRO=====================================
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(kmax, int) or not isinstance(eps1, (int, float)) or not isinstance(eps2, (int, float)):
        raise TypeError("Os valores devem ser números.")

    if eps1 <= 0 or eps2 <= 0:
        raise ValueError("As tolerâncias devem ser maiores que zero.")

    if kmax <= 0:
        raise ValueError("kmax deve ser maior que zero.")
    
    if f(a) * f(b) > 0:
        raise ValueError("O intervalo não possui mudança de sinal.")
#==============================================================================

    if f(a) == 0:
        return a, 0

    if f(b) == 0:
        return b, 0

    k = 0
    while k < kmax:

        x = (a * f(b) - b * f(a)) / (f(b) - f(a))#formula padrao

        if abs(f(x)) < eps2:
            return x, k + 1

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        if abs(b - a) < eps1:
            return x, k + 1

        k += 1

    return x, k