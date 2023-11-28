def to_rna(dna_strand):
    
    complement_strands = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U"
    }

    return_string = ""

    for i in dna_strand:
        if i in complement_strands:
            return_string += complement_strands[i]
        else:
            return_string += i
    
    return return_string
