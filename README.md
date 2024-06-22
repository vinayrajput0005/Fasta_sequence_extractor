# Fasta_sequence_extractor
This Python script extracts specific FASTA sequences from a larger FASTA file based on a list of desired headers provided in a separate txt file.

Features:

    Uses Biopython library for efficient FASTA parsing.

    Filters sequences based on a list of desired headers in a txt file.
    Prints IDs of extracted sequences for verification.
    Writes extracted sequences to a new FASTA file.

Usage:

    Install Biopython: pip install biopython
    Save the script as a Python file (e.g., extract_fasta.py).
    Update the file paths in the script:
        fasta_file: Path to your FASTA file containing all sequences.
        header_file: Path to the txt file containing desired sequence headers (one per line).
        output_file: Path to the desired output FASTA file where extracted sequences will be written.
    Run the script from the command line: python extract_fasta.py

Example Files:

    Sequence.fasta: Your original FASTA file containing all sequences.
    ID.txt: A text file containing the headers of sequences you want to extract (one header per line).
    extract_sequences.fasta: The output FASTA file containing the extracted sequences.

How it Works:

The script defines a function called extract_fasta that takes three arguments: the FASTA file path, the header file path, and the output file path. It then:

    Reads the desired headers from the txt file into a set for efficient lookups.
    Opens the output file for writing in FASTA format.
    Iterates through each FASTA record in the original file.
    Checks if the current record's header is present in the set of desired headers.
    If a match is found, it prints the extracted sequence ID and writes the entire record (header and sequence) to the output file.

Additional Notes:

    Ensure the headers in the txt file exactly match the headers (including ">" symbol) present in your FASTA file.
    The script handles case sensitivity based on how your FASTA file was generated.
