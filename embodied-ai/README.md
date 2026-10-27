### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-10-27T10:58:47.475675
  - **arXiv update** 2026-10-27T04:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Robotics & Embodied AI Paper Digest

Most of the feed falls outside the focus areas (LLM agents, benchmarks, medical imaging, RL systems). Below are the manipulation/embodied-relevant papers; the rest are noted briefly at the end.

---

## Dexterous Hands & In-Hand Manipulation

- **[ORBIT: A Modular Multi-finger Robotic Hand Platform with Rotational Finger Reconfiguration](https://arxiv.org/abs/2610.33241)** — Modular hand where fingers travel around a cylindrical palm via belt drive, enabling sub-second finger-layout reconfiguration. Demonstrated with anthropomorphic, isometric, and Barrett-style layouts across 11 objects; enables apples-to-apples morphology comparison and non-anthropomorphic tasks (cube reorientation, lid threading, sub-cm pinching).

- **[Scaling Dexterous Manipulation via Action Representation Pretraining](https://arxiv.org/abs/2610.34453)** — ARPG separates action representation learning (pretrained on large-scale human manipulation data) from action generation (frozen encoder + 130M generative backbone). SOTA on DexJoCo; bimanual dexterous success 10.1% → 44.7% over π0.5.

- **[Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation](https://arxiv.org/abs/2610.33486)** — Survey of 113 learning-based methods. Notes convergence on RL + privileged state + distillation, and the second branch of teleop-demonstration learning (VLA, diffusion policies). Useful inventory of hands, simulators, and reporting gaps.

- **[No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?](https://arxiv.org/abs/2610.23438)** — Blind Baoding rotation on Shadow Hand Lite using only proprioception + binary tactile. Zero-shot transfer via sensor-aligned embodiment, tactile calibration, and two new domain randomizations (slew-rate limits, STuck-AT Taxels). 225 consecutive 180° rotations at ~0.36 rot/s.

- **[PlayPolicy: Dexterity from Supervised Play](https://arxiv.org/abs/2610.22340)** — Learns a play policy from minutes of human play via BC, autonomously collects hours of data to train a world model, then uses the play policy to propose candidates for MPC. Distills a closed-loop goal-conditioned policy via self-play in the world model. +69.6% over hindsight BC; matches RL with 490× less data.

- **[AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking](https://arxiv.org/abs/2610.33852)** — Language-conditioned hand-object tracking with a modulator-in-the-loop doing three feedback corrections (reference, object-latent, positional-target). Distilled generalist tracker + RL-trained modulator; zero-shot sim-to-real.

- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444)** — Two-stage flow matching generating hand poses, object poses, and contact states conditioned on egocentric observation, language, and 3DGS scene. 1.7× higher physics-sim success than diffusion baselines, 40× faster inference; real-robot execution on four tasks.

- **[MDPO: Multi-constraint Dexterous Policy Optimization with Reinforcement Learning](https://arxiv.org/abs/2610.33480)** — Constrained RL handling both cumulative-cost and state-wise constraints via constraint-specific policy projections. Evaluated on ReDMan (joint safety, finger safety, grasping).

---

## Tactile Sensing

- **[High-resolution tactile observation makes hidden racket-control mechanisms learnable](https://arxiv.org/abs/2610.35563)** — 864-node tactile-inertial glove at 100 Hz, 14k strokes from 70+ badminton players. Mechanics-grounded two-layer framework infers object-driving vs grip-stabilizing control. Mechanism-guided learners gained 0.72 expert-rated skill levels vs 0.05 for level-only feedback.

- **[ArrayTac: A Closed-Loop Piezoelectric Tactile Platform for Continuously Tunable Rendering of Shape, Stiffness, and Friction](https://arxiv.org/abs/2603.13829)** — 4×4 actuator array with closed-loop Hall-effect feedback (5 mm displacement, >500 Hz refresh, 123 Hz bandwidth). Renders three tactile dimensions simultaneously; demonstrated image-to-touch and remote palpation over 1000+ km.

- **[High-Speed, Scalable Sensor Readout for Dexterous Robotic Hands via Shift-Register Multiplexing](https://arxiv.org/abs/2605.01434)** — SIPO shift-register readout: 20 channels at 1 kHz (stable to 1.5 kHz) on a tendon-driven hand with 16 joint + 4 tactile channels, using only three signal lines between modules. LSTM-based real-time force estimation and contact localization; closed-loop pinching.

- **[Haptic Sorter: A Unified Planning Framework for Online Shape Estimation and Real-Time Pose Inference](https://arxiv.org/abs/2605.31352)** — Bayesian optimization-guided haptic exploration with superellipse boundary approximation, plus an online ODE for real-time pose inference from tactile feedback. 2D robotic sorting in sim and multi-arm real setup.

---

## Grasping & Multi-Finger Manipulation

- **[MMGNet: Multi-Modal 6-DoF Grasp Synthesis for Cluttered Scenes](https://arxiv.org/abs/2610.34893)** — Hierarchical image-to-3D feature injection plus rotational graspness modeling (approach direction + in-plane rotation jointly predicted). 60.34 AP on GraspNet-1Billion RealSense; +8.46 pp over AnyGrasp on adversarial objects.

- **[CLARO: Clutter Aware Robot Orchestrator for Open-Vocabulary Grasping using VLM Agents](https://arxiv.org/abs/2610.24016)** — VLM agent orchestrating detection, segmentation, 6-DoF grasping, and non-prehensile pushing, with action memory for long-horizon execution. 89.1% average success, +16% over strongest baseline in high clutter; 88.8% on real arm.

- **[Nonprehensile Robotic Catching Using Virtual Constraints](https://arxiv.org/abs/2610.35851)** — Virtual nonholonomic constraints design end-effector motion directly from object states, avoiding trajectory prediction. MPC brings object and end-effector to rest post-contact; validated in simulation.

- **[DEX-PHD: A Dexterous Portable Handheld Device for Multimodal Data Collection](https://arxiv.org/abs/2610.35462)** — Untethered handheld with a dexterous hand, per-finger control, and multimodal logging (proprio, fingertip contact, wrist camera). Open-loop replay on a humanoid preserves finger motion and contact patterns.

- **[DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969)** — Same hand hardware for collection and deployment (no embodiment gap); operator sets wrist motion and selects skills rather than individual joints. 2,500+ demos; BC policies improve 11% → 64% using recorded commands vs states, and 36% → 78% with in-the-wild data.

---

## Visuomotor / VLA Policies

- **[Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control](https://arxiv.org/abs/2610.33288)** — Parameter-efficient BC policy maintaining persistent latent state with recursive within-step refinement over a shared module. Strong on long-horizon/context-dependent tasks (LIBERO-Mem); carry perturbation training improves robustness.

- **[X-World: Transferring Video Priors to Variable-View Robot Control](https://arxiv.org/abs/2610.34105)** — Residual cross-view attention extends a pretrained video backbone to 1–3 views; layer-aligned Q-Former + dataset-specific modules map to a shared action expert. 98.5% on LIBERO, 76.5% on LIBERO-Plus zero-shot; 81.7% on six dual-arm real tasks.

- **[RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions](https://arxiv.org/abs/2610.34356)** — RynnLAM learns 3D-grounded latent actions from video (residual feature prediction + camera-compensated 3D flow) over 30.1K hours. 4B policy: 98.8% LIBERO, 84.7% LIBERO-Plus, 88.6% RoboTwin 2.0 bimanual.

- **[EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models](https://arxiv.org/abs/2610.33685)** — Factorizes egocentric human video into shared manipulation priors and embodiment-specific kinematics. Same pretraining benefits parallel grippers and dexterous hands; gains on RoboTwin 2.0, RoboCasa GR1, and real tasks.

- **[HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience](https://arxiv.org/abs/2610.34186)** — 2,000+ hours of egocentric human + robot data; predicts latent motion tokens for a pretrained whole-body controller plus hand signals. Pseudo-proprioception via sim playback, arm re-rendering during fine-tuning. SOTA on HumanoidArena; real G1 pick-and-drop gains.

- **[SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control](https://arxiv.org/abs/2604.16677)** — Training-free wrapper for frozen VLAs: conformalized quantile regression ranks stochastic action candidates, and a Mahalanobis anomaly score on the latent execution state flags abnormal states.

- **[TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning](https://arxiv.org/abs/2610.34519)** — Token-level drift diagnostic decides per visual token whether to reuse cached KV or prune. Within 3 pp of full recompute while cutting prefill latency up to 48% on Jetson AGX Orin.

- **[JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.35010)** — ~80K-parameter learned scalar energy on a frozen base policy; its values rank discrete candidates, its gradients correct continuous actions. Small consistent gains across MetaWorld, VIMA, LanguageTable, LIBERO Plus, CLIPort.

- **[RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models](https://arxiv.org/abs/2610.34108)** — Coding agent writes a program that lets a full-task VLA attempt the task and check completion; an atomic VLA finishes remaining steps. No weight updates to the base policy; recovers failed rollouts on real robots.

- **[AdaPolicy: Action-Driven Anticipatory Robot Policies via Next-Chunk Prediction](https://arxiv.org/abs/2610.34280)** — Training-only cascaded next-chunk prediction through an evolved latent state gives implicit foresight with zero inference overhead. Up to +14 pp on mm-precision tasks.

- **[ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation](https://arxiv.org/abs/2610.34370)** — Interleaved reasoning-and-acting with tool orchestration spanning perception, navigation, manipulation, locomotion; keyframe memory for error recovery. 77% success vs 37.1% for strongest plan-then-act baseline.

- **[OSWAM: An Effective World Action Model with One-Step Action Generation](https://arxiv.org/abs/2610.35850)** — "Imagination tokens" initialize the diffusion process with structured action priors, enabling single-step action generation (~3× speedup, 40 ms latency on RTX 5090) with competitive or better quality.

- **[VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717)** — 18 VLA models, seven-stage latency breakdown on Jetson AGX Thor and AMD. Action-generation strategy dominates latency (82× spread); kernel fusion + 4-bit weights give 2.6–2.9× over torch.compile but exist for only two models.

- **[RoboReason: Boosting Robotics-Relevant VLM Reasoning Through Scalable Data Generation](https://arxiv.org/abs/2610.33778)** — Frames spatiotemporal ordering (frame ordering, depth ordering, left-right ordering) as robotics-relevant VLM probes, plus an autonomous data generation pipeline; SFT and RL on generated data both help.

- **[POD-RoPE: Rotary Position Encoding over Physical Observation Distributions for Embodied AI](https://arxiv.org/abs/2610.33745)** — Represents token observation footprints as distributions over camera centers, directions, and times; recovers pointwise RoPE in the degenerate case. +1.05 pp RoboTwin 2.0, +20 pp on two real tasks.

- **[From Language to Drives: A Multimodal Framework for Aligning Autonomous Robots with Human Purposes](https://arxiv.org/abs/2610.35629)** — LLM/VLM translate natural-language purposes into missions and drives for an open-ended learning architecture; bidirectional feedback loop.

---

## Teleoperation & Data Collection

- **[DEX-PHD](https://arxiv.org/abs/2610.35462)** and **[DexPort](https://arxiv.org/abs/2610.32969)** — Covered above; both target portable, hand-hardware-matched dexterous data collection.

- **[Revisiting Direct Control: A Field Evaluation of Sensor Fusion Efficacy in Teleoperating Full-Scale Autonomous Vehicles via Bird's Eye View](https://arxiv.org/abs/2610.35630)** — N=18 field study with a real car-sized vehicle. Fused LiDAR+camera BEV significantly beats LiDAR-only BEV (usability, NASA-TLX 34.58/100) and camera-only (faster completion, SUS 77.9). Relevant to operator-side teleop interface design.

- **[Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies](https://arxiv.org/abs/2610.35626)** — 3DGS-based data generation renders wrist-camera observations from robot-aligned poses for VLA fine-tuning plus an instruction-conditioned reach verifier. 80.0% precise-reaching vs 58.7% with 150 teleop demos, under 10 min of human capture.

- **[Retiming Robot Demonstrations with a Learned Speed Prior](https://arxiv.org/abs/2610.32676)** — Learns a speed distribution over a path given instruction + images; retimes demos to a consistent clock (including human-handheld pace). Up to half the jerk; real robot stacks cups 1.72× faster at equal success.

- **[OneDemo: Unified Policy Learning and Data Generation from a Single Demonstration](https://arxiv.org/abs/2610.18188)** — RL-trained editor decides when to transition between object-centric segments and how to geometrically adapt each. 92.7% on 15 Meta-World tasks; 98.4% demo generation on DexMimicGen.

---

## Sim-to-Real & Simulation Infrastructure

- **[Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data](https://arxiv.org/abs/2610.35075)** — Real-to-sim-to-real from smartphone captures: Gaussian-guided agentic reconstruction + motion-environment co-adaptation. 4,800 validated demos; GR00T N1.7 reaches 66.7% vs 46.7% with real-data training; generalized configs 23% → 69%.

- **[HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](https://arxiv.org/abs/2610.34126)** — Online, MoCap-free fine-tuning for humanoid tracking. Low-frequency reference perturbation for data collection, history-based neural dynamics model with differentiable forward kinematics, then direct gradient fine-tuning. Validated on Unitree G1.

- **[MimicAll: Structured Embodiment Conditioning for Cross-Humanoid Whole-Body Motion Tracking](https://arxiv.org/abs/2610.33508)** — Structured embodiment descriptor (global + joint-aligned) with body-matched motion references; trained over 4,096 variants from 16 families. 99.4% 30-s success on randomized G1 vs 42.9% for a single-body specialist.

- **[X-WBC: A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control](https://arxiv.org/abs/2609.15213)** — Shared human-centered command tokens + causal Transformer over mixed multi-robot rollouts, with lightweight per-robot I/O modules. Nine simulated embodiments and four real robots.

- **[Shooting for Contact: Contact-Implicit Multiple Shooting for Dynamic Motion Retargeting](https://arxiv.org/abs/2608.03116)** — Differentiable-simulator-in-the-loop NLP resolves contact, friction, impacts, self-collision without a prescribed contact schedule. Accelerates motion-imitation RL; zero-shot G1 walking, jogging, crawling, 180° jump-turn.

- **[SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745)** — 3DGS/photogrammetry/LiDAR/4D video → segmented, physics-parameterized, articulated, deformable sim scenes with "digital sisters" and scripted demos. F1@1cm 60.75% vs SimFoundry's 6.9%; dynamic IoU 0.86% → 99.09%.

- **[AuRA: From Atoms to Bits through Autonomous Robot Interaction](https://arxiv.org/abs/2610.35952)** — Automates interaction and data prep for digital-twin reconstruction: execution-aware grasp selection, gripper motion from robot states, registered pre-interaction priors. −88.5% human labor, −55.4% wall-clock across 13 deformable objects.

- **[Replicate What Varies: Resource Sharing for Domain-Randomized Embodied Simulation](https://arxiv.org/abs/2610.33582)** — Patchwork models envs as `E = T + Δ` (shared template + patch). 88–92% CPU RSS reduction at 32 replicas on robosuite/MuJoCo (LIBERO-plus, RoboCasa365).

- **[Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization](https://arxiv.org/abs/2610.35852)** — Central-path relaxation of the de Saxcé-corrected second-order-cone complementarity problem yields a smooth gradient that stays continuous through contact-mode transitions. 100k samples, <2 min desktop training, transfers to hardware without fine-tuning.

- **[Real-Time Human Trajectory Prediction from RGB-D for Mobile Robots Using Bi-Mamba](https://arxiv.org/abs/2610.33916)** — 262K-parameter bidirectional state-space model with a single shared train/deploy path (pose extraction → depth back-projection → smoothing). 0.29 m ADE on ETH/UCY; runs onboard a TIAGo with Jetson Orin.

- **[Physics-Informed and Data-Driven Composite Disturbance Separation and Predictive Control for Airborne Electro-Optical Gimbals with Multiple Constraints](https://arxiv.org/abs/2610.34849)** and companion **[Quantile-Based Command-Reserve MPC for Current-Command Gimbal Pointing](https://arxiv.org/abs/2610.34913)** — Constrained pointing control with disturbance prediction; hardware-validated pointing RMSE of 0.77°/0.35° and 3.94 mrad respectively. Outside the core manipulation focus but relevant to precision actuation under constraints.

---

## Embodied Intelligence: Surveys, Benchmarks, Memory

- **[MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.33446)** — Turns human-action videos, 3D assets, and reusable skills into executable humanoid programs via in-context task/contact reasoning, with physics feedback. 33 timestamped first approvals, median 97 min agent-turn time; continuous 101.75 s physical G1 bottle disposal; agent-generated skills distill into one BC/DAgger policy across 18 sim tasks.

- **[Learning Force-Reactive Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.35862)** — FLORE: robot-free demos from two force-sensing UMI-style grippers + wearable trackers; force-reactive diffusion policy predicts actions and per-hand force commands; hybrid compliance WBC tracks force with F/T feedback. 80% vs 26.7% for position-only.

- **[ReSight: Task-Driven Self-Improving Memory for Embodied Agents](https://arxiv.org/abs/2610.33487)** — Keyframe + spatiotemporal memory separating evidence from extensible derived fields; execution agent and coding agent share it. Explore-Distill-Mount turns exploration solutions into reusable memory builders/tools/skills. OC-NaVQA mean position error 33.10 m → 24.72 m; FindingDory success 38.3% → 63.8%.

- **[Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning](https://arxiv.org/abs/2610.33158)** — Persistent 3DGS map updated only where the scene changes, plus an agentic pipeline rendering novel views on demand. Introduces GEMS-Bench (3 real + 12 synthetic envs, 473 QA pairs).

- **[I Won't Know Until I Try: Interactive Information Gathering for Long-Horizon Manipulation](https://arxiv.org/abs/2610.33959)** — TAMP (PDDLStream) with interactive information-gathering actions: plans optimistically, verifies outcomes during execution, replans only the connections needed. Tasks include movability, pen-ink, drawer-openability, container-emptiness.

- **[RoboLongR: Causally Consistent Rewards Teach Robots to Progressively Master Long-Horizon Manipulation](https://arxiv.org/abs/2610.33863)** — Offline-to-online history-dependent rewards with stage-shuffle supervision, recurrent memory, and two-round training. 31.8% on 18 held-out RLBench long-horizon tasks (+9.2 pp); 57.5% on four real tasks.

- **[WorldFailBench: Do World Models Understand Policy Failures?](https://arxiv.org/abs/2610.33565)** — Three tasks (failure reason, stage, boundary) over LIBERO/RoboTwin and real G1. Seven world models show substantial gaps in understanding *how and when* policies fail, not just whether.

- **[RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](https://arxiv.org/abs/2610.33807)** — Hardware-prior-based benchmark (1,605 episodes; single-arm, bimanual, humanoid) with two VLM-free metrics: KIVA (kinematic stability) and RIGIS (multi-view geometric consistency).

- **[WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826)** — Paired real-world evaluation along physical state correctness, interaction spatial alignment, key-area fidelity, and multi-view action coherence. Seven ACWMs compared.

- **[What Does World Modeling Actually Improve in Robot Action Learning?](https://arxiv.org/abs/2610.34593)** — Controlled future-video-loss ablations in FastWAM/OpenWAM. Gains on seen tasks (+24.4, +72.9 pp) but inconsistent under distribution shift; future-video prediction as auxiliary loss lifts π0.5 from 82.94% → 89.19%.

- **[Video Prediction Policy 2: Predict Better, Act Better](https://arxiv.org/abs/2610.10270)** — Large manipulation-video continued pretraining with event-level captions, single-step visual planner distillation, MoT action module. VPP2-14B beats Cosmos3-64B by 11.0 pp on instruction-following; +18.5 pp zero-shot on real ALOHA.

- **[LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768)** — Conditions actions on predicted latent visual subgoals instead of reconstructed video. 98.6% LIBERO, 91.22% RoboTwin; 187 ms per action-chunk, up to 24× lower latency than pixel-space WAMs.

- **[GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation](https://arxiv.org/abs/2609.05588)** — All generative and action components trained from scratch on manipulation data; CoAE + single-step visual planner + IDM with knowledge-aligned selective optimization. Scaling 300 → 30,000 hours lifts G1-OP 17.1% → 44.1%, G2-90D 13.4% → 31.1%.

- **[LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence](https://arxiv.org/abs/2610.23334)** — VLM planner + WAM with MoT experts and dual-stream hierarchical visual memory; subtask-local value learning. 94.21% average over 50 RoboTwin tasks (95.56% with OpenWAM-α backbone); 65% on three long-horizon real tasks vs 28.33% for π0.5.

- **[PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy](https://arxiv.org/abs/2610.34147)** — Contrastive image-text learning of DLO physical properties as priors, plus SAM3 mask-guided future features distilled into the action expert. 68.9% average (+20.0 pp) across nine single/dual-arm tasks.

- **[3D-Force Estimation for Dual-arm Manipulation of Deformable Linear Objects via Factor Graphs](https://arxiv.org/abs/2610.35058)** — Probabilistic formulation relating DLO state and sensor data through factor graphs; estimates force magnitude, direction, and location while reconstructing shape from a single sensing modality.

- **[The Language of Deformation: Semantic Failure Analysis as a Prerequisite for Dexterous Manipulation of Deformable Objects](https://arxiv.org/abs/2610.35103)** — Position paper with proof-of-concept experiments arguing deformable manipulation needs semantic failure taxonomies (buckling, plastic deformation, pressure variation, tearing) with distinct corrective strategies.

- **[HumanoidNDM](https://arxiv.org/abs/2610.34126)**, **[Zero-HLM](https://arxiv.org/abs/2610.35075)**, **[MimicAll](https://arxiv.org/abs/2610.33508)**, **[X-WBC](https://arxiv.org/abs/2609.15213)** — Humanoid tracking/transfer cluster; see Sim-to-Real.

- **[LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876)** — 234 tasks, 51.5 h simulated teleop, 12 policies × shared controller, plus controller and data-mixture studies; three sim tasks mirror real setups with consistent policy rankings.

- **[Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30540)** — VLM selects relevant motion signals/body parts; keyframes get extra solver iterations and higher interaction weights; Mechanics-Aware Contact Anchoring refines contact. STRL for downstream control; G1 and R1 experiments.

- **[One-shot Human Video-Guided Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.19746)** — CapPro compresses a single human demo video into phase-aware tokens + task queries injected into a frozen VLA's action conditioning. No target-task robot data or fine-tuning.

- **[H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer](https://arxiv.org/abs/2609.24778)** — Standardized H2R protocol over real human videos and simulated robot demos. Sim performance predicts real performance (Pearson r=0.89, Spearman 0.85).

- **[Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](https://arxiv.org/abs/2610.26717)** — MuJoCo tomato environment + teleop demos; adapts Octo and π0.5 then fine-tunes on a Franka FR3. π0.5 performs better and degrades less under distribution shift.

- **[Toward Physical Recursive Self-Improvement: A Call for Body-Control Co-Design for Humanoid Robot](https://arxiv.org/abs/2510.03081)** — Position paper advocating joint morphology/policy evolution for humanoids, with discussion of strategic exploration, sim2real, and meta-policy learning.

- **[Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics](https://arxiv.org/abs/2610.34051)** — 3,256 spatial questions + 1,240 grounding queries + action evals on BEHAVIOR-1K. Baseline VLA: 41.6% held-out configs but only 16.1% under changed instructions; oracle target cues lift to 60.3%/38.0%.

- **[OSMA-Bench: Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)** — Spatially matched scenarios differing only in obstacle type, plus a Semantic Sensitivity Index. VLM-based and VLA policies recognize obstacle safety relevance but fail to reflect it in motion parameters — a semantic-to-motion grounding gap.

- **[TouchSafeBench: Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration](https://arxiv.org/abs/2605.31196)** — 2,940 Habitat 3.0 co-presence episodes with synchronized multi-view RGB-D and simulator contact labels. Best average Macro-F1 below 50%; explicit depth is not automatically converted into body-collision evidence.

- **[Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models](https://arxiv.org/abs/2512.01946)** — GuardianFail-36k synthesized from perturbed successful trajectories with structured reasoning traces; multi-view VLM verifier. Boosts success when integrated with an LLM-based manipulation policy.

- **[Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems](https://arxiv.org/abs/2610.32208)** — SAE representations of OpenVLA activations are outcome-predictive *before* unrecoverable states; identifies stage-associated features and a VLM-based interpretation pipeline.

- **[Priya等人: Learning Functional Specialisation for Bimanual Robotic Control](https://arxiv.org/abs/2610.33947)** — 2×2 study of differential vs shared controller objectives and fixed vs balanced hand-task assignment in a musculoskeletal sim. Differential+Fixed reaches 81.33% bimanual success but loses role flexibility (−80.46 pp when reversed).

- **[RoboGene: Diversity-Driven Agentic Task Generation Framework for VLA Pre-training](https://arxiv.org/abs/2602.16444)** — Diversity-driven sampling + agentic self-reflection + human-verified feedback memory; 18k trajectories. VLA models trained on generated data generalize better than GPT-4o/Gemini 2.5 Pro-sourced tasks.

- **[AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674)** — Open-vocabulary 3D affordance prediction → grounded grasps → motion-planned trajectories, with heavy randomization. 93% of manual-annotation trajectory success on affordance-critical tasks; zero-shot Franka FR3 24%.

- **[RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data](https://arxiv.org/abs/2605.13775)** — VLM planner + VGM simulator in a day/night co-evolutionary loop with semantic-controlled multi-granular rewards. +30 points on base planners; 500 unlabeled seeds suffice.

- **[BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation](https://arxiv.org/abs/2605.08571)** — Discrepancy-aware importance reweighting of source demos within a diffusion visuomotor policy, derived from a BEA bound. sim-to-sim, sim-to-real, multi-source.

- **[Gaussian Episodic Memory](https://arxiv.org/abs/2610.33158)** and **[SpatialMem: Metric-Aligned Long-Horizon Video Memory for Language Grounding and QA](https://arxiv.org/abs/2601.14895)** — Episodic 3D memory for grounding/QA; SpatialMem reaches 37.5 on VSI-Bench with RGB only and beats open-vocab 3D scene graphs on structural-parent assignment (0.24 vs 0.01).

- **[Semantic Anchoring for Robotic Action Representations](https://arxiv.org/abs/2607.13597)** — Probes show semantic structure in VLA action representations erodes during fine-tuning and correlates with success and OOD generalization; plug-and-play anchoring (discarded at inference) gives +18.7% ID / +21.5% OOD.

- **[Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models](https://arxiv.org/abs/2603.19233)** — Injecting task A's activations makes π0.5 execute A's trajectory in 99.6% of episodes, bound to absolute workspace coordinates. Confirmed on UR10e (26/26 and 18/26 rollouts; 50/50 grasp-at-recorded-coordinates).

- **[What Can One Sentence Fix? A Failure Taxonomy and a Minimal Language Correction for Frozen VLA Policies](https://arxiv.org/abs/2608.29967)** — Four failure modes; only "execution misalignment" is reachable by a single retrospective sentence grounded into an action bias. Recovers 65/139 ID and 33/328 OOD failures in sim; xArm7 pick-and-place 10/30 → 30/30 after base move.

- **[Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.28166)** — Represents reasoning state as a low-dimensional conditional distribution over plans; plans can be sampled, steered on request (0.48 → 0.94 adherence), and reweighted by outcomes without retraining the VLA.

- **[Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination](https://arxiv.org/abs/2610.02626)** — Latent spatiotemporal reasoning imagines future scene evolution in representation space; a Scene Gist Token internalizes it to skip explicit imagination at inference. ~6% on LIBERO-Plus language; 1081 ms → 169.5 ms per chunk.

- **[IG-VLA / RoboDoctor / VISTA](https://arxiv.org/abs/2610.35604)** — RoboDoctor: training-free diagnosis + intervention + operative refinement with linked experience records; 57.10 five-dimension mean on 54 RoboDojo-Sim tasks, 49.44% native success. VISTA: meta-agent actively explores to revise the harness, tracked in a harness graph; more rollout-efficient than static reflection on LIBERO-Pro, RoboCasa, RoboTwin.

- **[RoboAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)** — 50 household layouts, 90 atomic / 18 short-horizon / 8 long-horizon / 4 open-ended scenarios; multi-level evaluation of discovery, reasoning, manipulation, recovery, robustness.

- **[EmbodiedLab: Benchmarking Embodied Agents That Act to Know](https://arxiv.org/abs/2610.35385)** — 30 quantitative science experiments on 14 simulated apparatus platforms; parameters resampled per instance so answers cannot be known in advance. Best agent succeeds <50% with native control; failures concentrate in apparatus interaction.

- **[Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](https://arxiv.org/abs/2610.35252)** — Outcome-dependent behavioral adaptation in lab automation; VLA policies show target-selection errors despite successful transfers, GPT-driven control selects correctly but fails execution.

- **[Probe Before You Edit / PROBE](https://arxiv.org/abs/2606.00555)** — Medicinal-chemistry-style edit–response probing with a pocket-specific site map and EditManual; addresses the joint affinity/druggability failure mode in LLM-agent SBDD.

- **[Concept Acupuncturist / SAE Erasure](https://arxiv.org/abs/2610.32059)** and **[Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060)** — Not embodied; noted for SAE-based intervention and multi-agent failure taxonomy respectively.

---

## Brief Notes on Out-of-Scope Papers

- **Legged/wheeled/aerial navigation & control:** RAIWAY (wheeled biped), ISB-NMP