def to_rna(dna_strand):
    '''
    Given a DNA strand, return its RNA complement (per RNA transcription).
    Both DNA and RNA strands are a sequence of nucleotides.
    The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
    The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
    Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
    G -> C
    C -> G
    T -> A
    A -> U

    :param dna_strand: One DNA nucleotide from GCTA
    :return: its transcribed RNA strand
    '''

    convertion_dict = {"G":"C",
                       "C":"G",
                       "T":"A",
                       "A":"U"}

    new_string = ""

    for nucledotide in dna_strand:
        new_string += convertion_dict[nucledotide]

    return new_string
