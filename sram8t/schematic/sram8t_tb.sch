v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 170 0 210 0 {lab=#net1}
N 170 20 270 20 {lab=#net2}
N 270 0 270 20 {lab=#net2}
N 270 -80 270 -60 {lab=GND}
N 210 -80 210 -60 {lab=GND}
N 320 0 320 20 {lab=GND}
N 320 -80 320 -60 {lab=VDD}
N -170 0 -130 0 {lab=#net3}
N -170 -80 -170 -60 {lab=GND}
N -170 20 -130 20 {lab=#net4}
N -170 80 -170 100 {lab=GND}
N 80 140 160 140 {lab=VDD}
N 80 180 160 180 {lab=VDD}
N 60 140 80 140 {lab=VDD}
N 200 180 210 180 {lab=#net5}
N 200 100 200 110 {lab=GND}
N 160 170 160 180 {lab=VDD}
N 80 140 80 180 {lab=VDD}
N 200 140 200 180 {lab=#net5}
N 210 240 210 260 {lab=GND}
N 160 60 160 110 {lab=#net6}
N 160 60 180 60 {lab=#net6}
N 180 40 180 60 {lab=#net6}
N 170 40 180 40 {lab=#net6}
N 180 40 200 40 {lab=#net6}
C {vsource.sym} 320 -30 0 0 {name=V1 value=1.2 savecurrent=false}
C {vdd.sym} 320 -80 0 0 {name=VDD lab=VDD}
C {gnd.sym} 320 20 0 0 {name=GND lab=GND}
C {vsource.sym} 210 -30 2 0 {name=V3 value=1.2 savecurrent=false}
C {vsource.sym} 270 -30 2 0 {name=V2 value=0 savecurrent=false}
C {gnd.sym} 210 -80 2 0 {name=l1 lab=GND}
C {gnd.sym} 270 -80 2 0 {name=l2 lab=GND}
C {vsource.sym} -170 -30 2 0 {name=V4 value="PULSE(0 1.2 12n 10p 10p 5n 50n)" savecurrent=false}
C {gnd.sym} -170 -80 2 0 {name=l3 lab=GND}
C {vsource.sym} -170 50 0 0 {name=V5 value="PULSE(0 1.2 5n 10p 10p 5n 50n)" savecurrent=false}
C {gnd.sym} -170 100 0 0 {name=l4 lab=GND}
C {sram8t.sym} 20 20 0 0 {name=x1}
C {gnd.sym} 200 110 0 0 {name=l5 lab=GND}
C {code_shown.sym} -380 -280 0 0 {name=s1 only_toplevel=false value=".lib /opt/pdks/ihp-sg13g2/libs.tech/ngspice/models/cornerMOSlv.lib mos_tt

.tran 10p 20n uic

.measure tran t_write TRIG v(net3) VAL=0.6 RISE=1 TARG v(x1.q) VAL=0.6 FALL=1

.measure tran t_read TRIG v(net4) VAL=0.6 RISE=1 TARG v(net6) VAL=0.6 FALL=1

.measure tran p_avg AVG par('-v(VDD)*i(V1)') FROM=0n TO=20n

.measure tran p_write AVG par('-v(VDD)*i(V1)') FROM=12n TO=17n

.measure tran p_read AVG par('-v(VDD)*i(V1)') FROM=5n TO=10n

.ic v(x1.q)=1.2
.ic v(x1.qb)=0"}
C {sg13g2_pr/sg13_lv_pmos.sym} 180 140 2 0 {name=M1
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {vdd.sym} 60 140 3 0 {name=l6 lab=VDD}
C {vsource.sym} 210 210 0 0 {name=V_PRE value="PULSE(0 1.2 11n 10p 10p 20n 50n)" savecurrent=false}
C {gnd.sym} 210 260 0 0 {name=l7 lab=GND}
C {capa.sym} 200 70 0 0 {name=C1
m=1
value=10f
footprint=1206
device="ceramic capacitor"}
