import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math

def eval_rhs(t, x, p, vel, road_fun):
    """
    This function returns the time derivative of the generalized coordinates dot{q} and
    speeds dot{u} by calculating the right-hand side of the state-space equations.
    
    Inputs:
    ---------
        t: float,                  time of simulation [s]  
        x: array_like, shape(4,).  system state at time t: [q1, q2, u1, u2]   
        p: array_like, shape(7,).  parameters of the system: [sprung_mass, unsprung_mass, suspension_stiffness, tire_stiffness, suspension_damping,                                                                            vehicle_speed, road_type]
    
    Outputs:
    -------
        xd: ndarray, shape(4,),     time derivative of the states: [qd1, qd2, ud1, ud2]  
    """  
    # Extract the parameters from p
    sprung_mass          = p[0] # [kg]
    unsprung_mass        = p[1] # [kg]
    suspension_stiffness = p[2] # [N/m]
    tire_stiffness       = p[3] # [N/m]
    suspension_damping   = p[4] # [N/m/s]

    # Extract the state values from x
    q = x[:2] # generalized coordinates
    u = x[2:] # generalized speeds  

    # Renaming variables for ease of use and reading
    ms = sprung_mass
    mu = unsprung_mass
    ks = suspension_stiffness
    kt = tire_stiffness
    cs = suspension_damping

    # Evaluate the road input at the time t
    zr = road_fun(t, vel)
    
    # Damping and stiffness matrices
    C = np.array([ [-cs/ms, cs/ms], [cs/mu, -cs/mu] ])
    K = np.array([ [-ks/ms, ks/ms], [ks/mu, -(kt+ks)/mu] ])

    # Equations of motions
    qd = u
    ud = np.matmul(C,u)+ np.matmul(K, q) + np.array([0, kt/mu*zr])

    # Return the time derivative of the states
    xd     = np.empty_like(x)
    xd[:2] = qd
    xd[2:] = ud
    
    return xd

def run_planar_qcar(x0_vals, p_vals, t0_val, tf_val, ts_vals, vel_val, road_fun):

    # Solve the system of equations using eval_rhs
    sol = solve_ivp(eval_rhs, t_span = [t0_val, tf_val], y0 = x0_vals, t_eval=ts_vals,
                    method='RK45', args=(p_vals, vel_val, road_fun), atol = 1e-6, rtol = 1e-6)
    xsol = np.transpose(sol.y)
    tsol = sol.t
    
    # Calculate the time derivative of the generalized coordinates and speeds
    xdsol = np.empty_like(xsol)
    for i in range(len(sol.t)):
        xdsol[i,:] = eval_rhs(sol.t[i], sol.y[:,i], p_vals, vel_val, road_fun)

    return tsol, xsol, xdsol

