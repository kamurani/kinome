
import pandas as pd 

from pathlib import Path
from kinome import DATASET_DIR

kinase_table_path = DATASET_DIR / "kinase_table.tsv"

kinase_table = pd.read_csv(kinase_table_path, sep="\t")

# rename 
kinase_table = kinase_table.rename(
    columns={
        "xName": "x_name",
        "Manning Name": "manning", 
        "HGNC Name": "hgnc",
        "Kinase Name": "kinase",
        "Group": "group",
        "Family": "family",
        "SubFamily": "subfamily",
        "UniprotID": "uniprot_id",
})

