\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0,0] + x[0,1] + x[1,1] + x[3,3] + x[3,4] + x[3,5] + x[4,4] + x[4,5]
   + x[5,5] + x[5,6] + x[6,6] + xe[2,2] + ye[0,0] + ye[0,1] + ye[1,1]
   + ye[3,3] + ye[5,5] + ye[7,7] + ye[7,8] + ye[8,8]
Subject To
 n_sobrep_s1[0]: x[0,0] + x[0,1] = 1
 n_sobrep_s1[1]: x[0,1] + x[1,1] = 1
 n_sobrep_s1[2]: xe[2,2] = 1
 n_sobrep_s1[3]: x[3,3] + x[3,4] + x[3,5] = 1
 n_sobrep_s1[4]: x[3,4] + x[3,5] + x[4,4] + x[4,5] = 1
 n_sobrep_s1[5]: x[3,5] + x[4,5] + x[5,5] + x[5,6] = 1
 n_sobrep_s1[6]: x[5,6] + x[6,6] = 1
 n_sobrep_s2[0]: y[0,0] + ye[0,0] + ye[0,1] = 1
 n_sobrep_s2[1]: y[1,1] + ye[0,1] + ye[1,1] = 1
 n_sobrep_s2[2]: y[2,2] + y[2,3] + y[2,4] = 1
 n_sobrep_s2[3]: y[2,3] + y[2,4] + y[3,3] + y[3,4] + ye[3,3] = 1
 n_sobrep_s2[4]: y[2,4] + y[3,4] + y[4,4] + y[4,5] = 1
 n_sobrep_s2[5]: y[4,5] + y[5,5] + ye[5,5] = 1
 n_sobrep_s2[6]: y[6,6] + y[6,7] = 1
 n_sobrep_s2[7]: y[6,7] + y[7,7] + ye[7,7] + ye[7,8] = 1
 n_sobrep_s2[8]: y[8,8] + ye[7,8] + ye[8,8] = 1
 n_sobrep_saida_s1[8]: x[0,0] + x[0,1] = 1
 n_sobrep_entrada_s1[0,1]: x[0,0] - x[1,1] = 0
 n_sobrep_entrada_s1[1,2]: x[0,1] + x[1,1] - xe[2,2] = 0
 n_sobrep_entrada_s1[2,3]: - x[3,3] - x[3,4] - x[3,5] + xe[2,2] = 0
 n_sobrep_entrada_s1[3,4]: x[3,3] - x[4,4] - x[4,5] = 0
 n_sobrep_entrada_s1[4,5]: x[3,4] + x[4,4] - x[5,5] - x[5,6] = 0
 n_sobrep_entrada_s1[5,6]: x[3,5] + x[4,5] + x[5,5] - x[6,6] = 0
 n_sobrep_saida_s2[8]: y[0,0] + ye[0,0] + ye[0,1] = 1
 n_sobrep_entrada_s2[0,1]: y[0,0] - y[1,1] + ye[0,0] = 0
 n_sobrep_entrada_s2[1,2]: y[1,1] - y[2,2] - y[2,3] - y[2,4] + ye[0,1]
   + ye[1,1] = 0
 n_sobrep_entrada_s2[2,3]: y[2,2] - y[3,3] - y[3,4] = 0
 n_sobrep_entrada_s2[3,4]: y[2,3] + y[3,3] - y[4,4] - y[4,5] + ye[3,3] = 0
 n_sobrep_entrada_s2[4,5]: y[2,4] + y[3,4] + y[4,4] - y[5,5] = 0
 n_sobrep_entrada_s2[5,6]: y[4,5] + y[5,5] - y[6,6] - y[6,7] + ye[5,5] = 0
 n_sobrep_entrada_s2[6,7]: y[6,6] - y[7,7] = 0
 n_sobrep_entrada_s2[7,8]: y[6,7] + y[7,7] - y[8,8] + ye[7,7] = 0
 blocos_correspontes_0,0: xb[S1,0,0] + xb[S1,5,5] - xb[S2,4,4] - xb[S2,6,6]
   = 0
 blocos_correspontes_0,1: xb[S1,0,1] - xb[S2,4,5] = 0
 blocos_correspontes_1,1: xb[S1,1,1] - xb[S2,0,0] - xb[S2,5,5] = 0
 blocos_correspontes_3,3: xb[S1,3,3] - xb[S2,2,2] = 0
 blocos_correspontes_3,4: xb[S1,3,4] - xb[S2,2,3] = 0
 blocos_correspontes_3,5: xb[S1,3,5] - xb[S2,2,4] = 0
 blocos_correspontes_4,4: xb[S1,4,4] + xb[S1,6,6] - xb[S2,1,1] - xb[S2,3,3]
   - xb[S2,7,7] - xb[S2,8,8] = 0
 blocos_correspontes_4,5: xb[S1,4,5] - xb[S2,3,4] = 0
 blocos_correspontes_5,5: xb[S1,0,0] + xb[S1,5,5] - xb[S2,4,4] - xb[S2,6,6]
   = 0
 blocos_correspontes_5,6: xb[S1,5,6] - xb[S2,6,7] = 0
 blocos_correspontes_6,6: xb[S1,4,4] + xb[S1,6,6] - xb[S2,1,1] - xb[S2,3,3]
   - xb[S2,7,7] - xb[S2,8,8] = 0
Bounds
Binaries
 x[0,0] xb[S1,0,0] x[0,1] xb[S1,0,1] x[1,1] xb[S1,1,1] x[3,3] xb[S1,3,3]
 x[3,4] xb[S1,3,4] x[3,5] xb[S1,3,5] x[4,4] xb[S1,4,4] x[4,5] xb[S1,4,5]
 x[5,5] xb[S1,5,5] x[5,6] xb[S1,5,6] x[6,6] xb[S1,6,6] y[0,0] y[1,1] y[2,2]
 y[2,3] y[2,4] y[3,3] y[3,4] y[4,4] y[4,5] y[5,5] y[6,6] y[6,7] y[7,7]
 y[8,8] xe[2,2] ye[0,0] ye[0,1] ye[1,1] ye[3,3] ye[5,5] ye[7,7] ye[7,8]
 ye[8,8] xb[S2,0,0] xb[S2,1,1] xb[S2,2,2] xb[S2,2,3] xb[S2,2,4] xb[S2,3,3]
 xb[S2,3,4] xb[S2,4,4] xb[S2,4,5] xb[S2,5,5] xb[S2,6,6] xb[S2,6,7]
 xb[S2,7,7] xb[S2,8,8]
End
