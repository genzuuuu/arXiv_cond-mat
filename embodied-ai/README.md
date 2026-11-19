### Daily arXiv Embodied AI & Dexterous Manipulation Digest
  - **Generated at** 2026-11-19T14:40:52.701759
  - **arXiv update** 2026-11-19T05:00:00
  - **Demo** [Daily arXiv Embodied AI & Dexterous Manipulation Digest](https://genzuuuu.github.io/arXiv_cond-mat/embodied-ai/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# Embodied Intelligence & Manipulation — arXiv Roundup

A large batch this time (~480 papers), so I've grouped the relevant ones tightly and skimmed the rest. Roughly **60 papers** sit in the manipulation/embodied core; the remainder are LLM agents, medical imaging, RL theory, and simulation — noted briefly at the end.

---

## 1. Vision-Language-Action Policies & Long-Horizon Execution

- **BiCAT** — shares one motion tokenizer across both arms with symmetric cross-arm attention; +17.6 pp over 8 baselines on RoboTwin 2.0, 40.5 ms/chunk. [Paper](https://arxiv.org/abs/2611.23499)
- **RageVLA** — decouples "what" from "where" via frozen DINOv3 perception + augmented LIBERO data; 0.72 on LIBERO-PRO vs 0.53 prior SOTA at 0.21B params. [Paper](https://arxiv.org/abs/2611.23517)
- **RePlan-VLA** — VLA-agnostic progress monitoring + replanning; +21.9% (RoboCasa365) and +10.4% (CALVIN), validated on Franka FR3. [Paper](https://arxiv.org/abs/2611.23843)
- **GTI** — grounds task intent per subtask phase with phase-conditioned visual targets; real-robot full-task success 21.7% → 59.2%. [Paper](https://arxiv.org/abs/2611.23926)
- **WACO** — training-free canonicalization of camera/base shifts using forward kinematics as a metric anchor; +36.7 pp real-robot under pose shift, plus a new LIBERO-PoseShift benchmark. [Paper](https://arxiv.org/abs/2611.24360)
- **Homeward** — related but complementary: renders known robot links from kinematics and estimates only unknown scene depth; 1,599 camera variants on LIBERO-Plus. [Paper](https://arxiv.org/abs/2611.24455)
- **DUAC** — post-hoc adaptive action chunking from flow-field Jacobian-vector products; single chunk, no resampling. [Paper](https://arxiv.org/abs/2611.24178)
- **CoT-WAM** — jointly trains VLM + world-action model via learnable plan latents; SOTA on LIBERO/CALVIN/RoboCasa-Kitchen. [Paper](https://arxiv.org/abs/2611.23803)
- **LaST1.0** — control-centric latent world modeling from future wrist views; vision-encoder-free backbone. [Paper](https://arxiv.org/abs/2611.23974)
- **Z-sight** — predicts future directly in the VLM's own visual token space; 81.9% on SIMPLE, 73.3% on six Unitree G1 tasks at 110 ms/chunk. [Paper](https://arxiv.org/abs/2611.24940)
- **RecallFlow** — episodic memory as the *source distribution* for flow policies; 80.4% on MIKASA-Robo, +18.8 pts on four real tasks. [Paper](https://arxiv.org/abs/2611.23731)
- **LoRN** — low-rank noise steering for world-action models; video steering gives +26.2 pp vs +7.1 for action steering. [Paper](https://arxiv.org/abs/2611.23628)
- **F³** — what makes "good experience" for a WAM: form/fit/fusion over verified operation records; trained on only 200 examples. [Paper](https://arxiv.org/abs/2611.24708)
- **HINT-WAM** — on-policy self-distillation using future video as privileged hindsight, energy-score objective. [Paper](https://arxiv.org/abs/2611.24789)
- **JEPA Dots** — separates instruction-independent dynamics from language-conditioned task latents; 84.9% on LIBERO at 39.1M params. [Paper](https://arxiv.org/abs/2611.24062)
- **Phoenix** — scene-structure representations via dual-teacher distillation; 94.8% LIBERO-Plus, 72.4% RoboTwin 2.0 C2R. [Paper](https://arxiv.org/abs/2611.24938)
- **ZERITH V2.5** — which video-pretraining adaptation actually helps action learning (many noise levels yes; deployment noise level alone, no). [Paper](https://arxiv.org/abs/2611.23746)

**Robustness / adversarial / evaluation of VLAs:**
- **ExecGap** — adversarial patches that exploit the command-execution gap; validated on real robots. [Paper](https://arxiv.org/abs/2611.23714)
- **RECLAIM** — training-free defense using the frozen VLA's own attention response; LIBERO-Object 0% → 70%. [Paper](https://arxiv.org/abs/2611.24494)
- **Landmark synonyms study** — GR00T N1.7 fails object *choice* vs task *completion* differently; connector-only finetuning suffices. [Paper](https://arxiv.org/abs/2611.24076)
- **PIVOT-Q** — selective on-policy distillation to recover quantized VLA generalization; 20% of the distillation budget. [Paper](https://arxiv.org/abs/2610.05745)

---

## 2. Dexterous Hands, Tactile Sensing & In-Hand Manipulation

- **3DTouch** — shared 3D visuo-tactile representation with dense five-finger force vectors in base frame; +42 pp over VLA baseline on UR7e + XHand. [Paper](https://arxiv.org/abs/2611.23961)
- **T-WLA** — caches visual memory for a lightweight tactile editor that corrects unexecuted action chunks without rerunning the visual branch; 51.0% vs 23.0% baseline on real dexterous tasks. [Paper](https://arxiv.org/abs/2611.23804)
- **CoRA-VTLA** — queryable action-response memory + contact-guided gaze supervision for tactile post-training; 73.3% MuJoCo, 66.7% real. [Paper](https://arxiv.org/abs/2611.23963)
- **TacPilot** — separates *when to refresh* tactile features from *when to intervene* on a frozen visual policy. [Paper](https://arxiv.org/abs/2611.23804) *(note: shares the arXiv ID with T-WLA in the feed — verify before citing)*
- **LuxTac** — open-source optical taxel array, 3.5 mm thick, first to resolve shear at individual taxels; improves peg-in-hole over vision-only ACT. [Paper](https://arxiv.org/abs/2611.23575)
- **SHAPE** — discrete EEF-token supervision + parallel continuous streams for learning dexterous manipulation from egocentric human video; direct joint readout 0.80 vs 0.63 for π0.5. [Paper](https://arxiv.org/abs/2611.24585)
- **Finetuning VLAs for dexterous hands** — five SFT+DSRL recipes on π0.5 + LEAP hand; freeze the VLM, fully train the action expert, don't use SFT success to pick checkpoints. [Paper](https://arxiv.org/abs/2611.23676)
- **TapTacTouch** — training-free, vision-free mesh reconstruction from sparse tactile contacts via multi-scale GPIS; CD 1.610, ~50 s/object. [Paper](https://arxiv.org/abs/2611.24207)
- **SPICE** — tactile-only diffusion policy for reaching through foliage; 95% vs 45% branch maneuvering, 87.5% zero-shot transfer to unseen plants. [Paper](https://arxiv.org/abs/2611.23585)

---

## 3. Grasping & Task-Oriented Grasp Selection

- **MANGO-Grasp** — anisotropic Mahalanobis fields over geometry-oriented 3D Gaussians; +8.24 pp on seen hands, +16.57 pp zero-shot to an unseen hand, 86% real. [Paper](https://arxiv.org/abs/2608.02014)
- **LAGR** — language-aware grasp re-ranking with a 2.68M-annotation dataset; +9.3 pp over next best, validated on Franka FR3. [Paper](https://arxiv.org/abs/2611.23858)

---

## 4. Bimanual & Human-to-Robot Transfer

- **Φ-CON** — coupled-oscillator DLO dynamics with Lagrangian structure enabling a stability-guaranteed PD controller; 97.5–99.7% lower endpoint error in sim, 27.9% real. [Paper](https://arxiv.org/abs/2611.23563)
- **Ego2X** — object-centric CORE representation for egocentric video → executable robot data; 62.9% of annotated contacts realized vs 27.9% for HuRo, RoboTwin success 40.5% → 67.0% with no sim demos. [Paper](https://arxiv.org/abs/2611.24138)
- **DiWALI** — diffusion policies in a world model trained on action-free human + robot play via latent action inference. [Paper](https://arxiv.org/abs/2611.24836)
- **Doppel** — embodiment-agnostic video world model conditioned on rendered future body pose; 8 embodiments, ~600 h, +1.0–1.2 dB PSNR over action-only. [Paper](https://arxiv.org/abs/2611.24925)
- **SeRA** — set-valued relabeling of autonomous rollouts in interactive imitation learning; 80% vs 40% on real tomato picking. [Paper](https://arxiv.org/abs/2611.24273)

---

## 5. Cross-Embodiment Action Representation

- **RoboMorpher** — morphology-conditioned tokenizer reconstructing joint angles *and* link poses; MorphGen generates kinematic supervision; 56.40% RoboTwin 2.0. [Paper](https://arxiv.org/abs/2611.24816)
- **Grana** — composition of open-vocabulary subtask progress for long-horizon reward modeling, pretrained on 200 tasks. [Paper](https://arxiv.org/abs/2611.24926)

---

## 6. Sim-to-Real, Data Generation & Benchmarks

- **Pose6DAug** — 3D-anchored, multi-view-consistent object swapping for VLA data augmentation; +16.5% on novel objects, >2× real-robot success. [Paper](https://arxiv.org/abs/2606.20118)
- **WorldComposer** — generative Real2Sim2Real with "Digital Cousins" scene/object variation; strong sim-to-real correlation. [Paper](https://arxiv.org/abs/2604.15805)
- **RFW-S** — 83,365 simulation-verified deformable assets across 5 structural families with independent verification and sim-to-real replay. [Paper](https://arxiv.org/abs/2611.23056)
- **RoboBuilder** — agents co-design hardware + program, then get built and tested physically; 66% of sim passes hold in reality, video-feedback redesign removes 72% of level-1/2 failures. [Paper](https://arxiv.org/abs/2611.23855)
- **EmbodiedLab** — 35 simulated science experiments where agents must *act to know*; strongest of 7 frontier agents hits 41.4%. [Paper](https://arxiv.org/abs/2610.35385)
- **DOCK** — object-centric representation grounded in forward kinematics, fixing the poor rank correlation of frozen DINO/V-JEPA feature distance (≤0.11 vs 0.87 for mask centroids). [Paper](https://arxiv.org/abs/2611.23578)

---

## 7. Teleoperation & Human-in-the-Loop Interfaces

- **Single-controller mobile manipulator teleop** — Dingo-O + Kinova Gen3 Lite, automated ROS pipeline to Zarr datasets. [Paper](https://arxiv.org/abs/2611.24499)
- **Immersive telepresence study** — head-guided camera beat joystick camera control on time, wall contact, workload, and presence; locomotion choice mattered less. [Paper](https://arxiv.org/abs/2611.23939)
- **Remote endovascular teleop** — network emulation with 8 clinicians; 5% packet loss kept 87.5% success but all clinicians rated it unacceptable. [Paper](https://arxiv.org/abs/2611.24280)
- **TinyARM-X** — open-source, torque-controllable desktop arms under $350, reconfigurable to >3 DoF in 10 min. [Paper](https://arxiv.org/abs/2611.24554)
- **QDD-MM** — open-source quasi-direct-drive muscle module for tendon-driven robots. [Paper](https://arxiv.org/abs/2611.24279)
- **In-contact task segmentation** — NN-based segmentation of hand-guided demos into motion types (early-stage work). [Paper](https://arxiv.org/abs/2611.24226)

---

## 8. Safety, World Models & Planning for Manipulation

- **Recoverability instead of invariance** — certifies ability to re-enter a trusted recovery mode; validated on a full-scale IndyNXT racecar in rain. [Paper](https://arxiv.org/abs/2611.23589)
- **Self-correcting visual planning with frozen world models** — runs the model in reverse to detect actuation shift; reach error 36 mm → 3–5 mm on a real arm. [Paper](https://arxiv.org/abs/2611.23620)
- **ProbeShare** — 43.8–128.9× faster CEM planning by sharing probes across candidates. [Paper](https://arxiv.org/abs/2611.24229)
- **SCR** — learned gate for whether to continue CEM search; 23.81% fewer candidate plans evaluated. [Paper](https://arxiv.org/abs/2611.24470)
- **RTS** — risk-triggered search with amplitude-preserving metric for frozen JEPA models; +12.67–41.67 pp Safe Arrival Rate. [Paper](https://arxiv.org/abs/2611.24409)
- **JEPA counterfactual world models** — first-order counterfactual correction from factual data only; counterfactual R² 38–46% → 86–96%. [Paper](https://arxiv.org/abs/2611.24778)
- **Embodied Graph / RWM** — relational state abstraction for long-horizon imagination; only method to get diamonds in Minecraft within budget. [Paper](https://arxiv.org/abs/2611.24115)
- **Latent safety filter conservatism** — proves "overlap" is the minimum share of safe actions a latent filter must refuse. [Paper](https://arxiv.org/abs/2611.23685)

---

## 9. Quadruped / Humanoid Loco-Manipulation

- **WAM-Policy** — arm-centric WAM adapted to arm-free quadrupeds via on-policy self-distillation; 85.0% on QLM-Bench, deployed on Go2 Air. [Paper](https://arxiv.org/abs/2611.24011)
- **ReLoco** — behavior-conditioned motion priors for locomotion + get-up + command resumption in one proprioceptive policy; 96.8% get-up on Tiangong 3.0. [Paper](https://arxiv.org/abs/2611.23916)
- **SBEE** — proprioceptive base + terrain elevation estimation treating footsteps as landmarks; −22.1% ATE vs best prior on ANYmal-D. [Paper](https://arxiv.org/abs/2611.24310)
- **PR-MPPI** — exact command-space constraint-manifold MPPI with projection + retraction for dual-arm closed chains. [Paper](https://arxiv.org/abs/2608.07573)
- **Heave-Ho** — decentralized multi-humanoid collaboration, scales to 10 robots, speech-based leader-follower sync without network comms. [Paper](https://arxiv.org/abs/2611.22275)

---

## 10. Briefly Noted (outside core themes)

- **Generalist agentic manipulation**: AMP1 (generalist AI models commanding manipulators directly) reports 85.6% zero-shot on RoboLab-120 vs 49.2%/42.9% for VLAs/WAMs — worth a look even though it argues *against* specialist policies. [Paper](https://arxiv.org/abs/2611.09892)
- **Simulation/planning**: Facet-SLAM (real-time triangle splatting), SPARSER (variable projection for NLS), MAPF with turn constraints, FOCBS for unassigned agents.
- **Robot design**: Panini grammar for robot morphologies, BiPathCPG gearbox, RESCUE Jumper, SPROUT soft growing robot.
- **Off-theme**: ~400 papers on LLM agents/evaluation, medical imaging, RL theory, quantization, and autonomous driving. Happy to dig into any of these if useful.

---

⚠️ **Two feed issues to flag:** (1) Paper [TacPilot: Does Touch Need to Be Everywhere?](https://arxiv.org/abs/2611.23804) (TacPilot) and [T-WLA: Bridging Slow Vision and Fast Touch with a World-Language-Action Model](https://arxiv.org/abs/2610.28814) (T-WLA) are listed under the same URL `2611.23804` — one of these IDs is likely wrong. (2) Paper [Controllable Generative Trajectory Prediction via Weak Preference Alignment](https://arxiv.org/abs/2510.10731) has a 2025 ID mixed into an otherwise 2026 batch.

Want me to expand any section — e.g., a deeper dive on the tactile/VLA papers, or a comparison table of the world-action-model line (CoT-WAM / LaST / Z-sight / Phoenix / HINT-WAM)?