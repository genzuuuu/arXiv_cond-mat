### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-04T13:16:01.568365
  - **arXiv update** 2026-11-04T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Today's arXiv Digest: Embodied Intelligence & Robotic Manipulation

Most of today's submissions fall outside the target themes (LLM agents, IR, ML theory, scientific discovery). I've summarized the robotics/AI ones by topic and noted the rest briefly at the end.

---

## 1. Dexterous Hands, Grasping & In-Hand Manipulation

**DexHOT** learns a reusable relation-conditioned primitive for *hand-object configuration transfer*, treating dexterous goals as joint hand-object states rather than object poses alone. Reports 61.5% success on 200 real-hand transfers and 90% across six demonstration-guided tasks. [DexHOT](https://arxiv.org/abs/2611.05119)

**PACT** co-designs tendon routing, moment arms and capstan sizes for tendon-driven hands, maximizing task-force coverage at the weakest pose under a bandwidth constraint. Applied to a 4-DOF finger; prototype deviates from prediction by up to 24.5%. [PACT](https://arxiv.org/abs/2611.05302)

**DexCanvas** builds a hybrid real-synthetic dataset (7,000 hrs) of contact-annotated dexterous manipulation from 70 hrs of mocap via a real-to-sim RL pipeline. Contact features boost Diffusion Policy success from 67.5% to 82.2%. [DexCanvas](https://arxiv.org/abs/2510.15786)

**Dexterous Robot Manipulation from Human Demonstrations** uses contact-anchored retargeting plus residual policy learning to convert mocap into robot policies, transferring to four morphologically distinct hands. [Contact-Anchored Retargeting](https://arxiv.org/abs/2609.24093)

**In-Hand Object Pose Reaching** trains policies for a LEAP hand without human data, adds a learned residual safety filter, and transfers zero-shot to hardware (95.2% of goals within tolerance; drops cut 75%). [DexSafe](https://arxiv.org/abs/2610.37652)

**DexArena** is a new long-horizon bimanual dexterous benchmark (10 tasks, 30 stage-level tasks) with verified teleoperated demos. [DexArena](https://arxiv.org/abs/2611.02629)

**MABEL** is an open-source anthropomorphic mobile bimanual platform (56 DOF, ~$8.1k parts) with Apple Vision Pro whole-body teleoperation and an end-to-end imitation pipeline. [MABEL](https://arxiv.org/abs/2611.04083)

**RAIPAL** designs a humanoid arm from measured human upper-limb performance targets: 20 kg payload (2.25× its mass), 20.6 m/s endpoint speed, sustained hammering. [RAIPAL](https://arxiv.org/abs/2611.04334)

**Grasping Tumbling Objects** presents a rotating-base space manipulator method that synchronizes the target CoM with the system ICR for impact-free capture, then stabilizes the combined system via optimal control. [Space Manipulation](https://arxiv.org/abs/2611.04176)

---

## 2. Teleoperation & Handheld Data Collection

**Robot-Matched Soft Fingers for UMI** — 99.7-hour pick-and-place dataset over 53 objects with soft, visually force-indicating fingers. A top camera adds 13 points; multi-task mid-training lifts unseen-object success 35%→57%. [Soft-YUBI](https://arxiv.org/abs/2611.03779)

**AIRoA-0** trains a bimanual system from 16,151 hours of handheld YUBI demos with *zero* robot data, using only wrist cameras. 78% average success vs. 27% for the best post-trained VLA baseline; runs across Franka, TX-G2, OpenArm, UR. [AIRoA-0](https://arxiv.org/abs/2611.03815)

**PyRUA-DataFarm** replaces the teleoperator with a coding agent that rebuilds tasks in simulation, renders photorealistic rollouts, and produces deployable data at ~$0.80/episode. Farm-trained policies match teleop-trained (93 vs. 84/100) and are far more robust to visual shifts. [PyRUA-DataFarm](https://arxiv.org/abs/2611.05320)

**GUILD** closes the loop on *what data to collect* using VLM-proposed tasks plus predictive data attribution feedback. [GUILD](https://arxiv.org/abs/2611.05368)

**Haptic Shared Control for Multi-Robot Systems** compares single-agent, pinning, and centroid control modes with connectivity maintenance and haptic feedback. [Haptic Shared Control](https://arxiv.org/abs/2611.05027)

---

## 3. Visuomotor Policies & VLA Post-Training

**RAFT** does reasoning-aligned fine-tuning: train LoRA adapters on reasoning annotations, freeze them, then fine-tune on actions. OOD success on DROID rises 27.9%→75.0%. [RAFT](https://arxiv.org/abs/2611.04368)

**All-For-One** distills multiple visual foundation models into a lightweight RGB-only student via privileged learning — 30× fewer params, 50× lower latency than the teacher. [All-For-One](https://arxiv.org/abs/2611.04485)

**SR-DP** tackles multi-task diffusion policy interference with a frozen VGGT encoder plus SVD-decomposed spectral routing. 68.4% average on six RoboTwin tasks (+21.8 over multi-task VO-DP). [SR-DP](https://arxiv.org/abs/2611.04477)

**H2RB** bridges human and robot embodiment gaps for VLA co-training via geometry-anchored alignment and a decoupled-decoder tokenizer. Object transfer 8.0→51.8. [H2RB](https://arxiv.org/abs/2611.04391)

**Action-Intent Transfer (AIT)** extracts explicit action intents from human videos to transfer manipulation knowledge to robots. [AIT](https://arxiv.org/abs/2611.04522)

**RoboTryOn** frames human-to-robot video translation as virtual try-on, synthesizing robot demos from egocentric human video. Novel-task success 2%→60% with no real robot demos. [RoboTryOn](https://arxiv.org/abs/2611.05163)

**Asynchronous Robot Policies (ARP)** decouples a slow VLM (semantic memory) from a fast vision-action expert. +18% success, 20% less time on Franka; 3–5× baselines in dynamic sim. [ARP](https://arxiv.org/abs/2611.05155)

**PolicyIK** learns high-precision IK with RL: 93.5% of held-out tasks within 1 mm / 0.2°, 98.9% with a deployment protocol; executes π₀.₅ commands at 95.7% in sim pick-and-place. [PolicyIK](https://arxiv.org/abs/2611.05372)

**AdaIE** is a parameter-free reweighting of pretrained representations to counter action-head sensitivity concentration. Up to +19 pp average across five real tasks. [AdaIE](https://arxiv.org/abs/2611.04006)

**Action-Token Supervision vs. Gradient Routing** disentangles why gradient insulation works in MoT-style VLAs: coupling helps most (~40% route progress) when action tokens are *not* supervised. [Action Expert Gradients](https://arxiv.org/abs/2611.05249)

**CLAP** converts a VLM directly into a VLA by prepending natural-language action descriptions to numeric action tokens — 90.8% on LIBERO with 4–5 hours of training. [CLAP](https://arxiv.org/abs/2607.08974)

**Dexterous In-Hand / Fine-Tuning VLAs with Self-Demonstrated Generative Control** uses zero-shot VLA rollouts as extra fine-tuning data to retain generalist priors on a new embodiment. [Self-Demonstrated Control](https://arxiv.org/abs/2608.19490)

**PACE** selects action-chunk execution horizons online from low-speed valleys in predicted speed profiles (training-free). RoboTwin 57.8%→64.2%; real robots 50.7%→70.4%. [PACE](https://arxiv.org/abs/2606.00537)

---

## 4. World Models & Video-Based Policy Learning

**FloMo** argues dense 3D scene flow is the right intermediate for video pretraining → action transfer; co-trained on human video and robot teleop. Removing motion prediction hurts OOD generalization. [FloMo](https://arxiv.org/abs/2611.05062)

**HiLo-WAM** decouples long-horizon task evolution from local dynamics in a dual-DiT world action model. 93.70% on RoboTwin 2.0; 2.93× speedup via progressive inference. [HiLo-WAM](https://arxiv.org/abs/2611.05023)

**Cycle WAM** enforces cycle consistency between forward and inverse dynamics for better use of pretrained video priors. [Cycle WAM](https://arxiv.org/abs/2611.04711)

**DreamFree** distills a frozen video diffusion model's representations into a predictive visual encoder, enabling action prediction without generating future video. Real-time 11 Hz with a 14B backbone. [DreamFree](https://arxiv.org/abs/2611.04527)

**PrimeSim** is a generalist action-conditioned multiview world simulator midtrained on 30,110 hours across 22 platforms, with a fast-video/slow-memory post-training scheme. 10.1 FPS; supports GRPO policy optimization. [PrimeSim](https://arxiv.org/abs/2611.04870)

**3D World Simulator** jointly predicts appearance, geometry and touch from a hybrid particle-voxel representation at 50 Hz, supporting novel viewpoints and tactile signals. [Particle-Voxel Dynamics](https://arxiv.org/abs/2611.04492)

**TIF (Trusting Imagined Futures)** audits imagined rewards with execution feedback to select offline supervision for VLA post-training. 76.25% mean on LIBERO (+3.0 pp). [TIF](https://arxiv.org/abs/2611.04873)

**Action-Conditioned Latent Foresight** scores humanoid loco-manipulation command sequences with a latent WAM before execution. 89.7% on SIMPLE; 85.7% on real tasks. [Latent Foresight](https://arxiv.org/abs/2611.04839)

**PRIME W0** is a hierarchical conditional flow-matching VLA with per-layer KV injection, world-model subgoal images and a historical-frame DINOv2 bridge. [PRIME W0](https://arxiv.org/abs/2610.39528)

---

## 5. Tactile Sensing & Whole-Body Reflexes

**ReflexArc** integrates instantaneous tactile reflexes into learned humanoid whole-body control, delivering withdrawal poses to motors in 10 ms. Cuts first force peak by 34.1% and halves contact impulse. [ReflexArc](https://arxiv.org/abs/2611.04424)

**MagCilia** is a compact magnetic-cilia + Hall sensor for 3D force sensing (RMSE 0.40/0.57/0.69 N) with a causal history fusion regressor; 99.39% surface classification. [MagCilia](https://arxiv.org/abs/2610.09536)

**MagPillar** is a spider-hair-inspired magnetopillar array for surface perception — 99.34% material classification, captures periodic surface geometry. [MagPillar](https://arxiv.org/abs/2611.01609)

**VT-MUSE** learns unified sequential visuotactile representations via cross-modal temporal alignment and masked-view consistency. +11 pp over the strongest baseline in sim. [VT-MUSE](https://arxiv.org/abs/2608.21290)

---

## 6. Physics-Informed Manipulation & Deformable Objects

**Physical Diffusion Policy** recovers material properties by coupling 3DGS with differentiable MPM simulation, then conditions a material-aware MoE diffusion policy. [Physical Diffusion Policy](https://arxiv.org/abs/2611.04493)

**SCNC** optimizes trajectories for implicit-equilibrium systems without the frozen-tangent approximation; doubles the stable optimization rate on thin-walled tubes (83.3% vs. 41.7%). [SCNC](https://arxiv.org/abs/2611.03885)

**Shape Servoing Tutorial (Part II)** covers SVD-based controllability analysis, shape-feature selection, and failure modes (controllability/observability loss, mechanical instability). [Shape Servoing II](https://arxiv.org/abs/2611.03825)

---

## 7. Humanoids & Loco-Manipulation

**HLO-AMP** trains the low-level controller as an *object-aware* motion prior via mocap imitation with the payload physically present, then layers a reference-free high-level policy. Generalizes across masses and recovers from mid-carry drops on a G1. [HLO-AMP](https://arxiv.org/abs/2611.05113)

**SONIC-K1** ports a whole-body motion tracker to the Booster K1 on a single GPU; upper-body and slow motions track well, stepping/turning remain unreliable. [SONIC-K1](https://arxiv.org/abs/2610.39327)

**Online iLQR-MPC with Whole-Body Control** jointly optimizes contact forces and footholds in one receding-horizon problem, replanning at 100 Hz on a G1. [iLQR-MPC](https://arxiv.org/abs/2611.04204)

**DEED** reports a systems-level study of GR00T N1.6 on a Unitree G1 for supermarket restocking, arguing the lab-to-store gap is integration, not architecture. [DEED](https://arxiv.org/abs/2607.20345)

---

## 8. Sim-to-Real, Benchmarks & Evaluation

**RoboScope Kit** unifies policy/benchmark interfaces with separate simulator-worker and policy-replica pools — 4.45–25× evaluation speedups with identical outcomes. [RoboScope Kit](https://arxiv.org/abs/2611.03850)

**DuoBench** is a reproducible bimanual benchmark (11 tasks, FR3 Duo, sim + real) with stage-based failure analysis. [DuoBench](https://arxiv.org/abs/2606.11901)

**CRONOS** benchmarks non-episodic RL fine-tuning of VLAs; naive fine-tuning fails without targeted reset allocation. [CRONOS](https://arxiv.org/abs/2611.05080)

**LoopQ** is a closed-loop quantization benchmark for VLAs. Key finding: VLA-specific PTQ methods generally *underperform* plain RTN/AWQ/GPTQ, and at batch 1 no quantized π₀.₅ or OpenVLA-OFT config is faster than 16-bit. [LoopQ](https://arxiv.org/abs/2611.05093)

**LIBERO-RECOVER** shifts evaluation from "can it succeed" to "can it recover," with 1,000+ failure scenarios across four recovery levels. [LIBERO-Recover](https://arxiv.org/abs/2609.05178)

**DiMuRe** adds diagnosis-guided multilevel recovery to robot-use agents; 77.65% vs. 58.68% on disturbed LIBERO cases. [DiMuRe](https://arxiv.org/abs/2611.04226)

**GSBR** regularizes online RL by distance from the base policy's support. 33%→95% average success across 19 tasks. [GSBR](https://arxiv.org/abs/2611.05295)

**CANDO** combines conservative noise-space directional optimization with an action-space residual for adapting frozen generative policies. 91.4% final success. [CANDO](https://arxiv.org/abs/2611.04543)

**ResponsibleRobotBench** measures risk-aware task-level manipulation; notably, correct hazard recognition does not imply executable mitigation (GPT-4o mini identified hazards 100/100 but never requested help). [ResponsibleRobotBench](https://arxiv.org/abs/2512.04308)

**What the Guard Misses** shows implied-harm VLA instructions largely evade text guards — up to 95% complete the task with no flag raised. [Implied Harm](https://arxiv.org/abs/2610.05818)

**LLM4Robot-Bench** reports GPT-6 Astra's success collapsing from 80% (L1 contact geometry) to 0% (L3 coordinated contact reconfiguration). [LLM4Robot-Bench](https://arxiv.org/abs/2610.34527)

**Democratizing Robot-Use Agents** releases a unified harness where open-weight models reach a RoboDojo score of 31.39, above the published GPT-6 Astra result. [uni-robot-agent](https://arxiv.org/abs/2611.01560)

**VagueBench** documents "Ambient Context Illusion": embodied agents degrade ~20% relatively on semantically sufficient but contextually minimal instructions. [VagueBench](https://arxiv.org/abs/2611.03765)

**Test-Time Search Audit** finds a learned value selector is 1.66 pp *worse* than random on Cosmos Policy, 82% of states have identical candidate outcomes, and token pruning yields at most 1.15× end-to-end speedup. [Test-Time Search](https://arxiv.org/abs/2610.41970)

**SAFEVPR** replaces backbone cosine with an MNN patch score and flat LTT calibration for cross-condition loop closure; cuts erroneous constraints 29.6×. [SAFEVPR](https://arxiv.org/abs/2605.28048)

**RoboScope / IntentNav / SNAP / WayTrace** cover navigation and cross-embodiment transfer: [IntentNav](https://arxiv.org/abs/2606.08029), [SNAP](https://arxiv.org/abs/2611.03498), [WayTrace](https://arxiv.org/abs/2611.05129), [EchoNav](https://arxiv.org/abs/2610.27616).

---

## 9. Safety, Planning & Control (adjacent)

- **HJ Reachability GPU solver** runs 3D BRTs at 112 Hz onboard, 5.9–17.5× faster than JAX reference. [HJ Real-Time](https://arxiv.org/abs/2611.04096)
- **Caging VLN for Legged Robots** wraps VLA planners with SDF-based MPC and discrete exponential barrier constraints. [Caged VLN](https://arxiv.org/abs/2611.04972)
- **Nested FoV Barriers** solves the teleoperated relay-chain connectivity/mobility conflict with hard-soft visibility CBFs. [Relay Chains](https://arxiv.org/abs/2611.05074)
- **ActOR** uses ambient OR cameras + a digital twin to orchestrate humanoid autonomy; closed-loop feedback lifts success 46.7%→83.3%. [ActOR](https://arxiv.org/abs/2611.04255)
- **VARP** learns non-monotone rearrangement from visual states: 98.3% with 0.4 s planning. [VARP](https://arxiv.org/abs/2611.04093)
- **FEIJOA** grounds mobile-manipulation instructions at test time; 94.2% exact grounding, 35/50 real Spot trials. [FEIJOA](https://arxiv.org/abs/2611.04080)
- **WeaveRL** integrates online 3D surfel reconstruction into massively parallel RL training. [WeaveRL](https://arxiv.org/abs/2609.18685)
- **jaxipm** is the first GPU-batched NLP solver (JAX IPOPT), reaching 30.7–69.9% of a 64-core CPU fleet's throughput on one GPU. [jaxipm](https://arxiv.org/abs/2606.26341)

---

## Briefly Noted (outside core themes)

Swarm robotics ([DAO governance](https://arxiv.org/abs/2611.03975), [morphogenesis](https://arxiv.org/abs/2610.31900), [expressive swarms](https://arxiv.org/abs/2611.05244)); UAV/AUV control ([mass scaling laws](https://arxiv.org/abs/2611.04748), [multi-AUV LLM planning](https://arxiv.org/abs/2611.04518), [morphing quadrotors](https://arxiv.org/abs/2605.15999)); autonomous driving (FlowDrive, ReSMap, LMM survey, RFWorld); surgical/perception datasets ([iMED](https://arxiv.org/abs/2611.04755), [neurointervention user study](https://arxiv.org/abs/2611.03446)); and a very large volume of non-robotics LLM-agent, IR, scientific-discovery and ML-systems work that I've omitted.