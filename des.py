# Global matrix variables, they start at 1 when 0 is used in python lists so -1 is done on all called positions

# Initial Permutation (IP)
ip = [
58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7
]

# Final Permutation (FP)
fp = [
40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25
]

# Expansion E (32 → 48 bits)
e = [
32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,
12,13,14,15,16,17,16,17,18,19,20,21,
20,21,22,23,24,25,24,25,26,27,28,29,
28,29,30,31,32,1
]

# Permutation P (32 → 32 bits)
p = [
16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25
]

# PC-1 (64 → 56 bits)
pc1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,
10,2,59,51,43,35,27,19,11,3,60,52,44,36,
63,55,47,39,31,23,15,7,62,54,46,38,30,22,
14,6,61,53,45,37,29,21,13,5,28,20,12,4
]

# PC-2 (56 → 48 bits)
pc2 = [
14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,
26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,
51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32
]

# S-boxes (8 boxes, each 4x16)
sbox = [
# S1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# S2
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
# S3
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
# S4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
# S5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# S6
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
# S7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# S8
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

# left shift schedule
shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# Function to convert between 1 to 8 character long ASCII string into 64 bits in list,
# padding is PKCS-style for ONE BLOCK only even with maximum 8 characters used
def ascii_to_bits_in_list(h):
  
    list_to_dec = []
    # Characters into decimal list
    for character in h:
        list_to_dec.append(ord(character))
    list_of_64bit_inputs = []

    # Creates new list with padding using previous list
    for x in range(8):
        if x < len(list_to_dec):
            list_of_64bit_inputs.append(list_to_dec[x])
        else:
            list_of_64bit_inputs.append(8-len(list_to_dec))

    # Creates input_as_bits variable which is previous list as bits
    input_as_bits = ""
    for x in list_of_64bit_inputs:
        input_as_bits += format((x), '08b').replace("0b","")

    bit_as_list = list(input_as_bits)
    return bit_as_list

# PC1 permutation done on 64 bits of KEY, every eight bit is removed
# bits are rearanged according to PC1 order
def pci1_func(bits_list_64):
    bit_56_pci1 = []

    for y in range(0,56):
        bit_56_pci1.append(bits_list_64[pc1[y]-1])
    return bit_56_pci1

# Kn(1-16) are calculated based on PC1 input
# Kn are saved for future use
def ki16_subkey_func(pci1_56bit_input):
    # C0 left half of PC1 input, D0 is right
    sub_key_half_length = int(len(pci1_56bit_input)/2)
    c0 = pci1_56bit_input[:sub_key_half_length]
    d0 = pci1_56bit_input[sub_key_half_length:]
    z = 0
    ki = []
    # C0 and D0 are shifted left acording to shifts list
    # PC2 is done to make 56 bit into 48bit keys
    # process repeated 16 times and 48bit keys saved
    while z < 16:
        
        c0 = c0[shifts[z]:] + c0[:shifts[z]]
        d0 = d0[shifts[z]:] + d0[:shifts[z]]
        combined =  c0 + d0
        ki.append([])
        for x in range(0, int(len(pc2))):
            ki[z].append(combined[pc2[x]-1])
        z += 1
    return ki

# Function to use Kn 48 bit subkeys keys with input text 64 bit for encryption
def k1_to_16_xor_round_substitition(ascii_to_binary, kn):
    # Initial permutation is done on 64 bits, bits are rearanged according to IP matrix
    ip_applied = []
    for y in range(0,64):
        ip_applied.append(ascii_to_binary[ip[y]-1])

    # LN is variable for L(1-16), RN(1-16)
    # LN is left half and RN right half
    ln = ip_applied[:32]
    rn = ip_applied[32:]
    for round_one_to_sixteen in range(0,16):
        # RN is explanded from 32 to 48 bits to equal subkey length
        expanded_rn = []
        for y in range(0,48):
            expanded_rn.append(rn[e[y]-1])
        # RN XOR KN(y)
        xored = [int(int(a) ^ int(b)) for a, b in zip(expanded_rn, kn[round_one_to_sixteen])]
        # This XORED 48 bit expanded RN is devided into eight - six bit blocks
        xored_into_sixths = [xored[i:i+6] for i in range(0, 48, 6)]
        # Blocks are substituted according to S1-8 constants
        # A blocks first and last bit determin row of substitution matrix
        # , and second to fifth determine column
        substitution_n = []
        for x in range(0,8): 
            # Bits are shifted to combine column and row information
            # grouped 1 << 6, 2 << 3 << 4 << 5, example 011001 is 01 and 1100
            row_value = (xored_into_sixths[x][0] << 1) | xored_into_sixths[x][5]
            column_value = 0
            for bit in [xored_into_sixths[x][1], xored_into_sixths[x][2], xored_into_sixths[x][3], xored_into_sixths[x][4]]:
                column_value = (column_value << 1) | bit
            substitution_n.append(sbox[x][row_value][column_value])
        # int to four bits values, combined, split into list
        sub_full_as_32bits = [format(x, '04b') for x in substitution_n]
        sub_full_as_32bits = "".join(sub_full_as_32bits)
        sub_full_as_32bits = list(sub_full_as_32bits)
        # permutation operation on 32 bits
        permutated_substituted_32 = []
        for y in range(0,32):
            permutated_substituted_32.append(sub_full_as_32bits[p[y]-1])
        permutated_substituted_32 = "".join(permutated_substituted_32)
        # LN = original RN
        # RN = LN XOR previous permutated 32 bit containing substituted blocks
        ln_old = ln
        ln = rn
        rn = [str(int(a) ^ int(b)) for a, b in zip(ln_old, permutated_substituted_32)]
        # Repeat loop updating LN and RN
        temp_ln = "".join(ln)
        temp_rn = "".join(rn)

    # After 16 rounds of split, expland right side, XOR with sub key, split, substitute, permutate, update LN RN
    # Swop RN and LN place, final permutation
    final_cypher = rn + ln
    final_permutation_applied = []
    for y in range(0,64):
        final_permutation_applied.append(final_cypher[fp[y]-1])
    # Encryption  complete, display as hex
    final_permutation_applied = "".join(final_permutation_applied)
    encryption_hex = hex(int(final_permutation_applied, 2))[2:].zfill(16)

    return encryption_hex

# Function for DES operations: ASCI to bits for eight byte key & plaintext
# Kn 16 subkeys
# Plaintext XOR subkeys and substitution
def des_encrypt(plaintext, key):#

    key_bits = ascii_to_bits_in_list(key)
    plaintext_bits = ascii_to_bits_in_list(plaintext)
    subkeys = ki16_subkey_func(pci1_func(key_bits))
    return k1_to_16_xor_round_substitition(plaintext_bits, subkeys)
# Example key and plaintext test
def main():

    key = list("12345678")
    plaintext_input = list("12345678")

    ciphertext = des_encrypt(plaintext_input, key)
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()