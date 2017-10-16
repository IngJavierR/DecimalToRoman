"""Mapa de numeros decimales y romanos 1 to 3999"""

ROMAN_MAP = {1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
             90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

def decimal_to_roman(decimal):
    """Convierte decimal a romano"""
    result = ""
    for value, numeral in sorted(ROMAN_MAP.items(), reverse=True):
        while decimal >= value:
            result += numeral
            decimal -= value
    return result

def main():
    """Main"""
    decimal = raw_input("Ingresa un numero decimal entero: ")
    roman = decimal_to_roman(int(decimal))
    print "El valor romano es: " + roman

if __name__ == "__main__":
    main()
