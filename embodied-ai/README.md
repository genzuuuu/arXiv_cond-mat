### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-23T16:28:50.907745
  - **arXiv update** 2026-11-23T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv Roundup — Embodied Intelligence & Robotic Manipulation

A very large batch today. I'll cover the on-topic papers in depth and briefly note the rest.

---

## 🦾 Tactile Sensing, Force & Contact-Rich Manipulation

- **[WiTac: Wrist-Informed Tactile Representations for Contact-Rich Manipulation](https://arxiv.org/abs/2611.21057)** — Pretrained encoder fusing tactile + wrist vision + hand motion into a contact representation. Conditioning GR00T N1.7 and π₀.₅ on it gives +28.8% / +15.0% average success over vision-only baselines across four contact-rich tasks. Good evidence that where you fuse touch matters.
- **[FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing](https://arxiv.org/abs/2611.26744)** — Argues proxy-loss minimization doesn't imply physical force grounding. Forward-only tactile encoder, zeroth-order token adapter, and a continuous slip-verification gate. Reports 29× lower grip force than a reflex ramp on an elasto-plastic shell; 97.6% LIBERO average.
- **[FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in VLAs](https://arxiv.org/abs/2611.27011)** — Splits demonstrations into grasp and transport stages via force feedback, adds a dedicated retry policy trained with local RL from post-failure states. +18.4% (VLA-Adapter) and +6.5% (π₀.₅) on LIBERO-SUCTION; larger real-world gains.
- **[Geo-Force: A Theory of Force Sensing from Object Geometry](https://arxiv.org/abs/2611.26992)** — Theory paper on "virtual" tactile sensors predicting taxel forces from depth-rendered geometry. Proves rotation equivariance, vanishing under no contact, Lipschitz stability — and a fundamental limit: geometry cannot reveal stiffness.
- **[Mechanistic Analysis of Unified Proximity-Tactile Observation by a Capacitive Fingertip Array](https://arxiv.org/abs/2611.26950)** — Hardware/FEM modeling of a capacitive fingertip array. Useful device-level reference; the author is explicit that no bench results are validated yet.
- **[Highly Deformable Proprioceptive Membrane for Real-Time 3D Shape Reconstruction](https://arxiv.org/abs/2601.13574)** — Stretchable optical-waveguide membrane reconstructing its own deformation at ~90 Hz, 1.58 mm shape error. Relevant to soft/robotic skin.
- **[HermiteTwin: Bicubic Hermite Shell Digital Twins for Contact-Rich Deformable Manipulation](https://arxiv.org/abs/2611.27282)** — Decouples bending (coarse C¹ shell) from contact (dense material-space samples). Beats spring-mass twins on cloth and foam reconstruction, resimulation, and prediction.

---

## 🖐 Dexterous Hands, In-Hand Manipulation & Grasping

- **[Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design](https://arxiv.org/abs/2611.27967)** — A "Skill" package that turns a manipulation brief into a parameterized hand (URDF/MJCF plus evidence records) via cost-ordered contact → dynamics → learning gates. Produces the SAGE Hand (4 fingers, 16 DoF), beating LEAP on a hexagonal prism (45.6% vs 37.3%) and a bicolor cylinder (70.8% vs 51.6%). Dense simulated tactile input halves cylinder drop rate. The 164/165 vs 14/165 regression-guard result is the striking part.
- **[Going with the Flow: Koopman Behavioral Models as Pseudo Planners for Visuo-Motor Dexterity](https://arxiv.org/abs/2602.07413)** — Represents dexterous skills as coupled visual-flow/action-flow dynamical systems. Acts as its own runtime monitor and triggers replanning when predicted and observed visual flow diverge. Comparable to diffusion/transformer policies with smoother execution and fast inference.
- **[Autonomous Adaptive Learning System for Robotic Grasping in the Circular Factory](https://arxiv.org/abs/2611.27782)** — Disassembly grasping under aleatoric/epistemic uncertainty, VLM scene understanding plus active view planning and human-demo transfer. Mostly a framework proposal — quantitative validation is future work.
- **[SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2608.04196)** — Recall–rank–re-rank cascade over ~32M egocentric human samples for VLA post-training. Only ~1.49M mined samples lift success from 47.7% → 61.7% over random human-data mixing.
- **[Latent Jacobian Steer: Eliciting Contact-Rich OOD Behaviors from Pretrained Humanoid Controllers](https://arxiv.org/abs/2611.27338)** — Couples joint-action exploration with latent-space semantics via a damped local inverse of the policy Jacobian. Yields hurdling, articulated-object manipulation, door opening via non-prehensile contact; also steers a dexterous hand policy through four assembly tasks.
- **[An Autonomous Grasp Recovery / FoRe]** — *see tactile section above.*

---

## 🧠 VLA Models, Policies & Training Recipes

- **[GenPA: Image Generators as Efficient Robot Policies](https://arxiv.org/abs/2611.27446)** — Fine-tunes an image generation backbone with a 19M-param action adapter and *no* future-visual prediction at inference. 99.10% LIBERO, 83.79% LIBERO-Plus, 20.9 ms per action chunk on one H100. Current-depth supervision was the best auxiliary recipe.
- **[La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156)** — Trains a policy transformer from scratch in a frozen V-JEPA 2.1 feature space; predicts future features during training, outputs only actions at inference. SOTA RoboTwin 2.0 and LIBERO-Plus among non-embodied-pretrained policies, with 2–5× faster inference than Fast-WAM/Faster-WAM. Argues latent-space choice matters more than inheriting a generative backbone.
- **[Phoenix: Learning Scene Structure Representations for Generalizable World-Action Models](https://arxiv.org/abs/2611.24938)** — Dual-teacher distillation of geometry and spatiotemporal semantics into DINOv3 features, then CS-VAE latents jointly predicted with actions. 94.8% LIBERO-Plus, 72.4% RoboTwin 2.0 C2R; ~39k hours of pretraining data curated.
- **[SCAP: Stochastic Context for Action Expert Pretraining](https://arxiv.org/abs/2611.27187)** — Masks visual/text tokens during action-expert pretraining to preserve joint vision-language pathways. Improves four VLA architectures; +25 points over full-input pretraining on instruction-conditioned real-robot tasks.
- **[Beyond Linear Decodability: Understanding and Improving Instruction Following in World Action Models](https://arxiv.org/abs/2611.27401)** — Finds target information is encoded in both following and non-following WAMs but more linearly decodable in the former. Proposes linear decodability supervision: +26.8 / +42.9 points on LIBERO-CF. Also offers a prior-instruction competition account.
- **[Learning from Incomplete Actions: Interval Motion Supervision for VLA Policies](https://arxiv.org/abs/2611.27171)** — Handles gaps in egocentric action labels by constraining aggregate motion over missing segments. 87.9% LIBERO with 70.5% missing actions; 59.6% mean on five real-robot tasks.
- **[MomentMem: Memorizing Key Moments for Robot Manipulation](https://arxiv.org/abs/2611.26745)** — VLM memorizer selects keyframes; executor conditions on them. VMBench introduced; 49.9% average success (+31.7 points over best baseline); memorizer transfers zero-shot to unseen appearances.
- **[LexiconVLA: Learning Reusable Atomic Action Codebooks](https://arxiv.org/abs/2609.36774)** — Global + detail codebooks for atomic action reuse; unseen-task success 16.67% → 34.17% with BridgeVLA on RLBench.
- **[DIDO: Distilling Interaction-Centric Dynamics into One-Step Denoising for WAMs](https://arxiv.org/abs/2609.15570)** — One-step distillation with bounding-box reasoning tokens and DINOv3 layer alignment. 99.0% LIBERO, 92.0% RoboTwin.
- **[ReActWAM: Action-Consistent Caching for Efficient World-Action Models](https://arxiv.org/abs/2611.27372)** — Training-free prefix skipping + inner-chunk reuse; 1.41–5.44× GPU speedup, 1.46× end-to-end on FR3 with minimal success loss.
- **[SOAR: Training-Free Rank-Consistent Rollout Compression](https://arxiv.org/abs/2611.27639)** — Compresses world-model rollouts as far as the candidate *ranking* survives. 2.3× speedup at parity, 98% retained at 2.5×.
- **[Coherent Moment Propagation: Epistemic Uncertainty for Pretrained Robot Policies](https://arxiv.org/abs/2611.26855)** — Proves BayesDiff's variance decays as O(1/T), then fixes it with UKF/EKF-style recursions carrying state–weight cross-covariance. Useful for failure detection and demo selection.
- **[Trust Region Q Adjoint Matching](https://arxiv.org/abs/2605.27079)** — Off-policy RL fine-tuning of flow policies with an adaptively controlled path-space KL. 68% vs 46% on 50 OGBench tasks — a strong result worth knowing about.
- **[AceVLN / FreqCache / 2Dor3D / ArcVLN-adjacent efficiency work](https://arxiv.org/abs/2604.09244)** — *(2Dor3D)* joint 2D/3D token pruning for 3D VLAs: 1.86–2.10× end-to-end speedup within 0.5–0.6 points of unpruned.

---

## 🌍 World Models, Video Prediction & Planning

- **[Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models](https://arxiv.org/abs/2611.26825)** — VAE-encodes short action sequences into latent skills with a Gaussian prior so planner samples resemble training data. Goals 80 steps away: 42% → 62%; AntMaze two-cell goals: 0.4% → 38%. Clean diagnosis: the action space, not the planner, was the bottleneck.
- **[A Look at Selection/Action Spaces: NoPeWorld — Non-penetrating World Models](https://arxiv.org/abs/2611.27963)** — Introduces NoPeBench and a lightweight head on frozen DiT hidden states predicting whether a candidate action penetrates an obstacle. Violation rate averaged over six world models: 74% → 16%, with zero-shot transfer to open-domain imagery and third-person views.
- **[Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface](https://arxiv.org/abs/2611.27513)** — Jointly generates RGB, dense point maps, and scene flow from one egocentric image; FlowInverse maps 4D latents to actions. Argues geometry-grounded motion tokens beat latent-action and video-latent baselines OOD.
- **[LoCo-WAM: Test-Time Training as Long Context for World-Action Models](https://arxiv.org/abs/2611.26853)** — Low-rank adapter updated from observed frames within an episode, reset between episodes. A 4.8 s-history model beats a 9.6 s-trained one by 4.8 points on RoboCasa GR-1.
- **[PACE-WM: Parallel World Modeling with Action History for Visual Planning](https://arxiv.org/abs/2611.27173)** — Recurrent memory of executed actions conditioning a causal Transformer; parallel multi-step prediction with RAMP action selection. ~98% average success, 7–9× faster planning than autoregressive LeWM.
- **[Beyond Visual Fidelity: Comparing Categorical and Continuous World Models](https://arxiv.org/abs/2611.27870)** — Controlled 2D/3D study: categorical next-token prediction gives higher rollout validity with less compute, and greedy decoding is best for validity while sampling gives the best-calibrated stochastic predictions.
- **[When Does Predicting the Future Help Context-Dependent Robot Control? (PonderPounce-WM)](https://arxiv.org/abs/2611.26996)** — Future prediction helps as *auxiliary supervision* (60.83% → 67.42% on RoboMME) but delivering future tokens to the action model does not (64.00%). A useful negative result.
- **[More on World-Model Planning: MoReWorld — Motion-Region Guidance](https://arxiv.org/abs/2611.27344)** — Focuses dynamics learning and generation on the region that moves in response to the robot. Best simulator-faithfulness on WorldSimProbe.
- **[Where Structure Enters a World Model: From Predictive Fit to Physical Rollout](https://arxiv.org/abs/2611.27149)** — Conserved-quantity supervision and energy-based dynamics heads improve long-horizon rollouts; auxiliary physical readouts alone do not.
- **[LoopNav: Benchmarking Spatial Consistency in World Models](https://arxiv.org/abs/2505.22976)** — 200 hours of loop-based Minecraft navigation with a scene-graph consistency score invariant to pixel variation.
- **[EgoPhys: Physics-Informed Digital Twins for Deformable Objects from Egocentric Video](https://arxiv.org/abs/2606.16202)** — Spring-mass twin from a single moving-camera RGB interaction; amortized residual cuts refinement cost 10–59×.
- **[NormFlowSDE / CADA](https://arxiv.org/abs/2611.27362)** — *(NormFlowSDE)* amortized Bayesian state estimation for contact-rich systems with hard-to-model friction/impact.

---

## 📊 Benchmarks & Evaluation

- **[RoboDyna: Benchmarking Manipulation under Physically Grounded Dynamics](https://arxiv.org/abs/2611.26969)** — 20 dynamic tasks + 10 household tasks, paired sync/async evaluation. All evaluated policies below 20% success. Sync-vs-async flips 5–12% of episode outcomes while moving average success by ≤3%.
- **[RoboPRO: Perturbation-Resilient and Obstacle-Aware Benchmark](https://arxiv.org/abs/2611.26971)** — 80 bimanual tasks, four furnished environments, 16k demos, 5.6k instructions, distractor-density sweeps, two safety-aware collision metrics.
- **[RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](https://arxiv.org/abs/2611.27042)** — System-ID + composable physics/rendering; claims 0.9686 Pearson real–sim correlation over 22 configurations; eight evaluation tracks including dexterous and precision manipulation.
- **[ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization](https://arxiv.org/abs/2611.27305)** — 48 held-out scenes with changed task requirements. The finding: 84.6% of failures displace a distractor, and ten checkpoints follow every instruction on only 3.9% of reassigned-target states (below a 16% instruction-blind chooser). Strong evidence that "success ≠ instruction following."
- **[ROSWorld: When Digital Task Competence Meets Physical Execution](https://arxiv.org/abs/2611.27467)** — Couples a simulated robot workstation to a live OSWorld desktop. Desktop-complete 31–39 tasks becomes ≤23 with a rigid probe, ≤28 with dexterous hands. Very nice framing of the knowing–doing gap.
- **[Co-Design Gym: A Unified Benchmark for Embodiment-Policy Co-optimization](https://arxiv.org/abs/2610.02366)** — 20 domains, 85+ co-design presets. Includes manipulation, locomotion, soft dynamics, multi-agent warehouses.
- **[Sketch/Plan Space: SketchVerify](https://arxiv.org/abs/2511.17450)** — Verifies motion plans by rendering and ranking lightweight video sketches *before* invoking the generator. WorldModelBench 7.71 → 8.71 with 13.1× planning-stage speedup.
- **[Many Plans at Once: Diverse Top-Quality Planning in Continuous Time](https://arxiv.org/abs/2611.27012)** — Brings top-quality/diverse planning to continuous time. Only method to solve all 40 instances across four domains; ~10× more near-optimal plans on two contact-rich manipulation tasks.
- **[DIDO, Phoenix, MAWAM](https://arxiv.org/abs/2611.25105)** — *(MAWAM)* multi-agent world-action model; 67.8% mean on three real dual-arm tasks (+18.9 points over MA-VLA), 90.3% on eight simulated tasks with up to four arms.

---

## 🕹 Teleoperation, Humanoids & Whole-Body Control

- **[LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning](https://arxiv.org/abs/2610.27998)** — Go2 + 6-DoF Piper L, leader arm + two handheld controllers, force feedback without a dedicated F/T sensor or motion capture, unified 11D action shared by teleop and deployment. Validated by fine-tuning MolmoAct2 and deploying without retargeting or extra IK.
- **[BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight](https://arxiv.org/abs/2611.27047)** — Adds a synchronized exocentric view (frozen DINOv3) and 0.6 s dual-view representational foresight as privileged supervision on a 4.2M-param residual adapter. HELM benchmark: 48.0% → 92.0% in-distribution, 23.5% → 65.0% on 200 held-out shifted scenes.
- **[S-BFM: A Behavioral Foundation Model for Humanoid Control from Sparse Spatiotemporal Goals](https://arxiv.org/abs/2611.27552)** — Generates whole-body transitions from target postures/poses/arrival times alone. Fixed-goal reach 43.5% → 74.6%, terminal position error 1.67 m → 0.26 m; deployed on a full-size AGIBOT A3.
- **[Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance](https://arxiv.org/abs/2611.27182)** — Training-free event-driven harness where the agent writes a lightweight, stateful "tripwire" program that runs alongside the policy and can query a small VLM. On RoboHD with a simulated person: human contact rate halved, safety 61.3% → 81.3%, with no task-success loss. Nice practical safety idea for VLA deployment.
- **[Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter](https://arxiv.org/abs/2611.27845)** — Head-camera scene model + target-conditioned CBF-QP keeping the tool away from non-target switches. 10/10 real trials on a Unitree G1; 9/9 vs 5/9 safe completions in simulation.
- **[GRACE / Humanoid Pose / S-BFM]** — *(HumanoidPose)* monocular 3D humanoid whole-body pose benchmark + kinematic-grounded framework; zero-shot transfer to real 2D and 3D evaluation.
- **[Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking](https://arxiv.org/abs/2611.27648)** — Shows imagined gradients are largely unconfirmed by the simulator (top 0.5% of rollouts carry 22% of gradient norm but fail verification). Capping gradient norm and resampling yields 0.953 → 0.967 normalized return and halves persistently failing clips.

---

## 🔄 Sim-to-Real, Simulation & System Infrastructure

- **[One Behavior, Out of Order: Deterministic Execution and Parallel Simulation of ROS 2 Applications](https://arxiv.org/abs/2611.26676)** — Gives ROS 2 a lightweight read/write coordination scheme making applications deterministic, then an out-of-order parallel simulator requiring no changes to applications or ROS 2. Up to 2.6× faster than synchronous parallel simulation with an order of magnitude less message memory.
- **[LiDAR Signals for Robot Locomotion: Spherical Range Images Enable Robust Sim-to-Real](https://arxiv.org/abs/2611.27223)** — Recovers the physical LiDAR's angular sampling pattern and replays it via GPU ray casting for sensing-level alignment, plus identical spherical encoding on both sides. Beats depth- and elevation-map baselines without distillation or online mapping. This is a good template for perception-level sim-to-real.
- **[A Lightweight Method for Validating Simulated LiDAR Configurations](https://arxiv.org/abs/2611.27379)** — Platform-agnostic point-density-over-distance check using only boxes and point clouds; shows datasheet matching gives systematic near-field density errors.
- **[Mechanism Parity for Simulation-Based Validation of Autonomous-Driving Perception](https://arxiv.org/abs/2611.27447)** — Argues output/appearance agreement doesn't prove the perception system used the same evidence; introduces decisive-evidence diagnostics. Methodologically worth borrowing for robot perception validation.
- **[Instant-LIVO: Efficient LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2611.27633)** — Compact OctVox map and bounded single-reference-frame visual map; ~2.3× / 2.1× speedups and 1/20 peak memory vs baselines on x86/ARM.
- **[BRINA: Bottom-Referenced Inertial Navigation with AKAZE](https://arxiv.org/abs/2611.27817)** — FLS-only sonar-inertial SLAM recovering metric scale from seabed returns instead of a DVL; simulation plus ten field missions.

---

## 🎓 Datasets & Annotation

- **[RoboCap-10k: A Metrically Accurate Egocentric Dataset for Robot Learning](https://arxiv.org/abs/2611.26916)** — 10,000 hours of unscripted manipulation from paid workers in 11 countries on one 250 g six-camera hat rig, with <1 px epipolar calibration, gravity-aligned SLAM trajectories, and cm-precise hand poses. Notable for consistent hardware and reported accuracy.
- **[EgoSurgHands: An Egocentric 3D Hand Pose Dataset for Open Surgery Training](https://arxiv.org/abs/2611.27101)** — 41,909 training hand instances, human-validated evaluation, leave-one-wearer-out protocol. MediaPipe detects a hand in only 24.1% of evaluation rows — sobering for surgical hand tracking.
- **[Ego2Ego: Generative Visual Perspective Taking Across Collaborators](https://arxiv.org/abs/2611.27459)** — Generates a collaborator's egocentric video from your own, using shared 3D scene geometry and ego visual memory. Relevant for human-robot collaboration and for turning single-person recordings into multi-view robot learning data.
- **[Mem-X: A Memory-Dependent Cross-Episode Benchmark for VLN](https://arxiv.org/abs/2611.27166)** and **[FS-Nav / Beyond Future Views](https://arxiv.org/abs/2611.27418)** and **[NavRSI](https://arxiv.org/abs/2611.27499)** — Navigation-flavored; included only because they touch embodied memory/agent harness design. Mem-X's "does success actually require history?" framing is a good evaluation pattern for manipulation too.
- **[γ-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306)** — Mobile manipulation sim/benchmark with tool-based agent execution, reference programs, and demonstration collection via sustained contact.

---

## 🧪 Adjacent But Relevant — Agent Harnesses & Self-Improvement

Several papers converge on the same theme: **the harness around the model matters as much as the model**. Worth scanning for anyone deploying embodied agents.

- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)** — Actor + Reflector dual agent, hierarchical memory, refinable behavioral policy. 82.4% RoboTwin 2.0, 76.7% RoboSPA, 94.4% RMBench, 96.7% real-world average.
- **[EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection](https://arxiv.org/abs/2611.27797)** — Explorer/Diagnoser/Validator loop; 53.60% → 80.40% simulation, long-horizon real-world 20% → 80–100%.
- **[Search-Informed MPPI for Kinodynamic Motion Planning](https://arxiv.org/abs/2611.26763)** — Embeds MPPI optimization inside MCTS expansion with "bait"-guided targets; smallest search trees and smoothest control among three kinodynamic baselines.
- **[GeoSDF-Diff: Geometry-Aware Diffusion Planning for Collision-Free Trajectories](https://arxiv.org/abs/2611.27373)** — Multi-scale SDF conditioning in a DiT denoiser; 65.2% average success on held-out cluttered environments, +25.4 to +28.5 points over diffusion baselines, without post-hoc repair.
- **[What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage](https://arxiv.org/abs/2611.27939)** — Compares decision-policy vs outcome-model interfaces for damaged quadrupeds/humanoids. Capability contracts cut declined missions from ~32% → 7–8% (Go2) and 57% → 35–36% (H1).
- **[Frontier Voltage Boost Laplacian Path Planning](https://arxiv.org/abs/2611.27308)** — Harmonic-potential-field variant that scales better and handles narrow passages faster.

Two other mentions worth knowing: **[Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)** (27B open-weight model, RL entirely in simulation, 60% real dual-arm success vs 0% base) and **[RynnUnify](https://arxiv.org/abs/2610.32965)** (16B unified embodied model with a world-action extension at 51.5% on 20 RoboCasa365 tasks).

---

## ⏭ Out of Scope (briefly)

The remaining ~250 papers are in LLM evaluation, safety/guardrails, quantization, inference serving, medical imaging, chemistry/biology foundation models, speech/audio, and general agent benchmarks. If any of those matter for a specific downstream need (e.g., **Speculative Decoding Is Less Speculative Than You Think** for VLA serving, or **Grana** for reward modeling in long-horizon manipulation), say the word and I'll pull them into focus.