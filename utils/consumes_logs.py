import os
import re
import csv
from pathlib import Path

def main():
    instances = {}

    log_dir = Path('logs')
    
    for file in log_dir.glob("rmcsp_*.in"):
        filename = file.name
        
        match1 = re.search(rf"rmcsp_(\d+)_\d+_(\d+)_([-+]?\d*\.?\d*)-", filename)
        match2 = re.search(rf"rmcsp_(\d+)_\d+_(\d+)_(\d+)-", filename)
        if match1:
            s1, sigma, seed, frac = match1.groups()
            s2 = s1
        elif match2: 
            s1, s2, sigma, seed = match2.groups()
            frac = "Random"
        else:
            s1, s2, sigma, seed, frac = "Unknown", "Unknown", "Unknown", "Unknown"
            model_type = "CG" #if "CG" in filename else ("CS" if "CS" in filename else "CB")
        
        instance_key = (s1, sigma, seed, frac) if frac != "Random" else (s1, s2, sigma, seed)
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
            
            t_estruturas = re.search(r'Tempo de criação das estruturas:\s+([\d.]+)', content)
            t_modelo = re.search(r'Tempo de execução do modelo:\s+([\d.]+)', content)
            t_total = re.search(r'Tempo total:\s+([\d.]+)', content)
            
            metrics = {
                'Best objective': best_obj.group(1) if best_obj else 'N/A',
                'Best bound': best_bd.group(1) if best_bd else 'N/A',
                'Gap': gap.group(1) if gap else 'N/A',
                'Tempo de criação das estruturas': t_estruturas.group(1) if t_estruturas else 'N/A',
                'Tempo de execução do modelo': t_modelo.group(1) if t_modelo else 'N/A',
                'Tempo total': t_total.group(1) if t_total else 'N/A'
            }
            
            instances[instance_key][model_type] = metrics

    log_dir = Path('logs/cs')
    
    for file in log_dir.glob("rmcsp_*.in"):
        filename = file.name
        
        match = re.search(rf"rmcsp_(\d+)-", filename)
        if match:
            index = match.groups()
            if index.index(0) > 4:
                s1 = 1000   
                s2 = 1000
                sigma = 1000
                seed, frac = "Unknown", "Unknown",

            model_type = "CS"
        
        instance_key = (s1, sigma, seed, frac) if frac != "Random" else (s1, s2, sigma, seed)
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
            
            t_estruturas = re.search(r'Tempo de criação das estruturas:\s+([\d.]+)', content)
            t_modelo = re.search(r'Tempo de execução do modelo:\s+([\d.]+)', content)
            t_total = re.search(r'Tempo total:\s+([\d.]+)', content)
            
            metrics = {
                'Best objective': best_obj.group(1) if best_obj else 'N/A',
                'Best bound': best_bd.group(1) if best_bd else 'N/A',
                'Gap': gap.group(1) if gap else 'N/A',
                'Tempo de criação das estruturas': t_estruturas.group(1) if t_estruturas else 'N/A',
                'Tempo de execução do modelo': t_modelo.group(1) if t_modelo else 'N/A',
                'Tempo total': t_total.group(1) if t_total else 'N/A'
            }
            
            instances[instance_key][model_type] = metrics

    # 2. Define standard flattened headers for your tabular .csv file
    headers = [
        '|∑|', '|s1|', '|s2|', 'Fração de operações conservativas',
        'CG_Best_objective', 'CG_Best_bound', 'CG_Gap', 'CG_Tempo_estruturas', 'CG_Tempo_modelo', 'CG_Tempo_total',
        'CS_Best_objective', 'CS_Best_bound', 'CS_Gap', 'CS_Tempo_estruturas', 'CS_Tempo_modelo', 'CS_Tempo_total',
        'CB_Best_objective', 'CB_Best_bound', 'CB_Gap', 'CB_Tempo_estruturas', 'CB_Tempo_modelo', 'CB_Tempo_total'
    ]
    
    # 3. Write data to spreadsheet output
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