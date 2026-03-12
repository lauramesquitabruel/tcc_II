\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 y[0,0] + 0 y[0,1] + 0 y[1,1] + 0 y[3,3] + 0 y[3,4] + 0 y[3,5] + 0 y[4,4]
   + 0 y[4,5] + 0 y[5,5] + 0 y[5,6] + 0 y[6,6] + 0 ye[0,0] + 0 ye[0,1]
   + 0 ye[1,1] + 0 ye[3,3] + 0 ye[5,5] + 0 ye[7,7] + 0 ye[7,8] + 0 ye[8,8]
Subject To
 n_sobrep[0]: x[0,0] + x[0,1] = 1
 n_sobrep[1]: x[0,1] + x[1,1] = 1
 n_sobrep[2]: xe[2,2] = 1
 n_sobrep[3]: x[3,3] + x[3,4] + x[3,5] = 1
 n_sobrep[4]: x[3,4] + x[3,5] + x[4,4] + x[4,5] = 1
 n_sobrep[5]: x[3,5] + x[4,5] + x[5,5] + x[5,6] = 1
 n_sobrep[6]: x[5,6] + x[6,6] = 1
Bounds
Binaries
 x[0,0] x[0,1] x[1,1] x[3,3] x[3,4] x[3,5] x[4,4] x[4,5] x[5,5] x[5,6]
 x[6,6] y[0,0] y[0,1] y[1,1] y[3,3] y[3,4] y[3,5] y[4,4] y[4,5] y[5,5]
 y[5,6] y[6,6] xe[2,2] ye[0,0] ye[0,1] ye[1,1] ye[3,3] ye[5,5] ye[7,7]
 ye[7,8] ye[8,8]
End
