import numpy as np
import matplotlib.pyplot as plt

print("==============================================")
print("       AIRCRAFT PERFORMANCE CALCULATOR")
print("==============================================")

# ============================================================
# 1. USER INPUTS
# ============================================================

mass = float(input("Enter aircraft mass (kg): "))
wing_area = float(input("Enter wing area (m^2): "))
CL = float(input("Enter lift coefficient (CL): "))
CD = float(input("Enter drag coefficient (CD): "))
CL_max = float(input("Enter maximum lift coefficient (CLmax): "))
thrust = float(input("Enter engine thrust (N): "))
velocity = float(input("Enter aircraft velocity (m/s): "))
rho = float(input("Enter air density (kg/m^3): "))

g = 9.81
weight = mass * g

# ============================================================
# 2. BASIC AERODYNAMIC CALCULATIONS
# ============================================================

# Lift = 0.5 * rho * V^2 * S * CL
lift = 0.5 * rho * velocity**2 * wing_area * CL

# Drag = 0.5 * rho * V^2 * S * CD
drag = 0.5 * rho * velocity**2 * wing_area * CD

# Stall speed = sqrt(2W / (rho*S*CLmax))
stall_speed = np.sqrt(
    (2 * weight) /
    (rho * wing_area * CL_max)
)

wing_loading = weight / wing_area
thrust_to_weight = thrust / weight
lift_to_drag = lift / drag if drag != 0 else np.inf

print("\n==============================================")
print("                RESULTS")
print("==============================================")

print(f"Aircraft Weight       : {weight:.2f} N")
print(f"Lift                  : {lift:.2f} N")
print(f"Drag                  : {drag:.2f} N")
print(f"Stall Speed           : {stall_speed:.2f} m/s")
print(f"Stall Speed           : {stall_speed * 3.6:.2f} km/h")
print(f"Wing Loading          : {wing_loading:.2f} N/m^2")
print(f"Thrust-to-Weight      : {thrust_to_weight:.3f}")
print(f"Lift-to-Drag Ratio    : {lift_to_drag:.2f}")

# ============================================================
# 3. LIFT AND DRAG OVER A RANGE OF SPEEDS
# ============================================================

speed_range = np.linspace(10, 150, 200)

lift_range = (
    0.5 * rho * speed_range**2 * wing_area * CL
)

drag_range = (
    0.5 * rho * speed_range**2 * wing_area * CD
)

maximum_lift = np.max(lift_range)
maximum_lift_speed = speed_range[np.argmax(lift_range)]

print("\n==============================================")
print("             SPEED SIMULATION")
print("==============================================")

print(f"Maximum Lift          : {maximum_lift:.2f} N")
print(f"Speed at Maximum Lift : {maximum_lift_speed:.2f} m/s")

# Lift vs velocity
plt.figure()
plt.plot(speed_range, lift_range, label="Lift")
plt.axhline(weight, linestyle="--", label="Aircraft Weight")
plt.axvline(stall_speed, linestyle="--", label="Stall Speed")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift (N)")
plt.title("Lift vs Velocity")
plt.grid()
plt.legend()
plt.show()

# Drag vs velocity
plt.figure()
plt.plot(speed_range, drag_range, label="Drag")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Velocity")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 4. ESTIMATED TAKEOFF SPEED
# ============================================================

takeoff_speed = 1.2 * stall_speed

print("\n==============================================")
print("           TAKEOFF PERFORMANCE")
print("==============================================")

print(f"Stall Speed              : {stall_speed:.2f} m/s")
print(f"Estimated Takeoff Speed  : {takeoff_speed:.2f} m/s")
print(f"Estimated Takeoff Speed  : {takeoff_speed * 3.6:.2f} km/h")

# ============================================================
# 5. THRUST-TO-WEIGHT ANALYSIS
# ============================================================

print("\n==============================================")
print("        THRUST-TO-WEIGHT ANALYSIS")
print("==============================================")

print(f"Engine Thrust       : {thrust:.2f} N")
print(f"Aircraft Weight     : {weight:.2f} N")
print(f"Thrust-to-Weight    : {thrust_to_weight:.3f}")

# ============================================================
# 6. BASIC TAKEOFF ACCELERATION SIMULATION
# ============================================================

time_step = 0.1
simulation_time = 30

time = np.arange(
    0,
    simulation_time + time_step,
    time_step
)

velocity_sim = np.zeros(len(time))
acceleration_sim = np.zeros(len(time))
drag_sim = np.zeros(len(time))
lift_sim = np.zeros(len(time))

for i in range(1, len(time)):

    lift_sim[i] = (
        0.5 * rho * velocity_sim[i-1]**2
        * wing_area * CL
    )

    drag_sim[i] = (
        0.5 * rho * velocity_sim[i-1]**2
        * wing_area * CD
    )

    net_force = thrust - drag_sim[i]

    acceleration_sim[i] = net_force / mass

    velocity_sim[i] = (
        velocity_sim[i-1]
        + acceleration_sim[i] * time_step
    )

print("\n==============================================")
print("       TAKEOFF ACCELERATION SIMULATION")
print("==============================================")

print(f"Initial Velocity     : {velocity_sim[0]:.2f} m/s")
print(f"Final Velocity       : {velocity_sim[-1]:.2f} m/s")
print(f"Initial Acceleration : {acceleration_sim[1]:.2f} m/s^2")
print(f"Final Acceleration   : {acceleration_sim[-1]:.2f} m/s^2")

# Velocity vs time
plt.figure()
plt.plot(time, velocity_sim, label="Aircraft Velocity")
plt.axhline(takeoff_speed, linestyle="--",
            label="Estimated Takeoff Speed")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Aircraft Velocity vs Time")
plt.grid()
plt.legend()
plt.show()

# Acceleration vs time
plt.figure()
plt.plot(time, acceleration_sim, label="Aircraft Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Aircraft Acceleration vs Time")
plt.grid()
plt.legend()
plt.show()

# Lift vs time
plt.figure()
plt.plot(time, lift_sim, label="Lift")
plt.axhline(weight, linestyle="--",
            label="Aircraft Weight")
plt.xlabel("Time (s)")
plt.ylabel("Lift (N)")
plt.title("Lift vs Time During Takeoff")
plt.grid()
plt.legend()
plt.show()

# Drag vs time
plt.figure()
plt.plot(time, drag_sim, label="Drag")
plt.xlabel("Time (s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Time During Takeoff")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 7. FLIGHT PERFORMANCE SUMMARY
# ============================================================

print("\n==============================================")
print("       FLIGHT PERFORMANCE SUMMARY")
print("==============================================")

print(f"Maximum Lift              : {np.max(lift_sim):.2f} N")
print(f"Maximum Drag              : {np.max(drag_sim):.2f} N")
print(f"Maximum Velocity          : {np.max(velocity_sim):.2f} m/s")
print(f"Maximum Acceleration      : {np.max(acceleration_sim):.2f} m/s²")

# ============================================================
# 8. EFFECT OF AIRCRAFT MASS
# ============================================================

mass_range = np.linspace(0.5 * mass, 1.5 * mass, 50)

stall_speed_mass = np.sqrt(
    (2 * mass_range * g) /
    (rho * wing_area * CL_max)
)

plt.figure()
plt.plot(mass_range, stall_speed_mass,
         label="Stall Speed")
plt.xlabel("Aircraft Mass (kg)")
plt.ylabel("Stall Speed (m/s)")
plt.title("Effect of Aircraft Mass on Stall Speed")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 9. EFFECT OF THRUST
# ============================================================

thrust_range = np.linspace(0.5 * thrust, 1.5 * thrust, 50)

initial_drag = (
    0.5 * rho * velocity**2
    * wing_area * CD
)

acceleration_thrust = (
    thrust_range - initial_drag
) / mass

plt.figure()
plt.plot(thrust_range, acceleration_thrust,
         label="Acceleration")
plt.xlabel("Thrust (N)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Effect of Thrust on Aircraft Acceleration")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 10. EFFECT OF WING AREA
# ============================================================

wing_area_range = np.linspace(
    0.5 * wing_area,
    1.5 * wing_area,
    50
)

stall_speed_area = np.sqrt(
    (2 * weight) /
    (rho * wing_area_range * CL_max)
)

plt.figure()
plt.plot(wing_area_range, stall_speed_area,
         label="Stall Speed")
plt.xlabel("Wing Area (m²)")
plt.ylabel("Stall Speed (m/s)")
plt.title("Effect of Wing Area on Stall Speed")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 11. EFFECT OF AIR DENSITY
# ============================================================

density_range = np.linspace(
    0.5 * rho,
    1.5 * rho,
    50
)

stall_speed_density = np.sqrt(
    (2 * weight) /
    (density_range * wing_area * CL_max)
)

plt.figure()
plt.plot(density_range, stall_speed_density,
         label="Stall Speed")
plt.xlabel("Air Density (kg/m³)")
plt.ylabel("Stall Speed (m/s)")
plt.title("Effect of Air Density on Stall Speed")
plt.grid()
plt.legend()
plt.show()

print("\n==============================================")
print("     PARAMETER EFFECT SUMMARY")
print("==============================================")

print("1. Increasing aircraft mass increases stall speed.")
print("2. Increasing thrust increases aircraft acceleration.")
print("3. Increasing wing area decreases stall speed.")
print("4. Increasing air density decreases stall speed.")
print("5. Increasing velocity increases lift.")
print("6. Increasing velocity increases aerodynamic drag.")

# ============================================================
# 12. ANGLE OF ATTACK AERODYNAMIC MODEL
# ============================================================

print("\n==============================================")
print("     ANGLE OF ATTACK AERODYNAMIC MODEL")
print("==============================================")

alpha_min = -5
alpha_max = 20

alpha_range = np.linspace(
    alpha_min,
    alpha_max,
    100
)

# Simplified lift curve
CL_alpha = 0.1
alpha_zero_lift = -2

CL_alpha_range = (
    CL_alpha * (alpha_range - alpha_zero_lift)
)

CL_max_model = CL_max

CL_alpha_range = np.clip(
    CL_alpha_range,
    -0.5,
    CL_max_model
)

# Simplified drag polar
CD0 = 0.025
k = 0.045

CD_alpha_range = (
    CD0 + k * CL_alpha_range**2
)

# CL vs angle of attack
plt.figure()
plt.plot(alpha_range, CL_alpha_range,
         label="CL")
plt.axhline(CL_max_model, linestyle="--",
            label="Maximum CL")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("Lift Coefficient vs Angle of Attack")
plt.grid()
plt.legend()
plt.show()

# CD vs angle of attack
plt.figure()
plt.plot(alpha_range, CD_alpha_range,
         label="CD")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("Drag Coefficient vs Angle of Attack")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 13. LIFT AND DRAG VS ANGLE OF ATTACK
# ============================================================

lift_alpha = (
    0.5 * rho * velocity**2
    * wing_area * CL_alpha_range
)

drag_alpha = (
    0.5 * rho * velocity**2
    * wing_area * CD_alpha_range
)

plt.figure()
plt.plot(alpha_range, lift_alpha, label="Lift")
plt.plot(alpha_range, drag_alpha, label="Drag")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Force (N)")
plt.title("Lift and Drag vs Angle of Attack")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 14. LIFT-TO-DRAG RATIO VS ANGLE OF ATTACK
# ============================================================

LD_ratio_alpha = (
    lift_alpha / np.maximum(drag_alpha, 1e-9)
)

maximum_LD_index = np.argmax(LD_ratio_alpha)

best_alpha = alpha_range[maximum_LD_index]
maximum_LD = LD_ratio_alpha[maximum_LD_index]

print("\n==============================================")
print("       AERODYNAMIC EFFICIENCY")
print("==============================================")

print(f"Maximum L/D Ratio      : {maximum_LD:.2f}")
print(f"Best Angle of Attack   : {best_alpha:.2f} degrees")

plt.figure()
plt.plot(alpha_range, LD_ratio_alpha,
         label="L/D Ratio")
plt.axvline(best_alpha, linestyle="--",
            label="Best Angle of Attack")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Lift-to-Drag Ratio")
plt.title("Lift-to-Drag Ratio vs Angle of Attack")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 15. REALISTIC TAKEOFF SIMULATION
# ============================================================

print("\n==============================================")
print("       REALISTIC TAKEOFF SIMULATION")
print("==============================================")

dt = 0.05
takeoff_simulation_time = 40

takeoff_time = np.arange(
    0,
    takeoff_simulation_time,
    dt
)

takeoff_velocity = np.zeros(len(takeoff_time))
takeoff_acceleration = np.zeros(len(takeoff_time))
takeoff_lift = np.zeros(len(takeoff_time))
takeoff_drag = np.zeros(len(takeoff_time))
takeoff_alpha = np.zeros(len(takeoff_time))

initial_alpha = 2

for i in range(1, len(takeoff_time)):

    takeoff_alpha[i] = initial_alpha

    CL_current = (
        CL_alpha
        * (takeoff_alpha[i] - alpha_zero_lift)
    )

    CL_current = np.clip(
        CL_current,
        -0.5,
        CL_max_model
    )

    CD_current = (
        CD0 + k * CL_current**2
    )

    takeoff_lift[i] = (
        0.5
        * rho
        * takeoff_velocity[i-1]**2
        * wing_area
        * CL_current
    )

    takeoff_drag[i] = (
        0.5
        * rho
        * takeoff_velocity[i-1]**2
        * wing_area
        * CD_current
    )

    net_force = thrust - takeoff_drag[i]

    takeoff_acceleration[i] = (
        net_force / mass
    )

    takeoff_velocity[i] = (
        takeoff_velocity[i-1]
        + takeoff_acceleration[i] * dt
    )

# ============================================================
# 16. FIND TAKEOFF POINT
# ============================================================

takeoff_index = None

for i in range(len(takeoff_time)):

    if takeoff_lift[i] >= weight:
        takeoff_index = i
        break

if takeoff_index is not None:

    actual_takeoff_time = takeoff_time[takeoff_index]

    actual_takeoff_velocity = (
        takeoff_velocity[takeoff_index]
    )

    print(f"Estimated Takeoff Time : "
          f"{actual_takeoff_time:.2f} s")

    print(f"Takeoff Velocity        : "
          f"{actual_takeoff_velocity:.2f} m/s")

    print(f"Takeoff Velocity        : "
          f"{actual_takeoff_velocity * 3.6:.2f} km/h")

else:

    print("Aircraft did not generate enough lift "
          "during the simulation.")

# Takeoff velocity graph
plt.figure()
plt.plot(takeoff_time, takeoff_velocity,
         label="Aircraft Velocity")
plt.axhline(takeoff_speed, linestyle="--",
            label="Estimated Takeoff Speed")

if takeoff_index is not None:
    plt.axvline(actual_takeoff_time,
                linestyle="--",
                label="Takeoff Point")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Aircraft Velocity During Takeoff")
plt.grid()
plt.legend()
plt.show()

# Takeoff acceleration graph
plt.figure()
plt.plot(takeoff_time, takeoff_acceleration,
         label="Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Aircraft Acceleration During Takeoff")
plt.grid()
plt.legend()
plt.show()

# Lift and weight graph
plt.figure()
plt.plot(takeoff_time, takeoff_lift,
         label="Lift")
plt.axhline(weight, linestyle="--",
            label="Aircraft Weight")

if takeoff_index is not None:
    plt.axvline(actual_takeoff_time,
                linestyle="--",
                label="Takeoff Point")

plt.xlabel("Time (s)")
plt.ylabel("Force (N)")
plt.title("Lift and Weight During Takeoff")
plt.grid()
plt.legend()
plt.show()

# Drag graph
plt.figure()
plt.plot(takeoff_time, takeoff_drag,
         label="Drag")
plt.xlabel("Time (s)")
plt.ylabel("Drag (N)")
plt.title("Aerodynamic Drag During Takeoff")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 17. BASIC FLIGHT PATH SIMULATION
# ============================================================

print("\n==============================================")
print("        BASIC FLIGHT PATH SIMULATION")
print("==============================================")

flight_dt = 0.1

flight_time = np.arange(
    0,
    60,
    flight_dt
)

flight_velocity = np.zeros(len(flight_time))
flight_altitude = np.zeros(len(flight_time))
flight_distance = np.zeros(len(flight_time))

flight_velocity[0] = (
    actual_takeoff_velocity
    if takeoff_index is not None
    else takeoff_speed
)

# Simplified climb angle
climb_angle = np.radians(10)

for i in range(1, len(flight_time)):

    current_drag = (
        0.5
        * rho
        * flight_velocity[i-1]**2
        * wing_area
        * CD
    )

    net_force = thrust - current_drag

    acceleration = net_force / mass

    flight_velocity[i] = (
        flight_velocity[i-1]
        + acceleration * flight_dt
    )

    horizontal_velocity = (
        flight_velocity[i]
        * np.cos(climb_angle)
    )

    vertical_velocity = (
        flight_velocity[i]
        * np.sin(climb_angle)
    )

    flight_altitude[i] = (
        flight_altitude[i-1]
        + vertical_velocity * flight_dt
    )

    flight_distance[i] = (
        flight_distance[i-1]
        + horizontal_velocity * flight_dt
    )

# Altitude vs time
plt.figure()
plt.plot(flight_time, flight_altitude,
         label="Altitude")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Aircraft Altitude vs Time")
plt.grid()
plt.legend()
plt.show()

# Distance vs time
plt.figure()
plt.plot(flight_time, flight_distance,
         label="Flight Distance")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Aircraft Distance vs Time")
plt.grid()
plt.legend()
plt.show()

# Flight path
plt.figure()
plt.plot(flight_distance, flight_altitude,
         label="Flight Path")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Altitude (m)")
plt.title("Basic Aircraft Flight Path")
plt.grid()
plt.legend()
plt.show()

# ============================================================
# 18. FINAL AIRCRAFT PERFORMANCE REPORT
# ============================================================

print("\n==============================================")
print("       FINAL AIRCRAFT PERFORMANCE REPORT")
print("==============================================")

print(f"Aircraft Mass              : {mass:.2f} kg")
print(f"Wing Area                  : {wing_area:.2f} m²")
print(f"Air Density                : {rho:.3f} kg/m³")
print(f"Aircraft Weight            : {weight:.2f} N")
print(f"Engine Thrust              : {thrust:.2f} N")
print(f"Lift                       : {lift:.2f} N")
print(f"Drag                       : {drag:.2f} N")
print(f"Lift-to-Drag Ratio         : {lift_to_drag:.2f}")
print(f"Thrust-to-Weight Ratio     : {thrust_to_weight:.3f}")
print(f"Stall Speed                : {stall_speed:.2f} m/s")
print(f"Estimated Takeoff Speed    : {takeoff_speed:.2f} m/s")
print(f"Maximum Simulated Velocity : "
      f"{np.max(velocity_sim):.2f} m/s")
print(f"Maximum Acceleration       : "
      f"{np.max(acceleration_sim):.2f} m/s²")
print(f"Maximum L/D                : "
      f"{maximum_LD:.2f}")
print(f"Best Angle of Attack      : "
      f"{best_alpha:.2f} degrees")
print(f"Maximum Flight Altitude   : "
      f"{np.max(flight_altitude):.2f} m")
print(f"Maximum Flight Distance   : "
      f"{np.max(flight_distance):.2f} m")

print("\n==============================================")
print("       AIRCRAFT PERFORMANCE ANALYSIS")
print("              COMPLETED")
print("==============================================")
