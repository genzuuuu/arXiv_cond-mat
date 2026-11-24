### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-24T16:24:24.293373
  - **arXiv update** 2026-11-24T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Digest: Embodied Intelligence & Robotic Manipulation

This is an enormous dump (~990 entries), so I've grouped the on-topic embodied AI / manipulation / VLA / tactile / sim-to-real papers by theme and kept notes short. Off-theme papers (LLM agents, NLP, medical imaging, etc.) are skipped except where they touch embodied control.

---

## Vision-Language-Action (VLA) Models — Architectures & Efficiency

- **[FlowPAC: Flow-Guided Visual Pruning and Action Caching for Efficient VLA Inference](https://arxiv.org/abs/2611.28256)** — Training-free VLA acceleration using optical flow to jointly prune visual tokens and cache actions; 2.13× speedup on LIBERO.
- **[PhysPPF: Learning Robotic Manipulation with Past, Present, and Future Physical Representations](https://arxiv.org/abs/2611.28551)** — Unified spatiotemporal VLA in a compact physical token space (What-Where-How + Past-Present-Future); +17.2 on SimplerEnv, +29.3 on CALVIN.
- **[Intervention-Robust VLA: Diverse Demonstrations for Robot Deployment with Safety Filters](https://arxiv.org/abs/2611.28289)** — InteR-VLA broadens state coverage so safety-filter interventions don't degrade tasks; Safe Success Rate up to 90% from 0%.
- **[LoopSeek / S1Arena-MM](https://arxiv.org/abs/2611.29773)** — System-1 vs System-2 split for multimodal decisions; 51k questions, closed-loop game envs.
- **[SANA-Robot: Efficient World Action Model with Hybrid Memory](https://arxiv.org/abs/2611.28943)** — 4.5B WAM with minute-level memory, real-time 30 Hz control on edge devices.
- **[Spatially Grounded Latent Lookahead (SG-LL)](https://arxiv.org/abs/2611.28839)** — Frozen spatial teacher distills geometry; latent predicts near-future to refine actions.
- **[VITA-WAM: Manifold-Aligned World-Action Modeling](https://arxiv.org/abs/2611.31195)** — Manifold-aligned flow matching; 1-step generation beats 10-step FastWAM by 21.5 pp on LIBERO-Plus.
- **[ThinkWAM / Think Before You Forecast](https://arxiv.org/abs/2611.21258)** — Proposal-rethink-refine loop over latent futures; 98.7% on LIBERO.
- **[WeaveVLA: 3D Relational Grounding](https://arxiv.org/abs/2611.31126)** — Sparse graph GNN + recurrent edge states for 3D relations; +15 pp real-world success.
- **[W³H-VLA / ConsisX](https://arxiv.org/abs/2611.30291)** — Where/How/When spatial-geometric guidance; cross-view consistency thinking.
- **[Latent Reasoning VLA (LaRA-VLA)](https://arxiv.org/abs/2602.01166)** — Internalizes CoT into continuous latents, up to 90% lower latency.
- **[RMR-VLA: Recurrent Memory Reasoning](https://arxiv.org/abs/2611.30145)** — Explicit event→state→subgoal memory; SOTA on RoboMME and LIBERO-Mem.
- **[JEPA-Tuner](https://arxiv.org/abs/2611.29096)** — Action-conditioned future prediction regularizes VLA guidance; enables async chunk execution.
- **[SR-VLA: Stall-Reduced VLA Execution](https://arxiv.org/abs/2611.22356)** — Predicted-input lookahead + selective KV cache repair; 2.67× query speedup.
- **[LoopedWAM](https://arxiv.org/abs/2611.25595)** — Compact looped WAM, 0.58B params, 96.1% LIBERO, 7.4× less GPU memory.
- **[FlexWAM](https://arxiv.org/abs/2611.30024)** — View-routed action attention with counterfactual view credit; +16–23 pp real tasks.
- **[AsyncMixVLA](https://arxiv.org/abs/2611.28585)** — Proactive async switching across heterogeneous VLA policies under perturbations.

## VLA Grounding, Robustness & Test-Time Adaptation

- **[Probing Invisible Actuation Shifts for Test-time Calibration (PEA)](https://arxiv.org/abs/2611.28308)** — Active probing identifies gain/delay/drift; recovers success without training (61%→89.7%).
- **[RoboAda: Adapting Frozen Robot Policies at Test Time to Invisible Physics](https://arxiv.org/abs/2611.30209)** — Infers command→motion mapping from observed motion; 27.8%→62.9% under 11 physical shifts.
- **[DeRail: Counterfactual Action Steering](https://arxiv.org/abs/2611.28803)** — Training-free mid-execution instruction switching; π0.5 5.8%→54.6% on CALVIN-Switch.
- **[LIBERO-MOR: Multimodal Robustness Benchmark Across the VLA Pipeline](https://arxiv.org/abs/2611.28867)** — 22 perturbations × 3 severities × 40 tasks; exposes robustness gaps.
- **[ViewPACT: Multi-View Geometric Augmentation and Pose-Action Co-Training](https://arxiv.org/abs/2611.29068)** — Privileged pose supervision; 37.4%→78.4% under unseen viewpoints.
- **[A2I-VLA: Semantic-Physical Alignment and Integration](https://arxiv.org/abs/2611.29279)** — Two-stage force/tactile alignment; 70%→95% on contact-rich tasks.
- **[Bring Back Language to Actions (parameter merging)](https://arxiv.org/abs/2611.18891)** — Mitigates VLA fine-tuning's forgetting of VLM knowledge via task-vector merging.
- **[JEPA-ICL: Progress-Aligned Latent Plans](https://arxiv.org/abs/2611.30516)** — Demonstration context from human video + JEPA future prediction.
- **[Entangle: Scaling Human-Video In-Context World-Action Models](https://arxiv.org/abs/2611.28732)** — Single human video as context; 83.5/100 across six unseen tasks.

## Dexterous Hands, Grasping & In-Hand Manipulation

- **[Doing More with Less: Complex Manipulation with a Contact-Adaptive Robotic Hand](https://arxiv.org/abs/2611.28675)** — Underactuated contact-adaptive hand + motion glove; phone charging, in-hand manipulation, cable cutting.
- **[FunGrasp-Zero: Zero-Shot Cross-Embodiment Dexterous Functional Grasping](https://arxiv.org/abs/2611.29195)** — Field-conditioned graph attention, contact-map intent; 80% on 4 unseen real hands.
- **[Dr. Grasp-RL: Diverse and Robust Dexterous Grasping via RL](https://arxiv.org/abs/2611.29610)** — Time-reversed curriculum + coordinated reset; generalizes to 20k+ unseen objects.
- **[UnderGrasp: Envelopment-Oriented Grasp Refinement](https://arxiv.org/abs/2611.29907)** — Post-hoc refinement for underactuated grippers; success 0.55→0.82 with AnyGrasp.
- **[graspit-py: A Python Interface to GraspIt! for Grasp Planning Under Pose and Friction Uncertainty](https://arxiv.org/abs/2611.29011)** — Native closure/contacts, MuJoCo export, uncertainty sampling.
- **[Connectivity-Aware Exploration of Robotic Grasp Spaces](https://arxiv.org/abs/2609.22983)** — Multiscale connectivity structure of viable grasp sets in SE(3).
- **[RAGrasp: Geometry-Semantic Template Retrieval and Grasp Transfer](https://arxiv.org/abs/2610.04438)** — Deployment-specific retrieval-augmented grasping from local templates.
- **[DexLatentWorld: 3D Cross-Embodiment Latent Action World Models](https://arxiv.org/abs/2611.30907)** — Latent actions from point clouds; zero-shot on unseen dexterous hands (86% over 50 trials).
- **[DexDuet: Contact-Preserving Bimanual Dexterity from Human Demonstrations](https://arxiv.org/abs/2611.30495)** — Interaction rewards preserve hand-object contacts; +11–41 ADD-AUC.

## Tactile Sensing & Visuo-Tactile Policies

- **[Distilling Touch into Vision-Only Policies (TacitTouch)](https://arxiv.org/abs/2611.28697)** — Student learns tactile-guided actions without reconstruction; closes 2–3.75% gap to teacher.
- **[VTLA-RL: Visuotactile Policies for Load-Adaptive Grasping](https://arxiv.org/abs/2611.28752)** — Shared visual encoder + bilateral force targets, two-stage RL post-training.
- **[A2I-VLA](https://arxiv.org/abs/2611.29279)** — (cross-listed above) force-tactile alignment for contact-rich tasks.
- **[T-Tac: A Soft Thin Active Thermal Tactile Sensor](https://arxiv.org/abs/2611.28939)** — Thermal transient material ID, 92.7% across 12 materials.
- **[Tacinf: A Unified Tactile Infrastructure for Robot Manipulation](https://arxiv.org/abs/2611.29240)** — Sim synthesis + benchmark + VTLA policy + handheld data collection; sim-to-real r=0.998.
- **[TipDex-VTLA: Refine Actions with Visual Reliability and Tactile Feedback](https://arxiv.org/abs/2611.25683)** — VASE + TACE gating; robust to unseen lighting in dexterous tasks.
- **[TacInno: Teaching VLA Models the Contact Dynamics Beyond Vision and Action](https://arxiv.org/abs/2611.26405)** — Isolates "tactile innovation" as supervision; +10.7 sim / +9.0 real pp.
- **[VeriTouch: Verified Visuo-Tactile World Models](https://arxiv.org/abs/2611.30572)** — Generates + verifies synthetic visuo-tactile trajectories for policy learning.
- **[Force2Act: A Force-Aware Visuomotor Policy](https://arxiv.org/abs/2611.29208)** — Global force planning + Mixture of Force Experts; 93.8% sim, 94.2% real.

## World Action Models & World Models for Control

- **[Innata-0: A Native Embodied World System with Model-Agent Co-Design](https://arxiv.org/abs/2611.30254)** — Tri-tower MoT (understanding/prediction/action) + agent with memory/verification.
- **[Value function based Reward shaping for safety in quadrupeds](https://arxiv.org/abs/2611.30133)** — Barrier-function-inspired shaping; violations 27%→0.1%.
- **[ζ₀: World Action Models with Joint Scene and Body Foresight in Humanoid Control](https://arxiv.org/abs/2611.29277)** — Foresees visual features + joint trajectories; +16–19 pp on humanoid tasks.
- **[MAWAM: Multi-Agent World Action Model](https://arxiv.org/abs/2611.29501)** — Joint imagination across heterogeneous robot teams; 82.7% joint success.
- **[Fork-JEPA: Two Actions from One State](https://arxiv.org/abs/2611.28350)** — Fork futures identify action response; up to +14% planning success over LeWM.
- **[ActField: Learning Action Effects as Continuous-Time Latent Dynamics](https://arxiv.org/abs/2611.30659)** — Action-conditioned vector field over physical time.
- **[Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models](https://arxiv.org/abs/2611.29839)** — Perturbed-history training without teacher.
- **[SpikingWAM: Spiking World-Action Models](https://arxiv.org/abs/2611.30041)** — Sparse task-skeleton world state for low-power WAMs.
- **[Fast-JEPA / Decision-Aligned Selection](https://arxiv.org/abs/2611.28919)** — Candidate ranking matters more than prediction error (DRR analysis).
- **[JEPA-Shield: Safe Diffusion Planning with Latent World Models](https://arxiv.org/abs/2611.29609)** — Conformal uncertainty tubes + backup shield for constraint satisfaction.

## Sim-to-Real, Simulators & Benchmarking

- **[Neural Fidelity Calibration (NFC)](https://arxiv.org/abs/2611.28260)** — Flow-matching inference of simulator params + residual fidelity; rough-terrain navigation 26%→70%.
- **[Neural Fidelity Calibration for Informative Sim-to-Real Adaptation](https://arxiv.org/abs/2611.28274)** — Companion paper, fuller detail on the same framework.
- **[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts](https://arxiv.org/abs/2610.41857)** — SimuGuard finds PhysX false contacts throwing objects; LingBot-VA 89→98/100.
- **[RoboScope Kit: Unified Interfaces for Fast Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)** — 13–15× faster LIBERO/RoboTwin evaluation, outcome-exact.
- **[RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](https://arxiv.org/abs/2611.27042)** — Real–sim correlation 0.97 across 22 configurations, 8 evaluation tracks.
- **[Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real](https://arxiv.org/abs/2611.31098)** — Agent builds digital twins + "cousins" and develops policies.
- **[OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.08548)** — 3D-generated assets + sim teleop; zero-shot beats real teleop data on most tasks.
- **[EgoStudy: How Does Scaling Egocentric Data Affect VLA and WAM Pretraining?](https://arxiv.org/abs/2611.30490)** — Diversity + alignment matter; WAMs win when egocentric data is scarce.
- **[ScaleEvals: Scaling Generalist Policy Evaluation through Reset-Free Autonomous Play](https://arxiv.org/abs/2611.28411)** — VLM AutoPrompter/AutoGrader, 23 rollouts/hr, 98% less human labor.
- **[RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?](https://arxiv.org/abs/2611.30047)** — Paused-world benchmarks hide memory failures (97%→50%).

## Teleoperation & Human-Robot Interfaces

- **[TeleMultiStream: Low-Latency Multi-Stream Video Feedback Teleoperation](https://arxiv.org/abs/2611.29980)** — WebRTC + UDP; 60–66 ms glass-to-glass, supports DAgger-style correction.
- **[Arcadian: Open-Source Humanoid Ecosystem](https://arxiv.org/abs/2611.29868)** — ~$6,800 meter-scale humanoid, VR teleop, RL locomotion transfer.
- **[NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation](https://arxiv.org/abs/2609.39000)** — Terrain-aware teacher-student; ~1,000 h of paired motion data.
- **[CHAMP: Coordinated Humanoid Loco-Manipulation with Whole-Body Motion Priors](https://arxiv.org/abs/2611.30449)** — 84.8% sim / 91.4% real on Unitree G1.
- **[YUBI: Yielding Universal Bidigital Interface](https://arxiv.org/abs/2606.10244)** — Finger-aligned gripper; 8,434 h / 1.2M episodes bimanual dataset, cross-robot transfer.
- **[Teleoperator-Aware CBF Adaptive MPC for Legged Robots](https://arxiv.org/abs/2509.22815)** — Shared autonomy; 51% less human control effort on Unitree Go2.

## Agentic / Coding-Agent Robot Control (emerging theme)

- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)** — Team of persistent agents per control group; 28.2% lower time cost.
- **[RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)** — Instruction + feedback channels; drift recovery 0.42→0.84, far cheaper than agent-only.
- **[Agent on Guard (AoG)](https://arxiv.org/abs/2611.30101)** — Programmatic agent + frozen policy, physically-clock-aware intervention scheduling.
- **[RoboHarness-Zero: Body and Soul](https://arxiv.org/abs/2611.30550)** — Frozen VLA + zero-shot VLM monitor; 57.5%→70.5% on RoboCasa365.
- **[Embodied-Harness / ReWeave](https://arxiv.org/abs/2611.27689)** — Dual-agent self-improving harnesses; 82.4% RoboTwin 2.0.
- **[Contact Harness: VLM Agents for Contact-Rich Manipulation](https://arxiv.org/abs/2611.29377)** — Skills + force feedback; 90.7% full insertion across 15 connector types.
- **[EmboEagle](https://arxiv.org/abs/2611.31173)** — WAM + latency-gated VLM supervision; 74% fewer VLM calls.

## Teleop/BC/Diffusion Policies — Other Notable

- **[JEPA-Tuner](https://arxiv.org/abs/2611.29096)** and **[DelayOPSD](https://arxiv.org/abs/2611.30534)** — async/latency-aware policy training.
- **[Learning from Failure: Robot Self-Improvement via Human Videos](https://arxiv.org/abs/2606.21406)** — DGAC; 40%→81% across 7 real tasks.
- **[DUO Policy: Bridging Human Video Coverage and Robot Precision](https://arxiv.org/abs/2611.29101)** — Hand policy + robot policy + gate; 2.75× less data collection.
- **[SBTenv](https://arxiv.org/abs/2611.28547)** and others (split-belt treadmill) — off-theme for manipulation, noted for locomotion sim.
- **[Stubborn: Unified RL Framework for Humanoid Motion Tracking and Fall Recovery](https://arxiv.org/abs/2606.12814)** — Probabilistic termination + adaptive sampling.

---

## What to read first (my shortlist)

1. **Physical-shift adaptation without retraining**: PEA and RoboAda — highly practical, cheap, benchmark-backed.
2. **Tactile without tactile hardware**: TacitTouch and TacInno — good signal on where touch actually helps.
3. **Cross-embodiment dexterity**: FunGrasp-Zero, DexLatentWorld, Dr. Grasp-RL.
4. **Evaluation credibility**: SimuGuard (sim contact artifacts), RoboScope Kit (throughput), LIBERO-MOR (robustness).
5. **Agent+policy division of labor**: RoboThink, Contact Harness, ACAP — the clearest emerging paradigm.

Off-theme (LLM agents, benchmarks, medical, NLP, etc.) mostly skipped; happy to summarize any specific paper in more depth.