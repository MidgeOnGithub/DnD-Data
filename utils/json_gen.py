import json
from pathlib import Path

# Import Python script files from which to generate JSONS
import races as r


def generate_files(j_data, f_name: str):
    """
    Dumps JSON data to a file.

    Arguments:
    j_data -- JSON string to be written
    f_name -- full path and name of file to create/overwrite
    """
    with open(f_name, mode='w') as out:
        json.dump(j_data, out)


# Get directory of this script file, move to parent `data`
# .parent[1] = .parent.parent but former is incompatible with Windows
dir = Path(__file__).resolve().parent.parent
# Iterate over all imported data-holding files
for z in [r]:
    file_name = Path(dir, z.__name__).with_suffix('.json')
    generate_files(z.data, file_name)
    print(f'Successfully wrote {z.__name__} to {file_name}!')