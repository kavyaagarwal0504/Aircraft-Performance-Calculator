const cfg={responsive:true,displayModeBar:false};
function inp(){let ids=["mass","wing_area","CL","CD","CL_max","thrust","velocity","rho"];let o={};ids.forEach(id=>o[id]=+document.getElementById(id).value);return o}
function plot(id,title,x,y,n,xlab,ylab){Plotly.newPlot(id,[{x,y,name:n,mode:"lines"}],{title:{text:title,font:{size:16}},margin:{l:55,r:15,t:45,b:50},xaxis:{title:xlab},yaxis:{title:ylab},hovermode:"x unified",legend:{orientation:"h"}},cfg)}
function two(id,title,x,a,b,al,bl,xlab,ylab){Plotly.newPlot(id,[{x,y:a,name:al,mode:"lines"},{x,y:b,name:bl,mode:"lines"}],{title:{text:title,font:{size:16}},margin:{l:55,r:15,t:45,b:50},xaxis:{title:xlab},yaxis:{title:ylab},hovermode:"x unified"},cfg)}
function run(){document.getElementById("status").textContent=" Running...";fetch("/api/calculate",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(inp())}).then(r=>r.json()).then(d=>{if(!d.ok)throw Error(d.error);let m=d.result.metrics,c=d.result.charts;
let names=[["Weight",m.weight,"N"],["Lift",m.lift,"N"],["Drag",m.drag,"N"],["Stall Speed",m.stall_speed,"m/s"],["Takeoff Speed",m.takeoff_speed,"m/s"],["T/W",m.thrust_to_weight,""],["L/D",m.lift_to_drag,""],["Best AoA",m.best_alpha,"°"],["Max L/D",m.max_ld,""],["Max Accel",m.max_acceleration,"m/s²"]];
document.getElementById("metrics").innerHTML=names.map(x=>`<div class="metric"><small>${x[0]}</small><strong>${x[1].toFixed(2)} ${x[2]}</strong></div>`).join("");
two("g1","Lift and Drag vs Velocity",c.speed.x,c.speed.lift,c.speed.drag,"Lift","Drag","Velocity (m/s)","Force (N)");
plot("g2","Velocity During Takeoff",c.takeoff.x,c.takeoff.velocity,"Velocity","Time (s)","Velocity (m/s)");
plot("g3","Acceleration During Takeoff",c.takeoff.x,c.takeoff.acceleration,"Acceleration","Time (s)","Acceleration (m/s²)");
plot("g4","Lift During Takeoff",c.takeoff.x,c.takeoff.lift,"Lift","Time (s)","Lift (N)");
plot("g5","Drag During Takeoff",c.takeoff.x,c.takeoff.drag,"Drag","Time (s)","Drag (N)");
plot("g6","CL vs Angle of Attack",c.alpha.x,c.alpha.cl,"CL","Angle (°)","CL");
plot("g7","CD vs Angle of Attack",c.alpha.x,c.alpha.cd,"CD","Angle (°)","CD");
plot("g8","L/D vs Angle of Attack",c.alpha.x,c.alpha.ld,"L/D","Angle (°)","L/D");
plot("g9","Mass Effect on Stall Speed",c.mass.x,c.mass.y,"Stall Speed","Mass (kg)","Stall Speed (m/s)");
plot("g10","Thrust Effect on Acceleration",c.thrust.x,c.thrust.y,"Acceleration","Thrust (N)","Acceleration (m/s²)");
plot("g11","Wing Area Effect on Stall Speed",c.area.x,c.area.y,"Stall Speed","Wing Area (m²)","Stall Speed (m/s)");
plot("g12","Density Effect on Stall Speed",c.density.x,c.density.y,"Stall Speed","Density (kg/m³)","Stall Speed (m/s)");
document.getElementById("status").textContent=" Simulation complete";}).catch(e=>document.getElementById("status").textContent=" Error: "+e.message)}
run();