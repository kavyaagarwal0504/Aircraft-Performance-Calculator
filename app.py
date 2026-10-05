from flask import Flask, request, jsonify, send_from_directory
import numpy as np

app = Flask(__name__, static_folder="../frontend", static_url_path="")

def calculate(p):
    mass=float(p["mass"]); S=float(p["wing_area"]); CL=float(p["CL"])
    CD=float(p["CD"]); CLmax=float(p["CL_max"]); T=float(p["thrust"])
    V0=float(p["velocity"]); rho=float(p["rho"]); g=9.81
    W=mass*g
    L=.5*rho*V0**2*S*CL
    D=.5*rho*V0**2*S*CD
    Vs=np.sqrt(2*W/(rho*S*CLmax)); Vto=1.2*Vs
    # speed curves
    sp=np.linspace(10,150,150)
    Lsp=.5*rho*sp**2*S*CL; Dsp=.5*rho*sp**2*S*CD
    # time simulation
    dt=.05; t=np.arange(0,30+dt,dt)
    v=np.zeros_like(t); a=np.zeros_like(t); lt=np.zeros_like(t); dr=np.zeros_like(t)
    for i in range(1,len(t)):
        lt[i]=.5*rho*v[i-1]**2*S*CL
        dr[i]=.5*rho*v[i-1]**2*S*CD
        a[i]=(T-dr[i])/mass
        v[i]=v[i-1]+a[i]*dt
    # AoA model
    alpha=np.linspace(-5,20,120)
    cla=.1; a0=-2
    cl=np.clip(cla*(alpha-a0),-.5,CLmax)
    cd0=.025; k=.045
    cda=cd0+k*cl**2
    la=.5*rho*V0**2*S*cl; da=.5*rho*V0**2*S*cda
    ldr=la/np.maximum(da,1e-9); bi=int(np.argmax(ldr))
    # sensitivity
    masses=np.linspace(.5*mass,1.5*mass,50)
    areas=np.linspace(.5*S,1.5*S,50)
    dens=np.linspace(.5*rho,1.5*rho,50)
    thrusts=np.linspace(.5*T,1.5*T,50)
    sm=np.sqrt(2*masses*g/(rho*S*CLmax))
    sa=np.sqrt(2*W/(rho*areas*CLmax))
    sd=np.sqrt(2*W/(dens*S*CLmax))
    refD=.5*rho*V0**2*S*CD
    at=(thrusts-refD)/mass
    return {"metrics":{
        "weight":W,"lift":L,"drag":D,"stall_speed":Vs,"takeoff_speed":Vto,
        "wing_loading":W/S,"thrust_to_weight":T/W,"lift_to_drag":L/D if D else 0,
        "best_alpha":float(alpha[bi]),"max_ld":float(ldr[bi]),
        "max_takeoff_velocity":float(v.max()),"max_acceleration":float(a.max())},
        "charts":{
        "speed":{"x":sp.tolist(),"lift":Lsp.tolist(),"drag":Dsp.tolist()},
        "takeoff":{"x":t.tolist(),"velocity":v.tolist(),"acceleration":a.tolist(),"lift":lt.tolist(),"drag":dr.tolist()},
        "alpha":{"x":alpha.tolist(),"cl":cl.tolist(),"cd":cda.tolist(),"ld":ldr.tolist()},
        "mass":{"x":masses.tolist(),"y":sm.tolist()},
        "thrust":{"x":thrusts.tolist(),"y":at.tolist()},
        "area":{"x":areas.tolist(),"y":sa.tolist()},
        "density":{"x":dens.tolist(),"y":sd.tolist()}}}

@app.route("/")
def home(): return send_from_directory("../frontend","index.html")

@app.post("/api/calculate")
def api():
    try: return jsonify({"ok":True,"result":calculate(request.get_json())})
    except Exception as e: return jsonify({"ok":False,"error":str(e)}),400

if __name__=="__main__":
    app.run(debug=True)
