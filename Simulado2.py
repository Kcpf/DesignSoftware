import math

def reflexao_total_interna(n1, n2, o2):
    if (n2*math.sin(math.radians(o2)))/n1 > 1:
        return True
    return False