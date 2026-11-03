### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-03T12:59:46.933170
  - **arXiv update** 2026-11-03T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied Intelligence & Robot Manipulation — arXiv Digest

**Scope note:** This batch contains ~1000 papers, overwhelmingly outside robotics (LLM agents, NLP, medical imaging, ML theory). Below I cover the work that falls within embodied intelligence, manipulation, tactile sensing, VLA policies, teleoperation, sim-to-real, humanoids, and robot cognition. Non-robotics papers are omitted.

---

## 1. Tactile Sensing & Contact-Rich Manipulation

- **[TacMind](https://arxiv.org/abs/2611.00455)** — 128-task tactile benchmark (Precise/Recognition/Dynamic) plus an action-conditioned latent tactile world model with predictive tactile reflection.
- **[Evaluating Tactile Foundation Models for End-to-End Imitation Learning](https://arxiv.org/abs/2611.00957)** — Integrates multiple TFMs into Diffusion Policy; 5,000+ real rollouts. Useful empirical guide on when tactile pretraining helps.
- **[$TF^2$-Steering](https://arxiv.org/abs/2611.01483)** — Refines flow-matching action expert via tactile forecasts + real-time feedback (MoE). +10.7 pts sim, +9.1 pts real over strongest baselines.
- **[PanoTac](https://arxiv.org/abs/2611.03520)** — Low-cost ($<50) dense 3-axis (normal + shear) 12×32 tactile fingertip at 60 Hz; +46.7 pts over vision-only on scooping/pouring/tube tasks.
- **[Visuo-tactile Diffusion Policy with Auxiliary Tactile Dynamics Prediction](https://arxiv.org/abs/2611.02677)** — Predicts future fingertip images as an auxiliary training objective; +16.3 pts over vision-only in MuJoCo assembly.
- **[MagPillar](https://arxiv.org/abs/2611.01609)** — Magnetic pillar-array tactile sensor with 3-axis Hall sensing; 99.3% material classification.
- **[Exploring Proximity and Tactile Sensing for Robotic Manipulation](https://arxiv.org/abs/2611.03489)** — ToFTouch: multizone ToF + pressure array for pre-grasp adjustment, clutter extraction, tight insertion.
- **[ForceLDM](https://arxiv.org/abs/2611.03294)** — Force-aware latent dynamics model; distills privileged future force/torque + optical flow into a student, five real contact-rich tasks.
- **[History-Aware Force Sensing in a Pneumatic Kresling Origami Cell](https://arxiv.org/abs/2611.02140)** — GRU-based force estimation from angular history in a soft origami cell; tunable stiffness.
- **[Tactile MNIST](https://arxiv.org/abs/2506.06361)** — Benchmark suite for active tactile perception; 153.6K real tactile samples from 600 3D-printed digits.

## 2. Dexterous Hands, In-Hand Manipulation & Multi-Finger Grasping

- **[GoalDex](https://arxiv.org/abs/2611.02171)** — End-to-end visuomotor in-hand reorientation from RGB + proprioception, no pose estimation; image-goal conditioning; single-policy sim-to-real across 5 objects.
- **[DexArena](https://arxiv.org/abs/2611.02629)** — 10 long-horizon + 30 stage-level bimanual dexterous tasks with verified teleop demos and stage-grounded success conditions.
- **[Tactus](https://arxiv.org/abs/2610.39076)** — Textile sensing glove: 1.5 mm fingertip stack, capacitive tactile + IMU-fused pose through hand-object occlusion; 0.59 N detection, 11 mm fingertip error. Notable for naturalistic dexterous data collection.
- **[Any-ttach](https://arxiv.org/abs/2605.30569)** — Argues dexterity is partly a *tool-use* problem: standardized self-locking interface for autonomous end-effector swapping; 15 heterogeneous modules, multi-tool long-horizon tasks.
- **[OmniPiano](https://arxiv.org/abs/2611.00243)** — 1–5 Shadow Hands piano benchmark; 912 task settings, 36 RL baselines, standard/robust/safe/multi-agent regimes.
- **[HuG](https://arxiv.org/abs/2611.01659)** — Humanoid whole-body affordance grasping with active perception; controller-in-the-loop data curation rejects 73% of kinematically valid but destabilizing grasps; 87.5% real success, zero real demos.
- **[Pose accuracy is not grasp reliability](https://arxiv.org/abs/2609.13235)** — Key finding: a pose passing ADD(-S) still yields 0.79 grasp success vs 0.86 with annotated pose; residual pose posteriors recover much of the gap.
- **[Harnessing Plastic Deformation for Continuous Passive Stability in Soft Grippers](https://arxiv.org/abs/2607.15659)** — Kirigami metal-elastomer hybrid; 16 N passive holding without continuous energy.
- **[SomaAlign](https://arxiv.org/abs/2611.02794)** — 100-object, 74.9K-sample multimodal soft-grasping dataset with reliability-aware contrastive alignment; 84% early grasp-success prediction.

## 3. Vision-Language-Action (VLA) Policies

- **[Behavioral Steering of VLA Models in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)** — Freezes OpenVLA-OFT 7B; 8–384 trainable params via GRPO or CMA-ES steers execution style (carry height +120 mm at 92% success). Clean, practical result.
- **[WorldSketch](https://arxiv.org/abs/2611.00513)** — VLM builds a minimal kinematic world model rather than emitting actions; geometric planner optimizes over it. 91% RoboCasa zero-shot, 10× fewer VLM tokens.
- **[JADE](https://arxiv.org/abs/2611.01215)** — VLM and action expert *jointly* denoise actions; VLM reads noisy action latents at every step. SOTA among π0.5-based methods on RoboDojo.
- **[PREM](https://arxiv.org/abs/2611.00634)** — Prediction-regulated visual memory for VLA policies; huge gain on RMBench M(1) (14.4% → 83.8%), 7.7 ms overhead.
- **[MOST](https://arxiv.org/abs/2611.00734)** — Policy-internal memory supervised by object states + subtask progress; real-world success 6.7% → 43.3%. Introduces RoboCasa-Long.
- **[HeLM](https://arxiv.org/abs/2611.02660)** — Hierarchical explicit *language* memory for non-Markovian manipulation; +12.8 pts intra-episode, 4.5× less memory.
- **[2AM](https://arxiv.org/abs/2609.11308)** — Agent holds all task memory; a stateless RGB action model executes. 76.3% on LIBERO-Mem (+61.5 pts over prior best).
- **[Leap-VLA](https://arxiv.org/abs/2611.01011)** — Low-rate VLM semantic anchor + high-rate flow-matching expert with age-conditioned cache reuse; 95.5% LIBERO-Spatial at 2 s refresh.
- **[CalVLA](https://arxiv.org/abs/2611.00394)** — Shapes native action-token confidence with outcome supervision for failure discrimination (AUROC 0.74). Honest about inconclusive comparison to linear probes.
- **[Spotter](https://arxiv.org/abs/2609.36808)** — Reverses roles: embodied model leads, VLM runs in parallel and intervenes only on detected failure. π0.5 53% → 83% on a real robot; ~70% cheaper than VLM-led baselines.
- **[Vision-Language Models Are Joint Denoisers](https://arxiv.org/abs/2611.01215)** — see JADE above.
- **[Training task-relevant VLA capability reports:** [FineCraft](https://arxiv.org/abs/2611.03163) (MetaFine, 4th, 0.878), [Task-Specialized LC Models](https://arxiv.org/abs/2611.00955) (3rd, 0.914), [Learning from an Imitable Teacher](https://arxiv.org/abs/2611.00615) (2nd, 0.947 — strong lessons on teacher data quality).
- **[Auriga](https://arxiv.org/abs/2611.01112)** — Task-agnostic agent harness over a VLM planner; closes 68.3% of the planning-execution gap on RoboDojo; 1st on leaderboard (57.7%).
- **[MAESTRO](https://arxiv.org/abs/2511.00917)** — VLM coding agent orchestrating a curated perception/planning/control tool library; matches VLA baselines zero-shot.
- **[Democratizing Robot-Use Agents](https://arxiv.org/abs/2611.01560)** — Open harness + open-weight model beats a published proprietary RUA result; identifies four general capabilities.

## 4. Sim-to-Real, Real-to-Sim & World Models for Control

- **[Closing the Dynamics Gap through Self-Directed Robotic Interaction (CUE)](https://arxiv.org/abs/2611.02691)** — Agent builds its own perception, identifies friction/restitution, targets interactions where sim is least accurate. 72% error reduction on billiards; deployed on a real pool table.
- **[CoEnv / CoEx](https://arxiv.org/abs/2604.05484)** — Real-to-sim digital twin of the deployment workspace; code agent practices multi-arm programs in the twin, then transfers. 70% vs 50% success.
- **[RoboSnap](https://arxiv.org/abs/2607.06699)** — One RGB image → simulation-ready scene (collision-aware foreground + 3DGS background). Includes DROID-Sim (564 scenes).
- **[A Reproducible Reconstruction Framework for Lunar Analog Scenes](https://arxiv.org/abs/2611.00870)** — 3DGS benchmarking; finds training metrics are poor predictors of cross-reconstruction fidelity. Relevant to sim asset pipelines.
- **[KlaskTron](https://arxiv.org/abs/2611.03138) + [KlaskTron-IL](https://arxiv.org/abs/2611.03091)** — Open-source (<$2500) adversarial MARL testbed with learned actuator model enabling zero-shot sim-to-real; IL benchmark exposing BC/GAIL failure modes under contact-rich adversarial dynamics.
- **[World Models Need Not Be Right to Rank Policies Right](https://arxiv.org/abs/2611.01139)** — Small open-access message: model ranking fidelity, audit covariance, and model exploitation are distinct. Rank correlations high (τ 0.96/0.80) but audit-error correlation near zero.
- **[Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Tracking](https://arxiv.org/abs/2611.00951)** — Negative result with a clear mechanistic explanation (action-affine tangent argument). Worth reading before adding structure.
- **[Roz: A Taste Test for World Model Latents](https://arxiv.org/abs/2611.00612)** — Argues SOTA latent world models capture image similarity but not mass/friction/deformation; proposes 1,734-scenario probe suite.
- **[pico-WAM](https://arxiv.org/abs/2611.01039)** — Counterfactual branch training + simulator-cost scoring improve Push-T coverage; scoring is the better improvement target than proposal generation.
- **[W2A](https://arxiv.org/abs/2611.02600)** — Distills video-diffusion denoising representations into an action model; discards video model at test time. 95.9% LIBERO, ~21× faster.
- **[MoGAP](https://arxiv.org/abs/2610.36624)** — Motion-guided asymmetric noise for WAMs; GR-1 tabletop 38.8% → 47.5%.
- **[DARE (Disturbance-Aware RETrieval)](https://arxiv.org/abs/2611.02073)** — Relational dynamics with retrospective correction for retrieving objects from dense clutter.
- **[ReWorld](https://arxiv.org/abs/2601.12428)** — RL alignment of embodied video generators against a multi-dimensional reward (physical fidelity, task logic, embodiment, visual quality).

## 5. Humanoids & Whole-Body Control

- **[Anchor 1](https://arxiv.org/abs/2611.00193)** — Whole-body controller with calibrated sparse motion references and decoupled error feedback; 30–80% lower tracking error than existing controllers. Paired benchmark included.
- **[OpenHLM](https://arxiv.org/abs/2606.22174)** — Open recipe for whole-body humanoid VLA; joint-based teleop beats partial-DoF interfaces; VLA pretrained on wheeled/static platforms transfers surprisingly well.
- **[ReContact](https://arxiv.org/abs/2611.02968)** — Retargets human contact plans (not just object trajectories) from video; regrasp success 0.16% → 83.5% over best baseline; 7 tasks on Unitree G1.
- **[ROOF](https://arxiv.org/abs/2610.42097)** — Fall recovery under overhead constraints; 95/150 real attempts across 7 scenes including unseen furniture.
- **[CompliantBot](https://arxiv.org/abs/2611.01748)** — Whole-body compliance without task-specific interaction interfaces; yields farther, lowest joint mechanical power.
- **[MAPO](https://arxiv.org/abs/2611.02613)** — Identifies MoE divergence misestimation in PPO; alternating router/expert optimization tracks 182 motions vs 1 for PPO-MoE.
- **[Leap-VLA](https://arxiv.org/abs/2611.01011)**, **[ROOF](https://arxiv.org/abs/2610.42097)** — see above (humanoid deployment).
- **[MAPO](https://arxiv.org/abs/2611.02613)** — see above.
- **[Human-Oriented World Model](https://arxiv.org/abs/2611.02690)** — Position paper on task-relevant human state estimation + personalized dynamics prediction for assistive agents.
- **[HumiMimic](https://arxiv.org/abs/2610.36615)** — Transfers in-the-wild human-human interaction video to human-humanoid interaction; ~500K frames for two humanoids.
- **[Learning Agile Humanoid Dodgeball with Onboard Monocular Vision](https://arxiv.org/abs/2611.01197)** — Estimator-in-the-loop curriculum; >85% real single-throw success on G1.
- **[AnchorHEC](https://arxiv.org/abs/2611.02884) / [SyncHeC](https://arxiv.org/abs/2611.02999)** — Targetless hand-eye calibration (wrist + fixed cameras); SyncHeC also recovers image/joint-state time offset, worth +8.1 pts policy success.

## 6. Teleoperation, Data Collection & Imitation Learning

- **[Pixel / Pixel-UMI](https://arxiv.org/abs/2611.03648)** — Co-designed full-stack mobile manipulator: low-cost wheeled humanoid, human-aligned kinematics, robot-free data collection, unified whole-body controller. **[Pixel-UMI](https://arxiv.org/abs/2611.03647)** adds environment-aware retargeting + retargeting-error-aware masking; 87% average task progress across 5 task families.
- **[Tactus](https://arxiv.org/abs/2610.39076)** — see §2; strong option for collecting contact-aware dexterous demonstrations.
- **[Rollout then Recycle](https://arxiv.org/abs/2611.03168)** — Public dataset: 3,718 SO-101 episodes, 7 policies × 12 tasks, 73% failures. Useful for failure analysis.
- **[Does Validation Loss Predict Real-Robot Success?](https://arxiv.org/abs/2611.00283)** — Important negative result: held-out action error is a poor checkpoint selector; across policies the ranking *inverts*. Recommends reporting initiation failures separately.
- **[Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](https://arxiv.org/abs/2611.01565)** — large-k pass@k reveals coverage/reliability tradeoff invisible to pass@1; proposes offline checkpoint selection + generative data augmentation.
- **[When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03535)** — BC is less reliable when the arm is much heavier than the object; lower-inertia workspaces/demonstrations help. Practical and underexplored.
- **[Faster Imitation by Re-timing Demonstrations Within the Controller Limit](https://arxiv.org/abs/2611.00539)** — Diagnoses speed-up collapse as a mechanical command-merge limit; a one-parameter merge rule beats uniform re-timing.
- **[Teach, Abstract, Apply](https://arxiv.org/abs/2611.00297)** — Dialogue-driven skill teaching for cobots; abstraction improves success and lowers interaction cost.
- **[GazeVLA](https://arxiv.org/abs/2604.22615)** — Uses human gaze as a mid-level intention representation for cross-embodiment transfer.
- **[BEACON](https://arxiv.org/abs/2605.08571)** — Theory-guided cross-domain co-training (best-effort adaptation) for sim-to-sim/sim-to-real with limited target demos.
- **[ScheduleGen](https://arxiv.org/abs/2610.39429)** — Planning+scheduling for safe multi-arm demonstration generation; 79.6% data-gen success, zero-shot sim-to-real to 8 real variants.
- **[RynnVLA-Latent](https://arxiv.org/abs/2610.34356)** — 3D-grounded latent actions from 30.1K hours of heterogeneous video; 98.8% LIBERO, 88.6% RoboTwin 2.0.
- **[HALO-LP](https://arxiv.org/abs/2611.01038)** — New LP solver with warm-starting; demonstrated on centroidal walking/trotting SLP. Relevant if you solve QPs/contact problems.

## 7. Safety, Verification & Reliability for Embodied Agents

- **[When Delay Meets Drift](https://arxiv.org/abs/2611.02101)** — Strong result: 400 ms inference delay raises safety violations by 3.5 pts under training viewpoint but **37 pts** under a 60° camera shift — 33.5 pts more than the sum of parts. Cross-layer variation propagation.
- **[VLALagBench](https://arxiv.org/abs/2611.03103)** — 100 ms latency nearly halves success on moving targets; async execution recovers some at higher request rate; predictive model to 5.7–7.8% RMSE.
- **[Safe-Ballbot](https://arxiv.org/abs/2611.03307)** — Tilt-consistent MPC + CBFs with conformal obstacle inflation; 9–12 ms planning.
- **[Route-Guided CBF-QP Repair](https://arxiv.org/abs/2611.01713)** — Post-hoc CBF-QP repair that keeps the VLA's task direction (entry-exit-rejoin guidance) rather than only projecting to safety.
- **[Guarded Compression of Adam State](https://arxiv.org/abs/2611.00589)** / **[State-Aware Activation Recomputation](https://arxiv.org/abs/2611.00590)** — Systems papers; relevant if you train large policies on limited hardware.
- **[Reflex](https://arxiv.org/abs/2611.00524)** — Serving layer caching complete action chunks with two-level correction; 1.4–11× latency, 2.0–2.2× throughput. Directly applicable to real-time VLA deployment.
- **[Ripple](https://arxiv.org/abs/2611.01067)** — CPU-GPU co-scheduling on unified-memory edge devices for LLM/VLM inference alongside control deadlines.
- **[SafeLIBERO / AEGIS](https://arxiv.org/abs/2611.01713)** — see Route-Guided above.
- **[PointPilot](https://arxiv.org/abs/2611.02930)**, **[SCOUT](https://arxiv.org/abs/2611.01600)**, **[TAMPAgent](https://arxiv.org/abs/2611.03584)** — Object-centric 3D point-flow policies; occlusion-aware planning with MCTS; belief-space agentic TAMP. All relevant to manipulation under partial observability.

## 8. Robot Learning Infrastructure, Benchmarks & Evaluation

- **[RoboColosseum](https://arxiv.org/abs/2611.02497)** — Distributed in-the-wild evaluation: 5,699 pairwise comparisons, 124 sites, 4 embodiments. Key findings: frontier agents rival VLAs; rankings agree weakly across embodiments (Kendall W = 0.24); Open Track poorly predicts post-fine-tune ranking.
- **[VerifierBench](https://arxiv.org/abs/2610.28679)** — Agents writing executable verifiers; strong on rejecting invalid, weak on accepting all valid solutions. Directly relevant to RL reward design.
- **[LLM4Robot-Bench](https://arxiv.org/abs/2610.34527)** — Matched sim-real, 3-tier contact difficulty. GPT-6 Astra: 80% / 47.6% / 0% (L1/L2/L3) real. Clean capability-boundary evidence.
- **[Labference](https://arxiv.org/abs/2610.35252)** — Robotic lab benchmark separating operation selection, physical execution, and outcome-dependent adaptation.
- **[S1CogBench](https://arxiv.org/abs/2611.00911)** — System-1 decision models on 24 cognitive tasks; well-formed decisions do not imply evidence use.
- **[TriPhysBench](https://arxiv.org/abs/2611.01934)** — Physical intelligence benchmark; best VLM at 50.4%. Companion TriPhys policy improves +17.7% relative.
- **[Measuring AI Agents as Teammates](https://arxiv.org/abs/2611.02633)** — 240 tasks, 8 teamwork dimensions, 18 models. Frontier models cave under interpersonal pressure (best deal only 14% of conflicts).
- **[SyncHeC](https://arxiv.org/abs/2611.02999) / [AnchorHEC](https://arxiv.org/abs/2611.02884)** — Calibration matters for real deployment, not just offline accuracy.
- **[CUA-Master](https://arxiv.org/abs/2611.03126)**, **[WebHarbor](https://arxiv.org/abs/2611.03634)** — Computer-use agents; adjacent rather than embodied, but relevant to long-horizon agentic control.
- **[On the Limits of Test-Time Compute for Self-Evaluation](https://arxiv.org/abs/2611.00350)** — Ranking-error bias/variance decomposition; Scorpio improves verification and tree search. Relevant to action selection and best-of-N over policy rollouts.

## 9. Interpretability & Analysis of Embodied Models

- **[A Phenomenology of Neural Geometry in VLA Models](https://arxiv.org/abs/2610.20840)** — Concepts in VLA activations are multi-dimensional and constraint-shaped (wrist orientation = arc, distance = two orthogonal rulers). Actionable via geometry-aligned steering.
- **[Editing the Goal: Per-Token SAE Steering in π0.5](https://arxiv.org/abs/2611.00602)** — Swapping SAE features of a single goal word redirects behavior (20/20 rollouts at layer 0); effect bounded by depth, stronger with camera tokens. Includes a simpler difference-in-means baseline.
- **[From Concepts to Actual Causes](https://arxiv.org/abs/2611.00155)** — Position paper: MI decodes concepts but does not isolate the actual cause of an incident; formalizes fault isolation via actual causality.
- **[Learning to Live (LIFE)](https://arxiv.org/abs/2611.00180)** — Streaming event gates + plastic memory + explore-distill-mount for turning experience into reusable tools; 24 h real robot video case study.
- **[Neurosymbolic autonomy thesis](https://arxiv.org/abs/2611.00158)** — LIMP / REALM / PACTS: language grounding, editable 3D Gaussian scene with consequence prediction, and visuomotor skills with symbolic effect prediction.
- **[Energy-Based Policy Orchestration](https://arxiv.org/abs/2611.02546)** — Chooses policy-goal pairs at runtime via learned feasibility energies; sim-to-real on humanoid loco-manipulation.
- **[Back to the Future / DARE](https://arxiv.org/abs/2611.02073)** — see §4.
- **[SPARK (Self-Correcting Embodied Memory)](https://arxiv.org/abs/2611.00344)** — Semantic critic + targeted revisits repair embodied RAG; 13–41% fewer stored objects, up to 2.7× EQA gain. Note: same acronym as the behavior-tree paper below, different work.
- **[SPARK (Sequential Planning via Anchored Robotic Keypoints)](https://arxiv.org/abs/2606.30613)** — Behavior tree anchored to 3D observations; 75.1% LIBERO-PRO without task practice.
- **[LOGIV](https://arxiv.org/abs/2610.40016)** — Graph-verified execution with causal local repair above VLA/WAM policies; +10.7/+15.3 pts on dual-arm benchmarks.
- **[Behavior Graphs](https://arxiv.org/abs/2611.00405)** — Compresses rollouts into an interpretable directed graph; users preferred it to video (16/18) and it doubles as a progress predictor.
- **[When Prediction Shapes the Future](https://arxiv.org/abs/2611.02511)** — Blue-sky agenda: predictions that trigger interventions produce "AI-shaped" data; argues for closed-loop provenance and sequence identification.

## 10. Application Domains (Surgical, Agriculture, Field, Space)

- **Surgical:** **[Supervised Autonomous Bimanual Suction and Cauterization](https://arxiv.org/abs/2611.00237)** (82.9% coverage, ex vivo spleen); **[ArthroCut](https://arxiv.org/abs/2603.03957)** (86% on six resections, grammar-constrained decoding); **[Virtual Box cutaway AR](https://arxiv.org/abs/2611.02537)** (3D error 12.9 → 5.0 mm).
- **Endoscopy/continuum:** **[SaddleSense](https://arxiv.org/abs/2611.00582)** (saddle-shaped bend-sensor modules; 3.1% tip RMSE); **[SurgicalTS](https://arxiv.org/abs/2611.02034)** (4D triangle splatting); **[MPRF](https://arxiv.org/abs/2610.31028)** (anticipating retreat in flexible endoscopy).
- **Agriculture:** **[Beyond Synthesis Conditions (CNT growth)](https://arxiv.org/abs/2611.00739)** — observation-window analysis identifies mid-growth decision points, directly relevant to closed-loop autonomous synthesis.
- **Field/space:** **[MISLAM](https://arxiv.org/abs/2611.03106)** (magnetic-inertial SLAM, GNSS-denied, 45.7–78% closure error reduction); **[CHERI separation system](https://arxiv.org/abs/2611.02872)** (design + vibration qualification); **[GROVER](https://arxiv.org/abs/2605.24311)** (terrain-adaptive grouser wheel; 25–37% lower slip in the field).
- **Aerial:** **[Dual path following for aerial manipulator](https://arxiv.org/abs/2611.01442)** (QP with closed-form scalar reduction); **[Pneumatic bat wings](https://arxiv.org/abs/2611.00879)**; **[Fixed-wing RL interception](https://arxiv.org/abs/2610.37470)** (validated in real flight).
- **Soft robotics co-design:** **[Towards end-to-end co-design for one-shot printable soft robots](https://arxiv.org/abs/2611.03216)** (differentiable MPM + FDM-monolithic fabrication, sim-to-physical match).
- **Exoskeletons/human:** **[Recursive Self-Improvement of Exoskeleton Policies](https://arxiv.org/abs/2611.01581)** (LLM rewrites control code from user feedback; 29–35% muscle activation reduction, but poor adaptability — honest limitation).

---

### Bottom line

1. **Tactile sensing is having a strong week** — dense 3-axis hardware at low cost, plus multiple papers on *how* to inject touch into policies (predictive objectives, residual steering, action-conditioned tactile world models).
2. **Memory is the dominant VLA theme.** Six papers (PREM, MOST, HeLM, 2AM, LIFE, SPARK) attack non-Markovian manipulation; the converged lesson is that *what* you store matters more than *how much*.
3. **Evaluation methodology is being seriously questioned** — validation loss inverting policy rankings, latency interacting with viewpoint shift, model rankings failing to transfer across embodiments, and verifiers that over-reject.
4. **Action-chunk caching and latency-aware serving** (Reflex, Leap-VLA, VLALagBench) is becoming a first-class systems problem for real-time manipulation.
5. **Sim-to-real is shifting from domain randomization to explicit dynamics identification** (CUE) and digital-twin practice (CoEnv, RoboSnap).