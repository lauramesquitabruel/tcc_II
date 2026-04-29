\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0,0] + x[0,1] + x[0,2] + x[1,1] + x[1,2] + x[2,2] + xe[3,3]
Subject To
 fat_blocos_iguais: x[0,0] + x[0,1] + x[0,2] + x[1,1] + x[1,2] + x[2,2]
   - y[0,0] - y[0,1] - y[0,2] - y[1,1] - y[1,2] - y[2,2] = 0
 n_sobrep_s1[0]: x[0,0] + x[0,1] + x[0,2] = 1
 n_sobrep_s1[1]: x[0,1] + x[0,2] + x[1,1] + x[1,2] = 1
 n_sobrep_s1[2]: x[0,2] + x[1,2] + x[2,2] = 1
 n_sobrep_s1[3]: xe[3,3] = 1
 n_sobrep_s2[0]: y[0,0] + y[0,1] + y[0,2] = 1
 n_sobrep_s2[1]: y[0,1] + y[0,2] + y[1,1] + y[1,2] = 1
 n_sobrep_s2[2]: y[0,2] + y[1,2] + y[2,2] = 1
 n_sobrep_saida_s1[2]: x[0,0] + x[0,1] + x[0,2] = 1
 n_sobrep_entrada_s1[0,1]: x[0,0] - x[1,1] - x[1,2] = 0
 n_sobrep_entrada_s1[1,2]: x[0,1] + x[1,1] - x[2,2] = 0
 n_sobrep_entrada_s1[2,3]: x[0,2] + x[1,2] + x[2,2] - xe[3,3] = 0
 n_sobrep_saida_s2[2]: y[0,0] + y[0,1] + y[0,2] = 1
 n_sobrep_entrada_s2[0,1]: y[0,0] - y[1,1] - y[1,2] = 0
 n_sobrep_entrada_s2[1,2]: y[0,1] + y[1,1] - y[2,2] = 0
 blocos_correspontes_0,0: x[0,0] - y[0,0] = 0
 blocos_correspontes_0,1: x[0,1] - y[0,1] = 0
 blocos_correspontes_0,2: x[0,2] - y[0,2] = 0
 blocos_correspontes_1,1: x[1,1] - y[1,1] = 0
 blocos_correspontes_1,2: x[1,2] - y[1,2] = 0
 blocos_correspontes_2,2: x[2,2] - y[2,2] = 0
Bounds
Binaries
 x[0,0] x[0,1] x[0,2] x[1,1] x[1,2] x[2,2] y[0,0] y[0,1] y[0,2] y[1,1]
 y[1,2] y[2,2] xe[3,3]
End
