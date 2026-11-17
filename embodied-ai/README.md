### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-17T14:53:13.666600
  - **arXiv update** 2026-11-17T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied Intelligence & Manipulation — arXiv Roundup

Big day. Below, grouped by theme, with emphasis on hands, tactile, VLA plumbing, and sim-to-real. Navigation, detection, and generic LLM/benchmark papers are down at the bottom.

---

## 1. Dexterous Hands, Grasping & In-Hand Manipulation

- **DexFormer 2.0** — One RL policy for many arm–hand combos via a canonical joint interface + kinematic-tree attention; 89% on seen pairings, 51% on held-out, zero-shot to new hand types. [Paper](https://arxiv.org/abs/2611.20273)
- **TMA** — Tactile-driven motor adaptation for forceful humanoid manipulation; round-doorknob opening as benchmark; zero-shot sim-to-real on Unitree G1 + Revo2 hands, beats RMA and reactive tactile baselines. [Paper](https://arxiv.org/abs/2611.18976)
- **ARMFUL** — Whole-arm grasps for large objects; new 1.7M-config WAG dataset, diffusion over point clouds + motion planner; 70/100 on a real Franka across IKEA objects. [Paper](https://arxiv.org/abs/2611.20692)
- **TARGO / TARGO-Net** — Target-driven 6-DoF grasping under clutter occlusion; completion module + target-scene cross-attention; most robust across occlusion levels. [Paper](https://arxiv.org/abs/2407.06168)
- **Task-oriented grasping, training-free** — VLM-scored candidate grasps; up to +36.9% success over baseline. [Paper](https://arxiv.org/abs/2502.04873)
- **Contact-GraspNet + human-in-the-loop fixes** — VR demos target the grasps RL persistently fails; hard-case success 24%→45%. [Paper](https://arxiv.org/abs/2611.18919)
- **WinDEX** — Metric 3D hand reconstruction in the wild for dexterous teleop and policy learning; 7.6×/3.6× task success vs. WiLoR/HaWoR references. [Paper](https://arxiv.org/abs/2611.21143)
- **AsymEEF** — Cross-end-effector demo transfer across 2/3/5-finger grippers; 16.6× replay-valid expansion in sim; shared bimanual policy. [Paper](https://arxiv.org/abs/2611.20557)

---

## 2. Tactile Sensing & Force-Aware Control

- **TaF-Foundation** — Grounds tactile representations in 6D wrenches across 24 sensors (100M paired samples); −17.1% force RMSE, +13.1 R@1 cross-sensor retrieval; TaF-Policy 51.3% sim / 46.3% real. [Paper](https://arxiv.org/abs/2611.20718)
- **WiTac** — Wrist-informed tactile encoder pretrained on ~300h SharpaDex; conditioning GR00T N1.7 and π0.5 gives +28.8% / +15.0% over vision-only. [Paper](https://arxiv.org/abs/2611.21057)
- **TacBridge** — Unified tactile representations via cross-sensor correspondence (GelSight, DIGIT, GelSlim, TacTip). [Paper](https://arxiv.org/abs/2611.20939)
- **ForceHarness** — Gives frozen API-only models force perception via self-terminating force primitives; GPT-6 Astra zero-shot 3.3%→90.0% on a real arm. [Paper](https://arxiv.org/abs/2611.21099)
- **Non-imaging optical tactile sensors** — Review of transduction principles, timing/coverage, and task-level validation. [Paper](https://arxiv.org/abs/2611.20770)

---

## 3. VLA Policies: Robustness, Efficiency & Inference Plumbing

- **NF-VLA** — Autoregressive normalizing flows with one exact-likelihood objective; 98.35% LIBERO, 72.6% LIBERO-Plus, no robot pretraining. [Paper](https://arxiv.org/abs/2611.20314)
- **APS-VLA** — Learned action-guided visual token pruning, frozen backbone; 137→93 ms on dual-arm real tasks with 61% vs 60% success. [Paper](https://arxiv.org/abs/2611.13030)
- **ScaleVLA** — Pushes a VLA to 552B params; 10 demos beat a 2B model's 50; 216 ms median per chunk. [Paper](https://arxiv.org/abs/2611.21607)
- **Robustness as a transferable skill** — Source-task adversarial defense applied to target VLA encoders; printed-patch success 20.3%→45.8% on a real PiPER. [Paper](https://arxiv.org/abs/2611.18702)
- **VLALagBench** — Latency sensitivity study: 100 ms can halve success on moving targets; async execution recovers some. [Paper](https://arxiv.org/abs/2611.03103)
- **Refinement vs. replanning** — Inference-compute allocation for frozen chunked policies; fewer denoising steps often beats more frequent replanning. [Paper](https://arxiv.org/abs/2611.19034)
- **CAST** — Certify-then-select runtime steering of frozen diffusion policies with barrier conditions + value ranking; fewer constraint violations than output filters. [Paper](https://arxiv.org/abs/2611.19047)
- **ReRead** — Frozen policy's own cached representations re-read by a tiny corrector; +23.5 / +13.1 / +8.0 pts on hard RoboTwin tasks. [Paper](https://arxiv.org/abs/2611.20465)
- **ACiT** — Proprioceptive-prior action chunking; per-joint tokens + inverted decoding; gains on dynamics-heavy tasks, transfers to π0. [Paper](https://arxiv.org/abs/2611.20719)
- **ReGround** — Re-grounds frozen VLAs under actuation shift (latency, remounting) via motor babbling; π0.5 0.16→0.90 under 400 ms delay. [Paper](https://arxiv.org/abs/2611.20244)
- **Bring Back Language to Actions** — Parameter merging to recover VLM grounding lost during VLA fine-tuning. [Paper](https://arxiv.org/abs/2611.18891)

---

## 4. World / Action Models for Manipulation

- **ResWAM** — Supervises only the *residual* future feature change in frozen DINOv3 space; 81.1% LIBERO-Plus, 93.8% RoboTwin 2.0, +10% over π0.5 on real tasks at 92.7 ms. [Paper](https://arxiv.org/abs/2611.19559)
- **DiffWAM** — MoE with a visual-difference expert; experts dropped at inference; +15.0 pts over FastWAM on real manipulation. [Paper](https://arxiv.org/abs/2611.19904)
- **ThinkWAM** — Proposal→rethink→refine loop in latent space; 98.70% LIBERO, 64.4% across real OOD conditions. [Paper](https://arxiv.org/abs/2611.21258)
- **RoboActualizer** — Argues the world-model encoder is already the expensive part; 60M-param actualizer on a frozen encoder, 39 ms latency, single 32 GB GPU. [Paper](https://arxiv.org/abs/2609.36413)
- **OA-WAM** — Object-addressable keys for viewpoint/layout robustness; 90.5% zero-shot LIBERO-Plus, 89/100 real trials. [Paper](https://arxiv.org/abs/2605.06481)
- **JEPA4R** — 4D point-cloud JEPA world model with decodeable imagination (~1.1 cm error over 200 steps); zero-shot real arm with gripper and dexterous hand. [Paper](https://arxiv.org/abs/2611.19771)
- **Cache or denoise less?** — Sobering result: two uncached steps match ten; cross-cycle caching is fragile under the deployed sampler. [Paper](https://arxiv.org/abs/2611.19709)
- **WorldOracle** — Benchmark for action-conditioned world models against paired real executions. [Paper](https://arxiv.org/abs/2610.18826)

---

## 5. Sim-to-Real, Teleoperation & Humanoids

- **DAPPT** — Domain-aware procedural trajectories for dexterous tool use (sand scooping, dough rolling) without simulating deformables; 1.5–3.8× task metrics, zero-shot transfer. [Paper](https://arxiv.org/abs/2611.20202)
- **Ego2Sim2Humanoid** — Egocentric glasses → agentic real-to-sim → whole-body trajectories; GR00T N1.7 runs loco-manipulation on a G1 with no robot demos. [Paper](https://arxiv.org/abs/2611.19196)
- **MoViC** — Real-time whole-body humanoid control from live monocular RGB; frequency-domain motion representation, 10 Hz vision / 50 Hz control bridging; device-free bimanual teleop. [Paper](https://arxiv.org/abs/2611.19998)
- **Leaning Over to Reach** — Sampling-based whole-body MPC braces against surfaces to extend reach ~50 cm; 89% reach / 81% full cycle on H1-2. [Paper](https://arxiv.org/abs/2611.19100)
- **XMimic / XSoma** — JAX-compiled training learns 40 LAFAN1 clips in 0.86 min on 4×H100; locomotion in 0.77 min. [Paper](https://arxiv.org/abs/2611.20452)
- **QTOP** — Quantile critics for humanoid motion tracking; up to 10% over on/off-policy baselines; scaling law reported. [Paper](https://arxiv.org/abs/2611.20791)
- **Velocity-conditioned whole-body style** — Actor sees only locomotion commands; style from tracking reward; ≥98% sim, all real G1 trials, beats AMP without a crane. [Paper](https://arxiv.org/abs/2611.20888)
- **Residual RL for visual servoing** — SAC residual on inverse-Jacobian PI + delay-compensated Kalman filter; 1.1–1.4 mm → 0.3–0.7 mm tracking error, zero-shot sim-to-real. [Paper](https://arxiv.org/abs/2611.19318)
- **Safe RL on hardware** — RSGF-RL with PPO-style estimators; zero-shot whole-body G1 control and Crazyflie navigation. [Paper](https://arxiv.org/abs/2611.19616)
- **ImpedanceMimic** — Learned per-joint impedance as action space recovers contact forces from motion; transfers zero-shot to unseen humans and a humanoid. [Paper](https://arxiv.org/abs/2611.19153)

---

## 6. Agentic Manipulation, Planning & Skill Systems

- **RoboCoEvo** — Failure-guided co-evolution of an MLLM agent's code-as-policy programs and VLA weights; gains on BEHAVIOR-1K, RoboCasa, RoboTwin. [Paper](https://arxiv.org/abs/2611.19081)
- **MARS** — Dynamic routing between a frozen generalist VLA and RL-trained atomic skills; Tube Transport 20.0%→85.7%. [Paper](https://arxiv.org/abs/2611.19324)
- **Lazy-MOSAIC** — Learned skill-effect world model prunes simulator queries in long-horizon skill planning; validated on a physical robot. [Paper](https://arxiv.org/abs/2611.21517)
- **PlanDiv** — Test-time scaling where candidates differ by *plan*; 8 plan-conditioned candidates beat 8 resamples on CALVIN and a real Franka. [Paper](https://arxiv.org/abs/2611.20010)
- **ReuseMem** — One goal-agnostic visual memory reused for multiple later manipulation goals; +24.5 pts joint goal completion. [Paper](https://arxiv.org/abs/2611.21115)
- **CommitFlow** — Semantic commitment monitoring + local correction over a frozen π0.5; +22.7% on RoboTwin 2.0. [Paper](https://arxiv.org/abs/2609.21908)
- **HINT** — Human-intent inception for agentic manipulation; semantic reasoning only at pattern transitions, no extra trainable params. [Paper](https://arxiv.org/abs/2609.02653)
- **Dynamic Shaping** — Reference-free acquisition of interface + binding over frozen components; 86/300 → 295/300 on ViZDoom. [Paper](https://arxiv.org/abs/2611.20573)

---

## 7. Benchmarks, Datasets & Infrastructure

- **HospitalBench** — Ten long hospital chore chains in Isaac Sim with causal sub-task dependencies. [Paper](https://arxiv.org/abs/2611.19274)
- **Minari** — Reproducible offline-RL datasets (338 datasets, D4RL regeneration) with Gymnasium API and one-line loading. [Paper](https://arxiv.org/abs/2611.18644)
- **RoboKit** — GPU-parallel differentiable optimization toolkit; 4096 grasps in 2.97 s, 2–60× faster across seven tasks. [Paper](https://arxiv.org/abs/2611.20185)
- **Manipulation policy robustness under simulator misspecification** — Calibrated 90% intervals cover only 9–15% of rotation errors on harshly lit real data; nice counterpoint to the sim-to-real optimism above. [Paper](https://arxiv.org/abs/2611.20321)
- **ContactGuard** — Pre-contact execution monitor: predicts the consequence of an action chunk in latent space and aborts before contact. [Paper](https://arxiv.org/abs/2608.13438)
- **Robotic reward models survey** — 114 methods sorted into five semantic families, plus RRM-Bench-1K and RRM-Hub. [Paper](https://arxiv.org/abs/2611.20741)

---

## 8. Briefly Noted (outside the core themes)

- **Navigation / field robotics:** passage-focused multi-robot coordination [2611.18877](https://arxiv.org/abs/2611.18877); Sim-to-real ObjectNav on Spot/TurtleBot with Nav2 [2611.19720](https://arxiv.org/abs/2611.19720); EasyNav ROS 2 modular stack [2611.19894](https://arxiv.org/abs/2611.19894); AlphaTruck 1/5-scale off-road platform [2611.19730](https://arxiv.org/abs/2611.19730); VLN agents (VLN-Flash [2611.19287](https://arxiv.org/abs/2611.19287), SimpleVLN [2610.23203](https://arxiv.org/abs/2610.23203), LeaP-VLN [2611.20676](https://arxiv.org/abs/2611.20676)).
- **Grasping-adjacent manufacturing/medical:** Lazy-MOSAIC covered above; MoveIt IK for endoscopic scenarios hits 100% under 100 ms via problem splitting [2611.20978](https://arxiv.org/abs/2611.20978).
- **Driving:** SuperGlance single-pass driving VLA, 84 ms [2611.19138](https://arxiv.org/abs/2611.19138); ReactBench-AD on hazard reactions [2611.20011](https://arxiv.org/abs/2611.20011); WTR-Drive risk supervision [2611.20510](https://arxiv.org/abs/2611.20510).
- **Policy/theory:** subprocess-constrained MDPs [2611.21471](https://arxiv.org/abs/2611.21471); compositional MARL contracts [2611.19078](https://arxiv.org/abs/2611.19078); onboard p-bit weight representation [2611.19588](https://arxiv.org/abs/2611.19588).
- **Transparency/ethics:** robot demo videos should carry teleop/CGI disclosure labels — relevant to how sim-to-real results get communicated [2611.18982](https://arxiv.org/abs/2611.18982).
- **Clearly out of scope:** medical VQA/LLM, legal benchmarks, fintech, hardware verification, and most of the general-agent literature (papers 218–900 range).

---

### Quick takes

- **Hands are consolidating.** DexFormer 2.0, TMA, WinDEX, and ARMFUL all attack cross-embodiment or whole-arm capability rather than yet another single-gripper pick-and-place.
- **Tactile has found its shared coordinate system.** Wrench grounding (TaF) and wrist-informed fusion (WiTac) are both bets that heterogeneous sensors need a common physical or visual anchor.
- **World models are getting cheaper and more suspicious.** ResWAM/DiffWAM/RoboActualizer all argue the heavy lifting is done at pretraining; meanwhile the Flip Test and the cache-vs-steps paper suggest next-frame fidelity isn't the same as causal state.
- **Watch the sim-to-real honesty.** The SPEED+ misspecification result and the "cache or denoise less" negative result are useful correctives to the day's headline numbers.