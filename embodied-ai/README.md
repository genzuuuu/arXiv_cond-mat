### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-10-30T11:37:14.546583
  - **arXiv update** 2026-10-30T04:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied AI & Robotics — arXiv Roundup

Roughly 750 of the ~760 papers fall outside the target themes; I've filtered down to the on-topic core. Grouped below.

## Dexterous Hands, In-Hand & Tactile Manipulation

- **[DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks](https://arxiv.org/abs/2610.37799)** — Genesis-based sim framework: 30 tasks, 10 arms × 12 end-effectors (>100 single-arm robots, thousands of bimanual pairs), with teleop, simulated tactile sensing, a 16-task-embodiment benchmark, and 4,700 demo episodes. Open source.
- **[Echo: Scaling Visual Reinforcement Learning with Off-policy Experience](https://arxiv.org/abs/2610.37865)** — Single-stage off-policy visual RL with inverse distillation; 60%/56% faster time-to-reference on locomotion/hand tasks, +62%/+12% peak return.
- **[Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection](https://arxiv.org/abs/2610.39076)** — 3D-knit glove, 1.5 mm fingertip stackup, capacitive tactile + IMU-fused pose robust to occlusion; 0.59 N detection limit, 11 mm fingertip pose error. Argues for demonstration data with contact fidelity.
- **[Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand](https://arxiv.org/abs/2610.39044)** — Sim-to-real catching on Unitree G1 from one egocentric camera; zero-shot on 9 unseen objects, underhand and overhand, with wrist torque limits as low as 5 Nm.
- **[OMG: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194)** — 2.6M cluttered scenes / 0.4B grasp labels via seed-and-filter; Soft-WTA + physical constraints, physics-driven ranking, no post-optimization.
- **[TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](https://arxiv.org/abs/2610.40349)** — Wearable human interface paired with a robot interface; Tac-Retarget aligns fingertip contact patches without object mesh/pose/sim. 72.5% avg success from converted human demos (vs 77.5% teleop), 7× faster collection.
- **[Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment](https://arxiv.org/abs/2610.39582)** — Three-stage retargeting using object-centric contact wrench space; 96.7% replay success on pouring.
- **[Proprioceptive Finger Force Estimation for Reliable Box Manipulation](https://arxiv.org/abs/2610.38351)** — FEEL: uncertainty-aware residual per-finger force from proprioception only, 0.251 N RMSE, 92.8% better than virtual spring; lifts damage-free box pick-and-place from 7/10 to 10/10.
- **[SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing](https://arxiv.org/abs/2610.40646)** — Low-cost tool adapters with tactile sensors and autonomous swapping; tactile demos add 15–25 pts over RGB-only for contact-rich tool tasks.
- **[AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments](https://arxiv.org/abs/2610.40210)** — Human motion pretraining transferred to Inspire (6-ch) and Allegro (16-joint) hands; direct regression vs diffusion vs flow matching compared.
- **[Co-Evolving Policy and Rubric / DRIFT / etc.: unrelated to manipulation — skipped]** (RLHF/Rubric papers omitted.)

## Human Demonstration, Retargeting & Teleoperation

- **[UMI-Live for In-The-Wild Bimanual Robotics Data Collection](https://arxiv.org/abs/2610.39385)** — Full-stack open bimanual UMI with camera + LiDAR-inertial, onboard compute, async SLAM; fine-tunes π0.5 to 10/10 and MolmoAct2 to 8/10 on bimanual pick-and-place; releases 40 h of data.
- **[An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting](https://arxiv.org/abs/2610.37801)** — Reach-normalized vs reconstructed wrist targets on Unitree H1-2; reconstructed targets hit joint limits in 10/20 sweeps, normalized in none. Treat target construction and posture matching as separate decisions.
- **[HumiMimic: Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos](https://arxiv.org/abs/2610.36615)** — Converts human-human videos into human-humanoid interaction for 26-DoF Unitree R1 and 23-DoF Mini-hi; ~500k frames across 1,200 videos, with real-robot validation.
- **[Gaze-Assisted Supervisory Control for Lunar Robotic Arm Teleoperation Under Concurrent Monitoring](https://arxiv.org/abs/2610.39998)** — Gaze nominates + confirm authorizes + bounded autonomous grasp; 47.6 s → 18.4 s per rock, NASA-TLX 32.5 → 18.3, but manual wins on precision placement.
- **[Retrieving from Your Own Mistakes / Robotic Data Inoculation](https://arxiv.org/abs/2610.39054)** — Shared-control teleop where a residual policy perturbs human commands to broaden state coverage while the human supplies recovery demos; beats BC and offline RL on three real tasks.

## Visuomotor Policies & VLA Models

- **[When More Planning Hurts / Paired Evaluation of Inference Settings for π0.5 on BEHAVIOR-1K](https://arxiv.org/abs/2610.37917)** — Full 100-task paired evaluation of a fine-tuned π0.5 (Q-score 0.39); inference/data strategies from smaller settings do not transfer cleanly.
- **[Self-Labeled Preference Transfer for Steerable Robot Manipulation](https://arxiv.org/abs/2610.38000)** — Preference recognizer frozen and used to self-label unannotated target demos; 84.8% preference following / 89.2% success in sim, and 52.5% → 92.5% following on two real transfers.
- **[Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2610.…)** — Anchor-Align: layer-wise distillation from a frozen VLM plus motion-direction language-action alignment; consistent gains on novel targets/layouts and bimanual tasks.
- **[HiFOR: Hierarchical Foresight with Action-Guided World Grounding for VLA](https://arxiv.org/abs/2610.40373)** — Joint short-term state, semantic milestone, and goal prediction, with action-guided retrieval of future latents during denoising.
- **[Utility-WAM: Correcting Future-Induced Action Changes](https://arxiv.org/abs/2610.39367)** — Diagnoses future-induced negative transfer on precision tasks (Press Stapler −54 pts); residual adapter + pre-generation gate cuts latency 38%, 93.3% RoboTwin / 98.9% LIBERO.
- **[GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927)** — Asynchronous lookahead frame generation off the control path; 72.2% RoboCasa, 99.0% LIBERO, 24× lower control latency (48 ms on A100).
- **[PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528)** — Hierarchical flow matching with per-layer KV injection from a VLM, world-model subgoal images, and covariance-structured flow noise.
- **[CauProphet / AR/ CoRAct: Consequence-Grounded Alignment for VLA](https://arxiv.org/abs/2610.39543)** — Rewards based on movement consistency and waypoint agreement, optimizing action noise; grounds external ECoTs into executable behavior.
- **[ActionUNet: Efficient Multi-scale Fine-tuning for VLA Robustness](https://arxiv.org/abs/2609.34982)** — Temporal U-Net + conditional SIREN decoder with second-order smoothness; +9.8/+6.1/+11.4 pts on π0.5 across RoboTwin 2.0, LIBERO-Plus, and real evaluations.
- **[SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control](https://arxiv.org/abs/2610.38508)** — Current JEPA conditioning 82.5% vs 71.6% without; future supervision gives no aggregate gain at this budget.
- **[POD-RoPE: Rotary Position Encoding over Physical Observation Distributions](https://arxiv.org/abs/2610.33745)** — Distribution-based RoPE over camera centers/directions/time; +1.05 pts mean over 50 RoboTwin tasks, 32.5% → 52.5% on two real tasks.
- **[BURGER: Benchmarking Robotic Generalization via Embodied Drawing](https://arxiv.org/abs/2610.40532)** — 28,200 sim demos over 282 drawing tasks; five VLA models analyzed, deployed on Franka with human intervention.
- **[CuraEval (demonstration curation) / Cross-Controller Transfer via In-Context Behavior Adaptation](https://arxiv.org/abs/2610.39280)** — Behavioral interaction context for six controller types; +33 pts over naive pooling, 50% on unseen controller modes.
- **[Quantize by Doing: Task-Guided Mixed-Precision Quantization of VLA Models](https://arxiv.org/abs/2610.38661)** — ~4-bit weights / <6-bit activations; sim-selected allocations hold on FR3 for X-VLA but fail on π0.5.

## Grasping & Soft/Underactuated Hands

- **[SimTO-Robust: Automated Design of Soft Grippers Robust to Grasp Pose and Object Geometry](https://arxiv.org/abs/2610.39560)** — Topology optimization over multiple objects and grasp poses; 37 grippers physically tested, SimTO-Robust most reliable under disturbance.
- **[Skeleton-Guided Geometry-Aware Auto-Labeling for Robotic Grasping](https://arxiv.org/abs/2610.38443)** — 4-DoF skeleton-labeled grasp keypoints, generalized to 6-DoF quasi-3D skeletonization; 97.4% single-object / 95.0% cluttered on a Delta robot.
- **[EgoContact: Evaluating Physical Intelligence with Egocentric Video](https://arxiv.org/abs/2610.39167)** — 22.5K verified contact events; using it as a memory bank lifts grasp success 14.2% → 31.2% (sim) and 16% → 58% (real).

## Sim-to-Real & Real-to-Sim

- **[SimRetract: Zero-Shot Sim-to-Real for Retractor Take-Over in Open Surgery](https://arxiv.org/abs/2610.38234)** — Policy from simulated demos only; 90% grasp / 78% retraction preserved over 50 phantom presentations. Ablations localize the gap to components (dropping the instrument mask drops real grasp to 22%).
- **[TERRA / ScheduleGen (multi-arm demo generation) / EmbodiRSI (recursive self-improvement, real-to-sim-to-real)](https://arxiv.org/abs/2609.38905)** — EmbodiRSI: 50.4% → 83.5% sim success over two RSI updates; 83.1% real with 10 real refinement trajectories per subtask vs 75.0% from 200 real demos.
- **[LocoManiLab: Unified Testbed for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876)** — 234 tasks, 51.5 h sim teleop, 12 policies × shared controller; sim rankings match real on three tasks.
- **[ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation](https://arxiv.org/abs/2610.38388)** — Coding agent synthesizes RL problems from persistent failures; 98.4–100% on five tasks and transfers to hardware (18/20, 16/20) with no real-robot training.
- **[LLM-guided Planar Loco-Manipulation for Quadrupeds](https://arxiv.org/abs/2610.40248)** — Joint skill/object/target selection; 93.3% sim pushing, 34/45 end-to-end on hardware.

## Tactile & Force Sensing for Contact-Rich Tasks

- **[Language-Grounded Force/Torque Pretraining for Extrinsic Contact Perception](https://arxiv.org/abs/2610.39314)** — Six-axis F/T histories aligned to frozen language space; supports text-prototype readout of action/weight/grasp and LoRA adaptation to unseen connector insertion.
- **[Force-Driven Hook Disassembly via Constraint-Aware Object-Centric RL](https://arxiv.org/abs/2610.38513)** — Contact-force belief (particle filter) for hidden disassembly directions; zero-shot sim-to-real, 100/100/90/75% across four tasks, air-conditioner cover 45% → 75%.
- **[Reinforced Learning of Local Low-Loss Curves / OmniVIC / Safe Learning for Contact-Rich Robot Tasks](https://arxiv.org/abs/2512.11908)** — Survey of safe learning for contact-rich manipulation, including VLM/VLA safety opportunities; useful reference.

## World Models for Control

- **[WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)** — Mixture-of-Transformers denoising video + query-based 3D trajectories over 1.44M samples; 54.2% ADE reduction on SpatialCog vs strongest baseline.
- **[Differentiable Simulation / SALT / Bilinear World Models](https://arxiv.org/abs/2609.36305)** — Bilinear latent dynamics for JEPA-style models: ~3 orders of magnitude faster planning while matching or improving accuracy.
- **[Event2Reward / RETR / Beyond One-Step Accuracy](https://arxiv.org/abs/2609.33595)** — State-affine latent transitions trained with multi-step rollout supervision; +10 pts closed-loop success despite worse one-step error.
- **[GenSight: Unified Video Generation and 4D Perception](https://arxiv.org/abs/2610.39232)** — Single video DiT for RGB, depth, segmentation, and flow; multi-step generation and single-step dense perception.

## Safety, Robustness & Evaluation for Manipulation

- **[TACOS / TRIM / HERA — mostly locomotion, perception, or lab automation; skipped or noted briefly.]**
- **[CRAFT / Security & Prompt Injection work — mostly LLM-agent, not embodied; skipped.]**
- **[LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Tasks](https://arxiv.org/abs/2610.40083)** — Task-graph condition/resource edges checked at runtime with dependency-traced repair above frozen VLA/WAM policies; +10.7/+15.3 pts on RoboTwin V2 and BiCoord, 12/30 → 17/30 real.
- **[ProLoop / AtomTree / Evidence-Gated TAMP / BEHAVIOR-Spatial — planning/benchmarks tangentially relevant to embodied agents; noted only.]**

## Simulators, Benchmarks & Infrastructure

- **[Gym-Anything for Robotics: Scaling Physical Simulations with Digital Agents](https://arxiv.org/abs/2610.40565)** — Coding agents author sims; RoboWorld = 25 sims / 200 RL envs. Frontier models score 0.06 avg; privileged teachers and code policies (training π0.5) help substantially.
- **[RoboSeed: Multidimensional Evaluation of VLA and World-Action Models](https://arxiv.org/abs/2610.40026)** — Five-dimension scoring (capability, training/deployment affordability, research value, reproduction) with explicit evidence gaps.
- **[Do Mini-VLA / Paired eval / OpenFrontiers — skipped as out of scope.]**

## Briefly Noted (adjacent, not core)

- **[METATRON](https://arxiv.org/abs/2610.38027)** and **[FORGE](https://arxiv.org/abs/2610.37974)**: promptable whole-body humanoid control and agile humanoid locomotion — relevant if you care about humanoid platforms that manipulation policies sit on.
- **[Embodied at Sea](https://arxiv.org/abs/2610.38199)**: underwater VLA imitation learning; 93.3% success across 1,260 rollouts, plus an open ROV kit.
- **[HERON](https://arxiv.org/abs/2610.38233)**: neural obstacle-aware reachability maps for mobile manipulators, 115 ms on Jetson for a 2.56 m cube — practical for base repositioning.
- **[AffordSim](https://arxiv.org/abs/2604.11674)**: open-vocabulary affordance-driven data generation; 24% zero-shot on a real FR3 (weaker transfer).
- **[OpenVLA-adjacent / GOFish / CylindTrack / SpaceAct / EgoHTR](https://arxiv.org/abs/2610.…)** and other perception/dataset papers were excluded as not manipulation-focused.

If you want, I can go deeper on any cluster — e.g., a comparison table of the dexterous-hand data-collection papers (Tactus, TouchBridge, AcrossDEX, UMI-Live) or the VLA fine-tuning results.