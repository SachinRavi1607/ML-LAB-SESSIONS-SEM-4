import os
import urllib.request
import sys

def download_pdb(pdbcode, datadir, downloadurl="https://files.rcsb.org/download/"):
    pdbfn = pdbcode + ".pdb"
    url = downloadurl + pdbfn
    outfnm = os.path.join(datadir, pdbfn)

    # Create the output directory if it doesn't exist
    os.makedirs(datadir, exist_ok=True)

    try:
        urllib.request.urlretrieve(url, outfnm)
        return outfnm
    except Exception as err:
        print(f"Error downloading {pdbcode}: {str(err)}", file=sys.stderr)
        return None

if __name__ == "__main__":
    variant_codes = ["1HIV", "1PRP", "1DFH", "5E2W", "6RRS", "1PBW", "1PDP", "1PBD", "6Y41", "6FUC"]

    data_dir = "Output_PDBFiles"
    log_file_path = "downloaded_files.txt"

    with open(log_file_path, 'a') as log_file:
        for pdb_code in variant_codes:
            downloaded_file = download_pdb(pdb_code, data_dir)

            if downloaded_file:
                print(f"Downloaded PDB file for {pdb_code}: {downloaded_file}")
                log_file.write(f"{downloaded_file}\n")
            else:
                print(f"Failed to download PDB file for code: {pdb_code}")
