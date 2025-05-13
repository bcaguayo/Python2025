class Utils:
    """
    Convert a column letter to an index.
    """
    # [A1, B2, C3, D4, E5, F6, G7, H8, I9, J10]
    # [K11, L12, M13, N14, O15, P16, Q17, R18, S19, T20] 
    # [U21, V22, W23, X24, Y25, Z26]
    # AA -> 27, AB -> 28, AC -> 29, AD -> 30, AE -> 31,
    # AF -> 32, AG -> 33, AH -> 34, AI -> 35, AJ -> 36,
    # AK -> 37, AL -> 38, AM -> 39, AN -> 40, AO -> 41,
    # AP -> 42, AQ -> 43, AR -> 44, AS -> 45, AT -> 46,
    # AU -> 47, AV -> 48, AW -> 49, AX -> 50, AY -> 51, AZ -> 52,
    # BA -> 53, ..., ZZ -> 702

    def toIndex(c: chr) -> int:
        return ord(c.upper()) - ord('A') + 1
    
    def toIndexes(s: str) -> int:
        """
        Convert a string of letters to a list of indexes.
        """
        index = 0
        first = True
        for c in s:
            if first:
                index += Utils.toIndex(c)
                first = False
            else:
                index += 26 + Utils.toIndex(c) - 1
        return index