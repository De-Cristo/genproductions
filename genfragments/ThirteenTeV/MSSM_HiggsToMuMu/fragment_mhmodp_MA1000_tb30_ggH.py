COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2 = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     3.00000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.50666667E+03   # At
        12     1.50666667E+03   # Ab
        13     1.50666667E+03   # Atau
        23     2.00000000E+02   # MUE
        25     3.00000000E+01   # TB
        26     1.00000000E+03   # MA0
        27     1.00322671E+03   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95834286E+02   # MSf(1,1,1)
   1000011     5.02295880E+02   # MSf(1,2,1)
   2000011     5.01843810E+02   # MSf(2,2,1)
   1000002     1.49902739E+03   # MSf(1,3,1)
   2000002     1.49958945E+03   # MSf(2,3,1)
   1000001     1.50117722E+03   # MSf(1,4,1)
   2000001     1.50020509E+03   # MSf(2,4,1)
   1000014     4.95834286E+02   # MSf(1,1,2)
   1000013     5.02740033E+02   # MSf(1,2,2)
   2000013     5.01398885E+02   # MSf(2,2,2)
   1000004     1.49902793E+03   # MSf(1,3,2)
   2000004     1.49959001E+03   # MSf(2,3,2)
   1000003     1.50121083E+03   # MSf(1,4,2)
   2000003     1.50017147E+03   # MSf(2,4,2)
   1000016     9.97923664E+02   # MSf(1,1,3)
   1000015     9.97040283E+02   # MSf(1,2,3)
   2000015     1.00502007E+03   # MSf(2,2,3)
   1000006     8.76426091E+02   # MSf(1,3,3)
   2000006     1.13477990E+03   # MSf(2,3,3)
   1000005     9.92452622E+02   # MSf(1,4,3)
   2000005     1.00956179E+03   # MSf(2,4,3)
        25     1.25071787E+02   # Mh0
        35     9.99749899E+02   # MHH
        36     1.00000000E+03   # MA0
        37     1.00342592E+03   # MHp
   1000022     8.83213889E+01   # MNeu(1)
   1000023     1.52049632E+02   # MNeu(2)
   1000025    -2.10470056E+02   # MNeu(3)
   1000035     2.65570688E+02   # MNeu(4)
   1000024     1.48692309E+02   # MCha(1)
   1000037     2.66117031E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.02650085E-01   # Delta Mh0
        35     1.26517870E-02   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     5.96810959E-03   # Delta MHp
BLOCK NMIX
     1   1     9.33161766E-01   # ZNeu(1,1)
     1   2    -1.11637757E-01   # ZNeu(1,2)
     1   3     3.09461555E-01   # ZNeu(1,3)
     1   4    -1.44843625E-01   # ZNeu(1,4)
     2   1    -3.14536695E-01   # ZNeu(2,1)
     2   2    -6.93472054E-01   # ZNeu(2,2)
     2   3     5.12603053E-01   # ZNeu(2,3)
     2   4    -3.96738310E-01   # ZNeu(2,4)
     3   1     9.74524166E-02   # ZNeu(3,1)
     3   2    -1.35722538E-01   # ZNeu(3,2)
     3   3    -6.77905232E-01   # ZNeu(3,3)
     3   4    -7.15909852E-01   # ZNeu(3,4)
     4   1    -1.44148578E-01   # ZNeu(4,1)
     4   2     6.98722344E-01   # ZNeu(4,2)
     4   3     4.26516298E-01   # ZNeu(4,3)
     4   4    -5.55960539E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.06292879E-01   # UCha(1,1)
     1   2     7.95241438E-01   # UCha(1,2)
     2   1     7.95241438E-01   # UCha(2,1)
     2   2     6.06292879E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.95241438E-01   # VCha(1,1)
     1   2     6.06292879E-01   # VCha(1,2)
     2   1     6.06292879E-01   # VCha(2,1)
     2   2     7.95241438E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     6.96989496E-01   # USf(1,1)
     1   2     7.17081336E-01   # USf(1,2)
     2   1     7.17081336E-01   # USf(2,1)
     2   2    -6.96989496E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08252641E-01   # USf(1,1)
     1   2    -7.05959062E-01   # USf(1,2)
     2   1     7.05959062E-01   # USf(2,1)
     2   2     7.08252641E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.76329341E-01   # USf(1,1)
     1   2     7.36599364E-01   # USf(1,2)
     2   1     7.36599364E-01   # USf(2,1)
     2   2    -6.76329341E-01   # USf(2,2)
BLOCK ALPHA
              -3.42820865E-02   # Alpha
BLOCK DALPHA
               1.69617058E-05   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     3.00000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50666667E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50666667E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50666667E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     8.80994160E-05   # Yf(1,1)
     2   2     1.82161635E-02   # Yf(2,2)
     3   3     3.06371119E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72406273E-05   # Yf(1,1)
     2   2     7.39048222E-03   # Yf(2,2)
     3   3     9.95358881E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     1.00364128E-03   # Yf(1,1)
     2   2     1.58899845E-02   # Yf(2,2)
     3   3     6.54741643E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     4.61599152E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.49967405E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     9.86477409E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99977189E-01   # UASf(1,1)
     1   4    -6.75432353E-03   # UASf(1,4)
     2   2     8.17632607E-01   # UASf(2,2)
     2   5    -5.75740323E-01   # UASf(2,5)
     3   3     6.96989496E-01   # UASf(3,3)
     3   6     7.17081336E-01   # UASf(3,6)
     4   1     6.75432353E-03   # UASf(4,1)
     4   4     9.99977189E-01   # UASf(4,4)
     5   2     5.75740323E-01   # UASf(5,2)
     5   5     8.17632607E-01   # UASf(5,5)
     6   3     7.17081336E-01   # UASf(6,3)
     6   6    -6.96989496E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     1.18667149E-05   # UASf(1,4)
     2   2     9.99987063E-01   # UASf(2,2)
     2   5     5.08666769E-03   # UASf(2,5)
     3   3     7.08252641E-01   # UASf(3,3)
     3   6    -7.05959062E-01   # UASf(3,6)
     4   1    -1.18667149E-05   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -5.08666769E-03   # UASf(5,2)
     5   5     9.99987063E-01   # UASf(5,5)
     6   3     7.05959062E-01   # UASf(6,3)
     6   6     7.08252641E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99928333E-01   # UASf(1,1)
     1   4    -1.19719733E-02   # UASf(1,4)
     2   2     9.83626200E-01   # UASf(2,2)
     2   5    -1.80220692E-01   # UASf(2,5)
     3   3     6.76329341E-01   # UASf(3,3)
     3   6     7.36599364E-01   # UASf(3,6)
     4   1     1.19719733E-02   # UASf(4,1)
     4   4     9.99928333E-01   # UASf(4,4)
     5   2     1.80220692E-01   # UASf(5,2)
     5   5     9.83626200E-01   # UASf(5,5)
     6   3     7.36599364E-01   # UASf(6,3)
     6   6    -6.76329341E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99999918E-01   # UH(1,1)
     1   2     4.03998756E-04   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.03998756E-04   # UH(2,1)
     2   2     9.99999918E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     3.96466012E-03   # Gamma(h0)
     2.32710979E-03   2        22        22   # BR(h0 -> photon photon)
     1.49525891E-03   2        22        23   # BR(h0 -> photon Z)
     2.73070743E-02   2        23        23   # BR(h0 -> Z Z)
     2.25256812E-01   2       -24        24   # BR(h0 -> W W)
     7.14957712E-02   2        21        21   # BR(h0 -> gluon gluon)
     5.32357797E-09   2       -11        11   # BR(h0 -> Electron electron)
     2.36802199E-04   2       -13        13   # BR(h0 -> Muon muon)
     6.80246791E-02   2       -15        15   # BR(h0 -> Tau tau)
     2.03434100E-07   2        -2         2   # BR(h0 -> Up up)
     2.81777630E-02   2        -4         4   # BR(h0 -> Charm charm)
     8.71267513E-07   2        -1         1   # BR(h0 -> Down down)
     2.18803724E-04   2        -3         3   # BR(h0 -> Strange strange)
     5.75458845E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     2.24405672E+01   # Gamma(HH)
    -2.63631123E-07   2        22        22   # BR(HH -> photon photon)
    -9.46891577E-07   2        22        23   # BR(HH -> photon Z)
    -8.63198948E-06   2        23        23   # BR(HH -> Z Z)
    -1.15899807E-05   2       -24        24   # BR(HH -> W W)
    -2.14057891E-05   2        21        21   # BR(HH -> gluon gluon)
    -6.44796893E-09   2       -11        11   # BR(HH -> Electron electron)
     2.86997132E-04   2       -13        13   # BR(HH -> Muon muon)
    -8.05827511E-02   2       -15        15   # BR(HH -> Tau tau)
    -2.09530256E-13   2        -2         2   # BR(HH -> Up up)
    -2.90030363E-08   2        -4         4   # BR(HH -> Charm charm)
    -1.71418266E-03   2        -6         6   # BR(HH -> Top top)
    -6.90378965E-07   2        -1         1   # BR(HH -> Down down)
    -1.73371138E-04   2        -3         3   # BR(HH -> Strange strange)
    -4.08554150E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -1.21896717E-01   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)
    -8.08007845E-02   2  -1000037   1000024   # BR(HH -> Chargino2 chargino1)
    -8.08007845E-02   2  -1000024   1000037   # BR(HH -> Chargino1 chargino2)
    -2.64634400E-02   2  -1000037   1000037   # BR(HH -> Chargino2 chargino2)
    -1.20359579E-02   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
    -3.59489691E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)
    -2.35417530E-02   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)
    -2.37589417E-05   2   1000022   1000035   # BR(HH -> neutralino1 neutralino4)
    -2.16439012E-02   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)
    -1.27958535E-02   2   1000023   1000025   # BR(HH -> neutralino2 neutralino3)
    -4.07478113E-03   2   1000023   1000035   # BR(HH -> neutralino2 neutralino4)
    -4.73918367E-03   2   1000025   1000025   # BR(HH -> neutralino3 neutralino3)
    -6.16544302E-02   2   1000025   1000035   # BR(HH -> neutralino3 neutralino4)
    -2.21573464E-02   2   1000035   1000035   # BR(HH -> neutralino4 neutralino4)
    -6.61917466E-05   2        25        25   # BR(HH -> h0 h0)
DECAY        36     2.21968393E+01   # Gamma(A0)
     5.55284339E-07   2        22        22   # BR(A0 -> photon photon)
     1.16255216E-06   2        22        23   # BR(A0 -> photon Z)
     4.70906936E-05   2        21        21   # BR(A0 -> gluon gluon)
     6.37387623E-09   2       -11        11   # BR(A0 -> Electron electron)
     2.83699402E-04   2       -13        13   # BR(A0 -> Muon muon)
     7.96579764E-02   2       -15        15   # BR(A0 -> Tau tau)
     1.98483214E-13   2        -2         2   # BR(A0 -> Up up)
     2.74732204E-08   2        -4         4   # BR(A0 -> Charm charm)
     1.85925008E-03   2        -6         6   # BR(A0 -> Top top)
     6.82425669E-07   2        -1         1   # BR(A0 -> Down down)
     1.71373880E-04   2        -3         3   # BR(A0 -> Strange strange)
     4.03871804E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     1.46310216E-01   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)
     5.99255097E-02   2  -1000037   1000024   # BR(A0 -> Chargino2 chargino1)
     5.99255097E-02   2  -1000024   1000037   # BR(A0 -> Chargino1 chargino2)
     4.71584212E-02   2  -1000037   1000037   # BR(A0 -> Chargino2 chargino2)
     1.33856768E-02   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
     4.20737185E-02   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)
     1.84499362E-02   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)
     1.29768483E-04   2   1000022   1000035   # BR(A0 -> neutralino1 neutralino4)
     2.67843968E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)
     8.91923535E-03   2   1000023   1000025   # BR(A0 -> neutralino2 neutralino3)
     4.98904630E-03   2   1000023   1000035   # BR(A0 -> neutralino2 neutralino4)
     5.05038335E-03   2   1000025   1000025   # BR(A0 -> neutralino3 neutralino3)
     4.37410928E-02   2   1000025   1000035   # BR(A0 -> neutralino3 neutralino4)
     3.72507733E-02   2   1000035   1000035   # BR(A0 -> neutralino4 neutralino4)
     1.26872743E-05   2        23        25   # BR(A0 -> Z h0)
     1.54140786E-37   2        25        25   # BR(A0 -> h0 h0)
DECAY        37     2.18946913E+01   # Gamma(Hp)
     6.82651747E-09   2       -11        12   # BR(Hp -> Electron nu_e)
     2.91854886E-04   2       -13        14   # BR(Hp -> Muon nu_mu)
     8.25555104E-02   2       -15        16   # BR(Hp -> Tau nu_tau)
     6.70862304E-07   2        -1         2   # BR(Hp -> Down up)
     7.75128865E-06   2        -3         2   # BR(Hp -> Strange up)
     4.37522024E-06   2        -5         2   # BR(Hp -> Bottom up)
     3.22638286E-08   2        -1         4   # BR(Hp -> Down charm)
     1.67904684E-04   2        -3         4   # BR(Hp -> Strange charm)
     6.12685620E-04   2        -5         4   # BR(Hp -> Bottom charm)
     1.42833199E-07   2        -1         6   # BR(Hp -> Down top)
     3.34609342E-06   2        -3         6   # BR(Hp -> Strange top)
     3.99204627E-01   2        -5         6   # BR(Hp -> Bottom top)
     5.82012999E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     2.02521495E-03   2   1000022   1000037   # BR(Hp -> neutralino1 chargino2)
     1.03380299E-02   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)
     1.86699870E-01   2   1000023   1000037   # BR(Hp -> neutralino2 chargino2)
     6.89525191E-02   2   1000024   1000025   # BR(Hp -> chargino1 neutralino3)
     7.46015972E-02   2   1000025   1000037   # BR(Hp -> neutralino3 chargino2)
     1.14875531E-01   2   1000024   1000035   # BR(Hp -> chargino1 neutralino4)
     1.44285941E-03   2   1000035   1000037   # BR(Hp -> neutralino4 chargino2)
     1.30776717E-05   2        24        25   # BR(Hp -> W h0)
     4.15578139E-11   2        24        35   # BR(Hp -> W HH)
     2.92242882E-11   2        24        36   # BR(Hp -> W A0)
     2.42636293E-11   2  -1000011   1000012   # BR(Hp -> Selectron1 snu_e1)
     5.48422445E-07   2  -2000011   1000012   # BR(Hp -> Selectron2 snu_e1)
     1.69813286E-07   2  -1000013   1000014   # BR(Hp -> Smuon1 snu_mu1)
     3.75094726E-07   2  -2000013   1000014   # BR(Hp -> Smuon2 snu_mu1)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
