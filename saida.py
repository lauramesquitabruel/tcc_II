import re

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
                    grupos["S1'"].append(" ".join(S[i1:(i2+1)]))
                elif conjunto == "y":
                    grupos["S2'"].append(" ".join(T[i1:(i2+1)]))
                elif conjunto == "xe":
                    grupos["X"].append(" ".join(S[i1:(i2+1)]))
                elif conjunto == "ye":
                    grupos["Y"].append(" ".join(T[i1:(i2+1)]))
            

            part_selecionadas = ""
            for conjunto, items in grupos.items():
                saida_formatada = ", ".join(items)
                if conjunto == "S1'" or conjunto == "Y" or conjunto == "X":
                    if len(items) > 0:
                        if len(part_selecionadas) > 0:
                            part_selecionadas += f", {saida_formatada}"
                        else:
                            part_selecionadas += saida_formatada
                print(f"{conjunto} = ( {saida_formatada} )")
                
            aux1 = grupos["S1'"]
            aux2 = grupos["S2'"]
            for part in aux1:
                if part in aux2:
                    print(f"σ(S1'{aux1.index(part)}) = S2'{aux2.index(part)}")
                

            print(f'Partições Selecionadas = ( {part_selecionadas} )')

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
