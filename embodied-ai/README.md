### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-10-28T11:38:09.098319
  - **arXiv update** 2026-10-28T04:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & AI Digest — Embodied Intelligence, Manipulation, and Policy Learning

Below is a curated summary focused on embodied intelligence, dexterous manipulation, tactile sensing, VLA/world-action models, teleoperation/data collection, and sim-to-real. Papers outside these themes are briefly noted at the end.

---

## 1. World-Action Models & World Models for Manipulation

**E0.5** builds a geometry-native world-action model directly on a 3D foundation backbone, predicting future 3D states plus actions (89.9%/50.1% on RoboTwin 2.0 clean/randomized; +15/+7 pts real-world after AgiBotWorld pretraining). [E0.5](https://arxiv.org/abs/2610.36011)

**Rollback** turns world models into counterfactual engines—rewinding to critical decision points, branching alternative actions—with distributed search + asynchronous real-robot execution (+10.7–11.9 pts over strongest baseline; surpasses human players in ≤8h). [Rollback](https://arxiv.org/abs/2610.36068)

**TAPESTRY** treats robot actions as single-patch tokens in a pretrained video diffusion transformer, avoiding test-time video generation (84 ms/action chunk; single DDIM step). [TAPESTRY](https://arxiv.org/abs/2610.36823)

**Trace-WAM** adds future 3D motion prediction as auxiliary supervision to video-action learning via a Tri-MoT architecture; clear gains over Fast-WAM under limited demos and distribution shift. [Trace-WAM](https://arxiv.org/abs/2610.36840)

**GAWM** shows a compact (<100M param) latent WAM on frozen DINOv3 features can beat billion-parameter WAMs on RoboTwin 2.0 and match billion-param VLAs on LIBERO, with much lower latency. [GAWM](https://arxiv.org/abs/2610.37091)

**RynnWorld-Latent** uses 3D-grounded universal latent actions as a shared conditioning interface, enabling joint pretraining on human videos, robot demos, and sim rollouts (553.5M frames across 23 datasets); synthetic mid-training improves LIBERO policies. [RynnWorld-Latent](https://arxiv.org/abs/2610.36791)

**World Dreamer v5-lite** is a multi-robot WAM with a shared workspace-coordinate world state and per-robot query streams (74.0% RoboFactory, 78.8% real-robot mean). [World Dreamer v5-lite](https://arxiv.org/abs/2610.37518)

**JAM (Just Action Model)** argues the VLA-vs-WAM debate bundles separable choices; a foresight loss on current-observation features (head discarded at inference) beats matched FastWAM/ImageWAM on LIBERO/LIBERO-Plus, with 73% lower training FLOPs. [JAM](https://arxiv.org/abs/2610.37219)

**MoGAP** shows spatially focused (motion-guided asymmetric) visual supervision improves WAM policies (GR-1 tabletop: 38.8→47.5% Fast-WAM; 52.3→62.3% Cosmos3-Nano). [MoGAP](https://arxiv.org/abs/2610.36624)

**SWIM** learns state-feature weights from inverse dynamics for JEPA world-model supervision; improves planning success on five manipulation tasks without extra test-time compute. [SWIM](https://arxiv.org/abs/2610.36662)

**Best-of-N for WAMs**: a denoised counterfactual protocol measures selectable headroom (standard estimates overstate it); a fail-gated selector raises closed-loop success 76.9→81.6% (seen) and 62.6→69.8% (unseen). [Best-of-N WAM](https://arxiv.org/abs/2610.37196)

**Two critical analyses**: *What Does World Modeling Actually Improve in Robot Action Learning?* finds future-video prediction boosts seen-task success but gains don't consistently survive distribution shift — and a lightweight auxiliary predictor works for π₀.₅ (82.94→89.19%) without a large video DiT. [Paper](https://arxiv.org/abs/2610.34593) • *Understanding the limits of latent world models* shows none of the SOTA latent world models actually learns faithful environment dynamics (LRC metric, equivariance framing). [Paper](https://arxiv.org/abs/2610.37588)

Also: **Semantic World Models** (predict task-relevant semantics instead of pixels, via VLM SFT). [Paper](https://arxiv.org/abs/2510.19818) • **Calibrated for Which Policy?** (conformal coverage under policy intervention; 55.0%→90.9% with ratio calibration). [Paper](https://arxiv.org/abs/2610.35877) • **LOPAL** (local performance-aware active learning from imperfect demos, +27.3% on pipe inspection). [Paper](https://arxiv.org/abs/2606.16888) • **Dwell** (VLM as latent transition operator for model-based RL). [Paper](https://arxiv.org/abs/2610.36925)

---

## 2. VLA Policies: Robustness, Safety, Failure Recovery

**R2A (Retrieve to Act)** treats OOD robustness as geometric motion-primitive graph retrieval, gating retrieved priors into frozen VLA actions—up to +12 pts in sim and +40 pts real-world, no fine-tuning (GR00T N1.7, π₀.₅, StableVLA). [R2A](https://arxiv.org/abs/2610.37215)

**AWARE** is a training-free, plug-and-play module retrieving observation evidence into FFN memory, weighted by action entropy and instruction attention; gains on LIBERO/SIMPLER/CALVIN/real. [AWARE](https://arxiv.org/abs/2602.18020)

**VLA-Stem** keeps the VLA frozen and adds an RL-trained "stem" policy that adapts execution to obstacles (52.8% vs 23.7% collision-free success on six constrained sim settings). [VLA-Stem](https://arxiv.org/abs/2610.37378)

**AFIL** (in *Tokens of Motion*) generates failure rollouts online and trains dual action generators, steering sampling away from failure-prone regions. [Tokens of Motion](https://arxiv.org/abs/2610.37330)

**RePO-VLA** assigns distinct roles to success/recovery/failure trajectories with a progress-aware value function; adversarial success 20→75% (up to 80% real). Introduces FRBench. [RePO-VLA](https://arxiv.org/abs/2605.09410)

**PDRVLA** extracts physical-dynamics tokens via future RGB/depth/flow prediction (with frozen video world-model supervision), no online video generation (99.3% LIBERO, 81.5% SimplerEnv). [PDRVLA](https://arxiv.org/abs/2610.37381)

**RoboAuto** does LLM-based program search with object/scene/interaction-level physical understanding (89.1% LIBERO-PRO; beats ASPIRE and π₀.₅ on long-horizon real tasks). [RoboAuto](https://arxiv.org/abs/2610.36533)

**TOPS** adapts flow-matching source priors and schedules per task: LIBERO-10 53.4→69.7% at one integration step (~1/6 baseline time); real drawer task 20→80%. [TOPS](https://arxiv.org/abs/2610.36694)

**QCP** enables inference-time control of execution quality (speed, smoothness) with iterative hindsight relabeling that exceeds demo quality; validated on conveyor throughput and wine-glass transport. [QCP](https://arxiv.org/abs/2610.37393)

**Discrete vs. continuous actions**: a large controlled study finds naive uniform-bin discrete actions match or beat continuous policies in success rate across single-task, multi-task, sim, and hardware; the real challenge is factorization error, addressable via discrete flows / CFG. [Paper](https://arxiv.org/abs/2610.20429) • Related: **PDRVLA/DRIFT** residual flow adapter for continuous outputs in VLMs/VLAs. [DRIFT](https://arxiv.org/abs/2606.05758)

**Edge deployment**: *VLA-HWBench* measures 18 VLAs on Jetson Thor and AMD Ryzen AI Max+ with a seven-stage breakdown — action-generation strategy dominates latency (82–157× spread), not model size; kernel fusion + 4-bit helps 2.6–2.9×. [VLA-HWBench](https://arxiv.org/abs/2610.34717)

**SCRIM** quantifies per-state criticality in imitation learning and reweights BC losses; also enables compact high-value data subset selection. [SCRIM](https://arxiv.org/abs/2610.17709)

**TS-DP** uses speculative decoding for diffusion policies (they're I/O-bound), with an RL scheduler for time-varying difficulty: 3.2× wall-clock speedup, 26 Hz real control, +23% on conveyor task. [TS-DP](https://arxiv.org/abs/2512.15773)

---

## 3. Bimanual & Multi-Arm Manipulation

**BiDex-100**: 106-task bimanual dexterous benchmark across 5 capability axes, 2 embodiments, 8,080 success-validated teleop demos (6.25M frames); baselines for 7 VLAs. [BiDex-100](https://arxiv.org/abs/2610.25459)

**cuArms**: GPU-parallel conflict-based planner for multi-arm workcells with reusable multimodal roadmaps, lazy conflict resolution, and a high-level scheduler; real-time initial solutions, no domain-specific training. [cuArms](https://arxiv.org/abs/2610.36250)

**RoboSTD**: zero-shot single→dual transfer via sagittal mirroring plus LLM-generated spatio-temporal coordination constraints (2.11× cup collection vs single-arm baseline on ALOHA). [RoboSTD](https://arxiv.org/abs/2610.36685)

**Keeping Contact**: task-adaptive friction margins (signed friction distance) in a sequence of SOCPs for bimanual non-prehensile tilting—interpretable force redistribution, robust to object property variation. [Keeping Contact](https://arxiv.org/abs/2610.36961)

**Which Hand Was Late?** diagnoses bimanual tool-use failures: tool slip is read on the tool hand; "which hand was late" needs both arms; whether a late attempt was also weak is *not identifiable* from passive sensing. VLM internal states carry the late hand almost perfectly but may not report it. [Paper](https://arxiv.org/abs/2610.37533)

**Semantic-geometric task representations** from human demos for bimanual planning (MPNN encoder + Transformer decoder, decoupled from action labels; full success on two real bimanual tasks). [Paper](https://arxiv.org/abs/2601.11460)

**Temporal tactile encoding + compliance** for robot-to-human bimanual handover: VLA + compliance controller with temporally encoded tactile feedback outperforms both ablations in a human-subject study. [Paper](https://arxiv.org/abs/2609.05282)

---

## 4. Dexterous Hands, In-Hand Manipulation, Grasping

**Torch-Hand**: fully articulated 21-DoF humanoid hand (5-DoF thumb, 4 DoF/finger) with entirely linkage-based actuation, in-palm serial-like actuator layout; evaluates workspace, 33-grasp taxonomy, force, payload. [Torch-Hand](https://arxiv.org/abs/2610.36789)

**In-hand object pose reaching** (LEAP hand): sim-trained recipe with generated grasp datasets, adaptive friction curriculum, and zero-shot transfer via mocap or a wrist depth camera. State policy reaches 95.2% of 4,800 unseen goals within 2 cm/0.4 rad; a learned residual safety filter cuts drops by 75% while still reaching 91.5%. [Paper](https://arxiv.org/abs/2610.37652)

**CARD**: contact-anchored retargeting from human video/mocap/tactile gloves to dexterous robot actions, preserving contact force targets (contact maintained on 43–78% of frames vs <10%/22.5% for kinematic/object-aware baselines; strict GRAB success 12→32%). Includes Vid-HACO video-to-contact model and a tactile tracking controller. [CARD](https://arxiv.org/abs/2610.36539)

**Grasps to Dexterity**: 355k-trajectory grasp-pretraining dataset used to pretrain a low-level goal-conditioned controller for articulated tool use; +33.3 pts full-task success over DP3 in the real world. Introduces DexCraft benchmark (6 tool-use tasks). [Paper](https://arxiv.org/abs/2606.30749)

**GTP-FA**: grasp-then-plan framework with a learned failure-attribution model that diagnoses grasp vs. planning failures and optimizes each accordingly; improves RL/IL/DP/VLA base learners. [GTP-FA](https://arxiv.org/abs/2606.03385)

Also: **"Pushing Dexterity and Safety…"** releases the full sim recipe as a platform for studying reliability/safety in high-DoF dexterous systems.

---

## 5. Tactile Sensing & Contact-Rich Manipulation

**FTP-1**: first generalist foundation tactile policy, pretrained on ~3,000 h from 26 sources across 21 sensors; heterogeneous encoders → unified morphology-aware tokens. +17.2% on seen sensor setups and, notably, +31% zero-shot-ish transfer to two unseen tactile sensors. [FTP-1](https://arxiv.org/abs/2606.13102)

**DreamTacVLA**: grounds VLA in contact physics via a tactile world model predicting future tactile signals; hierarchical spatial alignment between tactile micro-vision, wrist, and third-person views; up to 95% on contact-rich tasks. [DreamTacVLA](https://arxiv.org/abs/2512.23864)

**FAWAM**: force-aware world-action model using force at perception, prediction (joint action + wrench forecasting), and execution (residual correction from predicted wrench reference); +36.25% over vision-only, +21.25% over force-aware baselines. [FAWAM](https://arxiv.org/abs/2606.08555)

**Active hardness classification** with vision-based tactile sensors: entropy/variance-driven active sampling reaches 90% accuracy vs. 48% human accuracy. [Paper](https://arxiv.org/abs/2505.13231)

**Bimanual contact-rich diagnosis**: see the "Which Hand Was Late?" entry above.

---

## 6. Humanoids & Loco-Manipulation (embodied control)

**ZAP** trains a small off-the-shelf VLM via a tool harness using only simulated tasks—96.7% real-world success, 3× faster and 17× cheaper than a frontier baseline, and generalizes to an unseen embodiment (55.9% RoboLab-120, +4.9 pts over leading VLA/WAM). [ZAP](https://arxiv.org/abs/2610.35817)

**GRAFT**: geometry-aware residual adaptation for frozen humanoid behavior trackers—lightweight lower-body adapter distilled from privileged terrain observations to onboard depth; validated on Unitree G1 with stairs/gaps/platforms. [GRAFT](https://arxiv.org/abs/2610.36507)

**HC2Robot**: predicted-foresight module (next touchdown timing/location/support quality) + Hyper-Connection Transformer for humanoid parkour (97.6% mean sim traversal success across stairs, gaps, platforms, slopes). [HC2Robot](https://arxiv.org/abs/2610.36825)

**Phase-conditioned PPO** for multi-phase loco-manipulation on both Unitree G1 and Spot+arm (phase-conditioned critic, phase-gated rewards, multi-phase reset curriculum). [Paper](https://arxiv.org/abs/2610.36270)

**Whole-body humanoid control via stochastic motion tokenization**: a discrete motion interface conditioned by a high-level controller generates 16.8 s dance/fight/walk motions and a 35 s fight-to-dance sequence on a physical G1. [Paper](https://arxiv.org/abs/2610.36452)

**REACH**: RL hierarchical crawling + variable-height walking for confined spaces (1.27–0.20 m), with history-conditioned latent and LiDAR planner; real G1 experiments. [REACH](https://arxiv.org/abs/2610.36546)

**HumiTransfer**: converts in-the-wild human-human interaction videos into physically plausible human-humanoid interactions across embodiments; produces HumiMimic (~500k frames for Unitree R1 and Mini-hi). [HumiTransfer](https://arxiv.org/abs/2610.36615)

**VLA-Stem** and **Stem-like brainstem safety** also apply to humanoid/legged execution; **"When Black-Box Robot Policies Fail"** diagnoses/repairs corrupted sensor inputs around a frozen Go2 locomotion policy via a structured surrogate (success 259→429/640 offline; 382/640 online repair). [Paper](https://arxiv.org/abs/2610.36852)

Also: **SWIM**, **MOSAIC of muscle-driven control across individual musculoskeletal models** (99.24% completion across 31 held-out models, zero-shot with image-based body estimates). [MyoAcross](https://arxiv.org/abs/2610.36535)

---

## 7. Teleoperation & Data Collection Interfaces

**OpenJaws**: fully open hardware/software sensorized UMI framework with a low-cost stereo camera for metric trajectories; introduces UMI-Loc-Bench-v1 and shows stereo localization substantially beats monocular. Policies trained on OpenJaws data deploy on real robots. [OpenJaws](https://arxiv.org/abs/2610.36598)

**MILD + AprilVINS**: a localization benchmark for UMI-style teaching (86 real sequences, sim subset) and a fisheye VIO + sequence-local AprilTag method reaching mm-level TCP-relative accuracy where VIO alone is cm-level. [Paper](https://arxiv.org/abs/2610.09857)

**EgoThumb**: open-source vision-driven supernumerary robotic thumb with forearm-relocated tendon actuation and a visual imitation policy mapping palm-camera images to joint positions. [EgoThumb](https://arxiv.org/abs/2610.37582)

**"From 12 to 200 Demonstrations"**: careful scaling study of ACT, Diffusion Policy, SmolVLA, π₀.₅ on a SO-101 (1,340 scored episodes); π₀.₅ wins at low data, ACT ahead from ~100 demos, SmolVLA/DP cap near 50%, and fine-tuning recipe matters more than data amount for π₀.₅. Useful methodology on measurement noise. [Paper](https://arxiv.org/abs/2610.37170)

---

## 8. Sim-to-Real, Real2Sim, and System Identification

**ActiveAlign**: uses active perception (hand waving + differentiable rendering for calibration; tactile touching for mm-level object alignment) to close Real2Sim gaps; enables G1 fine manipulation of buttons/sliders and curates uncalibrated open datasets. [ActiveAlign](https://arxiv.org/abs/2610.36859)

**IDTD**: informationally decoupled trajectory design for sim-to-real system identification—Schur-complement Fisher score with per-parameter normalization; 39.6% lower parameter error than strongest active-exploration baseline across linear systems, Go2, G1, Crazyflie, and a real K1 humanoid. [IDTD](https://arxiv.org/abs/2610.10905)

**DeFM**: DINO-style foundation model trained only on 60M depth images with metric-aware normalization, distilled for edge; SOTA on depth classification/segmentation/navigation/locomotion/manipulation with strong sim-to-real. [DeFM](https://arxiv.org/abs/2601.18923)

**Gradient-flow gap**: **"Pushing Dexterity…"** and **RoboSTD**, **GRAFT**, **RynnWorld** all report zero-shot sim-to-real transfer as core evidence.

Also: **Where Small Mistakes Matter (SCRIM)** for data curation; **LOPAL** for demo-quality-aware learning.

---

## 9. Robot Learning Infrastructure, Data & Benchmarks (brief)

- **AmaraSpatial-10K** — 10,071 standardized 3D assets (metric scale, anchors, collision hulls, PBR, metadata) with an evaluation suite; 99.1% settling stability in Habitat-Sim and 3.4× CLIP Recall@5 over Objaverse. [Paper](https://arxiv.org/abs/2604.23018)
- **BiDex-100**, **DexCraft**, **MILD**, **UMI-Loc-Bench-v1**, **FRBench**, **SCOPE-R** — new manipulation/agent benchmarks introduced above.
- **DeFM** and **GAWM** release pretrained/compact models for off-the-shelf use.

---

## 10. Briefly Noted (Outside Core Themes)

- **Autonomous driving**: CLAP-AD (closed-loop speed scoring; +28.5/+32.7 driving score on Bench2Drive), FastBEVFusion (>50 FPS multi-modal 3D detection), ExecDiffuser (sample-to-execution gap in diffusion planning), Boreas-RT dataset. [CLAP-AD](https://arxiv.org/abs/2610.36079) • [FastBEVFusion](https://arxiv.org/abs/2610.37153) • [ExecDiffuser](https://arxiv.org/abs/2610.36837) • [Boreas-RT](https://arxiv.org/abs/2602.16870)
- **Navigation/SLAM**: SG²SLAM (monocular 3DGS), SVIn+ (underwater multi-modal), RAVEN (aerial active SLAM), Goal2Pixel (VLN as pixel grounding), HGWM (zero-shot ObjectNav), Omni-IGN (drone ImageNav, zero-shot sim-to-real), KEPT (conformal keepouts in degraded sensing). [SG²SLAM](https://arxiv.org/abs/2610.36312) • [SVIn+](https://arxiv.org/abs/2610.36454) • [RAVEN](https://arxiv.org/abs/2610.37111) • [Goal2Pixel](https://arxiv.org/abs/2606.01621) • [HGWM](https://arxiv.org/abs/2610.32554) • [Omni-IGN](https://arxiv.org/abs/2610.36968) • [KEPT](https://arxiv.org/abs/2610.37217)
- **Aerial/agile flight**: rendering-free event-frame sim (400× faster; 82% real success on a 56 g Crazyflie), dynamic narrow-gap visuomotor flight via differentiable sim (80% real), fixed-wing RL interception. [Events](https://arxiv.org/abs/2610.37543) • [Gap flight](https://arxiv.org/abs/2610.37557) • [Interception](https://arxiv.org/abs/2610.37470)
- **Multi-robot / MARL**: MORLAX & MO-Playground (GPU-native MORL, 26–271× speedups), multi-robot IPP with spatio-temporal GP-KF, strategyproof deep RL for online resource allocation. [MO-Playground](https://arxiv.org/abs/2603.09237) • [IPP](https://arxiv.org/abs/2609.05515) • [Strategyproof](https://arxiv.org/abs/2610.37504)
- **Safety-critical control**: gradient-free neural HJ reachability (up to 80-D, F1-tenth with 16k-D observations), REACH, VLA-Stem, KEPT. [HJ reachability](https://arxiv.org/abs/2609.14087)
- **LLM/agent systems** (large cluster): harness evolution, memory, routing, evaluation — e.g., Evolving Agent Teams (GPU kernels, 1.2× over FlashInfer), AgentBaton (65.9% cost reduction via handoffs), Stratum (repository memory), Tool-using agent security (Log-To-Leak, AgentSentry, Concordat, Blindfold), many benchmarks (SWE-Skills-Bench, FeatureArc, InfraDev, kw-bench, UnityBench-Mini3D). These are outside manipulation but broadly relevant to embodied agent infrastructure.

---

## Cross-Cutting Takeaways

1. **World-action models are maturing fast** — but the field is also self-correcting: faithful latent dynamics are rare, and pixel/video prediction gains don't automatically transfer OOD.
2. **Frozen-policy augmentation** (R2A, VLA-Stem, AWARE, GRAFT, AFIL) is emerging as a cheap, practical alternative to full fine-tuning for robustness and safety.
3. **Tactile and force signals are moving from auxiliary inputs to first-class modeling targets** (FTP-1, DreamTacVLA, FAWAM, CARD).
4. **Data interfaces are being open-sourced and benchmarked** (OpenJaws, MILD, BiDex-100, DexCraft), addressing a longstanding bottleneck.
5. **Hardware progress continues** on anthropomorphic, linkage-driven hands (Torch-Hand) and supernumerary/assistive devices (EgoThumb).