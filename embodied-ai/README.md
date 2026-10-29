### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-10-29T11:44:35.326785
  - **arXiv update** 2026-10-29T04:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv — Embodied Intelligence & Manipulation Highlights

Most of today's feed is LLM-agent, RAG, and general ML work outside embodied manipulation. Below are the papers that genuinely fit your themes, plus brief notes on the rest.

## Robotic Hands, Grasping & In-Hand Manipulation

- **[cuArms: GPU-Accelerated Conflict-Based Planning for Multi-Arm Manipulation](https://arxiv.org/abs/2610.36250)** — Conflict-based planner co-designed with GPU parallelism for multi-arm workcells; real-time initial solutions with anytime improvement in motion quality and scheduling.
- **[Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation](https://arxiv.org/abs/2606.03385)** — Learns a failure-attribution model over grasp-then-plan pipelines, then does diagnosis-guided optimization of both grasp scoring and motion planning. Improves RL, IL, diffusion-policy, and VLA base learners.
- **[Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution](https://arxiv.org/abs/2610.37215)** — Test-time robustness for VLAs via retrieval from a graph of motion primitives from training demos, blended with the frozen policy's actions. +12% simulation, +40% real-world success under visual/contextual shift, no finetuning.
- **[Actionable CBFI: Prescriptive Interventional Diagnosis and Interaction-Aware Escalation for Sparse Causal Algorithmic Recourse](https://arxiv.org/abs/2608.27821)** — Not manipulation, but its prescriptive "cheapest single action / joint action only when needed" causal recourse framing is a useful analogy for intervention planning.

## Touch, Active Perception & Real2Sim2Real

- **[ActiveAlign: Aligning Egocentric Manipulation via Active Perception](https://arxiv.org/abs/2610.36859)** — Uses active hand waving (differentiable rendering hand-eye calibration) plus tactile touch alignment to close the Real2Sim2Real gap to millimeter precision. Demonstrated on a Unitree G1 pressing buttons and moving sliders.
- **[Counting the Bandages: On measuring the time that AI saves](https://arxiv.org/abs/2610.35942)** — Not robotics; included only because it's a rigorous framing of what "AI saves time" means (time saved vs. escaped defects), which transfers to evaluating human-in-the-loop robot teleoperation/oversight.

## Visuomotor Policies, VLA & Sim-to-Real

- **[TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823)** — Tokenizes actions as single-patch tokens in a pretrained video diffusion transformer's latent space; no video generation at test time. Strong sim and real-robot results at far lower inference cost than joint video-action policies.
- **[Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction](https://arxiv.org/abs/2610.36624)** — MoGAP focuses visual supervision on dynamic regions in WAM training. GR-1 tabletop 38.8% → 47.5% (Fast-WAM), 52.3% → 62.3% (Cosmos3-Nano).
- **[TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.36694)** — Task-conditioned flow-matching source priors and interpolation schedules; one-step inference beats 10-step FM on LIBERO-10 (53.4% → 69.7%) and transfers to π₀.₅. Real-world upper-drawer task 20% → 80%.
- **[Temporal-aware Reinforcement-based Speculative Diffusion Policy (TS-DP)](https://arxiv.org/abs/2512.15773)** — Identifies diffusion policies as I/O-bound, then applies speculative decoding with an RL scheduler. 3.2× wall-clock speedup, 26 Hz real-time control, +23% on a conveyor task.
- **[Rollback: Experience Backtracking in World Models for Policy Improvement](https://arxiv.org/abs/2610.36068)** — Rewinds world models to critical decisions for counterfactual branching; +10.7–11.9% success on three real tasks, beating average human players within 8 hours of training.
- **[RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.09410)** — Uses recovery and failure trajectories via a progress-aware value function; adversarial success 20% → 75%. Introduces FRBench for failure recovery.
- **[Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817)** — Small VLM + tool harness trained only in simulation reaches 96.7% real-world success, beating MolmoAct2 VLA (33.3%), and generalizes to unseen embodiments.
- **[When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies](https://arxiv.org/abs/2610.37547)** — Sparse human corrections define *when* and *where* residual RL explores on top of a frozen policy. Real-robot precision tasks 33.3% → 75.0%.
- **[HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](https://arxiv.org/abs/2610.36374)** — Replay-free continual imitation with dual-attention routing and key-level geometric regularization; strong on LIBERO variants.
- **[FrameForge / TAPESTRY / etc.](https://arxiv.org/abs/2610.36545)** — FrameForge is unified image generation, not robotics; noted only for its temporal-expert MoE idea.

## Teleoperation & Human-in-the-Loop

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835)** — Formalizes HITL approval that an agent cannot bypass even when it compromises the local harness. Motivated by an agentic wallet study where 10 frontier models autonomously harvested OTPs to raise caps. Relevant to safe teleoperation and approval gates.
- **[CIVER / Seeing the Options](https://arxiv.org/abs/2610.33702)** — Not teleoperation; Iris's typed decision over image candidates with a calibrated "none of the above" is a clean design pattern for teleop target selection.

## Benchmarks & Evaluation for Embodied Tasks

- **[Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks](https://arxiv.org/abs/2610.35905)** — Argues IQA should be goal-conditioned task utility; shows generic perceptual/MLLM scores weakly predict downstream VLM task success.
- **[SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding](https://arxiv.org/abs/2610.36384)** — 1,632 questions on body configuration, motion dynamics, temporal reasoning from egocentric video. Best MLLM 50.0% vs. human 68.5%.
- **[Kinematic Constraint-Referenced Evaluation for Articulated Object Manipulation](https://arxiv.org/abs/2610.37550)** — Constraint-Referenced Strategy separates joint progress from off-constraint waste; success-only metrics hide transfer failures.
- **[Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use](https://arxiv.org/abs/2610.37533)** — Studies what each sensing channel reveals in bimanual tool use, including failures not identifiable from passive sensing.
- **[VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717)** — Seven-stage latency breakdown across 18 VLAs on Jetson Thor and Ryzen AI Max+. Action-generation strategy dominates latency over model size.
- **[AmaraSpatial-10K](https://arxiv.org/abs/2604.23018)** — 10,071 metric-scaled, anchored 3D assets with collision hulls for embodied AI/spatial computing.
- **[Quality-Controllable Policy (QCP)](https://arxiv.org/abs/2610.37393)** — Inference-time control over speed and smoothness, with iterative hindsight relabeling; real conveyor and wine-glass transport results.
- **[Gym-Anything-RT](https://arxiv.org/abs/2610.37567)** — Real-time visual minigames for VLAs; GPT-6 Astra drops from 75% (paused) to 9% (real-time). Relevant to latency-aware embodied control.

## Briefly Noted (adjacent, not core)

- **[SFE-O](https://arxiv.org/abs/2610.37123)**, **[TeamGym](https://arxiv.org/abs/2610.37571)**, **[CogArena](https://arxiv.org/abs/2610.36484)** — ontology / team-decision / behavioral-experiment benchmarks; useful framing, not manipulation.
- **[Legislating World-Model-Based Planning with Legal Reasoning](https://arxiv.org/abs/2610.36824)**-adjacent work on normative robot control via defeasible deontic logic over a world-model planner; simulated arm on a grid.
- **[The Trinity](https://arxiv.org/abs/2610.36077)** — recursive self-improvement with Capability-Driven Real2Sim2Real; includes two real embodied tasks but is primarily an agent-evolution framework.
- **[Semantic World Models](https://arxiv.org/abs/2510.19818)** and **[Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588)** — both argue pixel-reconstruction objectives are the wrong target for control; the latter shows no current latent world model faithfully models dynamics.
- **[Evolving Agent Teams](https://arxiv.org/abs/2610.36848)** — mainly coding/kernel agents, but reports RoboDojo manipulation 62.1 vs. 55.3 best leaderboard entry.
- **[Edge-AI-Driven Learning-to-Rank](https://arxiv.org/abs/2605.16433)**, **[DIP-CAD](https://arxiv.org/abs/2609.22688)**, **[REACH](https://arxiv.org/abs/2610.36546)** — task allocation, CAD intent, humanoid crawling; the last is locomotion rather than manipulation.

Everything else in the input (RAG, quantized KV caches, medical imaging, recommendation, RLHF/GRPO variants, Lean formalization, water networks, astronomy, wind farms) is outside the embodied-manipulation scope and skipped.