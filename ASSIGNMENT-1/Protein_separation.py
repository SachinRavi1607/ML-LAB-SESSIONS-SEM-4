def segregate_pdb(input_file):
    protein_atoms = []
    ligand_atoms = []
    water_atoms = []

    with open(input_file, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('ATOM'):
                protein_atoms.append(line)
            elif line.startswith('HETATM'):
                residue_name = line[17:20].strip()
                if residue_name == 'HOH':
                    water_atoms.append(line)
                else:
                    ligand_atoms.append(line)

    return protein_atoms, ligand_atoms, water_atoms

def write_pdb(output_file, atoms):
    with open(output_file, 'w') as pdb_file:
        pdb_file.write(''.join(atoms))

import os

input_pdb_file = r"C:\Users\SACHIN.R\Downloads\1n27.pdb"
output_folder = r"C:\Users\SACHIN.R\Downloads"

if os.path.exists(input_pdb_file):
    protein_atoms, ligand_atoms, water_atoms = segregate_pdb(input_pdb_file)

    os.makedirs(output_folder, exist_ok=True)

    write_pdb(os.path.join(output_folder, 'protein.txt'), protein_atoms)
    write_pdb(os.path.join(output_folder, 'ligand.txt'), ligand_atoms)
    write_pdb(os.path.join(output_folder, 'water.txt'), water_atoms)

    print("Output files saved successfully.")
else:
    print(f"File not found: {input_pdb_file}")