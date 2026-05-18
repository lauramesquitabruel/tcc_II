import os
import re
import csv
from pathlib import Path

def main():
    #models = ["cg", "cs", "cb"]
    models = ["cg"]
    instances = {}

    for model in models:

        log_dir = Path(f'logs/{model}')
        for file in log_dir.glob("rmcsp_*.txt"):
            filename = file.name
            
            match1 = re.search(rf"rmcsp_(\d+)_(\d+)_(\d+)_([\d.]+)-", filename)
            match2 = re.search(rf"rmcsp_(\d+)_(\d+)_(\d+)_(\d+)-", filename)
            match3 = re.search(rf"rmcsp_(\d+)-", filename)

            s1, s2, sigma, frac = "Random", "Random", "Random", "Random"
            instance_key = None

            if match1:
                print(match1)
                s1, sigma, seed, frac = match1.groups()
                s2 = s1
                instance_key = (s1, sigma, seed, frac)
            elif match2:
                print(match2) 
                s1, s2, sigma, seed = match2.groups()
                frac = "Random"
                instance_key = (s1, s2, sigma, seed)
            elif match3:
                print(match3)
                index = int(match3.group(1))
                if index > 4:
                    s1, s2, sigma, frac = "1000", "1000", "1000", "Random"
                instance_key = (str(index))

            model_type = model.upper()
            
            if instance_key not in instances:
                instances[instance_key] = {
                    '|∑|': sigma, '|s1|': s1, '|s2|': s2, 'Fração de operações conservativas': frac,
                    'CG': {}, 'CS': {}, 'CB': {}
                }
                
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                best_obj = re.search(r'Best objective\s+([e\d.+\-]+)', content)
                best_bd = re.search(r'best bound\s+([e\d.+\-]+)', content)
                gap = re.search(r'gap\s+([e\d.+\-%]+)', content)
                
                t_estruturas = re.search(r'Tempo de execução para criação das estruturas:\s+([\d.]+)', content)
                t_modelo = re.search(r'Tempo de execução do modelo:\s+([\d.]+)', content)
                t_total = re.search(r'Tempo de execução total:\s+([\d.]+)', content)
                
                metrics = {
                    'Best objective': best_obj.group(1) if best_obj else 'N/A',
                    'Best bound': best_bd.group(1) if best_bd else 'N/A',
                    'Gap': gap.group(1) if gap else 'N/A',
                    'Tempo de criação das estruturas': t_estruturas.group(1) if t_estruturas else 'N/A',
                    'Tempo de execução do modelo': t_modelo.group(1) if t_modelo else 'N/A',
                    'Tempo total': t_total.group(1) if t_total else 'N/A'
                }
                
                instances[instance_key][model_type] = metrics


    headers = [
        '|∑|', '|s1|', '|s2|', 'Fração de operações conservativas',
        'CG_Best_objective', 'CG_Best_bound', 'CG_Gap', 'CG_Tempo_estruturas', 'CG_Tempo_modelo', 'CG_Tempo_total',
        'CS_Best_objective', 'CS_Best_bound', 'CS_Gap', 'CS_Tempo_estruturas', 'CS_Tempo_modelo', 'CS_Tempo_total',
        'CB_Best_objective', 'CB_Best_bound', 'CB_Gap', 'CB_Tempo_estruturas', 'CB_Tempo_modelo', 'CB_Tempo_total'
    ]
    
    output_csv = 'gurobi_models_report.csv'
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        
        for key, data in instances.items():
            row = [
                data['|∑|'], data['|s1|'], data['|s2|'], data['Fração de operações conservativas'],
                
                data['CG'].get('Best objective', ''), data['CG'].get('Best bound', ''), data['CG'].get('Gap', ''), 
                data['CG'].get('Tempo de criação das estruturas', ''), data['CG'].get('Tempo de execução do modelo', ''), data['CG'].get('Tempo total', ''),
                
                data['CS'].get('Best objective', ''), data['CS'].get('Best bound', ''), data['CS'].get('Gap', ''), 
                data['CS'].get('Tempo de criação das estruturas', ''), data['CS'].get('Tempo de execução do modelo', ''), data['CS'].get('Tempo total', ''),
                
                data['CB'].get('Best objective', ''), data['CB'].get('Best bound', ''), data['CB'].get('Gap', ''), 
                data['CB'].get('Tempo de criação das estruturas', ''), data['CB'].get('Tempo de execução do modelo', ''), data['CB'].get('Tempo total', '')
            ]
            writer.writerow(row)
            
    print(f"Sucesso! Relatório gerado em: '{output_csv}'")

if __name__ == "__main__":
    main()