### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-10T13:45:44.695922
  - **arXiv update** 2026-11-10T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied Intelligence & Robotics — arXiv Roundup

A large batch today. Grouped by theme below; papers outside these themes are noted briefly at the end.

---

## 1. Dexterous & Multi-Finger Manipulation

- **[GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation](https://arxiv.org/abs/2611.10343)** — Uses anomaly scores learned from policy training data as dense steering signal for diffusion/flow policies; +21/20 pts on Adroit, sim-to-real in-hand screwdriver rotation.
- **[SimDuoReal: Object-Centric Bimanual Policy for Emergent Dexterity](https://arxiv.org/abs/2611.10410)** — A single object-centric reward induces pre-grasp, regrasping, in-hand adjustment, and handover; distilled into one policy, 76.3% on real hardware.
- **[DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](https://arxiv.org/abs/2611.11166)** — Frozen action-conditioned spatial world model aligned into policy latents; no depth or future prediction at deployment. 49.4%→60.5% on DexJoCo.
- **[BAT-WAM: Bridging Action and Touch in World-Action Models for Dexterous Hands](https://arxiv.org/abs/2611.10967)** — Jointly reconstructs missing hand state and tactile signals via a shared RGB-conditioned latent bridge; large RMSE reductions.
- **[Grip, Trace, Write: Force-Aware Imitation and RL for High-DoF Robotic Handwriting](https://arxiv.org/abs/2611.10451)** — Freely held pen; two-branch actor separates grasp retention from writing; generalizes to unseen English/Chinese content.
- **[GAP: Generalized Adaptation Prior for Dexterous Piano Playing](https://arxiv.org/abs/2611.12111)** — Learns *how to adapt* in sim, transfers prior to hardware; ~7 min adaptation per piece.
- **[Grasp-Taxonomy Conditioning as a Mode Switch for Dexterous Grasping of Climbing Holds](https://arxiv.org/abs/2611.12017)** — Conditioning DP3 on a 4-class grasp label as an explicit mode switch; slip force 9.6→14.3 N.
- **[Design of a hybrid tendon-linkage finger with coupled and adaptive motion](https://arxiv.org/abs/2611.11885)** — 4-DoF, 3-actuator finger; DIP coupled to PIP via four-bar with spring/stopper.
- **[Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation](https://arxiv.org/abs/2611.25619)** — Hand-object mechanism formulation enabling pick-up→repose→wield across five hands.
- **[HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos](https://arxiv.org/abs/2610.41336)** — RL objective in object-motion space to decouple skill from hand trajectory.
- **[Lang2Morph: Language-Driven Morphological Design of Robotic Hands](https://arxiv.org/abs/2509.18937)** — LLM maps task text to fabricable hand morphologies in the OPH space.
- **[Flip Anything with Agentic Robotics Self-Learning](https://arxiv.org/abs/2611.11941)** — Coding agent iteratively develops flipping strategies; 24.7%→95.0%.

## 2. Tactile Sensing

- **[Tactile Sensors Are an Effective Substitute for Wrist Cameras in Contact-Rich or Occluded Manipulation](https://arxiv.org/abs/2611.10490)** — Direct A/B: tactile adds +31.7–60.0 pts vs. +18.3–28.3 for wrist cameras, and beats wrist-camera vision-only on all three tasks.
- **[Which Taxels, Not How Many: Tactile Sensor Placement for Dexterous Policies](https://arxiv.org/abs/2611.10647)** — Controlled study: a small contact-statistics-selected taxel set matches large uniform sets; uniform placement overestimates required taxels.
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://arxiv.org/abs/2611.12806)** — LingBot-Touch: unified tactile tokens across piezoresistive/magnetic/visuotactile sensors, plug-and-play into DP and VLA policies.
- **[PCTac: Mechanochromic Photonic-Crystal Tactile Sensor](https://arxiv.org/abs/2611.12383)** — Structural color as tactile observation; hue field into Diffusion Policy, 75.6% vs 32.2% vision-only.
- **[AetheRock: An Arm-Worn Robot Teaching System for Force-Guided Vision-Tactile Learning](https://arxiv.org/abs/2606.09777)** — Wearable data collection (GelSlim-Mini + finger pressure); ForceVT alignment framework robust to sensor degradation.
- **[SpectraTac: A Compact Camera-Free Optical Tactile Sensor](https://arxiv.org/abs/2608.30368)** — 3 distributed color sensors, <$5, 19.2 mm; 3D force MAE 0.16/0.16/0.43 N.
- **[Flexible Piezoelectric Tactile Sensing System for Intelligent Object Recognition](https://arxiv.org/abs/2611.07779)** — Spatiotemporal heatmaps + 2D-CNN; ~101 ms end-to-end on an edge platform.
- **[Tactile MNIST: Benchmarking Active Tactile Perception](https://arxiv.org/abs/2506.06361)** — Gymnasium-compatible suite + 153,600 real tactile samples; CycleGAN-based realistic rendering.

## 3. Visuomotor Policies & VLA Models

- **[SPARK-VLA: Spatial Representation Distillation and Knowledge Routing for VLAs](https://arxiv.org/abs/2611.10443)** — Distills a frozen 3D expert into a LoRA branch + router; 0.5B backbone, ~53M trainable params.
- **[Zero-Shot VLA Adaptation with Retrieved Guidance (RAGu)](https://arxiv.org/abs/2611.10894)** — Retrieval + geometric calibration + flow-matching guidance; real-world success 20%→80%.
- **[DASH: Decoupled Asynchronous System for Humanoids](https://arxiv.org/abs/2611.11854)** — Slow VLM + fast flow-matching head over LCM; holds 20 Hz control from 0.8B to 8B backbones.
- **[SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)** — 47k-hour data study of language-video(-action) supervision; 61.56% RoboTwin Random, 40% on 3 real tasks.
- **[VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation](https://arxiv.org/abs/2611.12286)** — Consolidates flow-matching specialists at intermediate ODE states; LIBERO 75.4%→98.9%.
- **[How Many Demonstrations Does a VLA Need?](https://arxiv.org/abs/2611.09964)** — Sample-efficiency comparison of six VLAs; π0.5 needs 2–5× fewer demos; frozen VLM hurts π but not GR00T.
- **[FlowEval: How Much Adaptation Does an Embodied Foundation Model Need at Deployment?](https://arxiv.org/abs/2611.11650)** — Training-free flow-matching-based diagnostic predicting adaptation data needs.
- **[PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation](https://arxiv.org/abs/2611.11798)** — Contrastive alignment of joint image-ray features via proprioception; +12.7/+26.7 pts under camera variation.
- **[A Unified Inertial Encoder for Human and Humanoid Motion](https://arxiv.org/abs/2611.10137)** — Shared IMU interface with kinematic synthesis; zero-shot transfer to Unitree G1.
- **[SPARK: Simple Post-training for Adapting Pretrained Knowledge to Robot Control](https://arxiv.org/abs/2611.12102)** — Temporal abstraction + knowledge preservation post-training of public foundation models.
- **[REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning](https://arxiv.org/abs/2611.10748)** — LLM planner grounded/verified, consolidated into indexed rule memory; 1.9–4.6 ms latency.
- **[Control-Aware Command Generation for Asynchronous Control and Action Inference](https://arxiv.org/abs/2611.11089)** — Treats discontinuous chunk predictions as a tracking problem; adaptive action skipping.
- **[LibEvoBench](https://arxiv.org/abs/2606.25402)** and **[A Forced-Structure Reduction… ](https://arxiv.org/abs/2608.11211)** are adjacent; **[DriveFoundry](https://arxiv.org/abs/2611.11532)**, **[DeltaForge](https://arxiv.org/abs/2611.11856)**, **[AutoVLA-D](https://arxiv.org/abs/2611.12382)** are driving-specific VLAs.

## 4. Cross-Embodiment & Human-to-Robot Transfer

- **[UniLatent: Cross-Embodiment Transfer via Latent Observation Alignment](https://arxiv.org/abs/2611.10061)** — Pairs simulated source/target renders, aligns encoders; up to 93% zero-shot, 27/30 real xArm→Franka with 10 demos.
- **[BATCH: Behavior Alignment for Cross-Embodiment Learning from Humans](https://arxiv.org/abs/2611.10148)** — Self-supervised temporal representations + cycle consistency; co-training and style transfer for video-action diffusion.
- **[HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations](https://arxiv.org/abs/2602.06643)** — Portable whole-body capture; 3× faster collection than teleop, 70% success in unseen environments.
- **[RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision](https://arxiv.org/abs/2611.10994)** — 200+ hours, 14 participants, 6 head cameras, 120 Hz optical MoCap with loco-manipulation coverage.
- **[Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.11554)** — Pretrained text-to-motion generator as action backbone + ControlNet visual conditioning; 72.14% HumanoidArena, 60% real.
- **[LHNav: Long-Horizon Humanoid Navigation](https://arxiv.org/abs/2611.12136)** — Brain/Cerebellum/Brainstem multirate system; 75.56% on long-horizon tasks, deployed on G1.
- **[One Agent to Guide Them All (GTA)](https://arxiv.org/abs/2602.15400)** and **[LessMimic](https://arxiv.org/abs/2602.21723)** — explicit world representation for VLN; geometry-conditioned humanoid-object interaction.

## 5. Teleoperation, Interfaces & Exoskeletons

- **[Beyond Retargeting: Low-Latency Robust Humanoid Whole-Body Teleoperation with Learned Atomic Motion Primitives](https://arxiv.org/abs/2610.07891)** — Retargeting-free single-pass policy with a motion-primitive codebook for OOD robustness.
- **[Compact and Wide-Force-Range Magnetorheological Hand Exoskeleton for Kinesthetic Feedback in Teleoperation](https://arxiv.org/abs/2611.12130)** — 39.8 g, up to 21 N rendering; 28.2% lower contact force than visual-only feedback.
- **[Human-Machine Interfaces for Subsea Telerobotics: From Soda-straw to Natural Language Interactions](https://arxiv.org/abs/2412.01753)** — Review of HMI evolution, shared autonomy, digital twins.
- **[AetheRock](https://arxiv.org/abs/2606.09777)** (above) is also a teleop/collection device.

## 6. World Models for Manipulation

- **[ObjectWorld: Scaling Object-Centric World Models with a Large-Scale 3D Full-Object Flow Dataset](https://arxiv.org/abs/2611.11085)** — Dense 3D trajectories over full object surface incl. occlusion; 1,210-hour dataset.
- **[DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/abs/2611.12468)** — Image-space action rendering + geometric calibration; interaction defect rate 48.12%→6.25%.
- **[ForeAct: Geometry-Guided Action Learning from World Representations](https://arxiv.org/abs/2611.11500)** — Single-pass reuse of a video world model with depth-supervised learnable tokens; 96.6% LIBERO.
- **[SWAM](https://arxiv.org/abs/2611.12870)** and **[BAT-WAM](https://arxiv.org/abs/2611.10967)** (above).
- **[World In-Context Learning for Agentic Robot Manipulation](https://arxiv.org/abs/2611.12885)** — Frozen model rehearses in a simulator and writes feedback into context, not weights; 83.4% on all 50 RoboTwin 2.0 tasks with one demo.
- **[SmolWAM](https://arxiv.org/abs/2610.13740)** — Compact latent WAM for edge; 57 ms per 16-action chunk.
- **[Library of Hands](https://arxiv.org/abs/2611.12678)** — Training-free correction of the action→applied-action map for frozen world models; 28.6%→62.3%.
- **[DreamLander](https://arxiv.org/abs/2611.12824)**, **[ScanDreamer](https://arxiv.org/abs/2611.11605)**, **[FlowPilot](https://arxiv.org/abs/2608.00635)**, **[Latent World Models with Monotone Planning Costs](https://arxiv.org/abs/2608.09073)** — navigation/control-flavored world models.

## 7. Sim-to-Real, Benchmarks & Evaluation

- **[MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation](https://arxiv.org/abs/2603.16861)** — 1.7M trajectories, procedural envs; 79.2% zero-shot real vs 39.2% for π0.5. Notably challenges the "sim alone isn't enough" assumption.
- **[HARP-Bench: Benchmarking Robot Manipulation Around Active Humans](https://arxiv.org/abs/2611.11123)** — Cueing/Contribution/Interruption/Co-presence; success ≠ safety.
- **[Embodied First Exam](https://arxiv.org/abs/2611.12177)** — 1,156 tasks, 47 robots, agent-native; best agent 34% on 456 core tasks.
- **[GeoMind](https://arxiv.org/abs/2611.12175)** — 54 task variants for spatial reasoning + spatial memory; agents struggle with identity tracking.
- **[DeliverBench](https://arxiv.org/abs/2611.03412)** — 11 multi-stage professional projects; best 65.0/100, showing task capability ≠ delivery.
- **[Benchmarking Real-World Robotic Manipulation through Stochastic Challenges](https://arxiv.org/abs/2611.12804)** — Reproducible scenes with hidden-test-set rigor.
- **[HolidayFactory 1.0](https://arxiv.org/abs/2611.11789)** — SDF hydroelastic contact + persistent-state job evaluation.
- **[FlowEval](https://arxiv.org/abs/2611.11650)**, **[Which Taxels](https://arxiv.org/abs/2611.10647)**, **[Tactile MNIST](https://arxiv.org/abs/2506.06361)**.
- **[HINT-VLM](https://arxiv.org/abs/2611.11665)**, **[CPNav](https://arxiv.org/abs/2611.10366)**, **[CSG-Nav](https://arxiv.org/abs/2611.11978)**, **[EffiNav](https://arxiv.org/abs/2606.18634)**, **[Compass 1](https://arxiv.org/abs/2611.12087)** — embodied navigation benchmarks.

## 8. Skill Libraries, Self-Improvement & Agent Harnesses for Robots

- **[ReSkill: Selective Self-Improvement for Robot Manipulation](https://arxiv.org/abs/2611.10510)** — Coding agent revises stage/skill organization against execution records; 30.0%→86.2% on RoboDojo, 77.5% on 8 real tasks.
- **[Beyond Action Residuals: ZPRL](https://arxiv.org/abs/2605.19919)** — Steering through a compact bottleneck latent rather than action residuals; +33.7 pts real-world.
- **[SkillDAG](https://arxiv.org/abs/2606.03056)** and **[Group of Skills](https://arxiv.org/abs/2605.06978)** — Typed/group-structured skill retrieval as agent-callable interfaces.
- **[RAIL](https://arxiv.org/abs/2611.12251)**, **[ACED-Bench](https://arxiv.org/abs/2610.14381)**, **[JoMoHa](https://arxiv.org/abs/2611.11499)**, **[Agentic-OPD](https://arxiv.org/abs/2611.12799)**.
- **[Who Taught the Robot That? Removing One User's Corrections from an Online-Learning Policy](https://arxiv.org/abs/2611.10280)** — Order of training updates matters for exact unlearning; nudge-style corrections are much harder.
- **[Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You](https://arxiv.org/abs/2611.12705)** — Only judging non-passed items can estimate recall.

## 9. Planning, Control & Optimization (adjacent)

- **[Simulation-aided RL with Control Variates](https://arxiv.org/abs/2611.12643)**, **[Sampling-based MPC as SMC Inference](https://arxiv.org/abs/2611.10877)** (1%→100% push-T in sim, 10%→90% on Franka), **[Efficient Learning of Differentiable MPC Policies on the GPU](https://arxiv.org/abs/2611.09937)** (4.4× throughput, 46× vs MPC-PPO on racing), **[Large-Scale Hierarchical Decision-Making via ADMM](https://arxiv.org/abs/2611.11090)**, **[Passivity-Guaranteed Variable Impedance Control](https://arxiv.org/abs/2611.10778)**, **[LARC trajectory certification](https://arxiv.org/abs/2608.29767)**.
- **[An improved algorithm for Quantified Boolean Formulas](https://arxiv.org/abs/2611.10633)** — 1.685^m bound, first improvement over Williams' 1.709^m in 20+ years.

---

## Briefly noted (outside core themes)

LLM/agent safety and evaluation: **[ShadowBench-MCP](https://arxiv.org/abs/2611.11720)**, **[MCP Tool Poisoning cross-framework study](https://arxiv.org/abs/2611.03555)** (22.9% ASR, 9,720 cells), **[MetaPI](https://arxiv.org/abs/2611.10026)**, **[PlanTERS](https://arxiv.org/abs/2611.11506)**, **[PolicyGuard](https://arxiv.org/abs/2616.29225)** — actually [here](https://arxiv.org/abs/2611.29225) is not in the list; use **[PolicyGuide](https://arxiv.org/abs/2608.19861)** and **[PolicyGuard](https://arxiv.org/abs/2611.29225)** — please verify links before citing. Also **[OpenClawBench](https://arxiv.org/abs/2605.29253)**, **[ErosionBench](https://arxiv.org/abs/2611.11266)**, **[TRIAGE](https://arxiv.org/abs/2605.13414)**, **[AgentRobustBench](https://arxiv.org/abs/2605.11928)**, **[ScrapeBench](https://arxiv.org/abs/2611.11306)**, **[FraudBench](https://arxiv.org/abs/2611.12167)**, **[CyberBinGym](https://arxiv.org/abs/2611.10723)**.

Interpretability/mechanistic: **[Feedback Forensics](https://arxiv.org/abs/2509.26305)**, **[SAE neural operators](https://arxiv.org/abs/2509.03738)**, **[Subliminal learning = steering vector distillation](https://arxiv.org/abs/2606.00995)**, **[algorithmic cores](https://arxiv.org/abs/2602.22600)**, **[rethinking on-policy self-distillation](https://arxiv.org/abs/2607.05184)**.

Medical/clinical AI, HCI, science-of-AI, economics/policy, and pure ML theory papers make up the remainder of the batch and I've skipped them for brevity. Tell me if you want any of those pulled in.

**Caveat:** a few links above (PolicyGuard, PolicyGuide) are worth double-checking against the original input — one arXiv ID looks malformed in the source.