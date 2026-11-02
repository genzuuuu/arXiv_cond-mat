### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-02T13:50:06.824955
  - **arXiv update** 2026-11-02T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & AI Digest — Embodied Intelligence Focus

## World Models & Video-to-Action

**[WorldBridge: Bridging Video and Action for Task Generalization in World Action Models](https://arxiv.org/abs/2610.40748)** — Separates video and action experts in a World Action Model; in-distribution supervision alone yields 25% OOD success, unlabeled task video raises it to 55.9%, one labeled demo per task to 70.7%. SOTA on RoboTwin 2.0 (96.23%), RoboCasa GR1.

**[CausalWAM: Learning the Causes of Actions in World Action Models](https://arxiv.org/abs/2610.42096)** — Adds a sparse routing path to a pretrained WAM's action head so action latents isolate causal factors from nuisance variables, with identifiability proof; improves closed-loop success on synthetic and real robots.

**[Hierarchical World Models with Implicit Dynamics](https://arxiv.org/abs/2610.42146)** — Decouples high-level state-space reachability from low-level inverse dynamics; 38.5% gain over SOTA planners and 135% over single-level world-model MPC on long-horizon tasks.

**[When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity](https://arxiv.org/abs/2610.41970)** — Sobering audit: learned value selectors underperform random by 1.66 pp on Cosmos Policy/RoboCasa, oracle headroom is 1.4 pp, and 82% of states have identical candidate outcomes. Also flags a silent rendering corruption on compute-heavy planning paths.

**[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)** — Lightweight module extracts physical tokens via future RGB/depth/flow prediction (no online video generation); 99.3% LIBERO, 93.6% RoboTwin 2.0, 81.5% SimplerEnv.

**[Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232)** — Single DiT jointly models video, depth, segmentation, and flow across robot embodiments and human hands.

## VLA Policies & Inference Efficiency

**[STAR: Steering Action Representations during Inference](https://arxiv.org/abs/2610.41009)** — Training-free: finds late-layer action representations lose visual grounding; EMA over late residual updates yields +4.0 pp success.

**[RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices](https://arxiv.org/abs/2610.41625)** — View-aware fusion + compressed tokens condition a flow-matching head; 52.26% RoboTwin 2.0 (above π₀), 72% real bimanual at 30 ms on RDK S600.

**[Direct Action-Manifold Modeling for Efficient and Robust Bimanual Manipulation](https://arxiv.org/abs/2610.41643)** — DMAT reformulates action generation as single-step modeling of clean action chunks; +129.1%/+95.7% relative success over IDP3 and DiTFlow3D on 567 trials, 1.3–2× faster.

**[$\pi$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs](https://arxiv.org/abs/2603.02083)** — Flow-native online RL treating SDE transitions as supervision units; 57.6%→92.0% (π₀) and 77.1%→94.0% (π₀.₅) on LIBERO.

**[VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression](https://arxiv.org/abs/2610.41609)** — All six checkpoints move even on empty instructions; prompt prefixes fail entirely, action-chunk gating works on 5/6, fine-tuning suppresses completion but not motion.

**[SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2610.41408)** — 1.5-bit weights on GR00T N1.7 with 93.85% LIBERO, 4.83× memory reduction, 1.51× faster with INT8 activations.

**[TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216)** — Harness evolution lifts teacher 33.4%→63.6% on RoboTwin; distilled 4B student reaches 62.8% at ~⅕ teacher compute, transferable to other frozen planners.

**[ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies](https://arxiv.org/abs/2610.41663)** — Residual RL (no new demos) plus residual-field consistency merging for continual adaptation; validated on LIBERO and a real Franka.

**[Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space](https://arxiv.org/abs/2610.42021)** — End-to-end joint human-robot training via hierarchical semantic alignment; 80.5% RoboCasa-GR1.

**[META-Robot: Self-Cognition and Capability Scaling in Agentic Robots](https://arxiv.org/abs/2610.41868)** / **[RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](https://arxiv.org/abs/2610.42141)** / **[REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](https://arxiv.org/abs/2610.42053)** — Agent-harness papers: action-level predicates for self-assessment; harness search lifts success 9.7%→43.3% on unseen scenes; hierarchical brain/router/reflex runtime scores 95.9% LIBERO-Pro with 25% fewer control steps.

## Dexterous Hands, Grasping & Tactile

**[Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds](https://arxiv.org/abs/2610.41028)** — Contact-grounded demos with contact-alignment-first retargeting plus hierarchical contact-surface planner/controller; ≥50 pp final-stage gain across six hand-task pairs (LEAP, Wuji).

**[HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos](https://arxiv.org/abs/2610.41336)** — Object-centric RL objective decouples skill from hand trajectory, with anatomical constraints; generalizes across spatial configurations in sim and real.

**[UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis](https://arxiv.org/abs/2607.28198)** — Single relational formulation for grasp, relocation, in-hand rotation and translation; one policy without skill IDs supports long-horizon chaining.

**[NDPP-Grasp: Non-Differentiable Physical Plausibility Constraint-Guided Task-Oriented Dexterous Grasp Generation](https://arxiv.org/abs/2606.02432)** — Injects physical-plausibility guidance into the denoising of a task-aligned grasp diffusion model, even for non-differentiable constraints.

**[TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation](https://arxiv.org/abs/2610.20320)** — 10,000+ hours, 1M episodes, 1B frames via a tactile UMI-style handheld; demonstrated cross-embodiment transfer to three robots without robot-specific demos.

**[TacO: Benchmarking Tactile Sensors for Object Manipulation](https://arxiv.org/abs/2605.21976)** — Task-driven comparison of visual, acoustic, magnetic and resistive sensors; usefulness depends strongly on modality, material and task.

**[FlowTouch: View-Invariant Visuo-Tactile Prediction](https://arxiv.org/abs/2603.08255)** — Predicts tactile images from object-local 3D mesh plus flow matching; bridges sim-to-real and transfers to new sensors; used for grasp-stability prediction.

**[EquiContact: A Hierarchical SE(3) Vision-to-Force Equivariant Framework for Spatially Generalizable Contact-rich Tasks](https://arxiv.org/abs/2507.10961)** — Diff-EDF planner + compliant G-CompACT policy; near-perfect peg-in-hole success under spatial OOD without retraining.

## Teleoperation, Imitation & Skill Transfer

**[From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation](https://arxiv.org/abs/2610.40828)** — 281 policies, ~1,700 real RJ45 insertion trials on a five-finger hand. Representation choices dominate (70–100 pp effects); offline metrics correlate with success only weakly and within single policy families.

**[I3L: Iterative Interactive Imitation Learning for Whole-Body Mobile Manipulation](https://arxiv.org/abs/2610.17748)** — JoyLo+ interface with touch-triggered takeover + iterative retraining; +68.3 pp over base policies, ≥90% on every task.

**[Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations](https://arxiv.org/abs/2607.25397)** — TAMP-gated composition of atomic visuomotor skills; 100 demos beats diffusion policies with 1,000 on DexMimicGen.

**[SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery](https://arxiv.org/abs/2610.38234)** — Policy from simulated demos only; grasp in 90% of 50 phantom presentations, retraction preserved at 78% handoff. Ablations localize the sim-to-real gap to the instrument mask (22%/12% without it).

**[FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations](https://arxiv.org/abs/2610.41540)** — Short-horizon differentiable actor-critic with OT-matched rollout windows; handles a 152-muscle humanoid.

**[Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736)** — FERT retrieves successful segments using failure contexts; 93.3–99.2% on five real tasks, phone packaging 79.2%→98.3% with 96 robots.

**[BioAgent: Self-Directed Skill Acquisition and Capability Growth for Long-Horizon Laboratory Protocols](https://arxiv.org/abs/2610.41383)** — Acquires 5 new skill types, reuses 17 unchanged; 66%/58% complete-task success on 20/31-step dual-arm protocols.

**[Learning and Transferring Closed-Loop Robot Software](https://arxiv.org/abs/2609.19906)** — Coding agent archives validated closed-loop policy code; archived implementations lift new-task success 45.2%→57.0%.

## Sim-to-Real, Benchmarks & Evaluation Integrity

**[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)** — Traces spurious ejections in RoboTwin to a triangle-area threshold in collision detection; fixing one constant drops artifact episodes from 12/100 to 0 and raises five container tasks 89%→98%. Essential reading for anyone reporting sim success rates.

**[MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies](https://arxiv.org/abs/2610.41377)** — New clutter/occlusion/affordance benchmark; success drops >50 pp as distractors increase, wrong-object actions in 30% of cases.

**[TacClaw-Infinity](https://arxiv.org/abs/2610.20320)** (see above) and **[Do Earth-Trained Humanoid Controllers Walk on the Moon? Gravity, Terrain, and Soil Transfer](https://arxiv.org/abs/2610.30080)** — Only gravity-randomized rough terrain with 3D RFT soil contact survives both Earth (>0.83) and lunar (>0.95) conditions.

## Safety, Robustness & Control for Manipulation

**[Confidence-Modulated Safety Filtering for End-to-End Policies](https://arxiv.org/abs/2610.40922)** — Policy confidence sets filter conservativeness at runtime; permissive inside the ODD, extra margin beyond it.

**[Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](https://arxiv.org/abs/2610.03498)** — SAE-identified patch feature suppressed only when a probe detects attack; continuous suppression degrades the policy.

**[Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation](https://arxiv.org/abs/2610.41348)** — Continuous per-joint health vector + HealthNet estimator; +15.2 pp manipulation success on ManiSkill Panda tasks.

**[Specification-Aware Distribution Shaping for Robotics Foundation Models](https://arxiv.org/abs/2603.17969)** — Enforces Signal Temporal Logic constraints on a frozen foundation model via minimally modified action distributions.

**[CalibSwitch: Observation-Driven Camera-LiDAR Extrinsic Recovery...](https://arxiv.org/abs/2610.41352)** and **[TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking](https://arxiv.org/abs/2610.41275)** — Notable but peripheral (perception calibration; embodied tracking safety gate).

## Briefly Noted / Adjacent

- Motion planning & multi-robot: [Contact-based optimization for a million robots](https://arxiv.org/abs/2610.41548), [analytical characterization for two robots](https://arxiv.org/abs/2610.41558), [CA-BRF](https://arxiv.org/abs/2610.41188), [CC-HGCBF](https://arxiv.org/abs/2610.41214), [D4orm denoising](https://arxiv.org/abs/2609.35651).
- Humanoids & whole-body: [HIPC](https://arxiv.org/abs/2610.41334), [DiffWBC](https://arxiv.org/abs/2610.41354), [$\nabla$Mimic](https://arxiv.org/abs/2610.41654), [ROOF fall recovery](https://arxiv.org/abs/2610.42097), [Movens-Zero](https://arxiv.org/abs/2610.41877).
- Infrastructure: [cuPIQP batched differentiable QP](https://arxiv.org/abs/2610.41021), [QuIK4/5 IK](https://arxiv.org/abs/2610.41752), [Panda ROS 2 stack](https://arxiv.org/abs/2608.19740).
- Aerial/field robotics: [OpenFlyV2](https://arxiv.org/abs/2610.39287), [SAFARI](https://arxiv.org/abs/2610.41456), [WildOS](https://arxiv.org/abs/2602.19308), [Veloxity](https://arxiv.org/abs/2610.41053).
- Surveys: [Embodied memory survey](https://arxiv.org/abs/2610.41688), [Long-term memory security in LLM agents](https://arxiv.org/abs/2604.16548).

**Off-theme (skipped):** the majority of today's feed — LLM post-training, alignment/interpretability, RAG, federated learning, scientific ML for biology/materials, time-series foundation models, and general agent-harness papers with no embodied component.