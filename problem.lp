\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0,0] + x[1,1] + x[1,2] + x[1,3] + x[2,2] + x[2,3] + x[3,3] + x[3,4]
   + x[3,5] + x[4,4] + x[4,5] + x[5,5] + ye[0,0] + ye[3,3] + ye[3,4]
   + ye[3,5] + ye[4,4] + ye[4,5] + ye[5,5]
Subject To
 fat_blocos_iguais: x[0,0] + x[1,1] + x[1,2] + x[1,3] + x[2,2] + x[2,3]
   + x[3,3] + x[3,4] + x[3,5] + x[4,4] + x[4,5] + x[5,5] - y[0,0] - y[0,1]
   - y[1,1] - y[1,2] - y[1,3] - y[2,2] - y[2,3] - y[3,3] - y[4,4] - y[4,5]
   - y[4,6] - y[5,5] - y[5,6] - y[6,6] - y[6,7] - y[7,7] = 0
 n_sobrep_s1[0]: x[0,0] = 1
 n_sobrep_s1[1]: x[1,1] + x[1,2] + x[1,3] = 1
 n_sobrep_s1[2]: x[1,2] + x[1,3] + x[2,2] + x[2,3] = 1
 n_sobrep_s1[3]: x[1,3] + x[2,3] + x[3,3] + x[3,4] + x[3,5] = 1
 n_sobrep_s1[4]: x[3,4] + x[3,5] + x[4,4] + x[4,5] = 1
 n_sobrep_s1[5]: x[3,5] + x[4,5] + x[5,5] = 1
 n_sobrep_s2[0]: y[0,0] + y[0,1] + ye[0,0] = 1
 n_sobrep_s2[1]: y[0,1] + y[1,1] + y[1,2] + y[1,3] = 1
 n_sobrep_s2[2]: y[1,2] + y[1,3] + y[2,2] + y[2,3] = 1
 n_sobrep_s2[3]: y[1,3] + y[2,3] + y[3,3] + ye[3,3] + ye[3,4] + ye[3,5]
   = 1
 n_sobrep_s2[4]: y[4,4] + y[4,5] + y[4,6] + ye[3,4] + ye[3,5] + ye[4,4]
   + ye[4,5] = 1
 n_sobrep_s2[5]: y[4,5] + y[4,6] + y[5,5] + y[5,6] + ye[3,5] + ye[4,5]
   + ye[5,5] = 1
 n_sobrep_s2[6]: y[4,6] + y[5,6] + y[6,6] + y[6,7] = 1
 n_sobrep_s2[7]: y[6,7] + y[7,7] = 1
 n_sobrep_saida_s1[7]: x[0,0] = 1
 n_sobrep_entrada_s1[0,1]: x[0,0] - x[1,1] - x[1,2] - x[1,3] = 0
 n_sobrep_entrada_s1[1,2]: x[1,1] - x[2,2] - x[2,3] = 0
 n_sobrep_entrada_s1[2,3]: x[1,2] + x[2,2] - x[3,3] - x[3,4] - x[3,5] = 0
 n_sobrep_entrada_s1[3,4]: x[1,3] + x[2,3] + x[3,3] - x[4,4] - x[4,5] = 0
 n_sobrep_entrada_s1[4,5]: x[3,4] + x[4,4] - x[5,5] = 0
 n_sobrep_saida_s2[7]: y[0,0] + y[0,1] + ye[0,0] = 1
 n_sobrep_entrada_s2[0,1]: y[0,0] - y[1,1] - y[1,2] - y[1,3] + ye[0,0] = 0
 n_sobrep_entrada_s2[1,2]: y[0,1] + y[1,1] - y[2,2] - y[2,3] = 0
 n_sobrep_entrada_s2[2,3]: y[1,2] + y[2,2] - y[3,3] - ye[3,3] - ye[3,4]
   - ye[3,5] = 0
 n_sobrep_entrada_s2[3,4]: y[1,3] + y[2,3] + y[3,3] - y[4,4] - y[4,5]
   - y[4,6] + ye[3,3] - ye[4,4] - ye[4,5] = 0
 n_sobrep_entrada_s2[4,5]: y[4,4] - y[5,5] - y[5,6] + ye[3,4] + ye[4,4]
   - ye[5,5] = 0
 n_sobrep_entrada_s2[5,6]: y[4,5] + y[5,5] - y[6,6] - y[6,7] + ye[3,5]
   + ye[4,5] + ye[5,5] = 0
 n_sobrep_entrada_s2[6,7]: y[4,6] + y[5,6] + y[6,6] - y[7,7] = 0
 blocos_correspontes_0,0: x[0,0] + x[2,2] - y[2,2] - y[7,7] = 0
 blocos_correspontes_1,1: x[1,1] + x[5,5] - y[1,1] - y[6,6] = 0
 blocos_correspontes_1,2: x[1,2] - y[1,2] - y[6,7] = 0
 blocos_correspontes_1,3: x[1,3] - y[1,3] = 0
 blocos_correspontes_2,2: x[0,0] + x[2,2] - y[2,2] - y[7,7] = 0
 blocos_correspontes_2,3: x[2,3] - y[2,3] = 0
 blocos_correspontes_3,3: x[3,3] - y[3,3] - y[4,4] = 0
 blocos_correspontes_3,4: x[3,4] - y[4,5] = 0
 blocos_correspontes_3,5: x[3,5] - y[4,6] = 0
 blocos_correspontes_4,4: x[4,4] - y[0,0] - y[5,5] = 0
 blocos_correspontes_4,5: x[4,5] - y[0,1] - y[5,6] = 0
 blocos_correspontes_5,5: x[1,1] + x[5,5] - y[1,1] - y[6,6] = 0
Bounds
Binaries
 x[0,0] x[1,1] x[1,2] x[1,3] x[2,2] x[2,3] x[3,3] x[3,4] x[3,5] x[4,4]
 x[4,5] x[5,5] y[0,0] y[0,1] y[1,1] y[1,2] y[1,3] y[2,2] y[2,3] y[3,3]
 y[4,4] y[4,5] y[4,6] y[5,5] y[5,6] y[6,6] y[6,7] y[7,7] ye[0,0] ye[3,3]
 ye[3,4] ye[3,5] ye[4,4] ye[4,5] ye[5,5]
End
