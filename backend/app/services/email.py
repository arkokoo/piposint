import pprint
import subprocess
import os
import pandas as pd

def get_holehe(email):
    domain_values = []
    command = f"holehe --csv {email}"
    try:
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Attend que la commande se finisse
        result.communicate()

        files = [file for file in os.listdir('.') if file.startswith('holehe_') and file.endswith('.csv')]
        if files:
            file_path = files[0]
            data = pd.read_csv(file_path)
            filtered_data = data[data['exists'] == True]
            domain_values = filtered_data['domain'].tolist()
            os.remove(file_path)
    except Exception as e:
        pass
    return domain_values
