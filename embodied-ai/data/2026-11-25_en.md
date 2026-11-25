### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-25T16:03:11.849842
  - **arXiv update** 2026-11-25T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & Embodied AI Roundup

A large drop. Below I've grouped the papers that matter for embodied intelligence, manipulation, dexterous hands, tactile sensing, VLAs, world-action models, teleoperation, and sim-to-real. Non-embodied papers are noted briefly at the end.

---

## 1. World-Action Models (WAMs) — the dominant theme this cycle

A striking number of papers revisit the "predict the future, then act" recipe: making it cheaper, more geometric, or more tightly coupled to action.

- **Hi3R-VLA** grounds vision, language, and action in a shared 3D point-cloud frame, with 3D-RoPE action-to-point attention. <250M trainable parameters, SOTA across RoboCasa/RLBench/RoboTwin2/DexJoCo/DexSuite including dexterous hands. [Hi3R-VLA: Grounding Semantics and Actions in 3D](https://arxiv.org/abs/2611.31535)
- **iWAM** asks whether you need to denoise a full future frame at all — conditioning the policy on intermediate features from a *single* video-model evaluation, via a learned bidirectional flow map. <[iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction](https://arxiv.org/abs/2611.33141)>
- **LeanWAM** compresses future representations into 32 predictive tokens from a frozen video generator; 25.1 ms per action chunk, 12–41× faster than representative WAMs. <[LeanWAM: Learning Latent World Action Models from Frozen Video Models](https://arxiv.org/abs/2611.31740)>
- **G0.7** scales a Fast-WAM along context (up to 5 min history) and pretraining data (teleop + human ego video); skips future-frame synthesis at deployment (60 ms/chunk, 7.6× faster than imagine-then-act). <[G0.7: Scaling Up a Fast World Action Model with Long Context](https://arxiv.org/abs/2611.31822)>
- **LoopedWAM** reuses a shared 6-block core recurrently per expert; elastic self-distillation gives one checkpoint with multiple accuracy–latency points. <[LoopedWAM: Looped World Action Models for Elastic Inference](https://arxiv.org/abs/2611.25595)>
- **ThinkWAM** adds a proposal–rethink–refine loop: correct future latents before a second action-head pass. <[ThinkWAM: Rethinking Latent Futures for Action Refinement](https://arxiv.org/abs/2611.21258)>
- **PreWAM** does a controlled study of prediction spaces and finds DINO-feature state-change supervision generalizes best under visual shift. <[PreWAM: Exploring the Design of Latent Future Prediction for World-Action Modeling](https://arxiv.org/abs/2611.31901)>
- **AG-WAM** adds explicit attention-guidance modules (content-adaptive, guidance-point visual, state-conditioned text) to a WAM. <[AG-WAM: Attention-Guided World Action Model](https://arxiv.org/abs/2611.32722)>
- **EffectWAM** predicts visual *change* relative to a shared anchor, plus camera-pose conditioning and end-effector "action grounding." <[EffectWAM: Learning Action-Grounded Effects for Robot Manipulation](https://arxiv.org/abs/2611.32053)>
- **DexWAC** unifies actor, action-conditioned world model, and bootstrapped critic in one pretraining stage; 75% real-world success vs 45% for π0.5. <[DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation](https://arxiv.org/abs/2611.32654)>
- **FoveaWAM** allocates precision by role: metric SE(3) trajectory for the target, sparse 3D flow for surroundings. Runs in 15.1 ms; introduces OnTimeBench for latency-aware eval. <[FoveaWAM: Role-Aware 4D World-Action Modeling for Dynamic Manipulation](https://arxiv.org/abs/2611.31705)>
- **PILOT** introduces a motion chain-of-thought to disentangle motion semantics from appearance in WAMs, improving data efficiency. <[Motion Chain of Thought: Disentangling Motion Semantics from Visual Appearance for Robotic Manipulation](https://arxiv.org/abs/2611.32241)

**Skeptical / diagnostic takes (worth reading):**
- **SimPWM** tests whether video world models actually follow a geometric proxy world; arm tracking is good, object state is partially ignored by some base models. <[Simulator-as-Proxy World Model for Robot Manipulation](https://arxiv.org/abs/2611.32786)>
- **Do Latent World Models Really Select the Right Actions?** finds the score is informative but unreliable — the top-scored candidate at end of search is no more likely to succeed than random at the released budget. <[Do Latent World Models Really Select the Right Actions?](https://arxiv.org/abs/2609.05461)>
- **RoboProbe / RP-Bench** measures physical plausibility of robot world-model videos with five law-specific metrics. <[RoboProbe: Benchmarking Physical Plausibility of Robot World Models](https://arxiv.org/abs/2611.32152)>
- **Occupancy world models** study: do they follow counterfactual actions? Proposes ReCast + a counterfactual action-faithfulness benchmark. <[Do Occupancy World Models Really Follow Actions?](https://arxiv.org/abs/2611.32029)>

---

## 2. Vision-Language-Action Policies

- **OmniAct** conditions directly on each robot's kinematic graph, trained on 1M procedurally generated embodiments; 63.0% on held-out embodiment–scene pairs vs 17.8% for π0.5. <[OmniAct: One Policy, One Million Embodiments](https://arxiv.org/abs/2611.33158)
- **WeaveVLA** explicitly models relative 3D relations via a task-conditioned sparse graph with recurrent edge states. Strong LIBERO-Plus and real-world OOD gains. <[WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2611.31126)
- **ConsisX** tackles cross-view incorrect association and fragmentation in multi-view VLAs. <[ConsisX: Cross-View Consistency Thinking in 3D for VLA Models](https://arxiv.org/abs/2611.30308)
- **SparQ4D** injects 4D structure via a query-based decoder attached to a pretrained policy, removable at inference (zero overhead). <[SparQ4D: Learning to Act through Sparse 4D Queries](https://arxiv.org/abs/2611.29682)>
- **TauPrune-VLA** — training-free, scale-adaptive visual token pruning; up to 1.86× speedup, validated on two real robots. <[Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for VLA Models](https://arxiv.org/abs/2611.31954)>
- **FAVLA** separates low-rate semantic reasoning from high-rate force-conditioned action refinement, with force-variance-scheduled inference. <[FAVLA: A Force-Adaptive Multi-Rate VLA Model for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2602.23648)>
- **Duo** splits each arm into its own action token per timestep, enabling cross-arm attention during flow matching. Improves all four base policies on RoboTwin 2.0. <[Duo: Towards Spatiotemporal Action Coordination in Bimanual Policies](https://arxiv.org/abs/2611.32108)>
- **ReGeoAnch** targets viewpoint generalization in RGB-only imitation learning via base-frame/ gripper-frame geometric anchors. <[Reading Geometric Anchors: Viewpoint Generalization in Imitation Learning](https://arxiv.org/abs/2611.32162)>
- **DRIFT** — one-phase visual RL with frozen pretrained vision encoders; avoids teacher-student distillation and transfers from rasterized sim. 58.8% relative real-world improvement. <[One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning](https://arxiv.org/abs/2611.31588)>
- **FAVLA**'s sibling in continual learning: **"Near-Zero Forgetting Is Not Enough"** shows OOD capabilities of Pi0 collapse under experience replay even when in-domain forgetting is ~0. <[Near-Zero Forgetting Is Not Enough](https://arxiv.org/abs/2611.31511)>
- **XIA (Cross-Instruction Anchoring)** preserves old-instruction responses by matching a frozen teacher on current observations, beyond expert replay. <[Beyond Expert Replay: Cross-Instruction Anchoring for Continual VLA Learning](https://arxiv.org/abs/2611.31903)>
- **PSG (Pathway-Separated Guidance)** — identifies "instruction shortcuts" overriding visual grounding in six VLAs and fixes it training-free. <[Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in VLAs](https://arxiv.org/abs/2611.32206)>
- **FLIPS/FluentAct/CALVIN-MAX** — three useful evaluation/diagnostic contributions: asynchronous handoff continuity (<[FluentAct](https://arxiv.org/abs/2608.13924)>), mid-execution change sensitivity (<[CALVIN-MAX](https://arxiv.org/abs/2611.31868)>), and instruction-fidelity benchmarking (<[RoboInF](https://arxiv.org/abs/2611.30555)>).

---

## 3. Agentic Manipulation & Skill Composition

An emerging cluster questioning whether generalist VLMs + code beat specialist policies at seams and boundaries.

- **Atomic Policy** composes learned skills via VLM-estimated symbolic state + PDDL planning + an agentic harness that steers each skill by language/visual pointing. <[Atomic Policy: Composing Atomic Manipulation Skills with Agentic Reasoning](https://arxiv.org/abs/2611.32813)
- **Skill Envelope** — a clever diagnosis: frozen VLAs rigidly retrace trajectories and collide with scene residue at seams. Measures each skill's 3D swept volume as a precondition, exposed as CHECK/FREE code tools. Lifts 3–4 step chains from 29.7% to 93.8%. <[VLAs Execute, Code Recovers](https://arxiv.org/abs/2611.32245)>
- **Boundary-Aware Policy Learning** shapes and expands a policy's "handoff boundary" so an agent can invoke it reliably. 98.4% on randomized RoboTwin 2.0. <[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238)>
- **On Agentic Manipulation Policies** makes the strong claim that generalist AI models commanding manipulators directly (AMP1) beat VLAs and WAMs: 85.6% zero-shot on RoboLab-120 vs 49.2%/42.9%, and 104/108 real-world trials. <[On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)>
- **Next-Manip** decouples executor allocation from costly agent inference via a lightweight invocation classifier. <[Next-Manip: On-Demand Agent-Policy Collaboration](https://arxiv.org/abs/2611.32533)>
- **RoboHarness-RL** trains compact open-weight VLMs as agents with tool calls via multi-turn RL and hierarchical memory (LiteHarness). <[RoboHarness-RL: Agentic RL for VLM-Based Robot Manipulation](https://arxiv.org/abs/2611.32016)>
- **Robo-Harness K1** gives VLM agents perception *as tools* (region grounding, calibrated depth, projected grasps). Lifts Gemini 3.7 Flash from 16.7% to 71.7% on LIBERO-PRO. <[Robo-Harness K1](https://arxiv.org/abs/2609.29389)>
- **MARGIN** converts successful rollouts into a "near-miss margin" risk signal; AUC 0.774 for predicting held-out failures. <[MARGIN: A Risk-Aware Agent for Robot Program Refinement](https://arxiv.org/abs/2611.32093)>
- **PyRUA-Dex** — coding agents develop dexterous *programmatic* policies with no demonstrations; learns piano and calligraphy in ~30 min. <[PyRUA-Dex](https://arxiv.org/abs/2611.33144)>
- **RESET** — one real demo → reconstructed verified world → self-improved white-box skill code → frozen deployment → transfer to unseen robots. 97% sim, 80% real. <[RESET: One Demonstration, One Verified World](https://arxiv.org/abs/2611.31894)>

---

## 4. Dexterous Hands, Bimanual & Tactile Manipulation

- **Ego2Real** — bimanual dexterous skill transfer from egocentric video + **tactile gloves**, with tactile-guided interaction reconstruction and contact-informed RL rewards. <[Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations](https://arxiv.org/abs/2611.32101)
- **HiMoDex** — hierarchical multimodal world-state pretraining fusing vision, tactile, force-torque, and **audio** on 1.19M synchronized timesteps; +32 points over strongest baseline on five real tasks. <[Many Senses, One World](https://arxiv.org/abs/2611.31782)>
- **ViTacLab** — ViTacSim (tri-modal tactile primitive: sparse contact-force lattice, dense force array, tactile images) + ViTacBench (parallel grippers, dexterous hands, bimanual) + ViTacPolicy. Cuts force RMSE substantially; 2,482 FPS at 256 parallel envs. Open challenge: purely tactile control remains hard. <[ViTacLab](https://arxiv.org/abs/2611.32476)>
- **Soft-Rigid Hybrid Hand** — five-fingered, 12 DoF, tendon-driven, self-contained compliance; 28/33 human grasp postures, plus position/task-space controllers and a teleop framework. <[Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers](https://arxiv.org/abs/2611.32582)>
- **Self-Sensing Compliant Hand** — series springs + potentiometers give joint state and finger force estimates with **no external sensors**; used for speed-dictated shared force control in VR teleop. <[Self-Sensing Compliant Anthropomorphic Hand](https://arxiv.org/abs/2611.32937)>
- **BendGS** — observation-conditioned Gaussian self-modeling for continuum robots; predicts next 3D shape, appearance, and tip pose from a virtual backbone, no joint angles needed. <[BendGS](https://arxiv.org/abs/2611.31844)>
- **Beyond Rigid Hands** — deforms rigid hand meshes onto contact for three published estimators; more than doubles skin-on-surface area while barely changing pose. <[Beyond Rigid Hands: Deforming Skin into Contact-Consistent Hand Meshes](https://arxiv.org/abs/2611.31950)>
- **RoMo Hands** — ~542K text-paired hand motion sequences (884 hours), with a 393-D bimanual representation and benchmark. <[RoMo Hands: A Large Scale Richly Organized Text to Hand Motion Dataset](https://arxiv.org/abs/2611.31766)>
- **DUALingo** — 271K task-conditioned, role-aware **bimanual** 3D affordance grounding tasks on 71K objects, fully auto-generated. <[DUALingo](https://arxiv.org/abs/2611.31919)>

---

## 5. Grasping, Contact & Sim-to-Real

- **VG-GP** — plug-and-play visuo-geometric GP memory for SE(2) residual grasp adaptation on frozen base policies; lifts unseen-object success from 38.6% to 53.4% with zero regressions. <[VG-GP: Uncertainty-Gated Visuo-Geometric Memory](https://arxiv.org/abs/2611.31826)
- **Co-DRIS** — physics-informed belief + variable-impedance catching; 66.6% under 10 coupled stress scenarios vs 27.6% for memoryless baselines. <[Co-DRIS](https://arxiv.org/abs/2611.31843)>
- **FabricBench** — bimanual deformable manipulation benchmark (Newton-based contact-driven solver, 10K assets). Best policy 77% avg, but ≤36% on long-horizon T-shirt folding and 6–14% under heavy initial deformation. Sim-to-real ordering preserved (ρ=0.94). <[FabricBench](https://arxiv.org/abs/2611.31577)>
- **Support2Sim** — Real2Sim from a single RGB image with an inferred support graph and physics-rollout pose refinement. <[Support2Sim: Visually Faithful Real2Sim with Stable Object Supports](https://arxiv.org/abs/2611.32727)>
- **RoboRecast** — agentic demonstration augmentation that preserves source interaction intent while re-targeting scenes/objects/embodiments. <[RoboRecast](https://arxiv.org/abs/2611.32622)>
- **Exact collision gradients for ellipsoids** — continuous collision detection on the Perram-Wertheim function; exact gradients at any step size for differentiable sim. <[Exact Collision Gradients for Ellipsoids in Differentiable Simulation](https://arxiv.org/abs/2611.31676)>
- **RoboPace** — online contact-aware time-optimal retiming for action-chunk policies (no retraining). <[RoboPace](https://arxiv.org/abs/2610.09696)>

---

## 6. Learning from Human Data, Corrections & Teleoperation

- **Learning from Human Corrections through Temporal Preferences** — uses both *when* and *how* humans intervene: pre-intervention preferences help correction forecasting, post-intervention preferences help goal inference. <[Learning from Human Corrections through Temporal Preferences](https://arxiv.org/abs/2611.31446)
- **EgoLoAF** — humanoid loco-manipulation learned entirely from egocentric demos with **no wearable trackers** and **no teleop data**; explicit hand-object affordances injected via cross-attention. 73.1 vs 74.4 task progress vs teleop, 4.03× data-collection efficiency. Releases 128,400 episodes / 1,000 hours. <[EgoLoAF](https://arxiv.org/abs/2611.32260)>
- **ActiveBridge** — learns human active perception priors (head motion to seek information) from egocentric video and transfers to a robot with only a head camera. <[ActiveBridge](https://arxiv.org/abs/2611.32098)>
- **Any2Act** — in-context robot learning where demonstrations are re-expressed in the *executor's* camera layout and action space; 57.5% zero-shot from one demo, beating VLAs fine-tuned on 50. <[Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations](https://arxiv.org/abs/2611.32353)>
- **MXI-MemICL** — treats demonstrations as retrievable memory with an intention predictor querying it. <[MXI-MemICL](https://arxiv.org/abs/2611.32564)>
- **KeyMemVLA** — subtask-guided sparse keyframe memory for long-horizon tasks, plus KMBench. <[KeyMemVLA](https://arxiv.org/abs/2611.32081)>
- **RoboDemo** — dual-cascaded test-time training reconciling demonstration intent with execution progress. <[RoboDemo](https://arxiv.org/abs/2611.32256)>
- **Exploratory Midtraining** — adversarial teleoperation data (β-Data) builds "connected behavioral coverage," improving data scaling laws and online finetuning. <[Exploratory Midtraining for Robot Policies](https://arxiv.org/abs/2611.33130)>
- **PICKER** — policy-intrinsic demonstration curation using forward passes only; matches performance-aware curation at retrieval-curation cost. <[Policy-intrinsic Demonstration Curation](https://arxiv.org/abs/2611.30099)>
- **XR teleoperation** — fixed dual-camera + LiDAR → vibrotactile feedback reduces cognitive load for obstacle avoidance. <[An XR-Based System for Enhanced Spatial Awareness in Mobile Robot Teleoperation](https://arxiv.org/abs/2611.32584)>
- **Keypose vs. dense action representations** — a careful controlled comparison; keypose is robust to demonstration perturbation but sensitive to executor mismatch. <[Keypose or Dense?](https://arxiv.org/abs/2611.32788)>

---

## 7. Benchmarks, Safety & Evaluation of Embodied Systems

- **FabricBench** (above) and **DeCoNav-Act** — 500 multi-robot mobile manipulation tasks testing *usable handoff states*, not just task allocation. All methods fail badly with weaker models. <[DeCoNav-Act](https://arxiv.org/abs/2611.32683)>
- **MRBench** — "physical necessity reasoning": which robots does the task actually require? Proposes MRScissors (85.4%/91.2% team-selection accuracy). <[MRBench](https://arxiv.org/abs/2611.32803)>
- **EmbodiSafety** — 1,092 snapshot + 540 trajectory tasks; six response modes including recovery vs. human escalation. Frontier model only 56.1%/61.5% complete decision accuracy. <[EmbodiSafety](https://arxiv.org/abs/2611.33054)>
- **RoboClock** — time-aware manipulation benchmark (60 tasks) with latency-aligned evaluation; best method only 8.3% temporal success on Easy. <[Roboclock](https://arxiv.org/abs/2611.32233)>
- **Embodied AI Fails the Mirror Test** — a simple mirror drops success 10.8–56.7 points across five policy families, largely *without* robot–panel contact. Phantom targeting of reflections. <[Embodied AI Fails the Mirror Test](https://arxiv.org/abs/2611.33010)>
- **ROAM-Bench** — embodied active spatial intelligence via evidence verification; exposes "correct outcome, unmet requirements" failures. <[ROAM-Bench](https://arxiv.org/abs/2611.33143)>
- **ICLWorld** — in-context learning from digital to physical; robot-use success is far below computer-use (26–27% vs 76–82%). <[ICLWorld](https://arxiv.org/abs/2611.32649)>
- **RoboValue** — fine-grained sim-and-real benchmark for robotic value models; strong progress scores coexist with poor regression detection. <[RoboValue](https://arxiv.org/abs/2610.26663)>
- **Sparse Poison, Strong Hijack** — trajectory-level VLA backdoors with only 1% poisoning (86.4% target success on OpenVLA-OFT). <[Sparse Poison, Strong Hijack](https://arxiv.org/abs/2611.32304)>
- **Embodied Neuro-symbolic AI** — position paper on auditable, machine-checkable robot behavior via knowledge-guided perception + constraint-aware planning. <[Embodied Neuro-symbolic AI](https://arxiv.org/abs/2611.31488)>
- **CALVIN-MAX** (above) and **RoboClock** together make a nice "temporal/change robustness" pairing.

---

## 8. Foundation Models & Generalist Control

- **DynaMimic** — physics-informed differentiable world model for humanoid motion tracking; predicts contact wrenches and residuals, then closed-form Lagrangian forward dynamics. −18.6% MPJPE vs SuperMimic; real A3 humanoid demos (cartwheel, vault). <[DynaMimic](https://arxiv.org/abs/2611.32944)>
- **DiffGR00T** — execution-aware differentiable training for humanoid whole-body VLAs, backpropagating through a frozen controller via a learned world model. +12.5 points on HumanoidArena. <[DiffGR00T](https://arxiv.org/abs/2611.32665)>
- **Ada-BFM** — lightweight adapters adapt pretrained behavior foundation models to scene interaction while preserving whole-body competence. <[Ada-BFM](https://arxiv.org/abs/2611.31863)>
- **EvoMisty / EvoMisty-style** — **EvoMisty** (social robot capability evolution via coding agents) is more of an agentic-software result than a manipulation paper, but shares the "verified capability library" pattern seen in RESET and Atomic Policy. <[EvoMisty](https://arxiv.org/abs/2611.31341)>
- **Grasp/retargeting note:** **DAA for delivery drones**, **flying-wing geometric control**, **AGV formation control**, **UAV SLAM/VIO**, and **aerial formation planning** are aerial/mobile-robotics papers; I've kept them out except where they touch manipulation.

---

## Briefly noted (outside core themes)

Speech/audio, NLP/agents-in-software, LLM evaluation, medical imaging, chemistry/protein/biology, hardware/compilers for LLMs, diffusion image/video generation, interpretability, and theory (optimization, generalization, math) papers make up the large remainder. A few that touch embodied or robot-learning infrastructure:

- **ICS** / cognitive architectures for agent simulation — relevant only if you study human-behavior modeling. <[COGENT](https://arxiv.org/abs/2611.31559)>
- **EmbodiedStudio** — task-driven sim generation with closed-loop verification, yielding both environment-authoring and policy-learning data. <[EmbodiedStudio](https://arxiv.org/abs/2611.32534)>
- **CrafterDojo** — lightweight foundation-model ecosystem for open-ended embodied agents. <[CrafterDojo](https://arxiv.org/abs/2508.13530)>
- **LocoMuJoCo** — imitation/RL benchmark for whole-body control with sim-to-real deployment repo. <[LocoMuJoCo](https://arxiv.org/abs/2611.26293)>
- **BARE** — body-aware reflexive evasion for humanoids, using local body adjustments rather than whole-body displacement. <[BARE](https://arxiv.org/abs/2611.32642)>

---

### Three threads worth following

1. **The "fast WAM" convergence.** iWAM, LeanWAM, G0.7, LoopedWAM, and FoveaWAM all independently conclude that *full future-frame generation is unnecessary at deployment* — the value is in the training signal. Expect consolidation around latent/token-level prediction with removable decoders.

2. **Agentic orchestration meets policy boundaries.** Atomic Policy, Skill Envelope, Boundary-Aware Policy Learning, and "On Agentic Manipulation Policies" are converging on the same insight from different directions: the hard problem is the *interface* between a reasoning agent and a frozen policy, not either component alone. The Skill Envelope paper's finding that frozen VLAs rigidly retrace trajectories is the sharpest diagnosis here.

3. **Tactile benchmarks are maturing but tactile control isn't.** ViTacLab, Ego2Real, and HiMoDex (with audio!) are building the data and simulation infrastructure, and ViTacLab is honest that purely tactile-dominant tasks still have low absolute success.