\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  ye[0,0] + ye[3,3] + ye[3,4] + ye[3,5] + ye[4,4] + ye[4,5] + ye[5,5]
Subject To
 fat_blocos_iguais: = 0
 n_sobrep_s2[0]: ye[0,0] = 1
 n_sobrep_s2[3]: ye[3,3] + ye[3,4] + ye[3,5] = 1
 n_sobrep_s2[4]: ye[3,4] + ye[3,5] + ye[4,4] + ye[4,5] = 1
 n_sobrep_s2[5]: ye[3,5] + ye[4,5] + ye[5,5] = 1
 n_sobrep_entrada_s1[0,1]: <= 0
 n_sobrep_entrada_s1[1,2]: <= 0
 n_sobrep_entrada_s1[2,3]: <= 0
 n_sobrep_entrada_s1[3,4]: <= 0
 n_sobrep_entrada_s1[4,5]: <= 0
 n_sobrep_saida_s2[7]: ye[0,0] = 1
 n_sobrep_entrada_s2[0,1]: <= -1
 n_sobrep_entrada_s2[1,2]: <= -1
 n_sobrep_entrada_s2[2,3]: ye[0,0] - ye[3,3] - ye[3,4] - ye[3,5] = 0
 n_sobrep_entrada_s2[3,4]: ye[3,3] - ye[4,4] - ye[4,5] = 0
 n_sobrep_entrada_s2[4,5]: ye[3,4] + ye[4,4] - ye[5,5] = 0
 n_sobrep_entrada_s2[5,6]: ye[3,5] + ye[4,5] = 0
 n_sobrep_entrada_s2[6,7]: ye[3,5] + ye[4,5] = 0
Bounds
Binaries
 ye[0,0] ye[3,3] ye[3,4] ye[3,5] ye[4,4] ye[4,5] ye[5,5]
End
