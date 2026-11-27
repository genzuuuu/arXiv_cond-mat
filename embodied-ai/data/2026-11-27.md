### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-27T15:35:04.881422
  - **arXiv update** 2026-11-27T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Digest: Embodied Intelligence & Robotic Manipulation

Below, only papers relevant to the target themes are summarized in detail. Papers outside those themes are noted briefly at the end. Several items are relevant mainly as tools or context for manipulation (sim-to-real, VLA, world models), so they are grouped accordingly.

---

## Robotic Hands, Dexterous Manipulation & Retargeting

**[DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data](https://arxiv.org/abs/2611.33579)**
A simulation pipeline that converts human hand-object demos into physically executable arm-hand trajectories. It places each clip within arm reach, solves an arm motion following the human hands, then corrects it in physics with residual RL. Produces ~5,200 clips per hand across four dexterous hands, expanded to ~65k trajectories / 325k episodes (~578 h). Tracks objects more accurately than floating-hand methods at >10× lower runtime; policies trained on this data outperform those trained without physics correction, including on a real robot.

---

## VLA Policies, World Models & Test-Time Adaptation

**[Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2611.33993)**
World-model-guided VLA that predicts object motion + positional uncertainty, proposes bounded arm corrections from history-vs-action-conditioned forecaster discrepancies, and learns a Reliability Gate to admit corrections when they beat the base action. ~2.45M trainable params. 56.72% success vs. 45.44% reproduced DynamicVLA on the DOM benchmark.

**[Best-of-N Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](https://arxiv.org/abs/2611.33398)**
Shows more samples in best-of-N steering don't guarantee better VLA behavior when the verifier is inaccurate; selected candidates can exploit verifier prediction errors (reward hacking). Studied on 60 LIBERO-Safety cases with a π₀.₅ policy and a MuJoCo verifier with controlled errors. Verifier calibration and softmax selection help in some settings.

**[RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)**
LLM reasoning agent supervises a robot policy via an instruction channel (what to do) and a feedback channel (how to move), trained with agent-labelled DAgger. Handles mid-episode goal changes (e.g., "the milk, not the butter") and persistent drifts. LIBERO success 0.09→0.87 under unknown constant drift; 50 RoboTwin 2.0 tasks 0.12→0.74. Uses 55 s and 8k tokens per success vs. 2.1 min / >1M tokens for pure agent control.

**[RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)**
Infers an inverse-dynamics model from observed motion to correct commands at test time under invisible physics shifts (mass, joint weakness, lag), with hypotheses weighted by predictive fit. No reward, gradients, or new data. More than doubles average success across five frozen policies (27.8%→62.9%), +17.3 pts over best test-time adaptation baseline; joint-space RoboTwin 0.249→0.788.

**[HOG-WAM: Improving Visual Robustness through Future Gradient Prediction](https://arxiv.org/abs/2611.34811)**
Adds a training-only HOG DiT aux module to a world-action model for structural supervision from demo images; removed at inference. Improves RoboTwin-Plus mixed-noise success 78.86%→82.86%; Franka tasks 40%→59% clean, 17%→24% noisy.

**[Sparse-WAM: Accelerating World Action Models via Action-Guided Sparse Imagination](https://arxiv.org/abs/2611.33984)**
Training-free, action-guided token selection for joint denoising in WAMs, with cross-step reuse of selections. ~2.0× / 1.8× speedups on LIBERO (FastWAM-Joint) and RoboLab-120 (Cosmos 3 Edge) on an RTX 4090.

**[RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies](https://arxiv.org/abs/2611.34864)**
Offline framework that uses an LM to pick per-window speedup profiles for demonstrations before fine-tuning, instead of fixed segment speedups. Better execution efficiency on LIBERO and RoboCasa-Kitchen; on a Franka Research 3, matches or beats accelerations while completing successful trials faster.

**[Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts](https://arxiv.org/abs/2611.28732)**
Maps one human video + current observations to future states and actions. Uses video-to-video generation to create aligned human contexts and an intra-task contrastive objective to prevent task-identity shortcuts. 83.5/100 average on six unseen Astribot S1 tasks; 69.5% on seven unseen RoboTwin tasks (+22.6 pts over Zero-WAM); transfers under layout/tool shifts.

**[Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform](https://arxiv.org/abs/2611.33772)**
Splits checkpoint loss into sensing / latency / distribution gaps, with feasibility gates (sensor contract, end-to-end latency) that no benchmark score can override, plus probes, ranking, and closed-loop monitored fine-tuning. On a full-scale vehicle, an added camera repaired a failed sensing gate, latency gate removed the two top-scoring candidates, and the selected model passed 4/5 closed-loop trips.

**[FLUENT: Practice Makes Fluent — Learning to Use Earlier Predictions in Looped Models](https://arxiv.org/abs/2611.33722)**
Trains looped models to exit earlier via distillation to a frozen teacher plus a compute-aware exit gate. Real-robot success 62.3%→74.6% with mean successful-episode time 69 s→31 s; also LIBERO and language gains at lower depth.

**[DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering](https://arxiv.org/abs/2611.34671)**
Coding agents + generative rendering synthesize photorealistic, physically grounded demonstrations: agent-written interaction programs in simulation, then a video renderer to close the visual gap. Policies beat raw-simulation training and approach equal-count real-demo training.

**[RoboEvo²: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)**
Alternates policy→harness evolution (agent writes Code / Code+ICL / Code+Policy routes, consolidates skills) with harness→policy evolution (SFT + Counterfactual Preference Distillation). LIBERO-PRO standalone 11.0%→84.1%, hybrid 30.4%→90.5%; 95.0% hybrid on Unitree G1-D.

**[A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models](https://arxiv.org/abs/2611.34698)**
Inserts task-relevant entities into reconstructed scenes to target absent scenarios, builds a failure map across conditions, and allocates generation quotas each round. Occluded-pedestrian collision-free rate 0.261→0.579 (AutoVLA) / 0.390→0.765 (ReCogDrive); stop-sign yield 0.100→0.897. Real-vehicle gains without real-world training.

**[OmniAct: One Policy, One Million Embodiments](https://arxiv.org/abs/2611.33158)**
Cross-embodiment flow-matching policy conditioned on a kinematic graph tied to visual observations, predicting per-node relative joint motions. Trained on 1M procedurally designed embodiments. 63.0% on 2,000 held-out embodiment-scene episodes vs. 17.8% for π₀.₅ and 57.9% for the strongest baseline; ~2× the success of the next-best method on a novel real robot. Learns morphology-specific strategies.

**[Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics](https://arxiv.org/abs/2611.34644)**
Representation world model that jointly predicts future DINO features and 3D object flow, with asymmetric noise schedules. Beats pixel-based baselines on 3D flow accuracy and unseen-scene generalization; needs only three denoising steps.

**[Learning World Models through Contrastive Identification of Actions](https://arxiv.org/abs/2611.32776)**
CIA replaces inverse-dynamics regression with contrastive action identification among history-conditioned alternatives. Improves planner mean success across five visual control benchmarks without changing the planner.

**[Long-Horizon Planning with Latent World Models via Graph Anchors](https://arxiv.org/abs/2611.34509)**
Diagnoses two latent-distance failures (directional signal loss far from goal; arm-vs-object weighting) and fixes both by planning to a nearby node on a sparse graph of recorded training frames. PointMaze-Medium 13%→85%, PointMaze-Large 8%→87%, Push-T 5%→71%.

**[EffectWAM: Learning Action-Grounded Effects for Robot Manipulation](https://arxiv.org/abs/2611.32053)**
World-action model with Effect (future-minus-anchor change), camera positional encoding, and Action Grounding on end-effector/gripper changes. Trained on >20k hours; executes actions without waiting for video synthesis. Consistent improvement across benchmarks (8B and 26B configs).

**[Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](https://arxiv.org/abs/2611.33925)**
Shows pretrained action-conditioned world models are weak off the "happy path," then adds a 62k-trajectory perturbation dataset plus Interaction Alignment and Surface Correspondence. Cosmos3 Nano object-motion error −28.2% (−35.0% unseen objects); action-divergence error −43.3%.

---
### Related items (world models / sim-to-real, less directly manipulation)
- **[Do We Still Need Reinforcement Learning When We Can Read the World Model?](https://arxiv.org/abs/2611.34656)** — LLM coding agents synthesize policies directly from readable environment source, matching/outperforming RL with far less experience.
- **[Not all world models can doubt: epistemic uncertainty in JEPA and RSSM world models](https://arxiv.org/abs/2611.34830)** — Controlled comparison of uncertainty propagation; RSSM attenuates deviations, JEPA passes them through.
- **[ε-WM: Error-Driven Dynamics Adaptation across Fast–Slow Timescales](https://arxiv.org/abs/2611.15215)** — Fast/slow adaptation for sudden unknown robot dynamics changes.
- **[WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](https://arxiv.org/abs/2611.34130)** — 300 tasks, 12K human annotations, six physical dimensions; most frontier world models struggle.
- **[Neural Fidelity Calibration for Informative Sim-to-Real Adaptation](https://arxiv.org/abs/2504.08604)** — Score-based diffusion calibration of simulator physics online during execution.

---

## Benchmarks, Data & Teleoperation

**[RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](https://arxiv.org/abs/2611.33390)**
90 MuJoCo tasks across six constraint types with privileged and real-sensor regimes. Coding agents (best: GPT-6 Astra in Codex) solve 86% privileged / 43% standard; four zero-shot VLA policies solve none of 18 one-arm puzzles. Object pose + part geometry together add the most (24%→60%).

**[RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time](https://arxiv.org/abs/2611.22138)**
36 long-horizon tasks controlling 4–16 arms in real time from camera images only, no ground-truth poses. Six models tested; adaptive agent systems complete 28/27 tasks at high cost (hours, >200M tokens), fixed systems are faster but token-heavy. No system is yet fast, cheap, and reliable.

**[BOP-Refer: Benchmark for Monocular 3D and 2D Object Grounding](https://arxiv.org/abs/2611.34862)**
First benchmark for monocular 3D/2D grounding of everyday and industrial objects from 9 BOP datasets. Best model (Gemini 4 Carbon) gets 72.6% 2D AP but only 12.4% 3D AP; depth/scale estimation is the main error source.

**[PLAICraft: Large-Scale Time-Aligned Vision-Speech-Action Dataset for Embodied AI](https://arxiv.org/abs/2505.12707)** — 5,525 h of multiplayer Minecraft with millisecond-aligned video/audio/mouse/keyboard, plus an evaluation suite.
**[AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241)** — Multi-game VLA dataset with task/subgoal/skill hierarchy; 95.8% annotation pass rate on a 500-trajectory audit.

---
### Relevant adjacent benchmarks
- **[LUDIUS: Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions](https://arxiv.org/abs/2611.34328)** — 15 social skills; models struggle when reasoning over others' prior observations or competing interests.
- **[Reforge / WorldReforge](https://arxiv.org/abs/2611.33925)** — (covered above) manipulation-failure data for world models.
- **[RoboEvo²](https://arxiv.org/abs/2611.34675)** — (covered above) harness transfer across embodiments.
- **[MeterRouter](https://arxiv.org/abs/2611.34327)** and **[Parallel Subagents for Coding](https://arxiv.org/abs/2611.33893)** — agent orchestration; not manipulation.

---

## Grasping / Hand-Object Interaction (adjacent)

- **[CLUE: Find the Clue, Not the Scene](https://arxiv.org/abs/2611.34681)** — VLM entity recognition; not manipulation but relevant to instruction grounding.
- **[360UAV-ETrack / 360UAV-TVLA](https://arxiv.org/abs/2611.33934)** — omnidirectional embodied UAV tracking with a VLA; relevant to embodied policy design under partial observability.
- **[DemoFoundry](https://arxiv.org/abs/2611.34671)**, **[DexEngine](https://arxiv.org/abs/2611.33579)** — data pipelines for hand/arm manipulation (above).

---

## Datasets & Simulation Infrastructure (relevant)

- **[DosePET](https://arxiv.org/abs/2611.34008)** — medical dose dataset; out of scope.
- **[Vessel/aneurysm SynVA](https://arxiv.org/abs/2605.17620)** — out of scope.
- **[Kairos: Fast and Reliable Symbolic Task Planning for Autonomous Robots](https://arxiv.org/abs/2610.39454)** — PDDL task planner covering full language, packaged for ROS; relevant infrastructure for mobile manipulation.
- **[RoboAda / RoboThink](https://arxiv.org/abs/2611.30111)** — covered above.

---

## Topics Outside Scope (brief notes)

The remainder of the feed is not embodied manipulation / robotics. Notable clusters:

- **LLM agents & harness engineering:** Context scaling, partial routing, self-evolving agents, memory systems, multi-agent security, coding-agent studies, verifier/critic methods, tool-use benchmarks.
- **Math, reasoning & benchmarking:** Lean formalization, proof corpora, math competitions, reasoning-trace mining, Puzzle bench.
- **Model internals & training:** SAE interpretability, LoRA factor effects, distillation, quantization, routing, attention variants.
- **Security & safety:** Prompt injection, adversarial attacks, poisoning, watermarking, T2I provenance, deepfakes, jailbreaks.
- **Science & medicine:** Materials, genomics, clinical prediction, medical VLMs, imaging.
- **Systems/infra:** Serving, MoE routing, speculation, TEEs, quantum ML, telecom.
- **Social/policy:** AI labor impacts, political content, corporate disclosure, education programs.

If you want, I can expand any of those clusters into a full structured digest, or produce a cross-paper synthesis focused on, e.g., "test-time adaptation of frozen manipulation policies" (RoboAda, RoboThink, FLUENT, Aegis-VLA, Sparse-WAM).