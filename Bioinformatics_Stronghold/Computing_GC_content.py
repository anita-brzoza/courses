from Bio import SeqIO

def computing_GC_content(path_and_filename):
    """
    The function that opens .fasta files and then calculates the GC content of each sequence 
    and returns the ID of the sequence with the highest GC content and its value.
    """

    try: 
        ids = [file.id for file in SeqIO.parse(path_and_filename, "fasta")]
        sequences = [str(file.seq) for file in SeqIO.parse(path_and_filename, "fasta")]

    except FileNotFoundError:
        print("File not found")

    else:
        GC_content = []

        for sequence in sequences:
            sequence_lenght = len(sequence)
            gc_count = [sequence.count(nucleotide) for nucleotide in "GC"]
            sequence_gc_content = round(((gc_count[0] + gc_count[1]) / sequence_lenght) * 100, 6)
            GC_content.append(sequence_gc_content)
        
        highest_GC_content = max(GC_content)
        print(ids[GC_content.index(highest_GC_content)], highest_GC_content)
