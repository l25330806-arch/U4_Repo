"""interpolacion_lineal — cuaderno 01.

Libro: ecuación (18.2). Recta por dos nodos, evaluada en ``x``.

La función devuelve **dos** cosas: el valor interpolado y el error. El error es
``None`` cuando no se da un tercer dato; si se da, se estima con (18.18).
"""

from ejercicios.interpolacion.error_estimado_interpolacion import (
    error_estimado_interpolacion,
)


def interpolacion_lineal(x0, y0, x1, y1, x, x2=None, y2=None):
    """Devuelve ``(y, error)``.

    y     : valor interpolado con la recta que pasa por (x0, y0) y (x1, y1).
    error : ``None`` si no hay tercer dato; si lo hay,
            ``R1 = f[x2,x1,x0] * (x - x0) * (x - x1)``.

    x2, y2 son OPCIONALES: puedes terminar el método sin usarlos y, cuando
    escribas ``error_estimado_interpolacion``, regresar aquí y activarlos.
    """
    def interpolacion_lineal(x0, y0, x1, y1, x, x2=None, y2=None):
    """ ...tu docstring tal cual... """
    m = (y1 - y0) / (x1 - x0)
    y = y0 + m * (x - x0)
    error = None
    return y, error
if __name__ == "__main__":
    # sin tercer dato: f(1)=0, f(4)=3  ->  (1.0, None)
    print(interpolacion_lineal(1, 0, 4, 3, 2))
    # con tercer dato: además del valor, el error estimado
    print(interpolacion_lineal(1, 0, 4, 3, 2, x2=6, y2=5))
