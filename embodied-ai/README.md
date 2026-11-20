### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-20T14:21:02.775545
  - **arXiv update** 2026-11-20T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & AI Digest — Embodied Intelligence Focus

This batch is dominated by world-action models (WAMs) and VLA post-training tricks. Below, papers are grouped by theme; off-topic items are noted briefly at the end.

---

## 1. World / World-Action Models for Manipulation

- **MAWAM** — Multi-agent world-action model predicting teammates' views + action chunks jointly for coordinated multi-arm manipulation. 67.8% real-robot success, 90.3% sim. [Paper](https://arxiv.org/abs/2611.25105)
- **GEMS** — Generated subgoals + latent experience memory for long-horizon world-model planning; big gains on Cube/Push-T/Meta-World. [Paper](https://arxiv.org/abs/2611.25134)
- **MoRE** — Mixture-of-experts world model with rigid/deformable/prehensile motion experts, integrated with MPC. [Paper](https://arxiv.org/abs/2611.25336)
- **Verify2Act** — VLM proposes plans, latent world model + dual-head critic verifies before execution; trained in digital twin, 83.3% success. [Paper](https://arxiv.org/abs/2611.25243)
- **WEVO** — Post-trains humanoid VLA inside a video world model via RL; teleoperation-free. Success 23.3%→75.0% across three real tasks. [Paper](https://arxiv.org/abs/2611.25251)
- **ThinkWAM** — Proposal–rethink–refine loop with latent futures; 98.7% LIBERO, real-world OOD 64.4%. [Paper](https://arxiv.org/abs/2611.21258)
- **CoT-WAM** — Jointly trains VLM and WAM via learnable plan latents; SOTA on LIBERO/CALVIN/RoboCasa. [Paper](https://arxiv.org/abs/2611.23803)
- **AFFECT** — Trains world models to match action-effect distributions; real-robot success correlation 0.47→0.79 on DROID. [Paper](https://arxiv.org/abs/2611.25980)
- **PILOT / Fast-JEPA / LATER / SemRole / PhysVAM / ReactWorld** — Additional world-model planning variants (subgoal priors, low-latency predictive search, action-conditioned memory, semantic-role states, value-guided policies, structured interaction responses). [PILOT](https://arxiv.org/abs/2610.14335) · [Fast-JEPA](https://arxiv.org/abs/2611.25927) · [LATER](https://arxiv.org/abs/2611.25671) · [SemRole](https://arxiv.org/abs/2608.22294) · [PhysVAM](https://arxiv.org/abs/2611.26105)
- **World models favor learned priors over visual evidence** — TailWorld benchmark + RIFT; relevant to sim-to-real physics transfer. [Paper](https://arxiv.org/abs/2611.26366)

---

## 2. Vision-Language-Action: Training, Adaptation, Efficiency

- **RefreshGrad** — Online adaptive data sampling for diffusion VLA; LIBERO-Plus 60.7%→76.1%. [Paper](https://arxiv.org/abs/2611.25398)
- **Dune** — Zeroth-order optimizer for VLA test-time adaptation, memory-light, stabilizes long-horizon updates. [Paper](https://arxiv.org/abs/2611.25400)
- **WAMotor** — Speculative inference for WAMs exploiting dual nonuniform denoising; 2.86–4.28× speedups. [Paper](https://arxiv.org/abs/2611.25413)
- **CauSyncVLA** — Causal latent world model + flow warm-start for asynchronous control; 93.8% LIBERO-10 at 5× throughput. [Paper](https://arxiv.org/abs/2611.25667)
- **UniVEP** — Unifies velocity & endpoint prediction targets; 1-step inference beats 16-step baselines on RoboTwin. [Paper](https://arxiv.org/abs/2611.26103)
- **LoopedWAM / LAQ / RAVEL** — Compact looped WAM (elastic inference), latent-aware 4-bit quantization preserving predicted futures, asynchronous rolling inference for low-latency flow VLAs. [LoopedWAM](https://arxiv.org/abs/2611.25595) · [LAQ](https://arxiv.org/abs/2611.25614) · [RAVEL](https://arxiv.org/abs/2609.34170)
- **HSD (Hindsight Self-Distillation)** — Uses later frames as teacher; 98.5% LIBERO, 92.3% RoboTwin. [Paper](https://arxiv.org/abs/2611.25777)
- **Homeward** — Training-free observation adapter that re-canonicalizes bumped cameras back to training view; large gains across LIBERO-Plus camera variants. Directly relevant to deployment robustness. [Paper](https://arxiv.org/abs/2611.24455)
- **One View, One Action (OVOA-VLA)** — Per-view action supervision + cross-graph consistency; base-only inference 28.3%→58.3% under spatial shifts. [Paper](https://arxiv.org/abs/2611.26161)
- **A²-VLA** — Agentic affordance discovery for adapting VLAs to new tools; +30.7 pts over π₀.₅ on real tool-use. [Paper](https://arxiv.org/abs/2611.25656)
- **TipDex-VTLA** — Vision-tactile-language-action policy that gates touch-based action refinement by visual reliability; 73.8% under unseen lighting. [Paper](https://arxiv.org/abs/2611.25683)
- **TacInno** — Supervises VLA on "tactile innovation" (contact dynamics unexplained by vision+action); +10.7/+9.0 pts sim/real. [Paper](https://arxiv.org/abs/2611.26405)
- **SimVLA / VLA life-cycle survey** — Minimal controlled VLA baseline attributing gains to training dynamics; and an 89-paper survey of design/training/deployment axes. [SimVLA](https://arxiv.org/abs/2602.18224) · [Survey](https://arxiv.org/abs/2611.18372)
- **Flatness preserves instruction following** — SAM regularization during VLA fine-tuning; +55% instruction following. [Paper](https://arxiv.org/abs/2606.23641)

---

## 3. Long-Horizon Task Execution with Agentic Scaffolds

- **CoachSI** — Frozen VLM names the next subgoal (no actions); hindsight relabeling lifts unassisted long-horizon success 47.4%→59.3%. [Paper](https://arxiv.org/abs/2611.25529)
- **RoC (Reasoning on Call)** — Event-triggered LLM review over low-level policy; +24 pts RMBench, −65.3% tokens. [Paper](https://arxiv.org/abs/2611.26341)
- **PGX** — Predicate state machine + VLA skills + world-coordinate locking for humanoid loco-manipulation, trained-free temporal control. [Paper](https://arxiv.org/abs/2611.26596)
- **LeCompass** — Frozen JEPA + state-indexed execution interface with proposal/search/memory; 86.9% Cube, PushT 4.7%→44.9%. [Paper](https://arxiv.org/abs/2611.25679)
- **M4M** — Learns manipulation-aware mobility from frozen policy representations; goal-pose-free mobile manipulation, 47.0% on RoboCasa kitchens. [Paper](https://arxiv.org/abs/2611.25366)
- **TCR (Trajectory-Calibrated Regression)** — Gradient-free merging of embodied policies with execution-time calibration; beats FeatCal/RegMean/Wiener averaging on LIBERO. [Paper](https://arxiv.org/abs/2611.25575)
- **Unstick** — Diagnoses JEPA planner failures as fixed-point "stalls"; loop-breaking recovers most of the adaptation gain. Useful debugging insight for MPC-over-world-model pipelines. [Paper](https://arxiv.org/abs/2611.25415)

---

## 4. Grasping, Dexterity, Tactile & Contact

- **Evo-DexBench** — Few-shot dexterous manipulation benchmark (Shadow Hand, 123 taxels, VR teleop); best policy only 24.4% — a useful gap-finder for transfer. [Paper](https://arxiv.org/abs/2610.21180)
- **GLoTouch** — Global-to-local haptic search/recognition/grasp with a parallel gripper and no external vision. [Paper](https://arxiv.org/abs/2609.27695)
- **StableGrasp** — Differentiable-simulation optimization recovering physically stable human grasps (separates visual pose from grasp control). Relevant to grasp synthesis and hand-object modeling. [Paper](https://arxiv.org/abs/2610.09195)
- **MIR-Depth** — RGB-D depth completion for transparent objects; validated on 6-DoF grasp pose prediction. [Paper](https://arxiv.org/abs/2611.25417)
- **Contact complementarity tutorial / frictional contact LCP for continuum robots** — Background reading on friction/contact modeling (relevant to sim-to-real contact fidelity). [Tutorial](https://arxiv.org/abs/2611.26600) · [LCP](https://arxiv.org/abs/2611.18546)

---

## 5. Teleoperation & Hardware Interfaces

- **PUPPET** — VR teleop framework with synchronized replica + trial-validation pipeline; 27.7% faster than 2D teleop, more validation-ready trials. [Paper](https://arxiv.org/abs/2611.26350)
- **dVRK + Haply Inverse3 shared control** — Open-source ROS 2 haptic-shared-control framework for surgical teleop with virtual-fixture guidance. [Paper](https://arxiv.org/abs/2611.26485)

---

## 6. Sim-to-Real, Data & Training Infrastructure

- **Physical-Unified / "Rollout then Recycle"** — Releases 3,718 labelled real-robot episodes (7 policies × 12 tasks, 73% failures) on SO-101 arms. Valuable for failure-mode and reward-model work. [Paper](https://arxiv.org/abs/2611.03168)
- **LoongForge-Embodied** — Unified native-PyTorch training framework for heterogeneous VLA/WAM models; 1.47–4.38× throughput, egocentric→robot data synthesis pipeline. [Paper](https://arxiv.org/abs/2611.25460)
- **Ego2X** — Contact-centric (CORE) ego-video→robot retargeting; 62.9% of annotated contacts realized vs 27.9% prior; post-training X-VLA lifts RoboTwin 40.5%→67.0%. [Paper](https://arxiv.org/abs/2611.24138)
- **Awaken-HI** — 50k hours egocentric stereo video + whole-body motion; humanoid VLA with shared action expert, 93.75% across 8 tasks. [Paper](https://arxiv.org/abs/2611.26420)
- **HumanCOIN** — 12,500-hour intent-annotated egocentric manipulation dataset (gaze/EMG/EEG tiers). [Paper](https://arxiv.org/abs/2611.26434)
- **AgenticTask** — Agent-based scaling of RoboCasa task instances for synthetic data collection and policy evaluation. [Paper](https://arxiv.org/abs/2611.26046)
- **SimAudit** — Audits success checkers in RoboTwin/RoboCasa/RoboDojo; 61 defects (40 phantom successes, 21 silent failures). Important for anyone reporting sim success rates. [Paper](https://arxiv.org/abs/2611.25179)
- **GNetSS / MIR-Depth** — Self-supervised GNSS correction and transparent-object depth (navigation/sensing support). [GNetSS](https://arxiv.org/abs/2611.25665)
- **3D generation for embodied AI survey** — 3D assets/scenes as sim2real bridge; useful roadmap. [Paper](https://arxiv.org/abs/2604.26509)

---

## 7. Briefly Noted (Adjacent / Outside Core Themes)

- **Agentic manipulation policies (AMP1)** — Generalist AI model directly commanding manipulators, strong zero-shot results; relevant to the specialist-vs-generalist debate, though not a learned policy. [Paper](https://arxiv.org/abs/2611.09892)
- **SimVLA, FastRoverVLA, FlowDrive, UniAD-planner comparison, FedE2E, Compositional driving style** — Autonomous-driving planning; only tangentially embodied manipulation. [SimVLA](https://arxiv.org/abs/2602.18224) · [FastRover](https://arxiv.org/abs/2611.26242)
- **Quadruped/humanoid locomotion**: terrain-adaptive gaits, SuperMimic, ECHO, Skateboarding, LocoMuJoCo benchmark, Awaken-HI — locomotion-heavy; included only where it touches whole-body manipulation. [SuperMimic](https://arxiv.org/abs/2610.28480) · [LocoMuJoCo](https://arxiv.org/abs/2611.26293)
- **Humanoids & whole-body**: SixthSense (proprioception-only wrench estimation), ROAM (VLM+RL legged nav), FAB (body estimation/retargeting), spiking CPG control — mostly locomotion/estimation. [SixthSense](https://arxiv.org/abs/2605.01427)
- **Multi-robot/planning**: SCTD, SGLayout, CRAFT, RMRRT, Passage-conditioned navigation, multi-robot LiDAR registration — motion planning, not manipulation learning. [SCTD](https://arxiv.org/abs/2611.26127)
- **Sensing/perception for robots**: stereo VO, multiple-camera rigid tracking, event/radar calibration, UAV active capture — perception infrastructure. [SVO](https://arxiv.org/abs/2611.25445)
- **Medical/biology foundation models, LLM agents for science, EDA/RTL agents, security/watermarking, benchmark/LLM-evaluation methodology** — large remainder of the batch; outside embodied manipulation scope. Notable if you care about agent harness design: [Harness-Zero](https://arxiv.org/abs/2609.24974), [Insights Generator](https://arxiv.org/abs/2605.21347).

---

### Takeaway for your focus areas
Three clusters look most actionable: (1) **world-action models are the new default** for manipulation policy backbones (MAWAM, ThinkWAM, CoT-WAM, WEVO), with efficiency work (WAMotor, LAQ, LoopedWAM) arriving fast; (2) **test-time adaptation/deployment robustness** (Dune, Homeward, VG-Steer, VG-Steer-style steering) is being treated as a first-class problem distinct from training; (3) **tactile/dexterous data and benchmarks** (Evo-DexBench, TacInno, TipDex-VTLA, GLoTouch) still show low absolute success (≈24–88%), so dexterous transfer remains the weakest link. Sim-audit findings (SimAudit) are worth reading before trusting any benchmark number cited above.