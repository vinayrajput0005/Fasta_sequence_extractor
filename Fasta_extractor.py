###Code Written By:Vinay Rajput, Email : srm.vinay0005@gmail.com 

from Bio import SeqIO


def extract_fasta(fasta_file, header_file, output_file):
  """
  Extracts fasta sequences from a fasta file based on headers in a separate txt file.

  Args:
    fasta_file: Path to the fasta file.
    header_file: Path to the txt file containing desired headers (one per line).
    output_file: Path to the output fasta file.
  """
  # Set to store desired headers
  desired_headers = set()
  # Read desired headers from txt file
  with open(header_file, 'r') as f:
    for line in f:
      desired_headers.add(line.strip())

  # Open output file for writing in fasta format
  with open(output_file, 'w') as out_f:
    # Iterate through fasta records
    for record in SeqIO.parse(fasta_file, 'fasta'):
      header = record.id
      # Check if header is present in desired set
      if header in desired_headers:
        # Print extracted ID
        print(f"Extracted sequence ID: {header}")
        # Write sequence to output file in fasta format
        SeqIO.write(record, out_f, 'fasta')


# Replace with your file paths
fasta_file = 'Sequence.fasta'
header_file = 'ID.txt'
output_file = 'Extract_sequences.fasta'

# Run the extraction function
extract_fasta(fasta_file, header_file, output_file)

print(f"Extracted sequences written to: {output_file}")

