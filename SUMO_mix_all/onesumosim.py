# run one time on sumo
import os
 #caratio=[0,0,0,1]
def runsumo(caratio):
    #cartype=["mv","av","cv","cav"]
  cartype=["mv","av","cv","cav","t","a","d","s"]
  sumcaratio=float(caratio[0])+float(caratio[1])+float(caratio[2])+float(caratio[3])
  caratio0=[ float(caratio[i])/sumcaratio for i in range(4) ]

  t=caratio[4]
  a=caratio[5]
  d=caratio[6]
  s=caratio[7]
  print(caratio0)

  orientation=["s2n","s2w","s2e","e2w","e2s","e2n","n2s","n2e","n2w","w2e","w2n","w2s"]
  flow=[1115,180,102,438,141,111,1225,165,328,532,252,123]
  dpLn=[1,3,0] #departLane Number

  filename='interscetion'
  for i in range(len(caratio)):
    filename+=cartype[i]+str(caratio[i])
    roufilename=filename+'.rou.xml'
    
  with open(roufilename,'w') as file_object:
    file_object.write("""<routes>
  
  <vType id="mv"  minGap="2.5" maxSpeed="14.4"  carFollowModel="IDM" accel="2.6" decel="4.5"  tau="1" delta="4" />
  <vType id="av" length="5" minGap="%f" maxSpeed="14.4" carFollowModel="IDM"  accel="2.6" decel="4.5"  tau="%f" />
  <vType id="cv" length="5" minGap="2.5" maxSpeed="14.4" carFollowModel="IDM"  />
  <vType id="cav" length="5" minGap="2.5" maxSpeed="55" carFollowModel="IDM"  accel="2.6" decel="4.5" tau="1" />
  

  <route id="route_s2n" edges="edgeS -edgeN"/>
  <route id="route_s2w" edges="edgeS -edgeW"/>
  <route id="route_s2e" edges="edgeS -edgeE"/>

  <route id="route_e2w" edges="edgeE -edgeW"/>
  <route id="route_e2s" edges="edgeE -edgeS"/>
  <route id="route_e2n" edges="edgeE -edgeN"/>

  <route id="route_n2s" edges="edgeN -edgeS"/>
  <route id="route_n2e" edges="edgeN -edgeE"/>
  <route id="route_n2w" edges="edgeN -edgeW"/>

  <route id="route_w2e" edges="edgeW -edgeE"/>
  <route id="route_w2n" edges="edgeW -edgeN"/>
  <route id="route_w2s" edges="edgeW -edgeS"/>
""")

    for ctn in range(4): #car type number
      if caratio0[ctn]>0:
        for ori in range(12):
          file_object.write("  <flow id=\"flow_%s_%s\" \
begin=\"0\" vehsPerHour=\"%d\" type=\"%s\" \
color=\"1,0,0\" route=\"route_%s\" departLane=\"%d\" \
arrivalLane=\"current\"/>\n" % (cartype[ctn],orientation[ori],\
    flow[ori]*caratio0[ctn],cartype[ctn],orientation[ori],dpLn[ori%3]))
    file_object.write("</routes>")

  cfgfilename=filename+'.sumocfg'
  outxmlfn=filename+'.xml'
  with open(cfgfilename,'w') as file_object:
    file_object.write("""<configuration>
    <input>
        <net-file value=\"M.net.xml\"/>
        <route-files value=\"""")
    file_object.write(roufilename)
    file_object.write("\"/>")
    file_object.write("""
    </input>
    <time>
        <begin value="0"/>
        <end value="100"/>
        <step-length value="0.1"/>
    </time>

    <output>
        <netstate-dump value=\"""")
    file_object.write(outxmlfn)
    file_object.write("\"/>")
    file_object.write("""
    </output>
</configuration>""")

# print("sumo "+cfgfilename)
  os.system("sumo "+cfgfilename)
  os.system("python xml2csv.py "+outxmlfn)
