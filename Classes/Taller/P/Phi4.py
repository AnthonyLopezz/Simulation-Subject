# Anthony Jardiel López Pérez || 2271557

def phi4(n):
    result = 0.0
    for n in range(terms):
        result += (-1)**n/(2*n+1)
    return 4*result


terms = int(input("Enter number of terms: "))
pi = phi4(terms)
print("Pi = ", pi)
