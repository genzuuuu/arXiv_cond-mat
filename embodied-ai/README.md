### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-16T14:00:08.666716
  - **arXiv update** 2026-11-16T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & Embodied AI Digest

A large batch today. Below, the relevant embodied-intelligence papers are grouped by theme; everything outside scope is listed briefly at the end.

## VLA Models: Post-Training, Architectures & Surveys

- **[Agentic-Teacher](https://arxiv.org/abs/2611.17394)** — Autonomous data engine that analyzes VLA failures, writes closed-loop code policies to collect demonstrations from weak states, and post-trains. Lifts π₀ on LIBERO-10 (79.4→87.8%) and RoboCasa (0→30%).
- **[ESI](https://arxiv.org/abs/2611.18176)** — "Embodied Self-Improvement" flywheel that co-trains LLM prompts, a shared skill interface, and VLA parameters from interaction. 49.41% success on 10 RoboDojo tasks, beating hybrid agent baselines.
- **[E0](https://arxiv.org/abs/2511.21542)** — Discrete-diffusion action head over quantized action tokens (Tweedie discrete diffusion) for fine-grained VLA actions; +8.1% average over baselines on LIBERO, VLABench, ManiSkill, and a real Franka.
- **[RB-VLA](https://arxiv.org/abs/2602.20659)** — Belief-centric VLA: a self-supervised world-model latent tracks task progress; the VLM is queried once per task. +52.5%/+37.5% over π₀ on long-horizon pick-and-place and stacking, ~5× lower latency.
- **[VLA Life-Cycle Survey](https://arxiv.org/abs/2611.18372)** — Reviews 88 works (design → training → deployment) and analyzes 22 models on seven axes; notes benchmark-to-real robustness gaps.
- **[D-VLA](https://arxiv.org/abs/2605.13276)** — Distributed async RL framework for billion-parameter VLAs with "plane decoupling" and a four-thread swimlane pipeline; strong LIBERO throughput.
- **[Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)** — 27B open-weight model trained purely in sim with robot-use RL; 60% success on a real dual-arm robot (base model: 0%), and 57.4% vs π₀.₅'s 0.75% on LIBERO-Pro.
- **[Enviconing Agentic Robotics](https://arxiv.org/abs/2611.18359)** — Position paper arguing "Embodied System 2" (foundation model + harness) is the core of agentic robotics, with an evaluation framework and roadmap.

## Dexterous Manipulation, Hands & Tactile Sensing

- **[TouchTwin](https://arxiv.org/abs/2611.17619)** — Closes the *force gap* in real-to-sim-to-real: rebuilds human touch recordings (880-taxel glove, RGB-D) in MuJoCo so replays match recorded grip force (0.99× vs 0.31× for pose imitation). Adds contact/force labels to augmented demos.
- **[VOKE](https://arxiv.org/abs/2611.16423)** — Kinematics-aware perception for in-hand manipulation: predicts object pose, linear/angular velocity and acceleration, refines pose estimates, and feeds a sim-trained kinematics-augmented policy transferred zero-shot to hardware.
- **[IORA](https://arxiv.org/abs/2610.30969)** — Support-aware grasp synthesis for low-DoF coupled hands; graph matching of hand/object surfaces plus wrist/motor refinement for object immobilization (e.g., cooking).
- **[The Missing Touch](https://arxiv.org/abs/2608.19372)** — Bilateral teleoperation with a vision-based tactile sensor plus a 32-pixel fingertip tactile display. Spatially distributed contact feedback shortens task time and yields better demos; policies trained on tactile demos inherit the gains.
- **[VOKE-adjacent: HEIR](https://arxiv.org/abs/2611.17238)** — Dataset pairing speech, gaze, egocentric video, and teleoperated nav-manipulation trajectories for intent grounding and long-horizon execution.

## Visuomotor Policies & Representations

- **[Pre-Trained Visual Representations for Contact-Rich Insertion](https://arxiv.org/abs/2611.17631)** — Controlled study on insertion: the best representation flips even between near-identical tasks, but spatially grounded / contact-centric cues consistently help — and are hard to estimate under realistic noise.
- **[Imitation Policies Learn a Proprioceptive Anchor](https://arxiv.org/abs/2611.17658)** — Derives and validates a predictive law for how policies discount noisy object readings (α = V/(V+s²)); one measurement predicts ten held-out sensitivities (MAE 0.025 vs 0.37 for classical EIV).
- **[Cross-View Consistency in Multi-View Augmentation](https://arxiv.org/abs/2611.17751)** — Controlled replay study: appearance coupling can often be relaxed (~0–2.5pp cost), but breaking cross-view *geometry* costs ~3.3pp — protect spatial correspondence.
- **[OaP: Objectives as Policies](https://arxiv.org/abs/2611.18298)** — VLM writes an editable cost program (stages, cost library, terminal conditions) executed by sampling-based MPC in a real-to-sim digital twin, iteratively revised before real deployment.
- **[SAI: Sequential Asymmetric Imitation](https://arxiv.org/abs/2606.16490)** — Single-teleoperator curriculum for physically coupled dual mobile manipulators; trains each robot against the deployed partner, with sparse human interventions near coordination failures.
- **[Fast Non-Parametric Heteroscedastic Imitation Learning](https://arxiv.org/abs/2610.08650)** — Geometry-aware kernel policies with heteroscedastic uncertainty and <3 ms updates for trajectories with position and orientation.

## Sim-to-Real, World Models & Evaluation

- **[Latent Goal Costs for Visual World-Model Planning](https://arxiv.org/abs/2611.17529)** — Small residual adapter on frozen I-JEPA embeddings for goal cost; succeeds 54→98% (DotWall) and 82→96% (PointMaze), no encoder retraining.
- **[LASR](https://arxiv.org/abs/2611.17775)** — Metric for whether world-model latents encode *action* beyond prediction shortcuts; includes controls and a benchmark protocol.
- **[Model-Free Assessment of Simulator Fidelity](https://arxiv.org/abs/2512.05024)** — Quantile-curve confidence sets for the sim-to-real gap on latent population parameters; demonstrated on LLM–human alignment (WorldValueBench).
- **[TelePhysica](https://arxiv.org/abs/2611.18078)** — Single-photo → executable physical scene (rigid, articulated, cloth, elastodynamics) via a VLM coding agent with equilibrium preflight; 0→81% equilibrium-verified recovery.
- **[Heavy Metal Acrobatics](https://arxiv.org/abs/2611.18365)** — RL in sim → real 5-tonne skid-steer loader performing wheelie-balancing acrobatics on rough terrain (Science Robotics).
- **[OneSteer](https://arxiv.org/abs/2610.41354)** — One-step diffusion whole-body controller for humanoids with differentiable test-time steering; 27/27 nominal trials on a Unitree G1, limbo under a 1.1 m bar and hurdle step-over included.

## Teleoperation & Human-Robot Interaction

- **[EViDS / Telerobotic Interventions for Self-Driving Labs](https://arxiv.org/abs/2611.18496)** — 6-DoF arm teleoperated via 3D mouse for fault recovery; decoupled translation/rotation control beats coupled mode, and path guidance shifts operator risk tolerance.
- **[Self-Building Labs](https://arxiv.org/abs/2610.23826)** — SDL that designs its own layout, digital twin, robot skills, and workflows given a scientific goal; validated on quantum-dot synthesis.
- **[Talk to Act](https://arxiv.org/abs/2611.17549)** — Synthetic multi-turn HRI dialogue benchmark; small open models (270M–8B) extract intent via tool-calling without fine-tuning.
- **[Personalization of Values for LLM Assistant Robots](https://arxiv.org/abs/2611.18230)** — Users want robots lower on personal-focus and higher on social-focus values; prompt engineering alone barely shifts LLM value profiles.

## Safety-Aware Manipulation & Planning

- **[Hazard Reasoning into 3D Risk Fields](https://arxiv.org/abs/2611.17566)** — VLM infers task-conditioned object-pair hazards, grounded via open-vocab segmentation + depth into continuous risk fields that correct nominal motions; includes task-rejection cases.
- **[Safety-Aware Behavior Planning with Explicit Constraint Space](https://arxiv.org/abs/2611.18026)** — Learns task/environment-conditioned applicability of textual safety rules, plus a multimodal Safety Inspector with test-time LoRA adaptation.
- **[PoliMop](https://arxiv.org/abs/2611.18110)** — Kinodynamic RRT that expands via policy rollouts in physics sim; preplanned mass-point path cuts planning time up to 63% across quadrupeds, humanoids, wheeled robots.

## Embodied Navigation

- **[X-Nav](https://arxiv.org/abs/2611.17598)** — First language-instructed indoor-to-outdoor long-horizon navigation on a bipedal humanoid (~100 m office-to-store mission), with digital-twin adaptation of the RGB-only navigation model.
- **[ERA](https://arxiv.org/abs/2611.17730)** — Training-free object navigation on *predicted* depth, treating movement as error correction ("Move with Error"); raises VLFM success 10.8→61.7%.
- **[VLAN](https://arxiv.org/abs/2611.18346)** — Embodiment-conditioned accessibility navigation benchmark (humanoid, quadruped, wheelchair, visual impairment) with Passable/Bypass/HighRisk/Blocked labels.
- **[Budget-Conditioned Object Search](https://arxiv.org/abs/2611.17442)** — Bellman-style supervision under partial observability beats privileged TSP-expert imitation for exploration (71.4% vs 65.5% of targets found).
- **[LLMs as Spatial Priors for ObjectNav](https://arxiv.org/abs/2611.18123)** — LLM-generated room layouts cut search area, but far less than priors from real layouts; best used for object–room associations, not placement.

## Locomotion (brief)

- **[PROOF](https://arxiv.org/abs/2611.18305)** — Teacher–student perceptive locomotion with uncertainty-gated proprioceptive fallback under occlusion/glare (Unitree Go2).
- **[Body-Aligned Virtual Joints](https://arxiv.org/abs/2611.18003)** — Standardized virtual joint space lets one locomotion recipe transfer across three humanoids; ~6× less heading drift on G1.
- **[PingpongDuo](https://arxiv.org/abs/2610.20579)** — Hierarchical humanoid table-tennis doubles with risk-filtered team coordination; >10 consecutive alternating strikes.
- **[Go2-W Long-Distance Navigation](https://arxiv.org/abs/2606.21387)** — Legged-wheeled controller with periodic foot-lifting to spread hip heat; 2.8 km autonomous Tsukuba Challenge route.

## Briefly Noted (outside core scope)

Multi-agent LLM systems and benchmarks (Soteria, Co-Sight, ModHarness-RL, AutoRL, MASTARS, AgenticPay, CoffeeBench, OutfitterBench, WebArena-Pro); interpretability and activation steering (persona polylogue, abliteration, pain-state introspection, DECODE); LLM evaluation/benchmarks (GDP.xlsx, LeCat, WeightBench, BigCodeBench, JFinBench, MineralExp, pXRD-Bench); medical imaging (aorta reporting, stroke segmentation, sleep staging, echocardiography synthesis); quantum computing and quantum-hybrid optimization (SQD parameter selection, drilling trajectories); time-series foundation models (FlexCast, SWIFT, TimesJev, T2ST); and assorted infrastructure (Superfluid, FlashSampling, VelServe, TorchTPU, LACCO).

**Overall signal:** the strongest embodied results today cluster around *failure-driven data engines and post-training* (Agentic-Teacher, ESI, sim-trained reasoning agents), *tactile/force fidelity in dexterous pipelines* (TouchTwin, Missing Touch), and *belief/state persistence for long-horizon control* (RB-VLA, OneSteer).