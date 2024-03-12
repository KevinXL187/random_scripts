def translate_with_key(input_string, key_table):
    # Check if the input string length is not divisible by 3
    if len(input_string) % 3 != 0:
        print("Input string length must be divisible by 3.")
        return ""

    # Split the input string into three-letter chunks
    chunks = [input_string[i:i+3] for i in range(0, len(input_string), 3)]

    # Translate each chunk using the key table
    translated_words = []
    for chunk in chunks:
        if chunk in key_table:
            translated_words.append(key_table[chunk])
        else:
            translated_words.append("???")

    # Join the translated words into a single string
    translated_string = " ".join(translated_words)
    return translated_string


# Example key table mapping three-letter combinations to words
key_table = {
    "UUU": "Phyenylalanine",
    "UUC": "Phyenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "stop",
    "UAG": "stop",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "stop",
    "UGG": "Tryptophan",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutatime",
    "CAG": "Glutatime",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "AGU": "Serine",
    "AGA": "Arginine",
    "AGC": "Serine",
    "AGG": "Arginine",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "GAU": "Aspartic Acid",
    "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid",
    "GAG": "Glutamic Acid",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"
    }

# Example input string
input_string = "AUGAGGAGAAAUACCUGACGCUCAAUGCAUUCCUUU"
input_string1 = "UAAAUGGUGGUCGCCUGACCCGGGAUGCCCAAGGGA"
input_string2 = "GUUCUGUAACGCAAGAUGGUUGACGAUUAAAUGCAC"
input_string3 = "AGGGUCAAAUGAAUGGACACCGUUCAGUGAGCAAGU"
input_string4 = "AUGACCGCUAACUCCUGAAUGUUCAGCAGGUAAAUG"
input_string5 = "UUCAGCCAUUGACAAAUGACCCCCCCACCGAGUGUU"
input_string6 = "UAACACAUGAGAUAAUGUAACUGAAUGCAUUCUAUU"
input_string7 = "UCAUCGUAG"


# Translate the input string using the key table
translated_result = translate_with_key(input_string, key_table)
translated_result1 = translate_with_key(input_string1, key_table)
translated_result2 = translate_with_key(input_string2, key_table)
translated_result3 = translate_with_key(input_string3, key_table)
translated_result4 = translate_with_key(input_string4, key_table)
translated_result5 = translate_with_key(input_string5, key_table)
translated_result6 = translate_with_key(input_string6, key_table)
translated_result7 = translate_with_key(input_string7, key_table)


print("Translated result:", translated_result)
print("Translated result:", translated_result1)
print("Translated result:", translated_result2)
print("Translated result:", translated_result3)
print("Translated result:", translated_result4)
print("Translated result:", translated_result5)
print("Translated result:", translated_result6)
print("Translated result:", translated_result7)
