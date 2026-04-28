import re
from utils.grafo import Grafo
from utils.aresta import Aresta

def imprime_saida(S, T):
    s1_formatada = ""
    for char in S:
        s1_formatada += f" {char}"
    print(f'S1 = ({s1_formatada} )')

    s2_formatada = ""
    for char in T:
        s2_formatada += f" {char}"
    print(f'S2 = ({s2_formatada} )')

    file_path = 'solution.sol'
    
    grupos = {
        "S1'": [],
        "S2'": [],
        "X": [],
        "Y": []
    }

    formato = re.compile(r"([a-z]+)\[(?:[^,]+,)?(\d+),(\d+)\]\s+(1)\n")

    try:
        with open(file_path, 'r') as file:
            conteudo = file.read()
            for match in formato.finditer(conteudo):
                conjunto, i1, i2, val = match.groups()
        
                i1 = int(i1)
                i2 = int(i2)

                if conjunto == "x":
                    grupos["S1'"].append(S[i1:(i2+1)])
                elif conjunto == "y":
                    grupos["S2'"].append(T[i1:(i2+1)])
                elif conjunto == "xe":
                    grupos["X"].append(S[i1:(i2+1)])
                elif conjunto == "ye":
                    grupos["Y"].append(T[i1:(i2+1)])
            

            part_selecionadas_list = []

            for conjunto, items in grupos.items():
                # 1. Join the numbers inside each sub-list with a space
                # Example: [1, 2] becomes "1 2"
                sub_grupos = [" ".join(map(str, sublist)) for sublist in items]
                
                # 2. Join those sub-groups with a comma and space
                # Example: ["1 2", "5 6 7"] becomes "1 2, 5 6 7"
                saida_formatada = ", ".join(sub_grupos)
                
                # 3. Print the set
                print(f"{conjunto} = ( {saida_formatada} )")
                
                # 4. Logic for Selected Partitions
                if conjunto in ["S1'", "Y", "X"] and items:
                    part_selecionadas_list.append(saida_formatada)

            # 5. Join the different sets with a comma (only if they are not empty)
            final_part_selecionadas = " , ".join(part_selecionadas_list)
                
            aux1 = grupos["S1'"]
            aux2 = grupos["S2'"]
            for part in aux1:
                if part in aux2:
                    print(f"σ(S1'{aux1.index(part)}) = S2'{aux2.index(part)}")
                

            print(f'Partições Selecionadas = ( {final_part_selecionadas} )')

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
