v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -170 -150 -170 -120 {lab=VDD}
N -0 -150 120 -150 {lab=VDD}
N 120 -150 120 -120 {lab=VDD}
N 120 -0 120 70 {lab=QB}
N -170 -0 -170 70 {lab=Q}
N -170 130 -170 180 {lab=GND}
N 0 180 120 180 {lab=GND}
N 120 130 120 180 {lab=GND}
N -170 -90 -0 -90 {lab=VDD}
N -0 -150 0 -90 {lab=VDD}
N -170 -150 -0 -150 {lab=VDD}
N 120 -90 120 -80 {lab=VDD}
N 0 -80 120 -80 {lab=VDD}
N -0 -90 -0 -80 {lab=VDD}
N -170 100 -0 100 {lab=GND}
N 0 110 0 180 {lab=GND}
N -170 180 0 180 {lab=GND}
N 120 100 120 110 {lab=GND}
N 0 110 120 110 {lab=GND}
N -0 100 0 110 {lab=GND}
N 30 -90 80 -90 {lab=Q}
N 30 -90 30 -20 {lab=Q}
N -130 -20 30 -20 {lab=Q}
N -130 -20 -130 -0 {lab=Q}
N -170 -0 -130 -0 {lab=Q}
N -170 -60 -170 -0 {lab=Q}
N 30 100 80 100 {lab=Q}
N 30 40 30 100 {lab=Q}
N -130 40 30 40 {lab=Q}
N -130 0 -130 40 {lab=Q}
N -250 -90 -210 -90 {lab=QB}
N -250 100 -210 100 {lab=QB}
N -250 -200 -250 -90 {lab=QB}
N -250 -200 240 -200 {lab=QB}
N 240 -200 240 -0 {lab=QB}
N 120 -0 240 -0 {lab=QB}
N 120 -60 120 -0 {lab=QB}
N -250 100 -250 220 {lab=QB}
N -250 220 240 220 {lab=QB}
N 240 0 240 220 {lab=QB}
N -330 -30 -230 -30 {lab=Q}
N -230 -30 -230 -0 {lab=Q}
N -230 -0 -170 -0 {lab=Q}
N 370 30 370 60 {lab=BLB}
N -330 30 -330 60 {lab=BL}
N 290 -30 370 -30 {lab=QB}
N 290 -30 290 -0 {lab=QB}
N 240 -0 290 -0 {lab=QB}
N -370 0 -370 20 {lab=WWL}
N 330 0 330 30 {lab=WWL}
N 120 340 120 370 {lab=#net1}
N 60 310 80 310 {lab=RWL}
N 60 400 80 400 {lab=Q}
N 120 260 120 280 {lab=RBL}
N 120 400 220 400 {lab=GND}
N 120 430 120 460 {lab=GND}
N 120 310 220 310 {lab=#net2}
C {sg13g2_pr/sg13_hv_nmos.sym} -190 100 0 0 {name=M1
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_nmos.sym} 100 100 0 0 {name=M2
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} -190 -90 0 0 {name=M3
l=0.4u
w=0.3u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 100 -90 0 0 {name=M4
l=0.4u
w=0.3u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {gnd.sym} 0 180 0 0 {name=l1 lab=GND}
C {vdd.sym} 0 -150 0 0 {name=l2 lab=VDD}
C {lab_pin.sym} -170 0 0 0 {name=Q sig_type=std_logic lab=Q}
C {lab_pin.sym} 120 0 0 0 {name=QB sig_type=std_logic lab=QB}
C {sg13g2_pr/sg13_hv_nmos.sym} -350 0 0 0 {name=M5
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_nmos.sym} 350 0 0 0 {name=M6
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {lab_pin.sym} -330 60 0 0 {name=BL1 sig_type=std_logic lab=BL}
C {lab_pin.sym} 370 60 2 0 {name=BLB sig_type=std_logic lab=BLB}
C {lab_pin.sym} 330 30 0 0 {name=WWL sig_type=std_logic lab=WWL}
C {lab_pin.sym} -370 20 0 0 {name=WWL1 sig_type=std_logic lab=WWL}
C {sg13g2_pr/sg13_hv_nmos.sym} 100 310 0 0 {name=M7
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_nmos.sym} 100 400 0 0 {name=M8
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {lab_pin.sym} 60 310 0 0 {name=RWL sig_type=std_logic lab=RWL}
C {lab_pin.sym} 60 400 0 0 {name=Q1 sig_type=std_logic lab=Q}
C {gnd.sym} 120 460 0 0 {name=l3 lab=GND}
C {lab_pin.sym} 120 260 0 0 {name=RBL sig_type=std_logic lab=RBL}
C {gnd.sym} 220 400 0 0 {name=l4 lab=GND}
C {gnd.sym} 220 310 0 0 {name=l5 lab=GND}
