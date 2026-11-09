### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-09T14:20:19.649136
  - **arXiv update** 2026-11-09T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Digest — Embodied Intelligence & Manipulation

A large batch today. I've grouped the relevant work by theme; papers on language/VLM safety, serving infra, RL theory, etc. are noted briefly at the end.

---

## 1. Vision-Language-Action Models & Generalist Policies

- **[Meituan-Robotics-0](https://arxiv.org/abs/2611.08577)** — VLA foundation model for desktop manipulation: 147M VLM samples + 15k hours of robot data over 12 embodiments; discrete action-token pretraining → flow-matching mid-training → real-robot post-training. Introduces "Rollback" for CFG-DAgger and an event-driven agent for task resumption. 93.6% on RoboTwin 2.0.
- **[A2-MEAS / A2-WLA](https://arxiv.org/abs/2611.09124)** — Agentic embodied framework using "code as scaling interface" with a MetaBrain that distills correction codes into policy weights. 0.6411 Q-score on BEHAVIOR 2026; RoboTwin 2.0 93.98–95.05%; 57.92% vs π0.5's 26.67% on 12 real tasks.
- **[Open-HumanWAM](https://arxiv.org/abs/2611.06817)** — Open recipe scaling egocentric human video pretraining to 50k hours; reports a log-linear scaling law from human pretraining hours to robot success. HumanWAM-Goal reaches 92.70% Clean2Clean / 84.60% Clean2Random on RoboTwin 2.0, with emergent in-context adaptation on hardware.
- **[VICTR](https://arxiv.org/abs/2611.08698)** — Progress-conditioned retrieval for in-context learning in VLAs; raises unseen-task success from 6.2% → 23.8% over a fine-tuned π0.5.
- **[PRISM](https://arxiv.org/abs/2611.08917)** — Skill retention via a bank of low-rank action-expert adapters + a VLM-conditioned per-chunk router. 56.43% atomic / 20.00% composite on RoboCasa365.
- **[ODEAction](https://arxiv.org/abs/2611.09672)** — Replaces action-chunk prediction with a learned ODE action-transition field, avoiding chunk-boundary discontinuities; gains especially on fine manipulation.
- **[SURE](https://arxiv.org/abs/2611.09684)** — Data-efficient VLA training with a probabilistic action decoder (spatial uncertainty) + Soft-DTW temporal alignment; matches baselines with 10% of demos.
- **[STAR](https://arxiv.org/abs/2611.09409)** — Training-free inference: EMA over late-layer residual updates + proprioception-gated mixing to restore visual grounding; +4.0 pts average.
- **[ActPrune](https://arxiv.org/abs/2611.08827)** — Training-free visual token pruning driven by the *previous* action chunk's geometry, applied before the vision encoder. Up to 1.61× speedup, 59.5% FLOP reduction.
- **[Real-Time Execution with Autoregressive Policies](https://arxiv.org/abs/2611.13355)** — Shows autoregressive VLAs can meet strict latency via tokenization-horizon adjustment + constrained decoding; beats matched flow-matching policies.
- **[VLA Handover](https://arxiv.org/abs/2611.08987)** — Switches small on-robot VLA → server VLA only on predicted failure; +11–22 pts success with 49–77% fewer server requests.
- **[HiMEM](https://arxiv.org/abs/2611.09355)** — Hippocampus-inspired memory consolidation/pruning/composition for VLA in 3D scenes; lifts π0 from 91.88% → 98.20% on LIBERO.

---

## 2. Dexterous Hands, Grasping & In-Hand Manipulation

- **[RevoSim](https://arxiv.org/abs/2611.08939)** — Multimodal tactile simulator for the BrainCo Revo3 hand, jointly modeling 285 piezoresistive taxels + 5 visuotactile fingertips; up to 4,096 parallel envs on one RTX 5090. Trains in-hand manipulation and grasping policies in sim.
- **[DexHOT](https://arxiv.org/abs/2611.05119)** — Frames dexterous manipulation as hand-object *configuration transfer* (hand articulation + object pose relative to wrist). 80.5% seen / 69.4% unseen on a 120-object benchmark; 61.5% over 200 real transfers.
- **[DexTeleop-0](https://arxiv.org/abs/2616.23431)**: bimanual dexterous teleoperation with ego-centric perception, adding tactile-driven contact-force corrections on top of human tracking commands (91% Ball Assembly, 62% Stir in Cup in sim replay).
- **[NoContactNoWorries](https://arxiv.org/abs/2616.24450)** — Infers binary contact from RGB-D + proprioception as a pseudo-tactile signal, supporting RL for in-hand reorientation and generalizing to novel objects.
- **[BLaFA](https://arxiv.org/abs/2604.08410)** — Maps open-vocabulary instructions → 3D functional affordance keypoints → dexterous grasp poses for tool use.
- **[HOC2R](https://arxiv.org/abs/2611.08920)** — Extracts hand-object contact trajectories from human video (DINOv3 + SAM 2.1) for human-to-robot motion transfer; ~10.46 px mean localization error.
- **[HaNDF](https://arxiv.org/abs/2611.08578)** — Object-conditioned neural distance fields over hand articulations; a geometric prior for pose refinement, occlusion-robust reconstruction, and manipulation synthesis.
- **[Grasp-TAGS](https://arxiv.org/abs/2611.09864)** — Distills a PPO critic into a grasp-utility network to pick grasps by downstream task value before contact; 89.84% vs 79.87% for best fixed-grasp policy.
- **[Auditing Grasp Feasibility Predictors](https://arxiv.org/abs/2611.09130)** — ⚠️ Important negative result: eight grasp-feasibility predictors drop from 0.92–0.996 AUROC to *chance* (0.47–0.50) under planner-verified counterfactual obstacles. They aren't using the geometry the planner checks.

---

## 3. Tactile & Contact Sensing

- **[RevoSim](https://arxiv.org/abs/2611.08939)** *(see above)* — the main tactile-sim contribution today.
- **[MDF++](https://arxiv.org/abs/2611.09293)** — Visuo-tactile world-action model with *end-to-end* (not frozen) representation learning; multi-task cross-modal strategy avoids feature collapse. Up to 50% better than frozen-encoder WAMs on contact-rich tasks (bolt screwing, nut mating).
- **[CompVLA](https://arxiv.org/abs/2619.23614)** — VLA that jointly predicts motion *and* a stiffness matrix, executed via geometric impedance control; targets contact-rich tasks where kinematic-only VLAs degrade.
- **[Cross-Point Resistive Array Readout](https://arxiv.org/abs/2611.09059)** — Time-domain optimization instead of frequency-domain readout for dense tactile arrays; 24.6% lower mean error, 77.6% lower std over 1,000 trials.
- **[Optoelectronic Soft Suction Cup for Kiwifruit](https://arxiv.org/abs/2611.09468)** — Compliant gripper with optical force estimation (R² ≈ 0.968, MAE 0.138 N).
- **[Continuum Robot Contact Localization](https://arxiv.org/abs/2611.09877)** — Proves contact location is structurally unidentifiable from tendon measurements alone (null space ≥ 7); a constrained MHE with known obstacle geometry recovers 0.9 mm / 0.22 N.

---

## 4. Learning from Human Data, Teleoperation & Intervention

- **[Q-OIL](https://arxiv.org/abs/2611.08576)** — Key empirical finding: simulated human-intervention models don't match real users (people intervene on *progress stalls*, and corrections are suboptimal). Introduces a progress-based intervention model + optimistic exploration with decoupled critics; 10–50% higher success and improves pretrained VLAs on two bimanual tasks.
- **[DexTeleop-0](https://arxiv.org/abs/2616.23431)** *(see above)*.
- **[Sketch-MoMa](https://arxiv.org/abs/2412.19153)** — 2D hand-drawn sketches as teleoperation instructions for mobile manipulators, parsed by VLMs; 7 tasks, 5 sketch shapes, 14-participant user study.
- **[VOMMI](https://arxiv.org/abs/2610.08220)** — Portable RGB demonstration collection for mobile manipulation; VO-conditioned tokens injected only into the base branch. 18.2% lower base-velocity error; +8.3 pts over OpenPI 0.5.
- **[ToolDex](https://arxiv.org/abs/2611.09036)** — Large ego-exo dataset of creative physical tool use, with annotations for hands, tools, targets, and deformable interactions; benchmark suite for reasoning, 3D/4D reconstruction, and policy learning.
- **[Wearable Haptic I/O with Personalized Perception Models](https://arxiv.org/abs/2611.09708)** — 36-channel electrotactile array + capacitive sensing; learns per-user perceptual models and demonstrates personalized haptic rendering in robot teleoperation.

---

## 5. Simulation, Sim-to-Real & World Models

- **[Lodos-v2](https://arxiv.org/abs/2611.08868)** / **[Lodos](https://arxiv.org/abs/2611.08872)** — GPU rigid-body sim specialized for detailed mesh-mesh contact; solves the *exact* frictional contact problem via cascaded convex relaxations in primal form. ~10× throughput vs established simulators in the mesh-mesh setting.
- **[RevoSim](https://arxiv.org/abs/2611.08939)** *(see above)*.
- **[ForPC](https://arxiv.org/abs/2611.08664)** — Force-aware whole-body control for humanoid cart pushing; infers force/state latents from onboard sensing (no F/T sensors), transfers zero-shot to Unitree G1, pushes 30 kg at 0.5 m/s.
- **[DKWBC](https://arxiv.org/abs/2611.09605)** — Decouples motion tracking (inverse dynamics feedforward + PD) from balance (learned residual torque); one balancing policy generalizes across motion datasets, payloads, and physical interaction.
- **[SUGARv2](https://arxiv.org/abs/2611.09266)** — Synthesizes interaction references from task templates, then distills privileged teachers into visual humanoid loco-manipulation policies; 91.0% mean sim success with real transfer.
- **[Autonomous PIV via Zero-Shot Sim-to-Real RL](https://arxiv.org/abs/2611.09679)** — RL agent controls a 6-DoF camera to frame hydrofoil wakes in a water tunnel; trained entirely in CFD-backed photoreal sim, ~half the time of a full scan.
- **[EGT](https://arxiv.org/abs/2611.09270)** — Execution-grounded traversability as a *distribution over closed-loop trajectories* (latent flow matching); cuts safe-path rejection to 2.2% and navigation failures by 24–42 pts. Zero-shot sim-to-real.
- **[CLAW](https://arxiv.org/abs/2606.04130)** — End-to-end latent action world model from action-free video via adversarial latent regularization; supports imitation from observation and planning.
- **[FRED](https://arxiv.org/abs/2610.30320)** — Self-distills future video representations in a *single* denoising step for world-action models; 50.0% success on human-video-only tasks vs 19.4% for best competing WAM.
- **[WorldBridge](https://arxiv.org/abs/2610.40748)** — Studies video vs action supervision for task transfer: OOD video-only → 55.90%, plus one action-labeled demo per task → 70.70%. 96.23% on RoboTwin 2.0.
- **[LAG-Fusion / MATE](https://arxiv.org/abs/2607.17257)** — Latency-aware asynchronous composition of diffusion policies (e.g., low-rate vision + high-rate force), with a reference-frame rebasing rule for relative actions.
- **[CS-Pi](https://arxiv.org/abs/2611.08654)** — Inference-time constraint satisfaction for flow policies via draw-project-renoise; 81% safe success on a 7-DoF shelf task, 55% on hardware vs 40% for pure projection.

---

## 6. Agentic Manipulation & Planning

- **[On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)** — Provocative: a generalist AI model commanding the manipulator directly ("AMP1") beats specialist VLAs/WAMs — 85.6% zero-shot on RoboLab-120 vs 49.2%/42.9%, and 104/108 real-world trials. No demonstrations, no task-specific training; agents invent strategies (searching for hidden objects, using tools, self-calibrating cameras).
- **[Computer-Use Agents Are Embodied Generalists](https://arxiv.org/abs/2611.09847)** — Argues embodied tasks can be cast as software interaction: a single CUA design won 1st/2nd/3rd/6th across four ECCV workshop competitions with no competition-specific tuning.
- **[A Controlled Study of Agentic Robotics](https://arxiv.org/abs/2611.09030)** — 9 tasks, 631 configs, 28K rollouts. Bottleneck isn't information access but *interpreting* it into the right policy update — failure attribution and spatial/geometric reasoning matter most.
- **[A2-MEAS](https://arxiv.org/abs/2611.09124)** *(see above)*.
- **[Behavior Graphs](https://arxiv.org/abs/2611.00405)** — Compresses deployment rollouts into an interpretable directed graph; 16/18 users preferred it to video, and it improves progress-prediction rank correlation by 22.9%.
- **[RoboFQE](https://arxiv.org/abs/2610.18699)** — Rollout-free policy evaluation from offline trajectories; preserves policy rankings where video world-model evaluators degrade on long horizons.

---

## 7. Humanoids, Locomotion & Whole-Body Control

- **[STRIDE](https://arxiv.org/abs/2611.08857)** — Learns humanoid locomotion from *acceleration* commands (IMU-only, no motion capture) using off-policy XQC + symmetry augmentation; walks in 14 minutes of samples, 81% fewer falls than ablations.
- **[DKWBC](https://arxiv.org/abs/2611.09605)** *(see above)*.
- **[ForPC](https://arxiv.org/abs/2611.08664)** *(see above)*.
- **[SUGARv2](https://arxiv.org/abs/2611.09266)** *(see above)*.
- **[COBRA Snake Robot Loco-Manipulation](https://arxiv.org/abs/2611.09777)** — Contact-implicit model unifying robot-ground/robot-object/object-ground contacts for whole-body pushing during sidewinding.

---

## 8. Datasets & Benchmarks for Embodied Evaluation

- **[ToolDex](https://arxiv.org/abs/2611.09036)** — ego-exo human tool-use dataset.
- **[HomeLoop](https://arxiv.org/abs/2611.08914)** — Isaac Sim framework for robot-IoT coordination in homes: 20 tasks, faulty sensors, evolving hazards; 2,100 auto-furnished layouts, 5 robot bodies. Best VLM scores 61.9%, with a clear over-reaction bias (prohibited interventions outnumber missed ones 2:1).
- **[Seeing What Matters](https://arxiv.org/abs/2611.09794)** — Benchmarks *task-conditioned actionable spatial belief*: 860 cases, >115k evaluator episodes. Reference pipeline hits 98.8%; seven VLMs reach only 26–43%.
- **[ManiTaskGen](https://arxiv.org/abs/2505.20726)** — Auto-generates comprehensive feasible manipulation tasks per scene for benchmarking and improving embodied decision-making.
- **[AtariBench](https://arxiv.org/abs/2611.08755)** — Spatiotemporal reasoning for VLMs over 20 Atari games; models fail to infer motion/direction and over-rely on text history.
- **[ObjView-Bench](https://arxiv.org/abs/2605.10707)** — Disentangles object complexity, planning difficulty, budget, and reachability in object-centric view planning; shows these change method rankings substantially.
- **[Flex-RSI](https://arxiv.org/abs/2611.08946)** — Benchmarks recursive self-improvement of agent *harnesses* on vision/robotics tasks under fixed budget.
- **[AceAction-5M](https://arxiv.org/abs/2611.04241)** — Multi-game 3D VLA dataset with hierarchical goals (task → subgoal → skill) and aligned KBM actions; 95.8% annotation pass rate.
- **[NormGym](https://arxiv.org/abs/2611.08613)** — Tests whether agents can *acquire unknown* social norms from interaction; best LLM hits 55.3% joint task+compliance.
- **[ABHBench](https://arxiv.org/abs/2611.09326)** — First-person moral decision-making from *Detroit: Become Human*; 75% of models shift significantly between text-only and multimodal versions.

---

## 9. Perception, SLAM & Sensing for Robots

- **[mmWave Human-State Sensing Limits](https://arxiv.org/abs/2611.08863)** — Cramér-Rao-style error floor for joint localization with compact arrays; second viewpoint drops error 97→65 mm, and a stronger estimator mainly just "completes" unresolvable joints. Good guidance on observation design vs estimator capacity.
- **[Polarization Calibration of Fisheye Cameras Using Skylight](https://arxiv.org/abs/2611.08911)** — Joint lens-analyzer calibration, 8 parameters, handheld outdoor sequence only; <0.5° AoLP MAE, demonstrated solar-heading estimation on a quadruped.
- **[DobotTrack](https://arxiv.org/abs/2611.09041)** — Target-grounded VLA for embodied person tracking; Q-identity compression of history tokens; 77.9% on EVT-Bench with 0.8B params.
- **[When to Trust the BIM](https://arxiv.org/abs/2611.09045)** — Identifiability-aware LiDAR-inertial-BIM fusion; abstains from attribution when as-built deviations are ambiguous. Conditional error 0.83% vs 31.67% for uncertainty-based abstention.
- **[TPS-A*](https://arxiv.org/abs/2611.09210)** — Certified collision checking over trajectory parameter space for arbitrary footprints; median 3 ms per query, 45% of hybrid A* paths overlap obstacles by comparison.
- **[FastFunnels](https://arxiv.org/abs/2611.09005)** — Multi-robot navigation via an RL-morphed "blob" formation + DMPC; 89% completion at 7.73 m/s vs baselines at ≤1.79 m/s.
- **[RADAR DOA for Quadrotors](https://arxiv.org/abs/2608.01855)** — mmWave radar + IMM tracker + CBF controller; 75 ms detection-to-avoidance, avoided all 39 untethered outdoor maneuvers at up to 5 m/s.

---

## 10. Cross-Cutting: Industrial & Applied Manipulation

- **[Learning-Augmented Robotic Automation](https://arxiv.org/abs/2604.22235)** — Deployed on an electric-motor line: deformable cable insertion + soldering, 5h10m continuous, 108 motors, 99.4% QC pass rate, no physical fencing, <20 min of real data per task.
- **[Augmentron](https://arxiv.org/abs/2611.09145)** — Geometry-aware, multi-view-consistent scene augmentation via reusable scene representations; replacing half the real data improves OOD distractor and workspace-variation success.
- **[Geometric Prior Pretraining](https://arxiv.org/abs/2609.12721)** — Auto-generates textureless plane/object/cube-hand scenes to pretrain ACT; higher early success with few demos across 3 sim robots × 5 tasks + 3 real tasks.
- **[Constraint Adherence / Goodhart in the Planner](https://arxiv.org/abs/2611.09670)** — ⚠️ Sampler-based MPC against preference-learned reward models *exploits* them: drawer-open succeeds 0/20 under human labels vs 10/10 for the cloned policy. Includes a theoretically grounded χ²-regularized fix.

---

## 11. Efficiency, Throughput & Infrastructure (brief)

Relevant to VLA deployment but not manipulation-specific: **[ActPrune](https://arxiv.org/abs/2611.08827)**, **[Real-Time Autoregressive Policies](https://arxiv.org/abs/2616.13355)**, **[Fused-Softmax attention](https://arxiv.org/abs/2611.09225)**, **[BitDecoding-FP4](https://arxiv.org/abs/2611.09825)**, **[FOSCAR](https://arxiv.org/abs/2611.09722)**, **[AdaFloor](https://arxiv.org/abs/2611.06984)**, **[TailSieve](https://arxiv.org/abs/2608.22788)**, **[GPU Kernel Library Issues](https://arxiv.org/abs/2611.09280)**.

---

## Skipped / out of scope (noted briefly)

Large volume of LLM-centric work today: prompt injection & jailbreaks, sycophancy audits, majority-vote TTRL, multi-agent debate, harness optimization (BOXBOX, HarnessMM, HarnessNet), RLVR variants (BNPO, RCEPO, Ordered Policy Optimization), weight-space programming, medical/clinical LLM evaluation, patent & fraud classification, federated learning privacy, mobile network PQC adoption, and general time-series/bio/audio ML. One borderline item: **[Autonomous Whole-body Loco-manipulation Using a Snake Robot](https://arxiv.org/abs/2611.09777)** is included above (§7) since it's a manipulation control result.

---

### Today's through-lines

1. **World-action models are consolidating** — MDF++, FRED, WorldBridge, CLAW, Open-HumanWAM all push the predict-future-then-act paradigm, with the key open question being representation quality (frozen reconstruction encoders vs end-to-end).
2. **Tactile simulation is maturing** — RevoSim's 285-taxel + visuotactile model at 4k parallel envs is a real infrastructure step for in-hand manipulation.
3. **Two uncomfortable negative results**: grasp-feasibility predictors fail counterfactual audits (§2), and preference-reward planners actively Goodhart (§10). Both suggest benchmark accuracy has been a poor proxy.
4. **Agentic manipulation is a serious challenger** — AMP1's zero-shot win over VLAs/WAMs on 104/108 real trials is worth reading in full, even if the framing is aggressive.
5. **Intervention data realism matters** — Q-OIL shows our simulated human models were wrong; that's a cheap fix with outsized impact for human-in-the-loop work.