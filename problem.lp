\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 xb[S2,0,1] + 0 xb[S2,3,5] + 0 xb[S2,5,6]
Subject To
 fat_blocos_guais: x[0,0] + x[0,1] + x[1,1] + x[3,3] + x[3,4] + x[3,5]
   + x[4,4] + x[4,5] + x[5,5] + x[5,6] + x[6,6] - y[0,0] - y[0,1] - y[1,1]
   - y[3,3] - y[3,4] - y[3,5] - y[4,4] - y[4,5] - y[5,5] - y[5,6] - y[6,6]
   = 0
 n_sobrep_s1[0]: x[0,0] + x[0,1] = 1
 n_sobrep_s1[1]: x[0,1] + x[1,1] = 1
 n_sobrep_s1[2]: xe[2,2] = 1
 n_sobrep_s1[3]: x[3,3] + x[3,4] + x[3,5] = 1
 n_sobrep_s1[4]: x[3,4] + x[3,5] + x[4,4] + x[4,5] = 1
 n_sobrep_s1[5]: x[3,5] + x[4,5] + x[5,5] + x[5,6] = 1
 n_sobrep_s1[6]: x[5,6] + x[6,6] = 1
 n_sobrep_s2[0]: y[0,0] + y[0,1] + ye[0,0] + ye[0,1] = 1
 n_sobrep_s2[1]: y[0,1] + y[1,1] + ye[0,1] + ye[1,1] = 1
 n_sobrep_s2[3]: y[3,3] + y[3,4] + y[3,5] + ye[3,3] = 1
 n_sobrep_s2[4]: y[3,4] + y[3,5] + y[4,4] + y[4,5] = 1
 n_sobrep_s2[5]: y[3,5] + y[4,5] + y[5,5] + y[5,6] + ye[5,5] = 1
 n_sobrep_s2[6]: y[5,6] + y[6,6] = 1
 n_sobrep_s2[7]: ye[7,7] + ye[7,8] = 1
 n_sobrep_s2[8]: ye[7,8] + ye[8,8] = 1
 n_sobrep_saida_s1[8]: x[0,0] + x[0,1] = 1
 n_sobrep_entrada_s1[0]: x[0,0] - x[0,1] - x[1,1] = 0
 n_sobrep_entrada_s1[1]: x[0,1] + x[1,1] - xe[2,2] = 0
 n_sobrep_entrada_s1[2]: - x[3,3] + xe[2,2] = 0
 n_sobrep_entrada_s1[3]: x[3,3] - x[3,4] - x[4,4] = 0
 n_sobrep_entrada_s1[4]: x[3,4] - x[3,5] + x[4,4] - x[4,5] - x[5,5] = 0
 n_sobrep_entrada_s1[5]: x[3,5] + x[4,5] + x[5,5] - x[5,6] - x[6,6] = 0
 n_sobrep_saida_s2[8]: y[0,0] + y[0,1] + ye[0,0] + ye[0,1] = 1
 n_sobrep_entrada_s2[0]: y[0,0] - y[0,1] - y[1,1] + ye[0,0] = 0
 n_sobrep_entrada_s2[1]: y[0,1] + y[1,1] + ye[0,1] + ye[1,1] = 0
 n_sobrep_entrada_s2[2]: - y[3,3] = 0
 n_sobrep_entrada_s2[3]: y[3,3] - y[3,4] - y[4,4] + ye[3,3] = 0
 n_sobrep_entrada_s2[4]: y[3,4] - y[3,5] + y[4,4] - y[4,5] - y[5,5] = 0
 n_sobrep_entrada_s2[5]: y[3,5] + y[4,5] + y[5,5] - y[5,6] - y[6,6]
   + ye[5,5] = 0
 n_sobrep_entrada_s2[6]: y[5,6] + y[6,6] = 0
 n_sobrep_entrada_s2[7]: ye[7,7] = 0
 blocos_correspontes_0,0: xb[S1,0,0] + xb[S1,1,1] + xb[S1,3,3] + xb[S1,4,4]
   + xb[S1,5,5] + xb[S1,6,6] - xb[S2,0,0] - xb[S2,1,1] - xb[S2,3,3]
   - xb[S2,4,4] - xb[S2,5,5] - xb[S2,6,6] = 0
 blocos_correspontes_0,1: xb[S1,0,0] + xb[S1,0,1] + xb[S1,1,1] + xb[S1,3,3]
   + xb[S1,4,4] + xb[S1,5,5] + xb[S1,5,6] + xb[S1,6,6] - xb[S2,0,0]
   - xb[S2,1,1] - xb[S2,3,3] - xb[S2,4,4] - xb[S2,4,5] - xb[S2,5,5]
   - xb[S2,6,6] = 0
 blocos_correspontes_1,1: 2 xb[S1,0,0] + xb[S1,0,1] + 2 xb[S1,1,1]
   + 2 xb[S1,3,3] + 2 xb[S1,4,4] + 2 xb[S1,5,5] + xb[S1,5,6] + 2 xb[S1,6,6]
   - 2 xb[S2,0,0] - 2 xb[S2,1,1] - 2 xb[S2,3,3] - 2 xb[S2,4,4] - xb[S2,4,5]
   - 2 xb[S2,5,5] - 2 xb[S2,6,6] = 0
 blocos_correspontes_3,3: 3 xb[S1,0,0] + xb[S1,0,1] + 3 xb[S1,1,1]
   + 3 xb[S1,3,3] + 3 xb[S1,4,4] + 3 xb[S1,5,5] + xb[S1,5,6] + 3 xb[S1,6,6]
   - 3 xb[S2,0,0] - 3 xb[S2,1,1] - 3 xb[S2,3,3] - 3 xb[S2,4,4] - xb[S2,4,5]
   - 3 xb[S2,5,5] - 3 xb[S2,6,6] = 0
 blocos_correspontes_3,4: 3 xb[S1,0,0] + xb[S1,0,1] + 3 xb[S1,1,1]
   + 3 xb[S1,3,3] + xb[S1,3,4] + 3 xb[S1,4,4] + 3 xb[S1,5,5] + xb[S1,5,6]
   + 3 xb[S1,6,6] - 3 xb[S2,0,0] - 3 xb[S2,1,1] - 3 xb[S2,3,3]
   - 3 xb[S2,4,4] - xb[S2,4,5] - 3 xb[S2,5,5] - 3 xb[S2,6,6] = 0
 blocos_correspontes_3,5: 3 xb[S1,0,0] + xb[S1,0,1] + 3 xb[S1,1,1]
   + 3 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 3 xb[S1,4,4] + 3 xb[S1,5,5]
   + xb[S1,5,6] + 3 xb[S1,6,6] - 3 xb[S2,0,0] - 3 xb[S2,1,1] - 3 xb[S2,3,3]
   - 3 xb[S2,4,4] - xb[S2,4,5] - 3 xb[S2,5,5] - 3 xb[S2,6,6] = 0
 blocos_correspontes_4,4: 4 xb[S1,0,0] + xb[S1,0,1] + 4 xb[S1,1,1]
   + 4 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 4 xb[S1,4,4] + 4 xb[S1,5,5]
   + xb[S1,5,6] + 4 xb[S1,6,6] - 4 xb[S2,0,0] - 4 xb[S2,1,1] - 4 xb[S2,3,3]
   - 4 xb[S2,4,4] - xb[S2,4,5] - 4 xb[S2,5,5] - 4 xb[S2,6,6] = 0
 blocos_correspontes_4,5: 4 xb[S1,0,0] + xb[S1,0,1] + 4 xb[S1,1,1]
   + 4 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 4 xb[S1,4,4] + xb[S1,4,5]
   + 4 xb[S1,5,5] + xb[S1,5,6] + 4 xb[S1,6,6] - 4 xb[S2,0,0] - 4 xb[S2,1,1]
   - 4 xb[S2,3,3] - xb[S2,3,4] - 4 xb[S2,4,4] - xb[S2,4,5] - 4 xb[S2,5,5]
   - 4 xb[S2,6,6] = 0
 blocos_correspontes_5,5: 5 xb[S1,0,0] + xb[S1,0,1] + 5 xb[S1,1,1]
   + 5 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 5 xb[S1,4,4] + xb[S1,4,5]
   + 5 xb[S1,5,5] + xb[S1,5,6] + 5 xb[S1,6,6] - 5 xb[S2,0,0] - 5 xb[S2,1,1]
   - 5 xb[S2,3,3] - xb[S2,3,4] - 5 xb[S2,4,4] - xb[S2,4,5] - 5 xb[S2,5,5]
   - 5 xb[S2,6,6] = 0
 blocos_correspontes_5,6: 5 xb[S1,0,0] + 2 xb[S1,0,1] + 5 xb[S1,1,1]
   + 5 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 5 xb[S1,4,4] + xb[S1,4,5]
   + 5 xb[S1,5,5] + 2 xb[S1,5,6] + 5 xb[S1,6,6] - 5 xb[S2,0,0]
   - 5 xb[S2,1,1] - 5 xb[S2,3,3] - xb[S2,3,4] - 5 xb[S2,4,4] - 2 xb[S2,4,5]
   - 5 xb[S2,5,5] - 5 xb[S2,6,6] = 0
 blocos_correspontes_6,6: 6 xb[S1,0,0] + 2 xb[S1,0,1] + 6 xb[S1,1,1]
   + 6 xb[S1,3,3] + xb[S1,3,4] + xb[S1,3,5] + 6 xb[S1,4,4] + xb[S1,4,5]
   + 6 xb[S1,5,5] + 2 xb[S1,5,6] + 6 xb[S1,6,6] - 6 xb[S2,0,0]
   - 6 xb[S2,1,1] - 6 xb[S2,3,3] - xb[S2,3,4] - 6 xb[S2,4,4] - 2 xb[S2,4,5]
   - 6 xb[S2,5,5] - 6 xb[S2,6,6] = 0
Bounds
Binaries
 x[0,0] xb[S1,0,0] x[0,1] xb[S1,0,1] x[1,1] xb[S1,1,1] x[3,3] xb[S1,3,3]
 x[3,4] xb[S1,3,4] x[3,5] xb[S1,3,5] x[4,4] xb[S1,4,4] x[4,5] xb[S1,4,5]
 x[5,5] xb[S1,5,5] x[5,6] xb[S1,5,6] x[6,6] xb[S1,6,6] y[0,0] y[0,1] y[1,1]
 y[3,3] y[3,4] y[3,5] y[4,4] y[4,5] y[5,5] y[5,6] y[6,6] xe[2,2] ye[0,0]
 ye[0,1] ye[1,1] ye[3,3] ye[5,5] ye[7,7] ye[7,8] ye[8,8] xb[S2,0,0]
 xb[S2,0,1] xb[S2,1,1] xb[S2,3,3] xb[S2,3,4] xb[S2,3,5] xb[S2,4,4]
 xb[S2,4,5] xb[S2,5,5] xb[S2,5,6] xb[S2,6,6]
End
