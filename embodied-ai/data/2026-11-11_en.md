### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-11T12:57:18.430470
  - **arXiv update** 2026-11-11T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv: Embodied Intelligence & Robotic Manipulation

This batch is unusually heavy on non-robotics LLM/agent work (papers 112–365). I've grouped the ~30 papers that fall within the requested themes below, and briefly noted the rest at the end.

---

## Dexterous Manipulation, Robot Hands & Grasping

- **[OpenDexGrasp: Open-vocabulary Task-Oriented Dexterous Grasping](https://arxiv.org/abs/2609.18117)** — Couples open-vocab VLM context with a shared perception-action latent to generate task-consistent dexterous grasps directly (no separate affordance-to-pose stage). Ships a paired data recipe (OpenDexVerse) with teleop alignment.

- **[Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration](https://arxiv.org/abs/2607.00033)** — CHORD represents human and robot motion in an object-centric contact-wrench space to guide RL. Adds a 4,739-task bimanual benchmark; reports 82% success and real-world transfer.

- **[DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](https://arxiv.org/abs/2611.11166)** — Trains a depth-based world model to predict 3D hand-point motion, then distills it into policy latents so deployment needs only RGB. 49.4→60.5% on DexJoCo; modest real-robot gains (58.3% vs 50.0%).

- **[DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning](https://arxiv.org/abs/2611.14092)** — Turns human hand-object video into executable dexterous VLA training data via grasp-mode-preserving retargeting, arm trajectory augmentation, and RL finger control.

- **[Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817)** — 50K-hour egocentric corpus with a reported log-linear scaling law from pretraining hours to robot success. Joint human-robot pretraining reaches 92.7%/84.6% on RoboTwin 2.0.

- **[RoboACE: Adversarial Co-Evolution for Robot Self-Improvement](https://arxiv.org/abs/2611.13034)** — Alternately evolves a curriculum and execution harness around frozen foundation models; 74.0% on LIBERO-PRO. Borderline fit, but relevant to skill-learning loops.

---

## Visuomotor / VLA Policies

- **[LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning](https://arxiv.org/abs/2611.14048)** — Inserts an interaction-centric latent between world and action experts in a MoT architecture. 99.5% on LIBERO and SOTA on ten RLBench tasks; pretrained on 14k+ hours.

- **[FAME-QP / Elastic-WAM / MetaWAM]** — Three efficiency-oriented world-action model papers worth skimming: **[Elastic-WAM](https://arxiv.org/abs/2611.14257)** adaptively allocates future-denoising compute; **[From Video Frames to Robot Meta-Frames](https://arxiv.org/abs/2611.14365)** packs all robot signals into one frequency-domain latent frame (68.9% RoboCasa, 39% lower latency); **[APS-VLA](https://arxiv.org/abs/2611.13030)** learns action-guided visual token pruning (137→93 ms on dual-arm hardware).

- **[How Much of Your VLA Is kNN](https://arxiv.org/abs/2611.13160)** — Strong provocative result: pure retrieval of nearby demonstrations hits 91.7% on LIBERO with no policy training, and degrades least under LIBERO-Plus. Introduces a Local Action Consistency metric.

- **[How Many Demonstrations Does a VLA Need?](https://arxiv.org/abs/2611.09964)** — Sample-efficiency study across six VLAs; π₀.₅ needs 2–5× fewer demos than π₀. Freezing the VLM badly hurts π models but barely affects GR00T.

- **[Meituan-Robotics-0](https://arxiv.org/abs/2611.08577)** — Desktop-manipulation VLA foundation model (147M VLM samples + 15k hours, 12 embodiments) with a "Rollback" data recipe pairing replaced segments with human corrections. 93.6% RoboTwin 2.0.

- **[ODEAction: From Predicting Chunks to Evolving Actions](https://arxiv.org/abs/2611.09672)** — Replaces action chunks with an ODE-defined continuous action evolution to remove chunk-boundary discontinuities. Modular head, gains especially on fine manipulation.

- **[ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control](https://arxiv.org/abs/2611.13482)** — Shifts RL adaptation from action space to *how long* each chunk executes — a low-dimensional, practical trick for real-robot fine-tuning.

- **[XS-VLA](https://arxiv.org/abs/2607.04171)** — Compact (244M) VLA trained with spatial distillation + demonstration-conditioned flow matching; 90.25% LIBERO, 21.7→65.0% on Mobile ALOHA.

- **[A³-VLA](https://arxiv.org/abs/2611.06447)** and **[CIALLO](https://arxiv.org/abs/2611.13732)** — The former adds perception-guided attention alignment to fix visual shortcuts; the latter learns a shared cross-embodiment intent codec (76.7% on SO-101/Piper with 20 demos).

- **[Control-Aware Command Generation for Asynchronous Control and Action Inference](https://arxiv.org/abs/2611.11089)** — Treats discontinuous policy output as a tracking problem to make asynchronous inference fast and smooth. Useful systems paper.

---

## Teleoperation, Human Video & Demonstration Transfer

- **[A human-in-the-loop Control Paradigm for Construction Robotics](https://arxiv.org/abs/2611.14062)** — Structured transitions between VR teleop, shared control, and rule-based autonomy for dual-arm facade installation. Semi-autonomy wins under disturbance and cuts workload.

- **[Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos](https://arxiv.org/abs/2611.13685)** — SPAR adds future-visual-state prediction alongside action prediction; gains grow with video scale.

- **[RedirectMimic](https://arxiv.org/abs/2611.14049)** — "Local motion content redaction" for humanoid WBC: decouples the observed reference from the training target to suppress specific movements while keeping interfaces unchanged.

- **[HABIT: Human-Aware Behavior and Interaction Training Dataset](https://arxiv.org/abs/2606.31682)** — 10K+ episodes of human-*present* manipulation (Collaborator / Coworker / Supervisor roles). A genuinely underexplored data axis.

- **[When Should Agents Remember? / Don't Just Trust Your Memory](https://arxiv.org/abs/2611.14326)** — Not robotics, but the falsification-gated memory-update idea transfers cleanly to long-horizon manipulation agents; see also [WikiTrace](https://arxiv.org/abs/2611.14320).

---

## Tactile, Force & Contact

- **[Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects](https://arxiv.org/abs/2611.13268)** — Clean closed-form necessary-and-sufficient condition, (l₁+l₃−b)(l₂+l₄−a)<0, independent of CoM. Large tracking-error reductions in narrow passages.

- **[Learning Beyond Rigid Manipulation with Hybrid Soft-Rigid Robots](https://arxiv.org/abs/2410.07787)** — Series rigid+soft arm with tailored imitation learning; matches rigid baselines on stacking and enables grasping through narrow openings.

- **[Softness is something you also need!](https://arxiv.org/abs/2611.13779)** — Theoretical note on information metrics and phase-space volumes for compliant/passive-dynamic walkers. Niche but interesting if you care about morphological computation.

- Deformable linear objects (adjacent to contact-rich manipulation): **[SPiD](https://arxiv.org/abs/2602.03623)** (physics-informed self-supervised rope control, strong sim-to-real) and **[GPF](https://arxiv.org/abs/2611.14274)** (argues physical context should be judged by decisions, not prediction accuracy — a good methodological point).

---

## Sim-to-Real, Benchmarks & Evaluation

- **[Awomo-SimDataEngine](https://arxiv.org/abs/2610.02274)** — Agentic asset/scene/demonstration generation pipeline; co-training with Isaac Sim demos lifts a WAM from 77.2→89.4% on LIBERO-Plus.

- **[Evaluating Long-Horizon Robot Planning under Uncertainty](https://arxiv.org/abs/2610.17326)** — 1,350 Habitat episodes comparing ReAct, VLM-TAMP, Tru-POMDP, including the effect of *incorrect initial memory*.

- **[RoboRisk / LEASH](https://arxiv.org/abs/2611.14115)** — Safety benchmark (92 sim + 13 physical tasks) plus a gate harness that cuts harm across six foundation models with little overhead.

- **[Seeing What Execution Needs](https://arxiv.org/abs/2611.09794)** — Benchmarks task-conditioned *actionable spatial belief*; notable that seven VLMs top out at 26–43% under a full-preview contract.

- **[XS-VLA / Open-HumanWAM / DexSeed]** (above) all report sim-to-real or cross-simulator results.

---

## Adjacent Locomotion & Whole-Body (brief)

Humanoid WBC had several strong entries: **[SuperMimic](https://arxiv.org/abs/2610.28480)** (differentiable world model, >1000× GPU-hour reduction), **[DKWBC](https://arxiv.org/abs/2611.09605)** (decouples tracking via inverse dynamics + learned balance residual), **[OneSteer](https://arxiv.org/abs/2610.41354)** (one-step diffusion WBC with test-time steering), **[Pose Distance Fields](https://arxiv.org/abs/2602.04851)**, **[SSR](https://arxiv.org/abs/2605.30770)** (foothold imagination), and **[CLF-RL](https://arxiv.org/abs/2509.19573)** (Control Lyapunov function rewards for running). Also **[ReACT](https://arxiv.org/abs/2611.13929)** on velocity tracking under asymmetric hand loads — relevant if you do loco-manipulation.

---

## Outside Scope (brief)

The bulk of this batch is general LLM/agent work: benchmark and safety papers (papers 112–152), retrieval/memory systems (202–204, 315), reasoning and RL-for-LLM methods (254, 272, 282, 289, 317, 427), interpretability (281, 331, 410), and non-robotics applications (medical, legal, finance, chip design). A few may be worth a look if you need agent-infrastructure ideas — **[ReTrace](https://arxiv.org/abs/2611.14492)** (distilling tool-using agents into planner-free workflows) and **[Synapse-Control](https://arxiv.org/abs/2611.13615)** (lightweight runtime advice selection) — but none touch embodiment.

**Two things worth flagging across the robotics set:** (1) the retrieval/kNN result in paper 7 is a real challenge to how VLA progress is measured on LIBERO; (2) a recurring theme this batch is *distilling frozen world models into policy latents* (DexForesight, LaST0.5, MetaWAM), which looks like it's becoming the default recipe for injecting physical priors at deployment.