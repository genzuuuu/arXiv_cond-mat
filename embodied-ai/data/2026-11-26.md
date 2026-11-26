### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-26T15:46:04.298973
  - **arXiv update** 2026-11-26T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied Intelligence & Manipulation — arXiv Roundup

## Dexterous Hands, Tactile Sensing & Contact-Rich Manipulation

- **[Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers](https://arxiv.org/abs/2611.32582)** — 5-fingered, 12-DoF tendon-driven hybrid hand; linear control gives 84.8% of human grasp postures and up to 1432°/s finger speed, with a teleoperation stack for thin deformable objects.
- **[DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data](https://arxiv.org/abs/2611.33579)** — Turns 9 human hand-object datasets into ~65k physics-corrected arm-hand trajectories (116 h) at 10× the speed of RL-based retargeting; policies trained on it beat uncorrected baselines in sim and on a real robot.
- **[FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884)** — Lets users specify which hand, which fingers, and which contacts; generated HOI motions serve as priors that an agent refines in a physics digital twin, then deploys on a real dexterous humanoid.
- **[DexLink: Synthesizing Dexterous Behaviors from Chained Hand-object Poses](https://arxiv.org/abs/2611.34936)** — Retargets sparse static hand-object templates into reference trajectories and refines them with residual RL; covers single-hand, bimanual, articulated, and dynamic tasks with zero-shot sim-to-real promise.
- **[T-Tac: A Soft and Thin Active Thermal Tactile Sensor for Robotic In-Grasp Material Identification](https://arxiv.org/abs/2611.28939)** — Film heater + ionic temperature sensor; 92.69% accuracy over 12 materials using a 3 s pulse and 10 s observation.
- **[CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation](https://arxiv.org/abs/2611.34117)** — Couples wrist vision and touch through shared contact semantics; robust to missing local observations and improves with autonomous retries across four real tasks.
- **[TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action](https://arxiv.org/abs/2611.26405)** — Isolates "tactile innovation" (tactile change unexplained by vision + action) as an auxiliary training target only; +10.7 pp sim / +9.0 pp real over the best visuo-tactile baseline, with no extra module at deployment.
- **[FAVLA: A Force-Adaptive Multi-Rate VLA Model for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2602.23648)** — Low-rate VLM reasoning + high-rate force-conditioned action expert, with inference rate scheduled from predicted force variance; 88.8% average success and lower peak contact forces.
- **[Can Visual World Models See Force?](https://arxiv.org/abs/2611.34422)** — Probing study: most visual/world/policy models detect *when* contact happens but not *how much* force — and robot post-training doesn't fix it.
- **[M²AdaptVLA: Multimodal Memory-Augmented VLA with Predictive Test-Time Adaptation](https://arxiv.org/abs/2611.34560)** — Visual memory via test-time-training fast weights plus gated wrench memory; online adaptation from wrench prediction; 82.71% mean success, +31.46 pp over the strongest baseline.

## Vision-Language-Action Policies

- **[HoloBrain-0.5 Technical Report](https://arxiv.org/abs/2611.34449)** — Cross-embodiment VLA family (continuous diffusion and discrete FSQ variants) pretrained on 10k+ hours across 15 embodiment categories; 94.52% vs π0.5's 86.25% after post-training; strong zero-shot transfer from Piper to Piper-X.
- **[FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions](https://arxiv.org/abs/2611.33635)** — High-pass prior + cross-timescale latent actions; 98.2% LIBERO, 98.0% LIBERO-Long, 80.4% zero-shot LIBERO-PLUS.
- **[PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.10925)** — Frozen prior expert + trainable adaptation expert (25% of full-FT params); +11 pts over π0.5 on RoboTwin 2.0-Hard, 99.1% LIBERO, big few-shot/OOD gains.
- **[X-World: Transferring Video Priors to Cross-Embodiment Robot Control](https://arxiv.org/abs/2611.33914)** — Adapts video diffusion with view-agnostic Q-Former and flow-matching action expert; 20 Hz inference with async chunking; 81.7% across six bimanual real tasks.
- **[OmniAct: One Policy, One Million Embodiments](https://arxiv.org/abs/2611.33158)** — Conditions on a per-scene kinematic graph and predicts relative joint motions; trained over 1M procedurally generated embodiments; 63.0% vs π0.5's 17.8% on held-out embodiment-scene episodes.
- **[Entangle: Scaling Human-Video In-Context World-Action Models](https://arxiv.org/abs/2611.28732)** — One human video as in-context task spec, with intra-task contrastive objective to block shortcut learning; 69.5% on seven unseen RoboTwin tasks (+22.6 pp over Zero-WAM).
- **[SOAR: Temporal Structure-guided One-step Action Generation](https://arxiv.org/abs/2611.30363)** — Predicts DCT of future actions for one-step generation; 83.9% over 53 Adroit/Meta-World tasks at 8.7 ms; 97.2% LIBERO when applied to π0.5.
- **[Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies](https://arxiv.org/abs/2611.34148)** — Training-free schedule optimization by distribution matching; +2.8 pp for π0.5 and GR00T N1.7 on RoboTwin 2.0, transferring to real tasks.
- **[iMFPO: Improving Mean Flow Policy Optimization for Embodied Control](https://arxiv.org/abs/2611.33922)** — One-step flow policy with drift-aware velocity alignment; cuts action-generation latency from 15.57 ms to 0.41 ms.
- **[ε̃: Does Initial Noise Induce Directional Bias in VLA Models?](https://arxiv.org/abs/2611.33816)** — Finds initial noise induces a consistent action-space direction (aligned with its temporal mean); antithetic-pair training + mean removal lifts π0.5 real success from 40% to 68%.
- **[DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body VLAs](https://arxiv.org/abs/2611.32665)** — Replaces the simulator with a learned world model so body-execution losses backprop into the VLA head; +12.5 pp on HumanoidArena.
- **[Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models](https://arxiv.org/abs/2611.34352)** — Swaps NL prompts for temporal logic with a typed graph encoder; 62.3% five-task CALVIN success and 65.0% on LIBERO-Mem without observation history.

## World / World-Action Models

- **[G0.7: Scaling Up a Fast World Action Model with Long Context](https://arxiv.org/abs/2611.31822)** — Up to five minutes of history and large teleop+ego-video pretraining; 60 ms per 16-step chunk (7.6× faster than imagine-then-act); 86.9% mean progress over seven real tasks including multi-minute box folding.
- **[PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)** — 30k hours, 22 platforms, multiview-consistent, 10.1 FPS with fast/slow memory; rollouts good enough for GRPO policy optimization.
- **[Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model](https://arxiv.org/abs/2611.34435)** — Freezes a 33B video backbone and trains 0.34% of parameters; key finding: *where* training is allocated across noise levels matters more than *how* actions enter.
- **[WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models](https://arxiv.org/abs/2611.34124)** — Imagines each candidate chunk's outcome in two denoising steps; Safe-Guard cuts hazardous closed-loop trials from 27.0% to 10.8% without losing success; 74.0% vs π0.5's 59.5% on five real tasks.
- **[Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model](https://arxiv.org/abs/2611.33993)** — Separates *whether* to apply a correction from *what* it should be, gated by predictive uncertainty; 56.72% vs 45.44% on dynamic object manipulation.
- **[A 3D Simulator for Passive SPAD Imaging](https://arxiv.org/abs/2611.33498)** — *(adjacent)* Photon-accurate sensor sim with zero-shot sim-to-real under 2 lux for classification, rotation estimation, and segmentation.

## Sim-to-Real, Benchmarks & Evaluation

- **[RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](https://arxiv.org/abs/2611.33390)** — 90 spatial-constraint tasks, frozen scenes with bit-identical replays. Sobering: best coding agent (GPT-6 Astra) solves 86% with privileged state but 43% from real sensors; four zero-shot VLAs solve **none** of their 18 one-arm puzzles.
- **[WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models](https://arxiv.org/abs/2611.34130)** — 300 tasks, 12k human annotations, six physics dimensions; current world models don't hold fine-grained physical plausibility consistently.
- **[DTU-Bench: Evaluating Runtime Task Adaptation in Robotic Manipulation](https://arxiv.org/abs/2611.34538)** — Instruction changes mid-execution drop success from 95.8% to 1.6%; a scripted retreat-and-restart recovers 2%→38% (π0.5) and 8%→48% (DM0.5).
- **[FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers](https://arxiv.org/abs/2611.33769)** — Controlled comparison: cloning 2,400 takeover recoveries gives +29.4 pp on held-out failures, but costs 30.0 pp of nominal success (−16.5 pp when mixed with demos). Takeover data is not free.
- **[Triage Before Fine-Tuning: Feasibility-Gated Selection of Embodied Foundation Models](https://arxiv.org/abs/2611.33772)** — Five-stage gate (sensor contract, latency, probes, ranking, monitored closed-loop); on a real vehicle the latency gate eliminated the two highest-scoring candidates.
- **[BOT-Scale: A Traceable Evaluation Methodology for Robotic Manipulation](https://arxiv.org/abs/2611.34297)** — Score defined as a sum of outcome-conditioned factor penalties, so every deduction names an inspectable deviation.
- **[Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](https://arxiv.org/abs/2611.34849)** — Avoids the N×M integration problem: 47 coding agents + 5 non-agent methods across 6 benchmarks, with contamination-filtered training data.
- **[Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos](https://arxiv.org/abs/2611.33705)** — Four-agent pipeline producing editable Blender assets with articulated mechanisms from egocentric video.

## Skill Discovery, Memory & Agents for Manipulation

- **[SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation](https://arxiv.org/abs/2611.33915)** — Keeps procedures *and* measured action effects across attempts; RoboDojo average score 27.0→54.4 over ten attempts with a frozen model.
- **[RoboEvo²: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)** — Alternates coding-agent skill discovery and policy learning; standalone success 11.0%→84.1% on LIBERO-PRO, 95.0% hybrid on Unitree G1-D, no extra human demos.
- **[Skeptic: Grounding Failure Diagnosis for Robot Skill Discovery](https://arxiv.org/abs/2611.33560)** — Attacks the "false impossibility" failure (19.5→8.5 per campaign) by grounding repairs in measured effects and gating skill admission on success.
- **[M²-WAM: Efficient Hierarchical Memory Across Modalities and Timescales](https://arxiv.org/abs/2611.33710)** — Bounded visual short/long-term memory plus action-prefix memory; +53.2% and +61.2% absolute on MIKASA-Robo and RMBench; +29.3% on three real tasks.
- **[SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Manipulators](https://arxiv.org/abs/2611.34750)** — Agent emits a sparse keypose sequence and a motion planner fills the gaps; 74.5% RoboDojo, 84.5% RoboLab at $1.7/episode (12× cheaper than dense agent policies), 88% on 16 zero-shot real tasks.
- **[RoboThink / RoboAda](https://arxiv.org/abs/2611.30111)** — See "Complementary Angles" below. **[Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs](https://arxiv.org/abs/2611.34914)** — Steers a frozen π0.5 along learned SE(3) object trajectories; 24.5%→95.1% on 1,941 obstacle/displacement scenes, and guides DROID π0.5 around an obstacle on a real Franka with a sim-trained prior.

## Teleoperation & Data Collection

- **[RoboJackVR: Turning Robot Tasks into VR Games for Scalable Demonstration Collection](https://arxiv.org/abs/2611.33731)** — Standalone headset VR game with on-device MuJoCo and recording; ACT trained only on VR demos retains ~91% of the simulation-demo baseline across 66 LIBERO-90 tasks.
- **[CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion](https://arxiv.org/abs/2611.34257)** — Even videos *without* object manipulation help: camera motion adds supervision; LIBERO 96.40%→98.10%, RoboCasa 365 22.96%→29.32%.
- **[DemoFoundry: Toward Scalable Photorealistic Robot Data](https://arxiv.org/abs/2611.34671)** — Coding agents write executable interaction programs; a generative renderer turns proxy videos photorealistic; approaches equal-real-data performance.
- **[RoboEdit / DataForgeVLA](https://arxiv.org/abs/2608.18948)** — *(human-video→robot and synthetic demo generation; see papers 123 and 48)*: RoboEdit-14M gives 174k aligned video pairs across 7 embodiments; DataForgeVLA's 300 synthetic episodes reach 80% real pick-and-place vs 90% for real teleop (preliminary, one object).

## Planning, Control & Locomotion (Brief)

- **[FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots](https://arxiv.org/abs/2611.33380)** — Collision via Gaussian overlap integrals; orientation-aware planning through tight gaps, seconds even with 100k+ Gaussians.
- **[Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid](https://arxiv.org/abs/2611.33828)** — Single RL policy for coordinated stepping + manipulation; >1 m box transport in all five real trials, no object-state sensing.
- **[Riding the Wave: Sim-to-Real Humanoid Control on Elastic Terrain](https://arxiv.org/abs/2611.34569)** — Pretensioned mass-spring terrain model in GPU sim; zero-shot balance/jump/trampoline-entry with proprioception only, tolerant to 0.35–2.8× stiffness without calibration.
- **[μMPC: Microsecond-Scale Nonlinear and World Model Control](https://arxiv.org/abs/2611.34597)** — Koopman-linearized precompilation; 23 μs on desktop CPU, 24 ms on a Crazyflie, up to 1907× faster visuomotor planning.
- **[CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with LLMs](https://arxiv.org/abs/2611.33911)** — LLM invents non-predefined cooperative motions (climbing on a partner, bridging gaps with boxes); 30/30 valid in simulation.

## Safety, Robustness & Failure Modes (Manipulation-Relevant)

- **[Why Does Sensor Depth Fail Learned Manipulation Policies?](https://arxiv.org/abs/2611.33352)** — Clean depth gives ~10 pp; most survives 20× noise, but *holes* over ~1/6 of the wrist image erase the benefit. Judge depth cameras by coverage, not precision.
- **[Best-of-N Test-Time Steering Can Lead to Reward Hacking in VLA Models](https://arxiv.org/abs/2611.33398)** — More samples hurt when the verifier is inaccurate; calibration and softmax selection mitigate.
- **[Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](https://arxiv.org/abs/2611.33925)** — Action-conditioned models barely beat a copy-first-frame baseline off the demo manifold; 62k perturbed trajectories cut object trajectory error 28.2% and action-divergence error 43.3%.
- **[Grounding Failure Diagnosis / SealedLoop](https://arxiv.org/abs/2611.33794)** — In-loop judges accepted 65 of 196 failures in one generation; only evidence the improver cannot influence reliably certifies improvement.
- **[Ask to Land: Mask-Conditioned Open-Vocabulary Landing via Differentiable Physics](https://arxiv.org/abs/2611.34020)** — Frozen open-vocab perception front-end + BPTT-trained policy; lands on user-described static and moving platforms. *(aerial, adjacent)*

## Complementary Angles Worth a Look

Two papers frame the same question from opposite ends and are worth reading together: **[RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)** teaches a policy to act on agent guidance via instruction and feedback channels (LIBERO drift: 0.09→0.87; 50 RoboTwin tasks: 0.12→0.74), while **[RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)** leaves the plan alone and corrects the commands using free inverse-dynamics labels (27.8%→62.9% under eleven physical shifts). Also: **[Toward Agentic Robotics: A Large-Scale Study of Harness Design](https://arxiv.org/abs/2611.34778)** — 470k rollouts, seven controlled studies on how VLM reasoning and VLA control should be wired together (+42.8 pts from harness design alone).

**Not covered here** (outside scope): quantum computing, medical imaging/clinical LLMs, telecom, security benchmarks, pure NLP/interpretability, and autonomous-driving planner papers. Several drive-adjacent world-model and VLA-post-training papers were included where the method transfers to manipulation.