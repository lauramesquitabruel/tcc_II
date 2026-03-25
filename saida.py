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

    # try:
    #     with open(file_path, 'r') as file:
    #         for index, line in enumerate(file, 2):
    #             if 
    # except FileNotFoundError:
    #     print(f"Error: The file '{file_path}' was not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

