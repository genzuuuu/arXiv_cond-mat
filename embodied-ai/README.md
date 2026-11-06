### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-06T13:13:35.703841
  - **arXiv update** 2026-11-06T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv: Embodied Intelligence & Robotic Manipulation

## Dexterous Manipulation & Robotic Hands

**[TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation](https://arxiv.org/abs/2611.07881)**
Built on IsaacLab, this framework simulates shear via optical flow from rigid-body dynamics rather than soft-body physics, producing "tactile flow" fields. Includes a real-to-sim translation method and a policy architecture processing long-horizon proprioception with tactile observations. Demonstrated on dual-arm and in-hand manipulation.

**[AnyDexRT: Calibration-Efficient Dexterous Hand Retargeting with Few-Shot Human Guidance](https://arxiv.org/abs/2607.08341)**
Combines self-supervised fingertip correspondence learning with few-shot human guidance and a contact classifier for pinch poses. Reduces manual tuning and improves teleoperation intuitiveness across multiple dexterous hands.

**[Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation](https://arxiv.org/abs/2610.21180)**
30 tasks in six functional families, 1,248 VR-teleoperated multimodal demos on Shadow Hands with 123 taxels. Best of six policies reaches only 24.4% average success, showing weak transfer of functional interaction knowledge.

**[Latent RL Priors for Data-Efficient Dexterous Manipulation](https://arxiv.org/abs/2611.08458)**
Two-stage: distill privileged RL rollouts into a flow-matching action decoder, then learn a visual interface to its latent context. Beats π0.5 and GR00T N1.7 in low-data regimes (10×/5× fewer demos on door lifting and bimanual assembly).

**[OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing](https://arxiv.org/abs/2610.31661)**
Resistive tactile skin with structured deformable overlay decoding shear and normal force, plus a CAD tool generating fabrication files from 2D outlines or text. Over 30 sensors fabricated; kilohertz partial readouts and high dynamic range demonstrated.

## Tactile & Contact-Rich Manipulation

**[VTAM: Efficient Visuo-Tactile World-Action Models for Contact-Rich Manipulation without Tactile Pretraining](https://arxiv.org/abs/2603.23481)**
Shares a frozen video VAE and transformer across RGB and tactile; predicts future visual/tactile latents then fine-tunes with an action expert. Matches models pretrained on 30K+ hours of visuo-tactile data (83.4% vs 84.5%) while running ~6–16× faster. Notably, ablations show that feeding tactile features directly to the action expert (bypassing tactile world modeling) fails on every task.

**[Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation](https://arxiv.org/abs/2611.07532)**
A VLM localizes task-relevant regions, then human-in-the-loop residual RL learns fine contact behaviors with force feedback. Object-centric augmentation randomizes backgrounds for visual robustness across six real tasks.

**[A Multimodal Haptic Interface for Simultaneous Softness and Thermal Modulation](https://arxiv.org/abs/2611.08398)**
Particle jamming plus heated/cooled water achieves 300% stiffness change and 10–50 °C with 0.2 °C closed-loop error. Relevant to haptic display but not robot manipulation per se.

## Grasping & Benchmarking

**[GraspBench: Execution-Aware Cross-Robot Evaluation of 6-DoF Grasp Generation in MuJoCo](https://arxiv.org/abs/2611.07651)**
3,240 method-scenario evaluations across four embodiments with IK filtering, motion planning, and fixed execution. GraspGen leads at 73.1%; GPG's large candidate sets yield only 44.3%, showing proposal volume ≠ executable grasps.

**[Wedge-Jamming Mechanism for String Configuration](https://arxiv.org/abs/2611.07748)**
Adds wedge-shaped contact surfaces to wire-jamming modules; out-wedge resists vertical disturbances, in-wedge resists torsion. Anisotropic holding tunable by wedge angle.

**[LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation](https://arxiv.org/abs/2611.07515)**
Quadruped loco-manipulation with explicit base-placement/approach-direction reachability and a stage-aware mixture-of-experts policy. Jointly determines base pose, pre-grasp alignment, and grasp execution.

## Visuomotor Policies & VLA Models

**[La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156)**
Trains a policy transformer from scratch in V-JEPA 2.1 feature space, predicting future features jointly with actions during training but only actions at inference. SOTA among policies without embodied pretraining on RoboTwin 2.0 and LIBERO-Plus, faster than Fast-WAM at comparable performance. Argues robot foundation models should use control-native architectures rather than adapted generators.

**[Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)**
Encodes each control step as a continuous latent action token inside a shared diffusion VLM backbone; active action projections are just 0.21% of a 4.46B model. 98.15% on LIBERO, 85.9% on LIBERO-Plus.

**[SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373)**
Aligns VLA visual embeddings with a frozen 3D perception model during continual pretraining, with feature-dependent gates for multi-layer aggregation and partial depth/calibration as teacher. Auxiliary components are training-only.

**[T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](https://arxiv.org/abs/2611.08413)**
Segmentation-guided token pruning (85% of scene-camera tokens removed on LIBERO-Spatial with matched success) plus saliency-guided attention biasing. Up to 3.3× speedup as resolution grows; +7 points under OOD placement shifts.

**[JADE: Vision-Language Models Are Joint Denoisers in Robotic Action Generation](https://arxiv.org/abs/2611.01215)**
The VLM reads the noisy action at every denoising step and guides via gated cross-attention, rather than static conditioning. 12.67% on RoboDojo; +20.8 points over π0.5 on four real bimanual tasks.

**[Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing](https://arxiv.org/abs/2611.08425)**
Lightweight probe (VLA-Tug) over VLA latent layers for runtime failure detection and mode prediction. Up to +30% early detection at matched FPR; bounds remain valid under shift in up to 86% of runs.

**[OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](https://arxiv.org/abs/2611.08462)**
Infers intent behind a handful of corrective demos via abduction, encodes it as dense spatial costs, and generalizes corrections to novel objects and scenes without new data.

**[When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](https://arxiv.org/abs/2602.17659)**
Introduces LIBERO-CF and finds VLAs act on visual shortcuts instead of language. A training-free dual-branch inference scheme (CAG) improves language grounding by 9.7–15.5% and real-world success by 17.2%.

## Teleoperation & Egocentric Data

**[VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations](https://arxiv.org/abs/2611.07272)**
PICO 4 Ultra demonstrations with per-recording grasp thresholds and mask propagation. 40 demos yield 60–74/100 placements in simulation—comparable to Project Aria recordings.

**[EgoKit: Towards Unified Low-Cost Egocentric Data Collection with Heterogeneous Devices](https://arxiv.org/abs/2605.16797)**
Identical recording workflow across six host devices (phones, tablets, glasses, XR) with uniform logs, plus wrist-camera accessories. Validated by replicating HumanEgo results.

**[Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)**
RoboTryOn swaps the human for a target robot while preserving motion, objects, and scene; a depth-aware IDM infers actions. Raises novel-task success from 2% to 60% with no real demos, matching teleoperation at ~1/3 the cost.

**[CubeDAgger: Interactive Imitation Learning for Dynamic Systems with Efficient yet Low-risk Interaction](https://arxiv.org/abs/2505.04897)**
Adds threshold regularization, optimal consensus over action candidates, and colored exploration noise to EnsembleDAgger. Learns robust scooping from 30 minutes of interaction without destabilizing dynamics.

## World Models & Sim-to-Real

**[GPWM: Modeling the World as 3D Particle Motion](https://arxiv.org/abs/2611.08338)**
Generative particle world model operating in 3D physical space across rigid, deformable, cloth, and granular materials. One unified model reduces prediction error 31% and enables contact-rich planning by searching latent noise rather than action space.

**[WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977)**
Explicitly manages imperfect imagined dynamics via keyframe-initialized rollouts and world-model–policy co-evolution. Stable long-horizon imagined rollouts yield LIBERO gains and real-robot improvements.

**[RoboCurate: Harnessing Diversity with Action-Verified Synthetic Data for Robot Learning](https://arxiv.org/abs/2602.18742)**
Executes IDM-predicted actions in simulation and verifies motion agreement with generated video. +90.3% on GR-1 Tabletop and +179.9% on real humanoid benchmarks over real-data-only training.

**[Stress Test for Test-Time Search: When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity](https://arxiv.org/abs/2610.41970)**
Pre-registered audit on Cosmos Policy/RoboCasa: learned value selectors underperform random by 1.66 pp, 82% of states have identical candidate outcomes, and token pruning yields only 1.15× end-to-end speedup. Also identifies and fixes a silent rendering corruption.

**[MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation](https://arxiv.org/abs/2611.08372)**
Combines 3D Gaussian Splatting, feed-forward 3D models, and kinematics retargeting to re-render both scene and manipulated object from unseen base poses. More than doubles baseline success on five real tasks.

**[VisionSIM: Beyond Idealized Sensors — A Multi-Modal Simulator for Robot Perception](https://arxiv.org/abs/2611.08368)**
Models raw physical measurement processes (LiDAR pileup/glare, iToF phase wrapping, event refractory drops, thermal history dependence), enabling cross-modality comparison on identical scenes.

**[Learning Robotic World Models with Semantic and Visual Feedback](https://arxiv.org/abs/2611.07850)**
RoboImagine post-trains autoregressive world models via candidate-future comparisons with a frozen multimodal evaluator and pixel/perceptual feedback. +1.26 dB PSNR and −11.93% LPIPS on RT-1 versus continued SFT.

## Humanoids & Whole-Body Control

**[HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness](https://arxiv.org/abs/2611.08039)**
Perception returns 3D positions of VLM-selected points; execution turns pelvis/torso/hand/walking/gaze commands into whole-body motion. A fine-tuned VLM completes 51% of SIMPLE and 42.5% of HumanoidArena episodes, with five demos per task raising SIMPLE to 95%.

**[Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.31166)**
WholeBodyMem tracks task objects with SAM3 and causally selects keyframes before action. Raises success from 29.1% to 72.6% in sim and 36.7% to 88.3% on a real G1.

**[AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction](https://arxiv.org/abs/2611.07712)**
Intent-gated VLA on a Unitree G1 with dexterous hands; low-confidence predictions suppress motion, and contact-specific compliance profiles plus a latched safe-stop. ~1,300 VR-teleoperated episodes; intent gating lifts GR00T macro-F1 from 0.75 to 0.90.

**[GigaBrain-WBC-0.5: A Behavior World Model for Robust Humanoid Whole-Body Tracking with Environment Interaction](https://arxiv.org/abs/2608.18234)**
Jointly predicts next action, state, and behavior distribution. 81.3% terrain-interaction success (4.3× best baseline) and 99.3% fall recovery, with real-time cross-terrain whole-body teleoperation on a humanoid.

**[CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation](https://arxiv.org/abs/2611.07268)**
Decomposes a humanoid into SRB torso plus floating-base arms/legs, with holonomic constraints parametrizing shoulder and end-effector interaction wrenches optimized jointly by NMPC. Validated in sim and on a G1.

## Perception, Calibration & Sim Infrastructure

**[Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model](https://arxiv.org/abs/2611.07560)**
Identifies waist and both arms jointly with compliances driven by measured/gravity torques. Held-out mean error drops from 11.3–31.1 mm to 0.50–1.11 mm; independent single-chain calibration raises the other arm's error to up to 3.21 mm.

**[Aligning Policy Encoders with a Shape Teacher](https://arxiv.org/abs/2611.08275)**
Aligns image-patch features to Point-MAE shape features during training only. Speeds convergence 4.7×/5.6× on LIBERO Object/Spatial with no depth at deployment.

**[Hand Estimation: Fast and Accurate Hand Estimation in Pixels, Interaction and World Space](https://arxiv.org/abs/2611.07711)**
Fine-tunes SAM 3D Body's hand branch; predicts 2D/3D joints and surface points directly, with optional contact estimation. 65 fps with mesh fitting on a consumer GPU.

**[A Unified Fractal Impedance Control Framework](https://arxiv.org/abs/2611.08009)**
Introduces the Harmonic-Passive Motion Paradigm with an open-source ROS2/MuJoCo suite; blends admittance and impedance behaviors with no computational overhead on a Kinova Gen3.

## Briefly Noted (Adjacent)

- **[MessyNav](https://arxiv.org/abs/2611.07417)** — zero-shot VLM affordance reasoning for interactive navigation; +27 pp real-robot success.
- **[Dual-Arm Tabletop Rearrangement with Movable Stacking and Gap-Aware Push Transfers](https://arxiv.org/abs/2611.07726)** — asynchronous cross-boundary transfer via MCTS; better in dense scenes.
- **[Tactile Sensing System for Intelligent Object Recognition](https://arxiv.org/abs/2611.07779)** — piezoelectric skin, 2D-CNN on spatiotemporal heatmaps, ~101 ms latency at 63.8 µJ/inference.
- **[Closed-Loop Physics-Based Manipulation Evaluation at a Commodity Price](https://arxiv.org/abs/2611.07441)** — $3.50 / 4.4 L4-hours per 200-rollout replication; negative result on action chunking with sparse data.
- **[PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion](https://arxiv.org/abs/2611.07679)** — VLMs prefer jerkier motion (r=+0.66); smoothness gains come from the physical correction channel, and don't transfer to IsaacLab/G1.
- **[RoboARCade](https://arxiv.org/abs/2611.08209)** — long-horizon agentic robot control benchmark; GPT-6 Astra 49.8% vs Claude Fable 5.1 43.6%, with 24–39% false success claims.
- **[Position: Agentic Evolution is the Path to Evolving LLMs](https://arxiv.org/abs/2602.00359)** and **[openJiuwen](https://arxiv.org/abs/2608.27969)** — harness evolution for long-horizon agents; relevant background for embodied agent scaffolding.

Skipped: legal/financial LLM work, medical imaging, compression/quantization for LLM serving, RLHF/alignment theory, and other non-embodied topics.