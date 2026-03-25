import re

def imprime_particao(E, Ee, str, nome):
    p = []
    for t in E:
        p.append(str[t.v1:(t.v2)+1])
    for t in Ee:
        p.append(str[t.v1:(t.v2)+1])
    p = set(p)

    print(f"{nome} = ({p})")


def imprime_saida(S, T, E1, E2, Ee1, Ee2):
    s1_formatada = ""
    for char in S:
        s1_formatada += f" {char.upper()}"
    print(f'S1 = ({s1_formatada} )')

    s2_formatada = ""
    for char in T:
        s2_formatada += f" {char.upper()}"
    print(f'S2 = ({s2_formatada} )')

    imprime_particao(E1, Ee1, S, "S'1")
    imprime_particao(E2, Ee2, T, "S'2")

    file_path = 'solution.sol'
    
    t1_escolhida = r"^x\[\d+,\d+\] 1$"
    t2_escolhida = r"^y\[\d+,\d+\] 1$"
    t1_ex_escolhida = r"^xe\[\d+,\d+\] 1$"
    t2_ex_escolhida = r"^ye\[\d+,\d+\] 1$"

    sx = ""
    sy = ""

    try:
        with open(file_path, 'r') as file:
            for index, line in enumerate(file):
                clear_line = line.rstrip()
                print(clear_line[3])
                #print(S[clear_line[3]:(clear_line[5])+1])
                # if re.match(t1_ex_escolhida, clear_line):
                #     sx += f" {S[clear_line[3]:(clear_line[5]+1)].upper()}"

                # if re.match(t2_ex_escolhida, clear_line):
                #     sy += f" {T[clear_line[3]:(clear_line[5]+1)]}"

            print(f"X = ({sx} )")
            print(f"Y = ({sy} )")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

