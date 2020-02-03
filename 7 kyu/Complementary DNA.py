def DNA_strand(dna):
    # code here
    chain = list('ACGT')
    reverse = list('TGCA')
    opp_chain = []
    for base in dna:
        chain_index = chain.index(base)
        opp_chain.append(reverse[chain_index])
    return ''.join(opp_chain)