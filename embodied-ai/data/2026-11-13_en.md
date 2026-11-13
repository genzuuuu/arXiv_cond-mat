### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-13T13:25:47.389406
  - **arXiv update** 2026-11-13T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv Digest — Embodied Intelligence & Manipulation

A large batch today, with a strong cluster around visuomotor policies / VLA infrastructure, plus solid work on world models, humanoids, and a few dexterous-hand/tactile items. Papers outside your scope are grouped at the end under "Briefly Noted."

---

## 1. Vision-Language-Action Policies & Serving Infrastructure

The dominant theme today: efficiency, reactivity, and serving of VLA models.

- **[Scaling VLA Serving Under Robotic Execution Constraints](https://arxiv.org/abs/2611.14969)** — XInfer, a production VLA serving system that coordinates heterogeneous computation with robotic execution timing; reports 1.26–3.75× effective robot capacity over SOTA.
- **[Fast Inference-Time Policy Refinement via Action-Affine World Models](https://arxiv.org/abs/2611.15011)** — A²WM learns local action sensitivities offline, turning refinement into a convex QP; 3.8 ms overhead per control step, best success across four simulated manipulation tasks.
- **[ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490)** — Non-neural tokenizer that releases actions incrementally, with exact minimum primitive sets derived for translation and tight bounds for rotation; enables closed-loop state feedback within a chunk.
- **[What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491)** — Systematic study of prediction/execution horizons and async inference with π₀.₅; key finding: the execution pipeline matters as much as the policy.
- **[Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration](https://arxiv.org/abs/2611.11098)** — Zora uses RAG-based drafting plus kinematics-guided acceptance; up to 7.6× speedup with hardware support.
- **[ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.08827)** — Training-free pruning placed *before* the vision encoder using the previous action chunk as a geometric prior; 1.61× speedup, 59.5% FLOP reduction.
- **[Decoupled Asynchronous System for Humanoids (DASH)](https://arxiv.org/abs/2611.11854)** — Splits slow VLM (System 2) from fast flow-matching action head (System 1) over LCM; holds 20 Hz from 0.8B to 8B backbones.
- **[ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning](https://arxiv.org/abs/2609.34982)** — Temporal U-Net in action feature space with conditional SIREN decoder; +9.8% / +6.1% / +11.4% on π₀.₅ across benchmarks.
- **[STVLA: Spatial-aware and Temporal-memory for Vision-Language-Action Models](https://arxiv.org/abs/2611.16589)** — Injects visual geometry foundation features into temporal memory; large real-world gains over π₀.₅ (+58.3 pt on block stacking).
- **[TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models](https://arxiv.org/abs/2608.07314)** — Two-timescale RL: semantic projection updated slowly, action expert frequently, to limit latent-action drift.
- **[WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](https://arxiv.org/abs/2609.03681)** — Selective, bounded imagination during post-training; ~80% less GPU time than full imagination.
- **[VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models](https://arxiv.org/abs/2611.08698)** — Progress-conditioned context retrieval improves in-context learning; 6.2% → 23.8% success on unseen real tasks.
- **[NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models](https://arxiv.org/abs/2603.09542)** — Parses instructions into primitive plans with a gated monotone pointer; strong long-horizon gains.
- **[MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes](https://arxiv.org/abs/2611.15937)** — Role-specific semantic masks + depth → geometric tokens injected into the action expert; +5.1% in clutter, +9.7% under visual perturbation.
- **[TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216)** — Harness self-improvement on a teacher, then distill a 4B student into the frozen harness; matches 552B planner on several benchmarks.
- **[Can I join you? …** (skip — humanoid social navigation, not manipulation)](https://arxiv.org/abs/2611.14853)

---

## 2. Humanoids: Loco-Manipulation, Tracking, and Whole-Body Control

- **[PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation](https://arxiv.org/abs/2611.15117)** — EE-trajectory-only interface across four arm morphologies with URDF-derived conditioning; 93.95% completion in IsaacLab, 69–72% EE error reduction vs UMI-on-Legs.
- **[ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking](https://arxiv.org/abs/2611.14985)** — Plug-in, sensor-free adapter for pretrained trackers; 63.6–75.4% reduction in guidance-target error, works across three trackers without retraining.
- **[OneSteer: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control](https://arxiv.org/abs/2610.41354)** — Test-time steering of a one-step diffusion controller via differentiable task costs; 27/27 nominal trials on Unitree G1, 4/5 low-bar passes.
- **[MotionSkill: From Bipedal Motion Video to Control across Embodiments](https://arxiv.org/abs/2611.16346)** — Monocular video → timed reference → per-robot residual policies; 98% completion on held-out initial states.
- **[FORGE: Force-Aware Multi-Granularity Control for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.17142)** — Wrist-force estimation from proprioception (no F/T sensors) plus quasi-static virtual-target loop; demonstrated on squat-and-lift with a diffusion policy.
- **[OCLO: Dataset-Free Compliant Humanoid Loco-Manipulation with Dynamic Online Posture](https://arxiv.org/abs/2610.05678)** — No human motion data; analytic reachability prior for pelvis/torso; 77.8% vs 37.8% without the prior.
- **[ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder](https://arxiv.org/abs/2611.16374)** — 112 tasks in 4 calibrated difficulty levels, validated to preserve ordering in the real world.
- **[BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU](https://arxiv.org/abs/2611.16422)** — 40 LAFAN1 clips in 3.4 min on one RTX 4090, with leave-one-out ablation of contributions.
- **[Runtime Safety and Emergency Stops on a Full-Size Humanoid](https://arxiv.org/abs/2611.15928)** — Deployment lessons on the Unitree H1-2; argues e-stop removes balance control and the fall can be worse than the trigger.
- **[PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control](https://arxiv.org/abs/2611.16188)** — Freezes a pretrained MoE policy, adds ~1% parameter task experts; all 126 original motions preserved.
- **[BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594)** — 20 tasks on Unitree G1 with a unified whole-body controller; VLA fine-tuning leads on the 9-task mean.

---

## 3. World Models, Planning & Model-Based Control

- **[The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals](https://arxiv.org/abs/2611.14955)** — Single-seed case study: a frozen probe drops 0.85 → 0.71 AUC over 15 imagined steps, and ensemble disagreement fails to flag the loss (0.52 AUC). Good cautionary read.
- **[Does Your World Model Know Actions Have Consequences?](https://arxiv.org/abs/2611.15048)** — Position paper arguing current metrics miss counterfactual action sensitivity; proposes sensitivity-analysis audits.
- **[Prediction or Persistence? What Future-Prediction Scores Miss About World Models](https://arxiv.org/abs/2611.15082)** — Matched persistence control isolates predictor contribution; V-JEPA 2.1 adds +0.291 top-1 over persistence but V-JEPA 2 adds only 0.03–0.04 — the score alone is uninterpretable.
- **[AFTER: A World Model with Adaptive Fast–Slow Timescales for Error-Driven Retention](https://arxiv.org/abs/2611.15215)** — Predictive-coding-inspired fast/slow corrections for sudden dynamics changes (e.g., unknown payload); 16–34% lower multi-step error.
- **[Rethinking Actions: Continuity-Aware Priors for World-Model Planning](https://arxiv.org/abs/2611.16645)** — Locality-gated deep-kernel GP prior over action continuations; 87.07% macro success vs 71.03% (INTACT).
- **[Bind-WAM: Binding-Uncertainty-Guided Selective Future Imagination in World Action Models](https://arxiv.org/abs/2611.15368)** — Router decides *when* to imagine the future based on language-object binding uncertainty.
- **[Native Action-Prior Learning from Videos for World Action Models](https://arxiv.org/abs/2610.03391)** — NAVA-WAM pretrains the action policy directly from observation-only video via flow matching through joint attention.
- **[SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)** — 47k-hour data study of language-video(-action) supervision; 88.1% / 61.6% on RoboTwin Clean under Easy/Hard.
- **[Generating Critic-Guided Synthetic Experience in Latent World Models](https://arxiv.org/abs/2610.39100)** — Refines candidate actions within a trust region using a critic, imagines with a frozen world model; +7.1% relative.
- **[Sim-to-Real Game State Detection for the Chef's Hat Card Game](https://arxiv.org/abs/2611.15524)** — Fully automated synthetic data pipeline with domain randomization; F1 0.906 for card-to-zone assignment on a real NICO.
- **[Elastra: A Simulation Framework for Elastic Bodies](https://arxiv.org/abs/2611.15118)** — Vertically-moving surface elements for mattresses/trampolines; residual policies lift HoST from 44.1% → 72.5% standing up.

---

## 4. Dexterous Hands, Grasping & Tactile Sensing

- **[DexRemo: A Force-Sensing Hand Platform and Task Suite for Contact-Rich Removal Manipulation](https://arxiv.org/abs/2611.15981)** — Three-finger hand with 3-axis fingertip force sensing and a 9-scenario removal suite; wrist-frame force representation beats local-frame and no-force baselines.
- **[BLaFA: Bridging Language to 3D Functional Affordances for Dexterous Robotic Grasping in Tool Use](https://arxiv.org/abs/2604.08410)** — Parses instructions into 3D functional contact keypoints via 3DGS, then maps to wrist poses and finger/force commands.
- **[GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors](https://arxiv.org/abs/2611.15659)** — Fuses 6-DoF grasp hypotheses into continuous action prediction via bidirectional cross-attention; 99.30% on LIBERO.
- **[VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation](https://arxiv.org/abs/2611.16423)** — Recovers full object kinematic state (pose, velocity, acceleration) and refines poses; demonstrated in sim-to-real in-hand transfer.
- **[A Tactile-Informed Bi-Level Framework for Robust Model-Based In-Hand Manipulation](https://arxiv.org/abs/2505.04978)** — Contact-implicit MPC for planning + tactile-reactive force-motion tracking; handles external disturbances without retraining.
- **[AgenticTactileVLA: Contact-Guided Execution-Time Supervision for Generalizable Dexterous Manipulation without VLA Retraining](https://arxiv.org/abs/2610.04391)** — Execution-time supervisor using proprioceptive contact evidence only; 61.3% → 84.0% on held-out objects.
- **[Input-output characterization of robotic grasping: Connecting design parameters to grasp behavior through the admittance](https://arxiv.org/abs/2611.16507)** — Small-signal admittance analysis reveals grasps with identical stiffness can differ by two orders of magnitude.
- **[Sensorless strain-bounded grasping of fruit](https://arxiv.org/abs/2608.23983)** — Bounds compression strain using only encoder and motor effort; reduces tomato markings from 8/10 to 1/10.
- **[Where to Generate Touch: Do Image Latents Preserve Material Recognition?](https://arxiv.org/abs/2611.15834)** — Audits latent spaces for tactile generation; SD-VAE retains material identity far better than 16× discrete tokenizers.

---

## 5. Teleoperation, Data Collection & Interfaces

- **[RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with AR and Haptic Feedback](https://arxiv.org/abs/2611.15802)** — Matches the Robotiq 2F-85's nonlinear mechanics with exchangeable fingertip sensors; AR live-robot visualization cuts joint-limit-violating episodes from 16/50 to 3/50.
- **[HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation](https://arxiv.org/abs/2611.16439)** — Kinesthetic teaching on a low-resistance platform with deployment-aligned processing; up to 2.9× faster collection, 73.3% on a six-stage long-horizon task.
- **[CrowdMAPS: Crowdsourcing Multiple Actions per State for Real-World Imitation Learning](https://arxiv.org/abs/2611.15078)** — Web-based annotation multiplies actions per visited state; +35.6 pt (keypose) and +33.0 pt (trajectory) success at width 10.
- **[I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History](https://arxiv.org/abs/2611.16419)** — VIAMO dataset (6,600 episodes) for joint action/mission inference; fine-tuned VIM lets a VLA take over mid-task, cutting teleop time 34.6–39.8%.
- **[AVI-HT: Adaptive Vision-IMU Fusion for 3D Gloved Hand Tracking](https://arxiv.org/abs/2605.21714)** — Cross-sensor attention over on-glove IMUs and egocentric vision; 16.1% lower keypoint error, fewer contact losses under occlusion.
- **[Reactive Task-Oriented Robot-Human Handovers via Generative Hypothesis Selection](https://arxiv.org/abs/2610.08003)** — VLM-generated hand-object hypotheses matched to observed human hand pose in real time; 83.3% of users preferred it.

---

## 6. Sim-to-Real, Benchmarks & Evaluation

- **[Genie Sim Benchmark: Real-to-Sim Fidelity and Evaluation](https://arxiv.org/abs/2611.15020)** — 22 robot-task pairs; pi0.5 score correlation 0.9686, plus joint-torque and contact-transfer system identification.
- **[MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments](https://arxiv.org/abs/2611.15066)** — Scaled replicas with inverse-scaled depth; <10% miniature data improves mean ADD-S AUC for both PVN3D and RDPN6D.
- **[Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement](https://arxiv.org/abs/2611.15658)** — On a Jetson AGX Orin: 70.0% (learned hybrid) and 74.0% (force-guided) over 50 real trials, 34.55 ms perception latency.
- **[Single-View RGB-D Force–Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials](https://arxiv.org/abs/2611.15650)** — Force–volume characterization with an FR3; reports held-out RMSE 1.857 N (R² = 0.44 — modest, treat as a measurement basis, not a finished estimator).
- **[Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction](https://arxiv.org/abs/2611.15651)** — Embodied-Corrector builds Judge-Cause-Sub-Fine supervision from injected failures; +6.1 pt with frozen VLA, +13.9 pt with GPT-5.5.
- **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)** — Ablates harness, action interface, experience reuse, and scene geometry; a lean harness alone lifts RoboDojo from 29.7 to 50.3.
- **[Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot](https://arxiv.org/abs/2611.16632)** — Harness with condition-gated action chaining and a continuous "narrator"; GPT-6.1 Sol succeeds on 88% of real episodes.
- **[ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](https://arxiv.org/abs/2611.17072)** — Frozen programs reach 92.1% (221/240) across eight real manipulation tasks with "demonstrations on request" and "simulation on demand."
- **[Video-Action Models for Data-Efficient Industrial Manipulation](https://arxiv.org/abs/2611.15974)** — FLUX-mimic reaches 77.5% on deformable-part kitting with two hours of task-specific action-labeled demos.
- **[Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning](https://arxiv.org/abs/2611.15381)** — SO-101 × TurtleBot 4 platform with 250 demos; π₀ best at 60% strict / 90% with intervention.
- **[BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation](https://arxiv.org/abs/2611.15317)** — LLM → PDDL with a temporal planner enforcing inter-arm constraints; beats ReAct-style closed-loop planning and runs on a real bimanual robot.
- **[Online-posture … (OCLO, see §2)](https://arxiv.org/abs/2610.05678)**
- **[Visibility-Aware Task and Motion Planning with Task-Centric Perception](https://arxiv.org/abs/2611.16213)** — Interleaves sensing actions into a fully-observable plan skeleton with persistent object-mesh memory; beats non-active-perception baselines under heavy occlusion.
- **[Generalized Inverse Kinematics via Conditional Flow](https://arxiv.org/abs/2611.15565)** — GenGenIK returns a *distribution* over IK solutions supporting mobile bases, multiple end-effectors, and scene awareness.
- **[Optimization: Decentralized Primal Averaging (DPA)](https://arxiv.org/abs/2611.16871)** — Marginal to manipulation; included only if you track distributed training. *(Consider skipping.)*

---

## 7. Briefly Noted (outside your core themes)

- Soft robotics / actuation: [SunLightBots](https://arxiv.org/abs/2611.14729), [passive tendon-driven soft extensions](https://arxiv.org/abs/2611.15386), [soft pneumatic actuator modeling](https://arxiv.org/abs/2605.21836), [soft pneumatic review](https://arxiv.org/abs/2605.25109), [complex soft-robot fabrication](https://arxiv.org/abs/2608.13233), [printed force-sensitive resistors](https://arxiv.org/abs/2611.16250).
- Navigation / field robotics: [terrain-aware Thompson sampling for SAR drones](https://arxiv.org/abs/2611.14685), [DIVAL nonholonomic planning](https://arxiv.org/abs/2611.14918), [aerial trail racing bicycle](https://arxiv.org/abs/2611.15280), [APG-Planner](https://arxiv.org/abs/2611.15296), [DroneDiffusion](https://arxiv.org/abs/2611.15277), [EMS-Nav](https://arxiv.org/abs/2611.15589), [PreNav ObjectNav](https://arxiv.org/abs/2611.15093), [VINE exocentric navigation](https://arxiv.org/abs/2611.16282), [socially compliant crowd MPC](https://arxiv.org/abs/2611.15781).
- SLAM / perception / autonomous driving: [EM-ViT depth](https://arxiv.org/abs/2611.14958), [RTAB-Map vs ORB-SLAM3 on Pi 5](https://arxiv.org/abs/2611.16472), [COSMO-Bench](https://arxiv.org/abs/2508.16731), [riMESA](https://arxiv.org/abs/2603.01178), [AnyCamVLA](https://arxiv.org/abs/2603.05868), [snow-autonomous driving challenges](https://arxiv.org/abs/2611.15217), [FloCOS occupancy prediction](https://arxiv.org/abs/2611.15488), [BEVCast](https://arxiv.org/abs/2611.08631), [OmniDreams](https://arxiv.org/abs/2606.03159), [Instant NuRec](https://arxiv.org/abs/2607.14203), [surround-view driving VQA](https://arxiv.org/abs/2611.15225).
- Benchmarks / datasets / general agents: [ManiLadder](https://arxiv.org/abs/2611.16374), [BiGym 2.0](https://arxiv.org/abs/2610.07594), [SPARC rescue platform](https://arxiv.org/abs/2611.15443), [Robo-SWE](https://arxiv.org/abs/2611.16116), [Singularity-Bench](https://arxiv.org/abs/2611.16591), [AstroMemBench](https://arxiv.org/abs/2611.16590), [SideTaskBench](https://arxiv.org/abs/2611.14548), [ReA-Bench](https://arxiv.org/abs/2611.16493), [CamChoreo](https://arxiv.org/abs/2608.10932), [PhysCapBench](https://arxiv.org/abs/2611.16424).
- Unrelated: theoretical physics, quantum computing, biomedicine, linguistics, education, policy work throughout the batch.

---

**A few threads worth pulling on:** (1) the world-model evaluation skepticism in papers [The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals](https://arxiv.org/abs/2611.14955), [Does Your World Model Know Actions Have Consequences?](https://arxiv.org/abs/2611.15048), [Prediction or Persistence? What Future-Prediction Scores Miss About World Models](https://arxiv.org/abs/2611.15082), and [AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention](https://arxiv.org/abs/2611.15215) — the persistence-baseline and counterfactual-sensitivity critiques are complementary and could inform how you validate any world model you build on; (2) the VLA efficiency cluster ([Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion](https://arxiv.org/abs/2611.14958), [ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490), [What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491), [ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.08827), [Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](https://arxiv.org/abs/2611.11854)) converges on *decoupling inference timescales*; (3) force-aware manipulation shows up in three places ([DexRemo: A Force-Sensing Hand Platform and Task Suite for Contact-Rich Removal Manipulation](https://arxiv.org/abs/2611.15981), [FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.17142), [Video-Action Models for Data-Efficient Industrial Manipulation](https://arxiv.org/abs/2611.15974)) suggesting the wrist-frame / sensorless-force estimation line is maturing.

*Dates: note that a subset of the filenames (26xx.xxxxx) are anomalous for today's feed — flag if you need to confirm indexing.*