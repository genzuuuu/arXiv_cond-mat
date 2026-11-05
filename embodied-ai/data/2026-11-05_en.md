### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-05T13:29:07.056089
  - **arXiv update** 2026-11-05T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Robotics & Embodied AI — arXiv Roundup

**Focus papers (core themes):** dexterous hands & grasping ([73](https://arxiv.org/abs/2606.23689), [87](https://arxiv.org/abs/2610.39076), [71](https://arxiv.org/abs/2606.12109), [20](https://arxiv.org/abs/2611.05979), [47](https://arxiv.org/abs/2611.06724), [94](https://arxiv.org/abs/2611.05163), [93](https://arxiv.org/abs/2611.04527), [95](https://arxiv.org/abs/2611.04527)‑adjacent), tactile sensing ([18](https://arxiv.org/abs/2611.05936), [43](https://arxiv.org/abs/2611.06673), [101](https://arxiv.org/abs/2608.20817)), VLA/visuomotor policies ([25](https://arxiv.org/abs/2611.06184), [33](https://arxiv.org/abs/2611.06447), [46](https://arxiv.org/abs/2611.06710), [62](https://arxiv.org/abs/2611.06905), [70](https://arxiv.org/abs/2606.09258), [72](https://arxiv.org/abs/2606.14084), [86](https://arxiv.org/abs/2610.37381), [93](https://arxiv.org/abs/2611.04527)), teleoperation ([7](https://arxiv.org/abs/2611.05667), [44](https://arxiv.org/abs/2611.06689), [73](https://arxiv.org/abs/2606.23689), [75](https://arxiv.org/abs/2607.13455), [87](https://arxiv.org/abs/2610.39076)), sim-to-real & humanoid manipulation ([2](https://arxiv.org/abs/2611.05507), [10](https://arxiv.org/abs/2611.05754), [37](https://arxiv.org/abs/2611.06564), [52](https://arxiv.org/abs/2611.06908), [40](https://arxiv.org/abs/2611.06649)).

---

## 1. Dexterous hands, grasping & in-hand manipulation

- **[AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection](https://arxiv.org/abs/2606.23689)** — Self-running grasp loop (plan, execute, label, reset) collects 3.5k trials on 100 objects with Allegro/Inspire hands; cuts human effort ~0.2 vs 9.3 hours per 500 trajectories vs teleop, and library retrieval hits 76% vs 34% for sim-screened candidates.
- **[Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection](https://arxiv.org/abs/2610.39076)** — 1.5 mm knit glove with fingertip capacitive force + IMU pose that survives hand-object occlusion; 0.59 N min detectable force (1.6–2.7× better than commercial), 11 mm fingertip error during manipulation.
- **[Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/abs/2606.12109)** — InDex adds a scalar grasp-intent signal + diffusion hand decoder to parallel-gripper VLAs; +35.5 pts over native π0.5 in sim (85.8%), 71%→83% on real hardware.
- **[Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979)** — Predicts future hand-object states from HOI data and uses them as a general RL reward; beats SOTA on success and novel-object generalization, transfers across robot hands.
- **[RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)** — Treats human→robot video translation as "try-on" (keep motion, swap body); raises novel-task success from 2%→60% with zero real demos, matching teleop at ~1/3 cost.
- **[GRASP: Gradient-Guided Sampling for Contact-Rich Physics-Based Motion Retargeting](https://arxiv.org/abs/2611.05754)** — Sampling + gradient refinement without a differentiable simulator; 92.8% success on 1,352 bimanual OakInk2 demos, improves PPO tracking and demos real dexterous/whole-body hardware.
- **[Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey](https://arxiv.org/abs/2611.06724)** — Five-layer survey (hardware, data, cross-embodiment transfer, learning, evaluation); argues human-data value hinges on kinematic/visual/contact alignment, and that contact-rich zero-shot hand transfer remains unproven.

## 2. Tactile sensing

- **[LumiTac: Compact, High-Rate Six-Axis Optical Tactile Sensing for Human-Robot Interaction](https://arxiv.org/abs/2611.05936)** — 12 mm × 4.75 mm, <2 g, ~$7 camera-free optoelectronic sensor; R² 0.966–0.994 for 3-axis force + 3-axis moment, 304 Hz online, validated on tactile-guided manipulation and pHRI.
- **[Which Physical Tactile Cues Matter for Contact-Rich Imitation Learning? A Controlled Real-Robot Study](https://arxiv.org/abs/2611.06673)** — 720 real trials: tactile lifts success 57.8%→78.9%; marker flow is the best single cue (74.4%); cue-factorized encoding and cross-attention fusion help most.
- **[GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817)** — First contactless EMI attack on tactile sensors (15 sensors, 10 modules, 2 dexterous hands); induces stable DC offsets and dangerous force behavior in grasping/slip/material tasks — a physical-layer security warning for tactile stacks.

## 3. VLA & visuomotor policies: alignment, latency, test-time scaling

- **[A³-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](https://arxiv.org/abs/2611.06447)** — Derives target/interaction regions from interaction-induced visual changes and adds attention-allocation + contrastive losses; +6.5–25.2% success across VLA backbones, sim and real.
- **[Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs](https://arxiv.org/abs/2611.06710)** — Measures 7 optimization families on 7 VLAs across H100→Jetson Thor; shows CPU launch overhead, bandwidth and kernel efficiency interact, and derives stacking guidelines (VLA-Triage).
- **[Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905)** — Online multi-task RL can improve generalist policies and even transfer gains to tasks not trained on; training task distribution and value-based RL are the critical ingredients.
- **[Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection](https://arxiv.org/abs/2606.09258)** — Pre-generates a "milestone bank" of familiar futures and re-anchors the policy to one at recovery time; 56.3%→74.0% on failure-injected LIBERO without touching the action generator.
- **[Test-Time Improvement of VLA Policies via Selected Diffusion Noise for Spurious-Robust Action Smoothing](https://arxiv.org/abs/2606.14084)** — Training-free candidate selection: counterfactual visual grounding filter then JerkRMS smoothing; +8–10% sim, +18.3% real.
- **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)** — Lightweight module predicts future RGB/depth/flow features as physical tokens (no online video generation); 99.3% LIBERO, 89.9% LIBERO-Plus, 93.6% RoboTwin 2.0.
- **[Future Representation Distillation for Imagination-free World Action Models](https://arxiv.org/abs/2611.04527)** — Distills a frozen video diffusion model into a predictive visual encoder, avoiding future-video denoising; real-time 11 Hz closed loop with a 14B backbone, beats VLA/WAM baselines and learns from other-embodiment video.
- **[FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video](https://arxiv.org/abs/2611.05062)** — 5B model predicts 3D scene flow + actions; action tokens attend far more to motion than video, and adding a video objective hurts success — motion, not pixels, carries the transfer.

## 4. Teleoperation, human-in-the-loop & data collection

- **[Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning](https://arxiv.org/abs/2611.05667)** — XR preview of predicted futures lets operators intervene before failure; 44.0%→70.3% (diffusion policy) and 57.8%→76.9% (X-VLA) vs HG-DAgger.
- **[Reverse to Advance: Teleoperation-Cost Effective Hard Policy Learning from Reversed Easy Tasks](https://arxiv.org/abs/2607.13455)** — Exploits forward-hard/reverse-easy asymmetry: closed-loop auto-reset collection, temporal inversion + critic filtering, iterative learning; beats reversal and RL baselines without hard-task teleop.
- **[Cognitive and Behavioural Effects of Haptic Feedback for ROV Teleoperation in Hazardous Environments](https://arxiv.org/abs/2611.06689)** — Haptic cross-current cues reduce physical/temporal demand and speed up driving, at the cost of higher mental demand and frustration.
- **[ELA: End-to-End Latent Action Policy Learning from Video Demonstrations](https://arxiv.org/abs/2611.05571)** — Jointly trains latent action model, policy and decoder so latent actions are optimized for control; lightweight 4M-param decoders plug into existing IL pipelines.

## 5. Humanoids, whole-body & loco-manipulation

- **[Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.05507)** — Adds an explicit 3-D contact-force command channel to motion tracking; hardware drags/pushes/lifts 20 kg boxes and adapts online to mid-task loads where force-blind tracking fails.
- **[Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors](https://arxiv.org/abs/2611.06564)** — One skill-conditioned policy over a latent human mocap manifold covers dribbling, trapping, kicking with fluid transitions; zero-shot to Unitree G1.
- **[Perceptive Humanoid Motion from Simulation](https://arxiv.org/abs/2611.06908)** — HALO synthesizes vision-language-motion data across 1,000 procedural homes and transfers zero-shot to reality: 91% success over 360 trials in six unmapped environments.
- **[SCRUB: Contact-Based Surface-Frame Estimation for Force-Motion Control with an Armless Quadruped](https://arxiv.org/abs/2611.06649)** — Kalman filter fusing force and gait-averaged velocity cues estimates unknown surface normals; Go1 completes every wall traverse/column orbit, and fails when either cue is removed.
- **[PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting](https://arxiv.org/abs/2610.12642)** — Replaces weighted multi-objective retargeting with a priority hierarchy so foot placement and interaction contacts dominate; better interaction preservation and more trackable references across four datasets.

## 6. Simulation, benchmarks & evaluation

- **[MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567)** — Five suites isolating ID and four generalization axes, plus MESA-Gen and BiMESA (first large bimanual benchmark); best baseline only 52%/49%, rankings align with RoboArena.
- **[Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.06475)** — Nine memory-dependent tasks with behavior-conditioned evaluation (later constraints derived from the robot's own earlier actions) plus a hierarchical memory baseline (HMAP).
- **[VABAR: A Variational Automation Benchmark for Agentic Robotics](https://arxiv.org/abs/2611.06881) / [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness](https://arxiv.org/abs/2607.05369)** — Six industrial/medical manipulation task classes and a graph-of-skills coding harness that rehearses in internal sim; GaP outperforms baselines on 8 sim/real VA tasks.
- **[HexaShell: A Universal Harness for Robot Coding Agents in Simulation and the Real World](https://arxiv.org/abs/2610.23479)** — 14 task-agnostic tools (motion/perception/state) let one code agent hit 69.9% RoboDojo, 82.2% RoboTwin 2.0 without task-specific input; 76/90 real dual-arm episodes.
- **[Compounding Physical RSI: Turning Execution Failure into Inherited Capability](https://arxiv.org/abs/2611.06654)** — Stage-localized failure diagnosis + behavior-regularized offline RL + weight-space retention; tops RoboDojo-Sim (42 tasks) at 26.15 score.
- **[Can Astra Solve RoboMME without Breaking the Bank?](https://arxiv.org/abs/2611.06184)** — Three-tier memory system (planner / π0.5 executor / completion monitor): 79.13% with 3.63 planner calls per episode, 34.6 pts above best non-oracle baseline.
- **[Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627)** — Shared framework for streaming action-conditioned world simulation across camera navigation, manipulation, controllable video transfer and multi-view AV simulation; code and checkpoints released.
- **[SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](https://arxiv.org/abs/2610.06598)** — Latent motion distillation + multi-block sim conditioning; best PSNR/SSIM/LPIPS/FVD on Bridge without embodied pretraining, and initializes a VLA that improves LIBERO.
- **[OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments](https://arxiv.org/abs/2611.05738)** — Habitat-Sim + FDS odor transport benchmark for gas-leak and early-fire source seeking; multimodal RL policy beats baselines.

## 7. Safety, robustness & adaptation for manipulation

- **[Online Adaptation to Latent Physical Properties for Learning from Demonstration](https://arxiv.org/abs/2611.06118)** — Jointly learns dynamics model + object latents to condition imitation and update latents online; helps on real objects but only ~30% on unseen center-of-mass in sim.
- **[TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics](https://arxiv.org/abs/2611.06442)** — 3DGS + physics twins provide policy init and dense visual rewards; 98% success across five lab tasks within 25 min of real interaction each.
- **[When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03511)** — Heavy arms hurt BC more than RL; lighter-robot demos and low-inertia workspaces are imitated more reliably — a practical data-collection guideline.
- **[Warp: Structured Output-Space Adaptation for Frozen Robot Policies](https://arxiv.org/abs/2606.31043)** — Context-conditioned monotone spline adapters on frozen policies; best recovery under ES in ManiSkill, and ~30% shorter successful cycles in real SO101 peg insertion.
- **[Beyond Terminal Constraints: Reliable Robot Control with Learned Safe Sets](https://arxiv.org/abs/2611.06196)** — Broader safe-set classes with multi-node MPC constraints and safe-abort; fewer constraint violations on a 6-joint arm at comparable tracking cost.
- **[cuRoboV2-Fast: Fast Torque-Limited Collision-Free Motion Planning](https://arxiv.org/abs/2611.06913)** — 4.4 ms mean planning with 3 kg payload (14.7× faster than cuRoboV2), 34.6% shorter pick-and-drop cycles on YAM.

## 8. Adjacent but relevant

- **[RACE: Calibrated Cumulative Scoring for Rollout-Free Robot Policy Checkpoint Selection](https://arxiv.org/abs/2611.05838)** and **[FWIK: Multi-Waypoint IK Selection via Lookahead Graph Search](https://arxiv.org/abs/2611.05897)** — practical deployment tooling (checkpoint ranking; 12.8–37.2% shorter planned motion).
- **[3D Pose Estimation in Projection Space via Pixel-level Visible Light Communication](https://arxiv.org/abs/2611.06121)** and **[Fluidic Body: Swarm Robots as a Fluid Extension of the Hand](https://arxiv.org/abs/2611.06068)** — novel human-robot interfaces; the latter lets users tune swarm "fluid" stiffness by hand gestures.
- **[Behavior Graphs: Unsupervised Graph Structures for Interpreting Robot Deployment Data](https://arxiv.org/abs/2611.00405)** — Compresses rollouts into interpretable graphs; 16/18 users preferred them to video, and they improve progress-prediction rank correlation by 22.9%.
- **[AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation](https://arxiv.org/abs/2611.00177)** — Exo→ego synthesis to cheaply produce robot-centric manipulation data.
- **[Riemannian Optimization-based Whole-body Obstacle Avoidance for Mobile Continuum Robots](https://arxiv.org/abs/2611.06214)**, **[Dynamic Shape Control of Soft Trunk Robots](https://arxiv.org/abs/2611.06625)**, **[Learning Soft Robotic Dynamics with Active Exploration](https://arxiv.org/abs/2510.27428)** — soft/continuum manipulation; aSSM-MPC beats linear baselines 10× and balances a ball >25 s where a 12-hour RL policy fails.
- **[Vortex-Induced Torque in Grasping Soft Objects](https://arxiv.org/abs/2611.06359)** — vortex gripper torque modeling for compliant objects, with GPR the best predictor.
- **[OUCH](https://arxiv.org/abs/2611.05741)** and **[Metamaterial tactile displays with programmable virtual pixels](https://arxiv.org/abs/2606.05572)** — haptics outside manipulation proper (clinical stimulation; 8-actuator wave-mediated tactile display at cm resolution).

---

### Noted but skipped (outside scope)
Autonomous driving (Jev-AD, CoSafe, corridor braking, failure-boundary profiles), SLAM/VIO/loop closure (UniLoop, RegimeVGGT, reflection-robust VIO, event SLAM, SALAD anchoring), general motion planning/RRT* on meshes, and the large volume of LLM-agent, interpretability, benchmark-audit, and generation papers (harness/RLM studies, SlackBench, PersonaCodeBench, medical/legal/finance agents, diffusion-sampling and quantization work). Say the word if you want a secondary digest of any of those clusters.