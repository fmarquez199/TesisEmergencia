with open("consumo_neto.md", "r") as file:
  lineas = file.readlines()

with open("timestamps.txt", "r") as f:
  tiempos = f.readlines()

nodos = {"192.168.1.19":  0.0, "192.168.1.58":  0.0, "192.168.1.201": 0.0}
muestreo, i, limite = dict(), 0, len(lineas)
while i < limite:
  info, stamp = tuple(lineas[i].split(" # "))
  time = float(stamp.strip())
  try:
    muestreo[time]
  except:
    muestreo[time] = {
      "192.168.1.19":  0.0,
      "192.168.1.58":  0.0,
      "192.168.1.201": 0.0
    }
  finally:
    muestreo[time][info.split(" | ")[0]] += float(info.split(" | ")[2])
  i += 1
from numpy import trapz
# from scipy.integrate import simpson

with open("integrales.csv", "w") as f:
  f.write("Consulta,Iteracion,Manager,Worker1,Worker2\n")
  for tiempo in tiempos:
    q, step, start, end = tuple(tiempo.split(";"))
    #print(q, step, start, end.strip())
    x, y, y1, y2 = [], [], [], []
    for t, i in muestreo.items():
      if float(start) <= t <= float(end):
        x.append(t)
        y.append(i["192.168.1.201"] / 1e6)
        y1.append(i["192.168.1.19"] / 1e6)
        y2.append(i["192.168.1.58"] / 1e6)
    if len(x) > 1:
      f.write("%s,%s,%s,%s,%s\n"%(q,step,trapz(y,x),trapz(y1,x),trapz(y2,x)))
    elif len(x) == 1:
      f.write("%s,%s,%s,%s,%s*\n"%(q,step,y[0],y1[0],y2[0]))
    else:
      f.write("%s,%s,-,-,-\n"%(q,step))
