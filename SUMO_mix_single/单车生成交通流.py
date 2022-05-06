import os
import numpy as np
import pandas as pd

roufilename = '1.rou.xml'
with open(roufilename, 'w') as file_object:
    file_object.write("""<routes>

		<vType id="AV"  minGap="1" maxSpeed="14" color='0,0,1'  jmStoplineGap="4" carFollowModel="ACC" accel="1.8" decel="4.5" tau="1.5"   />
		<vType id="CAV"  minGap="2.2" maxSpeed="14" color='0,1,1'  jmStoplineGap="4" carFollowModel="CACC" accel="1.8" decel="4.5" tau="0.6"   />
		<route id="route_s2n" edges="edgeS -edgeN"/>
""")

    for i in range(1, 40):
        firstone = i % 40

        g = i
        a = i // 14.001
        b = 45 + 183 * a
        c = 183 + 183 * a
        file_object.write(            '  <flow id="flow_av_s2n%d" begin="%d" end="%d" number="1" type="CAV"  route="route_s2n" departLane="0" arrivalLane="0"/> \n  ' % (
            i, b, c))

    # if firstone==11 or firstone==12:# or firstone==3 or firstone==4 or firstone==5 or firstone==6 or firstone==7 or firstone==8 or firstone==9 or firstone==10 or firstone==11 :# or firstone==12 or firstone==13 :# or firstone==0:
    # 	g=i
    # 	a=i//14.001
    # 	b=45+183*a
    # 	c=183+183*a
    # 	file_object.write('  <flow id="flow_av_s2n%d" begin="%d" end="%d" number="1" type="AV"  route="route_s2n" departLane="0" arrivalLane="0"/> \n  '  %(i,b,c))
    # elif firstone==13 or firstone==0 :#or firstone==13:#
    # 	g=i
    # 	a=i//14.001
    # 	b=45+183*a
    # 	c=183+183*a
    # 	file_object.write('  <flow id="flow_cav_s2n%d" begin="%d" end="%d" number="1" type="CAV"  route="route_s2n" departLane="0" arrivalLane="0"/> \n  '  %(i,b,c))
    # else:
    # 	a=0
    # 	a+=i
    # 	b=i//14.001
    # 	c=45+183*b
    # 	e=183+183*b
    # 	file_object.write('<flow id="flow_mv_s2n%d" begin="%d" end="%d" number="1" type="vehDist%d"  route="route_s2n" departLane="0" arrivalLane="0"/> \n  '   %(i,c,e,i))
    file_object.write("</routes>")

cfgfilename = "1.sumocfg"
os.system("sumo " + cfgfilename)
outxmlfn = "E:\\SUMO_test\\test_leader\\1.xml"
os.system("python xml2csv.py " + outxmlfn)

pd = pd.read_csv(r'E:\SUMO_test\test_leader\1.csv', encoding='utf-8', sep=';')
pd1 = pd.loc[pd['vehicle_id'] == 'flow_av_s2n14.0', ['timestep_time', 'vehicle_pos', 'lane_id', "vehicle_speed", ]]
pd1 = pd1.loc[pd['lane_id'] == ':nodeC_2_0', ['timestep_time', 'vehicle_pos', "vehicle_speed", ]]
pd1['list'] = pd1['timestep_time'] - 183
pd1.to_csv(r'E:\SUMO_test\test_leader\AV11 12.csv')
