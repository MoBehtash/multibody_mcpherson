# Multibody Dynamic Simulation of a McPherson Suspension System

<h2>Description</h2>
This project is a multibody dynamic simulation of a McPherson suspension system, employing a quarter-car approach to model one corner of the vehicle. The multibody model is based on the work of [Hong, 1999], and the solution approach is based on the multibody dynamics approach introduced in [Kane, 1985] and Jason Moore's online course on multibody dynamics [Moore]. Validation of the multibody system's solutions involves comparison with a planar quarter-car model, assessing their performance in both time and frequency domains under step and sine sweep road inputs, respectively. The latter resembles a four-post rig test that is common for suspension analysis. Results demonstrate strong agreement between the multibody and planar models in equivalent scenarios.<br>

<br>

Note that based on [Hong, 1999], the planar and the multibody models are equivalent when $L_{23} = L_{24}$ and $\theta_0 = 0$.

## Limitations
In this work, linear spring and damper elements are assumed, and the mass of the control arm is neglected. The wheel is also assumed to be in contact with the ground (actuator) and its lift-off is not considered here. Additionally, the model exhibits anomalous responses for road heights exceeding 0.1 m, and some deviations from the planar quarter car at lower frequencies, which are currently under investigation.

## Acknowledgment
Some parts of the codebase in this project are adapted from the “Learn Multibody Dynamics” course [Moore].

<img src="https://github.com/MoBehtash/multibody_mcpherson/blob/main/images/schematic.jpg" alt="Alt Text" width="800">



  <table style="border-collapse: collapse; border: 1px solid black; background-color: white;">
      <tr>
        <td colspan="2" align="center" style="border: 1px solid black;"><strong>Simulation Results</strong></td>
      </tr>
  <tr style="background-color: lightgray;">
    <td align="center" style="border: 1px solid black;">Step Input</td>
    <td align="center" style="border: 1px solid black;">Sine Sweep (Four-Post Rig)</td>
  </tr>  
    <tr>
      <td align="center" style="border: 1px solid black;"><img src="https://github.com/MoBehtash/multibody_mcpherson/blob/main/images/step_animation.gif" alt="Image 1" width="380"><br><strong></strong></td>
      <td align="center" style="border: 1px solid black;"><img src="https://github.com/MoBehtash/multibody_mcpherson/blob/main/images/chirp_animation.gif" alt="Image 2" width="380"><br><strong></strong></td>
    </tr>
  </table>
  <table style="border-collapse: collapse; border: 1px solid black; background-color: white;">
    <tr>
      <td align="center" style="border: 1px solid black;"><img src="https://github.com/MoBehtash/multibody_mcpherson/blob/main/images/time_res.png" width="380"><br><strong></strong></td>
      <td align="center" style="border: 1px solid black;"><img src="https://github.com/MoBehtash/multibody_mcpherson/blob/main/images/freq_res.png" width="380"><br><strong></strong></td>
    </tr>
  </table>
  
  
## Disclaimer
Please note that while this vehicle model and analysis framework can provide valuable insights, there is no guarantee of its accuracy in representing real-world vehicle behavior. The model's simplicity and assumptions may not fully capture the complexities of actual automotive vehicles.

**Note:** Feel free to contribute, share your insights, or open issues for discussion. Collaboration is key to expanding our understanding of vehicle dynamics.

<h2>Languages and Utilities Used</h2>

- <b>Python 3.12</b>
- Packages: numpy, matplotlib, scipy, sympy, IPython


## References
- Hong, K. S., Jeon, D. S., & Sohn, H. C. (1999, June). A new modeling of the Macpherson suspension system and its optimal pole-placement control. In Proceedings of the 7th Mediterranean Conference on Control and Automation (MED99) (pp. 559-579).
- Thomas R. Kane, and David A. Levinson. Dynamics, Theory and Application. McGraw Hill, 1985
- Moore, J. K., “Learn Multibody Dynamics”, 2022, https://moorepants.github.io/learn-multibody-dynamics/


