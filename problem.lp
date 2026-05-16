\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0,0] + x[0,1] + x[0,2] + x[1,1] + x[1,2] + x[2,2] + x[3,3] + x[4,4]
   + x[4,5] + x[4,6] + x[5,5] + x[5,6] + x[6,6] + x[7,7] + x[7,8] + x[8,8]
   + x[8,9] + x[9,9]
Subject To
 fat_blocos_iguais: x[0,0] + x[0,1] + x[0,2] + x[1,1] + x[1,2] + x[2,2]
   + x[3,3] + x[4,4] + x[4,5] + x[4,6] + x[5,5] + x[5,6] + x[6,6] + x[7,7]
   + x[7,8] + x[8,8] + x[8,9] + x[9,9] - y[0,0] - y[0,1] - y[0,2] - y[1,1]
   - y[1,2] - y[2,2] - y[2,3] - y[3,3] - y[4,4] - y[5,5] - y[5,6] - y[6,6]
   - y[7,7] - y[7,8] - y[7,9] - y[8,8] - y[8,9] - y[9,9] = 0
 n_sobrep_s1[0]: x[0,0] + x[0,1] + x[0,2] = 1
 n_sobrep_s1[1]: x[0,1] + x[0,2] + x[1,1] + x[1,2] = 1
 n_sobrep_s1[2]: x[0,2] + x[1,2] + x[2,2] = 1
 n_sobrep_s1[3]: x[3,3] = 1
 n_sobrep_s1[4]: x[4,4] + x[4,5] + x[4,6] = 1
 n_sobrep_s1[5]: x[4,5] + x[4,6] + x[5,5] + x[5,6] = 1
 n_sobrep_s1[6]: x[4,6] + x[5,6] + x[6,6] = 1
 n_sobrep_s1[7]: x[7,7] + x[7,8] = 1
 n_sobrep_s1[8]: x[7,8] + x[8,8] + x[8,9] = 1
 n_sobrep_s1[9]: x[8,9] + x[9,9] = 1
 n_sobrep_s2[0]: y[0,0] + y[0,1] + y[0,2] = 1
 n_sobrep_s2[1]: y[0,1] + y[0,2] + y[1,1] + y[1,2] = 1
 n_sobrep_s2[2]: y[0,2] + y[1,2] + y[2,2] + y[2,3] = 1
 n_sobrep_s2[3]: y[2,3] + y[3,3] = 1
 n_sobrep_s2[4]: y[4,4] = 1
 n_sobrep_s2[5]: y[5,5] + y[5,6] = 1
 n_sobrep_s2[6]: y[5,6] + y[6,6] = 1
 n_sobrep_s2[7]: y[7,7] + y[7,8] + y[7,9] = 1
 n_sobrep_s2[8]: y[7,8] + y[7,9] + y[8,8] + y[8,9] = 1
 n_sobrep_s2[9]: y[7,9] + y[8,9] + y[9,9] = 1
 n_sobrep_saida_s1[9]: x[0,0] + x[0,1] + x[0,2] = 1
 n_sobrep_entrada_s1[0,1]: x[0,0] - x[1,1] - x[1,2] = 0
 n_sobrep_entrada_s1[1,2]: x[0,1] + x[1,1] - x[2,2] = 0
 n_sobrep_entrada_s1[2,3]: x[0,2] + x[1,2] + x[2,2] - x[3,3] = 0
 n_sobrep_entrada_s1[3,4]: x[3,3] - x[4,4] - x[4,5] - x[4,6] = 0
 n_sobrep_entrada_s1[4,5]: x[4,4] - x[5,5] - x[5,6] = 0
 n_sobrep_entrada_s1[5,6]: x[4,5] + x[5,5] - x[6,6] = 0
 n_sobrep_entrada_s1[6,7]: x[4,6] + x[5,6] + x[6,6] - x[7,7] - x[7,8] = 0
 n_sobrep_entrada_s1[7,8]: x[7,7] - x[8,8] - x[8,9] = 0
 n_sobrep_entrada_s1[8,9]: x[7,8] + x[8,8] - x[9,9] = 0
 n_sobrep_saida_s2[9]: y[0,0] + y[0,1] + y[0,2] = 1
 n_sobrep_entrada_s2[0,1]: y[0,0] - y[1,1] - y[1,2] = 0
 n_sobrep_entrada_s2[1,2]: y[0,1] + y[1,1] - y[2,2] - y[2,3] = 0
 n_sobrep_entrada_s2[2,3]: y[0,2] + y[1,2] + y[2,2] - y[3,3] = 0
 n_sobrep_entrada_s2[3,4]: y[2,3] + y[3,3] - y[4,4] = 0
 n_sobrep_entrada_s2[4,5]: y[4,4] - y[5,5] - y[5,6] = 0
 n_sobrep_entrada_s2[5,6]: y[5,5] - y[6,6] = 0
 n_sobrep_entrada_s2[6,7]: y[5,6] + y[6,6] - y[7,7] - y[7,8] - y[7,9] = 0
 n_sobrep_entrada_s2[7,8]: y[7,7] - y[8,8] - y[8,9] = 0
 n_sobrep_entrada_s2[8,9]: y[7,8] + y[8,8] - y[9,9] = 0
 blocos_correspontes_0,0: x[0,0] - y[0,0] = 0
 blocos_correspontes_0,1: x[0,1] - y[0,1] = 0
 blocos_correspontes_0,2: x[0,2] - y[0,2] = 0
 blocos_correspontes_1,1: x[1,1] + x[2,2] + x[4,4] - y[1,1] - y[2,2]
   - y[7,7] = 0
 blocos_correspontes_1,2: x[1,2] - y[1,2] = 0
 blocos_correspontes_2,2: x[1,1] + x[2,2] + x[4,4] - y[1,1] - y[2,2]
   - y[7,7] = 0
 blocos_correspontes_3,3: x[3,3] - y[4,4] = 0
 blocos_correspontes_4,4: x[1,1] + x[2,2] + x[4,4] - y[1,1] - y[2,2]
   - y[7,7] = 0
 blocos_correspontes_4,5: x[4,5] - y[2,3] - y[7,8] = 0
 blocos_correspontes_4,6: x[4,6] - y[7,9] = 0
 blocos_correspontes_5,5: x[5,5] + x[6,6] + x[8,8] + x[9,9] - y[3,3]
   - y[6,6] - y[8,8] - y[9,9] = 0
 blocos_correspontes_5,6: x[5,6] + x[8,9] - y[8,9] = 0
 blocos_correspontes_6,6: x[5,5] + x[6,6] + x[8,8] + x[9,9] - y[3,3]
   - y[6,6] - y[8,8] - y[9,9] = 0
 blocos_correspontes_7,7: x[7,7] - y[5,5] = 0
 blocos_correspontes_7,8: x[7,8] - y[5,6] = 0
 blocos_correspontes_8,8: x[5,5] + x[6,6] + x[8,8] + x[9,9] - y[3,3]
   - y[6,6] - y[8,8] - y[9,9] = 0
 blocos_correspontes_8,9: x[5,6] + x[8,9] - y[8,9] = 0
 blocos_correspontes_9,9: x[5,5] + x[6,6] + x[8,8] + x[9,9] - y[3,3]
   - y[6,6] - y[8,8] - y[9,9] = 0
Bounds
Binaries
 x[0,0] x[0,1] x[0,2] x[1,1] x[1,2] x[2,2] x[3,3] x[4,4] x[4,5] x[4,6]
 x[5,5] x[5,6] x[6,6] x[7,7] x[7,8] x[8,8] x[8,9] x[9,9] y[0,0] y[0,1]
 y[0,2] y[1,1] y[1,2] y[2,2] y[2,3] y[3,3] y[4,4] y[5,5] y[5,6] y[6,6]
 y[7,7] y[7,8] y[7,9] y[8,8] y[8,9] y[9,9]
End
