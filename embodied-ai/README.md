### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-10-26T11:32:03.316115
  - **arXiv update** 2026-10-26T04:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Robotics & Embodied AI Digest

## Manipulation Policies & VLA Models

A dense cluster this cycle. Several papers push on deployment-time behavior of flow-matching VLAs rather than architecture: [Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies](https://arxiv.org/abs/2610.32102) surfaces a nice counterintuitive coupling — coarse numerical integration *hurts* rapid replanning but *helps* extended open-loop commitment, acting as implicit regularization. Relatedly, [Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](https://arxiv.org/abs/2610.31859) is a sobering engineering note: 9 of 12 open VLA codebases train bf16 weights without an fp32 master copy, erasing up to 79%+ of updates, with LIBERO success jumping from 4.3%→49.3% (SmolVLA) and 5.1%→80.9% (π0.5) after the fix.

Recovery and steering are also active: [If at First You Don't Succeed, Backtrack](https://arxiv.org/abs/2610.32941) adds a tiny failure-prediction head (0.48–0.88% params) to frozen VLAs and rewinds to earlier states, cutting LIBERO-Long failures 19–48%. [Martingale GRPO](https://arxiv.org/abs/2610.32431) argues trajectory-level advantages unfairly penalize recovery attempts and truncates failure feedback after the last unrecovered error via a VLM. [MAST-VLA](https://arxiv.org/abs/2610.32312) combines skill-conditioned LoRA-MoE with trajectory-affordance priors (CALVIN avg len 4.65).

Scaling from heterogeneous data: [EgoForesight](https://arxiv.org/abs/2610.31845) tackles noisy egocentric action labels via reliability-weighted regression and privileged-future distillation; [DiscoDemo](https://arxiv.org/abs/2610.32093) uses RL as a *data generator* to find diverse solution modes (real-robot success 39%→78%); [Retiming Robot Demonstrations with a Learned Speed Prior](https://arxiv.org/abs/2610.32676) normalizes teleoperator pacing and stacks cups 1.72× faster. [TTT in VLA Models](https://arxiv.org/abs/2610.32094) is an honest negative result — test-time training did not yield consistent demonstration-conditioned behavior at current scale.

Also worth a look: [RoboCode](https://arxiv.org/abs/2610.32225) (soft-gated reusable action primitives), [LogLook](https://arxiv.org/abs/2610.32348) (execution-grounded memory for frontier planners, 43% fewer tokens), [Backtrack-adjacent DynaSlots](https://arxiv.org/abs/2610.32330) (slot-centric 3D dynamics pretraining), and [DASH](https://arxiv.org/abs/2610.05792), a da Vinci instrument adapter for general-purpose arms.

## Dexterous Hands, Tactile Sensing & In-Hand Manipulation

[No Eyes, No Problem](https://arxiv.org/abs/2610.23438) is the standout: blind Baoding ball rotation on a Shadow Hand Lite using only proprioception and binary tactile, achieving 225 consecutive 180° rotations at ~0.36 rot/s in a single continuous trial — reportedly the strongest hardware result for this task regardless of sensing modality. Transfer was enabled by sensor-aligned embodiment plus two clever domain randomizations (slew-rate action limits, stuck-at taxels).

[ContactBench 1.0](https://arxiv.org/abs/2610.24512) is a valuable community resource: 36 tasks, 40+ reproducibly 3D-printable objects with matched sim models, organized around eight contact skills. Their headline finding is deflating — visual-tactile policies did *not* meaningfully outperform vision-only ones. [DexPort](https://arxiv.org/abs/2610.32969) offers a pragmatic data-collection path: use the robot hand *itself* as a handheld interface, specify wrist motion plus high-level finger skills, and record both commands and states (11%→64% with recorded commands; 36%→78% with in-the-wild data). [PartialBiGrasp](https://arxiv.org/abs/2608.19188) generates bimanual grasp pairs directly from partial point clouds via convolutional occupancy networks.

## Contact-Rich Manipulation & Force

[FORCA](https://arxiv.org/abs/2610.31841) is a coding agent that writes Python programs from visual + wrist F/T observations, diagnosing failures between executions — no demos, no training, no sim. Nice complement to [SEVI](https://arxiv.org/abs/2610.31829), which adds an evidential safety critic with epistemic uncertainty to real-world RL, overriding risky actions with a recovery policy (13.4–57.1% fewer unsafe events on USB insertion).

## Sim-to-Real, World Models & Real-to-Sim

[WorldMirror](https://arxiv.org/abs/2610.31834) formulates real-to-sim as iterative refinement of an executable world program, with a coding agent orchestrating image/3D generation tools and a camera-pose-anchored scene representation that preserves physical validity of DROID trajectories. [Does LeWorldModel Preserve Local Action Geometry?](https://arxiv.org/abs/2610.31716) is a sharp diagnostic: the most sensitive action directions differ by ~36–42° median from ground truth at small perturbation scales — worth reading alongside [Do Robotic World Models Really Follow Actions?](https://arxiv.org/abs/2608.24885), which finds expert-trained world models struggle with off-expert trajectories and proposes action-forcing alignment.

[Regularised RL improves sim-to-real transfer](https://arxiv.org/abs/2610.32855) makes the case that PPO's dominance is somewhat unjustified — SMM-AC achieves higher real-robot return and better robustness to observation/environment/dynamics perturbations. [DepState-JEPA](https://arxiv.org/abs/2610.29246) grounds a JEPA in metric 3D via RGB-D dual streams, with ray-conditioned readouts.

## Humanoids & Loco-Manipulation

[From Tabletop to Walking Bot](https://arxiv.org/abs/2610.32271) is a practical deployment report on a Unitree Go2 + AgileX Piper: expanding demo coverage cut held-out end-effector error 30%, and adding push-as-alternative-to-grasp introduced new modes without degrading baseline. [Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers](https://arxiv.org/abs/2610.32277) is a clean, useful result — unrandomized trackers survive only 15% at 40ms delay vs. 95% with 0–50ms randomization, and the authors note the 0–20ms ranges common in locomotion training sit *inside* the existing margin. [HoloBoxing](https://arxiv.org/abs/2610.32909) is a fun 7-minute-single-GPU recipe on top of a frozen whole-body controller. [RynnUnify](https://arxiv.org/abs/2610.32965) proposes a 16B unified embodied brain with interleaved video-language reasoning.

## Teleoperation & Data Infrastructure

[FLORA](https://arxiv.org/abs/2610.31779) is an industrial data engine (reward labels, timestamped captions) used for GR00T, labeling 200k hours/day. [KiRoSe](https://arxiv.org/abs/2610.31801) segments demonstrations from *kinematic* data alone using sparse motion tokens — a nice complement to vision-based segmentation, and it transfers zero-shot across embodiments and egocentric human motion. [TIDE](https://arxiv.org/abs/2610.29264) does human-in-the-loop online post-training without a critic, with sub-hour sessions. [Haptic bilateral teleoperation for free-hand dental procedures](https://arxiv.org/abs/2503.21288) is a domain-specific but well-executed system with force scaling for safety.

## Benchmarks, Analysis & Tooling

[Do VLAs Know They Will Fail?](https://arxiv.org/abs/2610.32208) shows SAE features of OpenVLA activations predict failure before unrecoverable states. [Sensorimotor Alignment](https://arxiv.org/abs/2610.31670) proposes a training-free offline proxy (S²) correlating with downstream success — useful for cheap model pre-screening. [RobustRLlib](https://arxiv.org/abs/2610.32971) unifies 17 robust RL algorithms across 273 perturbation configs. [3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509) organizes the field around data generation, simulation environments, and sim2real bridging. [SceneBloom](https://arxiv.org/abs/2610.32978) generates physically stable indoor layouts, and notably its navigation policies beat those trained on equal numbers of *real* scans.

## Briefly Noted (outside core themes)

Worth flagging for adjacent interest: [RAPAC-DP](https://arxiv.org/abs/2608.15924) (pending-action compensation for cloud-inference delay), [SMR](https://arxiv.org/abs/2610.29169) (streaming motion retargeting), [CoCarry](https://arxiv.org/abs/2610.32460) (dual-humanoid cooperative carrying dataset), [Baseline-Bench](https://arxiv.org/abs/2610.00854) (frontier VLM agents as robot generalists), and [Language as a Sensor](https://arxiv.org/abs/2606.08666) (treating natural-language spatial descriptions as calibrated probabilistic observations).

Skipped as out of scope: navigation-only/GNSS papers, UAV localization, autonomous driving control, swarm thermoregulation, and the large volume of pure-LLM agent/compression/evaluation work.