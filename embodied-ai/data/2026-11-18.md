### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-18T14:32:44.014957
  - **arXiv update** 2026-11-18T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied AI & Manipulation — arXiv Roundup

A dense batch, heavy on VLA systems, dexterous manipulation data, and hand/teleoperation hardware. Below, grouped by theme; off-topic items (autonomous driving, LLM-agent benchmarks, pure NLP) are noted at the end.

---

## 1. Dexterous Hands, Tactile Sensing & Contact-Rich Manipulation

**[TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](https://arxiv.org/abs/2610.40349)** — Wearable human demo rig + robot rig with matched fingertip tactile; Tac-Retarget aligns contact patches without object mesh or physics sim. Policies fine-tuned purely on converted human data hit 72.5% vs 77.5% for equal teleop data, with 7× faster collection.

**[WiTac: Wrist-Informed Tactile Representations for Contact-Rich Manipulation](https://arxiv.org/abs/2611.21057)** — Pretrained encoder fusing touch with wrist vision and hand motion (300h SharpaDex). Conditioning GR00T N1.7 and π0.5 on it gives +28.8% / +15.0% over vision-only.

**[Haptic Probing for Subsurface-Aware Force Distribution on Layered Soft Tissue](https://arxiv.org/abs/2611.22195)** — Active haptic probing distinguishes muscle from bone-backed tissue before applying task force; patch area becomes a controlled variable under a passivity budget.

**[Physics-Informed Tactile-based Shape Estimation of Deformable Linear Objects](https://arxiv.org/abs/2611.22990)** — Vision-free DLO shape estimation from dense tactile imprints + proprioception via a physics-informed ViT; transfers to new materials/geometries.

**[Right Labels, Wrong Reasons: Signed Feature Attribution for Multi-Label Explainability](https://arxiv.org/abs/2611.22515)** — Not robotics-specific, but relevant to interpreting multi-label perception.

---

## 2. Cross-Embodiment Data, Human Video & Teleoperation

**[From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors](https://arxiv.org/abs/2611.21908)** — PriDex turns human video priors into executable bimanual dexterous demos in sim; object-motion confidence adaptively balances object vs wrist guidance. Four real tasks incl. pouring, cap unscrewing.

**[HandUMI: A Modular Hand-Worn Parallel-Jaw Interface for Robot-Free Bimanual Data Capture](https://arxiv.org/abs/2611.22146)** — $557 open-source hand-worn gripper interface with swappable fingertips; retargets to 7 sim arms (≤1.2mm median error). ACT 12/20 on towel folding with 562 robot-free demos.

**[EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming](https://arxiv.org/abs/2611.16728)** — Modular Embodiment Dreamer with per-modality tokenizers, shared trunk, training-only future-latent prediction. 13 task-embodiment pairs; OOD progress 0.53→0.77 with pretraining.

**[Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations](https://arxiv.org/abs/2512.19583)** — HOG generator + HOT tracker trained purely in sim; RL + interaction imitation for long-horizon in-hand reorientation and cross-simulator transfer.

**[Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos](https://arxiv.org/abs/2605.23762)** — Tracks human keypoints directly in task space with sampling-based MPC, skipping the geometric-retargeting intermediate. Zero-shot on H1-2 and R1.

**[HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning](https://arxiv.org/abs/2611.21938)** — 10,124h egocentric video with 100Hz IMU, 15,548 environments, 83% workplace. LeRobot/MCAP, CC BY 4.0. Useful data-scaling resource.

**[Data Pyramid for Embodied Manipulation: A Survey](https://arxiv.org/abs/2607.24744)** — Organizes real-robot / UMI-style / ego-exo / sim / general VL data by scalability vs robot alignment; consolidates 10k+ hours into LeRobot with frame-level quality annotations.

**[Where Do Human-to-Robot Transfer Gains Come From?](https://arxiv.org/abs/2611.22302)** — Sobering audit: a random 5,000-recording subset recovers most of a "task-informed" subset's gain in HPT on MetaWorld. Worth reading before believing data-recipe claims.

---

## 3. VLA Policies: Architecture, Efficiency, Robustness

**[InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](https://arxiv.org/abs/2611.22584)** — Bidirectional geometric interface lets an LLM agent steer a frozen flow-based VLA via test-time input gradients and read back reprojected actions. 99.4% LIBERO-Plus, 48.62% RoboDojo.

**[SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair](https://arxiv.org/abs/2611.22356)** — Speculative KV precompute from predicted next observations, with selective repair when predictions mismatch. 2.67× / 1.27× query speedups on π0.5 / OpenVLA-OFT.

**[VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2611.22666)** — Draft model with feature alignment and continuation reuse; 1.28–2.10× lossless speedup on four VLAs.

**[CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation](https://arxiv.org/abs/2611.22395)** — 250M-param VLA with shared discrete step codes between language encoder and visual planner. 81.1% on LIBERO-Para vs 36.5% for SmolVLA LoRA; 17ms/step.

**[GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors](https://arxiv.org/abs/2611.15659)** — Injects 6-DoF grasp hypotheses as geometric priors via bidirectional cross-attention. 99.30% LIBERO, 73.7% LIBERO+.

**[ThinkWAM: Rethinking Latent Futures for Action Refinement](https://arxiv.org/abs/2611.21258)** — Proposal→rethink→refine loop where corrected future latents feed back into the action head. 98.70% LIBERO; 64.4% on real-world OOD.

**[Making Future-Predictive Representations Actionable](https://arxiv.org/abs/2611.22994)** — Diagnoses depth-dependent divergence between future-prediction and action gradients in Fast-WAM; RelayWAM adds a transition space. 72.03% vs 51.50% LIBERO-Plus.

**[Task Convergent Flow Matching for Generative Robotics](https://arxiv.org/abs/2611.22609)** — Inference-time refinement with physics rollouts and task-convergence funnels, CMA-ES over source seeds. PushT 31.3%→88.5%, stacking 77.0%→86.0%.

**[Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies](https://arxiv.org/abs/2611.22878)** — RL post-training for flow VLAs with success-rate-reweighted advantages and periodic linear-bridge flow refitting.

**[Future Prediction as Training-Only Video Supervision for Pretrained VLA Policies](https://arxiv.org/abs/2610.34593)** — Auxiliary video-prediction expert, discarded at inference. RoboTwin 2.0: 71.18% vs 58.33% for π0.5.

**[ALOHA Lightning: Learning Fast and Precise Manipulation](https://arxiv.org/abs/2611.21919)** — Kinesthetic teaching on a backdrivable bimanual rig plus test-time action smoothing. >80% on ball tossing, battery insertion, bussing at near-human speed.

**[VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2611.22453)** — Black-box SBFL over TCP trajectories; 0.704 macro ROC-AUC across four VLAs, 96k Pick-Up trajectories.

**[Agent-Centric Observation Adaptation for Robust Visual Control under Dynamic Perturbations](https://arxiv.org/abs/2604.24661)** — VDCS degradation suite + ACO-MoE repair routing; recovers 81.2% of lost return, and 75–95% success on real Piper VLA under blur/low light.

**[GraSLA / EgoX / TouchBridge** above also relevant here.

---

## 4. Bimanual & Multi-Arm Systems

**[Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](https://arxiv.org/abs/2611.22275)** — Low-level multi-agent post-training of a humanoid tracker + VLM planner with speech-based leader-follower sync (no network). Scales to 10 robots, heterogeneous teams; HH-Bench.

**[RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time](https://arxiv.org/abs/2611.22138)** — 4–16 arms, 36 long-horizon tasks, camera-only, world never pauses. Best models finish 27–28/36 but at 3.5h and 218M input tokens.

**[Distilling World Action Models for Efficient Bimanual Manipulation via Anchored Path Matching](https://arxiv.org/abs/2611.22592)** — Few-step distillation of joint video-action models; 1/2/4-step from one checkpoint, 21.3× lower control-cycle latency vs 8-step teacher.

**[Capability Composition in Heterogeneous Teams via Barrier-Guided Diffusion Sampling](https://arxiv.org/abs/2611.23149)** — Enforces team constraints during sampling from per-agent diffusion models, generating cooperative trajectories never demonstrated together.

---

## 5. Grasping & Whole-Body Loco-Manipulation

**[DexFormer 2.0: Towards a Cross-Embodiment Foundation Policy for Dexterous Grasping](https://arxiv.org/abs/2611.20273)** — Single RL policy over 18 arm-hand combos via canonical joint interface, kinematic-tree-biased attention, Transformer-XL memory. 89% seen, 51% held-out pairs; zero-shot sim-to-real on Flexiv.

**[Body Schema Policy: Body as the Vision-Action Interface for Efficient Loco-Manipulation](https://arxiv.org/abs/2611.22713)** — Kinematic-tree token layout with body-queried vision. Matches Ψ0 on nine G1 tasks with 75× fewer params; real G1 + Fetch.

**[Learning Accurate End-Effector Trajectory Tracking with Inertial Feedback for a Quadruped Manipulator](https://arxiv.org/abs/2611.22695)** — EE IMU feedback compensates leg-arm chain errors; 17.3% / 28.0% RMSE reduction over nominal, further vs proprioception-only.

**[ALERT: Extending Humanoid Motion Trackers with a General and Lightweight Human Avoidance Pipeline](https://arxiv.org/abs/2611.22258)** — Lightweight adaptation adds proactive human avoidance to pretrained trackers while preserving motion fidelity.

**[Orchestra (Let the Mind Conceive, Let the Hand Achieve)](https://arxiv.org/abs/2610.18352)** — Agent harness separating planning from action generation with a trained progress evaluator; 68.22% on RMBench, new RMBench-Compose benchmark.

---

## 6. World Models for Manipulation

**[DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects](https://arxiv.org/abs/2611.22001)** — From-scratch, robot-native world model (no internet video pretraining); 10 FPS on a commercial GPU, strong long-horizon contact prediction; used for policy evaluation and mixed-data co-training.

**[JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics](https://arxiv.org/abs/2611.22543)** — Plug-in scene-graph dynamics correcting visual world model drift. 11–28% joint-position error reduction; real-robot pole-angle error 12.56°→6.69°.

**[FailureGen: Scalable Robot Failure Data Generation with World Models](https://arxiv.org/abs/2611.22767)** — Recombines donor failure motion into successful hosts via a fine-tuned Cosmos model; failure detector AP 0.41→0.51.

**[Executable Memory / Perception into Imagination** ([EPM](https://arxiv.org/abs/2611.22294)) — Explicit perceptual state advanced alongside latent dynamics; +7.00 return on Memory Maze 13×13.

**[AVL-JEPA: Preventing Causal Dynamics Information Collapse](https://arxiv.org/abs/2610.03587)** — Action-anchored invariance to keep action-consequence information in JEPA world models.

**[WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)** — MoT backbone jointly denoising video and query-based 3D trajectories; 1.44M samples, WorldFlowBench.

---

## 7. Simulation, Sim-to-Real & Benchmarks

**[Levio: Smart Actuated Back-Exoskeleton via Retrofit of a Commercial Passive Device](https://arxiv.org/abs/2611.22767)** — Actually exoskeleton work, but a nice retrofit pipeline: pose-modulated assistance (25.2→17.9 Nm resistive in bending, 30.6→37.7 Nm assist in lift).

*Note: [Paper 46] URL duplicates [FailureGen: Scalable Robot Failure Data Generation with World Models](https://arxiv.org/abs/2611.22367); flagging as a likely dataset error.*

**[RFW-S: Everyday Deformable Objects with Independent Simulation Verification](https://arxiv.org/abs/2611.23056)** — 83,365 sim-verified deformable assets across 485 categories with LLM-assisted parameter calibration and independent verification; sim-to-real fragile-object replay.

**[DASH: A da Vinci Adapter for Serial-link and Humanoid Robots](https://arxiv.org/abs/2610.05792)** and **[Open-Source da Vinci X/Xi Instrument Module](https://arxiv.org/abs/2611.21771)** — Two complementary low-cost surgical-robotics research platforms; the latter adds a recorded electrosurgical interposer with pedal priority.

**[PAIR: Bringing Household Robots into the Smart Home](https://arxiv.org/abs/2611.23070)** — Matter-grounded appliance simulation; notably, two fine-tuned VLAs complete 0/120 episodes, with >90% of failures at navigation/grasping/door operation.

**[Stereo-Planner: Learning Stereo-to-Trajectory Planning for Zero-Shot Sim-to-Real Quadrotor Navigation](https://arxiv.org/abs/2610.15560)** — Aerial, but a clean sim-to-real example: RGB-only, 8 m/s, 14.44 ms onboard.

---

## 8. Other Robotics (Brief)

- **[ALOHA Lightning](https://arxiv.org/abs/2611.21919)**, **[RoboTeam](https://arxiv.org/abs/2611.22138)** covered above.
- **[ASTRA: ASV Simulator for Transferable Realistic Autonomy](https://arxiv.org/abs/2611.21789)** — Isaac Sim marine sim with Fossen dynamics and ROS 2 interfaces.
- **[Agile Monoped Hopping on Complex and Discrete Terrain](https://arxiv.org/abs/2611.21905)** — Flow-matching distillation of a multi-start MPPI expert for set-valued RRT steering; 80% success in 1s on inclined terrain.
- **[From Temperature-Limited to Battery-Limited Legged Locomotion](https://arxiv.org/abs/2611.22231)** — Thermal-asymptote reward, no temperature input; Go2 runtime 19→174 min.
- **[CADENCE: Learning Acyclic Gaits for Model-Based Quadruped Locomotion](https://arxiv.org/abs/2611.23102)** — Learned step planner over convex MPC; 85.1% vs 67.8% for OCS2-Trot on void terrain.
- **[Auditing a Learned Simulator for Legged Robots](https://arxiv.org/abs/2611.23118)** — Valuable negative result: one-step accuracy does not predict policy success for RWM on ANYmal D; nine self-withdrawn claims.
- **[Autonomous Track Racing with a Commercially Available Humanoid](https://arxiv.org/abs/2611.22445)** — Real G1 deployment at World Humanoid Robot Games; thermal margin set the pace.
- **[SE(3)-LIVOM](https://arxiv.org/abs/2611.22047)**, **[Pelorus](https://arxiv.org/abs/2611.22850)**, **[DGV-DLIVO](https://arxiv.org/abs/2611.22385)**, **[RaDiVe](https://arxiv.org/abs/2607.28045)** — SLAM/odometry; included for completeness, not manipulation.
- **[Towards Reliable Local Security Agents](https://arxiv.org/abs/2603.17673)** — Not manipulation, but a nice verifiable-RL post-training recipe (4B → 93.3% on Linux privesc).

---

## 9. Off-Theme (Skipped)

The bulk of this batch is outside embodied intelligence: autonomous driving (papers 4, 23, 42, 53-54, 67, 75, 84-85, 88-89, 115, 342), LLM agent/eval infrastructure (148-159, 163, 167, 170, 181-183, 187, 194-195, 199, 202, 204-205, 214, 219, 223, 226, 229-230, 233-234, 236-237, 242-243, 253, 258, 260, 262, 265-266, 271-272, 282, 288, 290, 298-300, 306, 308, 313, 317, 323, 326, 343-344, 349, 354, 358-362, 368-369, 381-383, 397-398, 400, 402, 407-408, 411, 414, 417, 425, 428-429, 433-434, 436, 441, 443-445, 449-453, 460, 463-464, 467-469, 471, 478, 480, 483-487, 490, 493-497, 500-503), scientific ML/bio/chem/weather/quantum (173-176, 196, 208, 217, 222, 225, 241, 256, 261, 267-268, 278, 283-286, 294-296, 304, 311, 318, 324, 330, 337, 346-348, 353, 363-366, 371, 375-380, 385-386, 389, 392, 394, 396, 399, 401, 404-406, 409-410, 413, 415-416, 418-420, 422-423, 426, 430-432, 435, 437-440, 442, 446-448, 454-459, 461-462, 465-466, 470, 472-477, 479, 481-482, 488-489, 491-492, 498-499, 504).

---

**Highest-signal reads for your themes:** TouchBridge + WiTac (tactile latch onto VLA policies), InteractVLA (steerable frozen VLA — strong LIBERO-Plus number), PriDex and HandUMI (data acquisition cost collapse), DexFormer 2.0 (cross-embodiment foundation policy), DreamFAR (real-time robot-native world model), and the RWM audit (a caution about trusting sim).