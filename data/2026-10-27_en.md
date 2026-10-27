### Daily arXiv Condensed Matter Digest
  - **Generated at** 2026-10-27T10:26:45.808986
  - **arXiv update** 2026-10-27T04:00:00
  - **Demo** [Daily arXiv Condensed Matter Digest](https://genzuuuu.github.io/arXiv_cond-mat/)
  - **Source** [GitHub repo](https://github.com/genzuuuu/arXiv_cond-mat/)

# arXiv Condensed Matter Physics — Key Advances

## Machine Learning for Materials Discovery and Simulation

Several papers push ML beyond interpolation toward physically constrained, transferable models. **CrystalREPA** shows that aligning crystal generative encoders with frozen universal MLIP representations closes a representation gap and improves thermodynamic stability of generated crystals, with a practical criterion for choosing teacher potentials. **DeepSciReasoner** enforces hard physical constraints (conservation laws, spectral geometry) when predicting eDOS, phDOS, XANES, and Raman spectra. **TCSP3.0** fixes composition-correctness bugs in template-based crystal prediction and reaches 72.2% Top-1 on T180, while **SymADiT** adds Wyckoff-position symmetry awareness to latent flow-matching generation. Active-learning advances include **LLPR-based training/fine-tuning of MLFFs** and an **uncertainty-aware KMC–continuum coupling** that cuts atomistic simulations by 2–3 orders of magnitude. Two papers address data quality: a **precision-first electro-optic database pipeline** and a companion **error taxonomy** arguing "no value is better than a wrong value." **MatOS** presents an agent operating system for multi-stage materials research, and **JEPA** self-supervised embeddings organize XRD patterns by crystallographic semantics. On the methodology side, a **thermodynamic correction layer** shifts MLIP phase free energies without retraining, and a **retention-constrained fine-tuning** protocol preserves bulk elastic/phonon response while improving defect energetics in Al.

- [Chemistry-resolved disagreement between Materials Project-compatible PBE(+U) and r2SCAN stability verdicts in the GNoME materials database](https://arxiv.org/abs/2610.33101)
- [Exploring Joint-Embedding Predictive Architectures for Self-Supervised Representation Learning of Powder X-ray Diffraction Patterns](https://arxiv.org/abs/2610.33310)
- [Deep Scientific Reasoning under Physical Constraints: Structure-Aware Spectrum Prediction](https://arxiv.org/abs/2610.34021)
- [TCSP3.0: Template-Based Crystal Structure Prediction with Coefficient-Preserving Element Substitution and Structural Diversity](https://arxiv.org/abs/2610.34029)
- [A thermodynamic correction layer for machine learning interatomic potentials](https://arxiv.org/abs/2610.34551)
- [From Autonomous Knowledge Generation to Generalizable Property Prediction: A Precision-First Pipeline for Electro-Optic Materials Discovery](https://arxiv.org/abs/2610.34628)
- [No Value Is Better Than a Wrong Value: Finding and Handling Erroneous Data in Literature-Mined Datasets for AI](https://arxiv.org/abs/2610.34642)
- [Retention-constrained fine-tuning of a pre-trained aluminium MACE potential for non-equilibrium defect dynamics and plasticity](https://arxiv.org/abs/2610.35653)
- [Autonomous atomistic-continuum coupling through uncertainty-aware active learning](https://arxiv.org/abs/2610.33272)
- [Full-data accuracy with fewer labels for training and fine-tuning machine-learning force fields](https://arxiv.org/abs/2607.14486)
- [MatOS: An Agent Operating System for Materials Research](https://arxiv.org/abs/2610.34203)
- [CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models](https://arxiv.org/abs/2605.08960)
- [SymADiT: Symmetry-Aware Crystal Generation with Latent Flow Matching](https://arxiv.org/abs/2605.10115)
- [Computational screening of amorphous lithium trivalent-metal chloride solid-state electrolytes](https://arxiv.org/abs/2610.34505)

## Altermagnetism and Unconventional Magnetism

Altermagnetism is expanding rapidly in scope. A **microscopic four-band p-wave model** identifies winding-controlled topological descendants of altermagnets, with first-principles predictions for LaMnAu₅. **CoNb₄Se₈** is established spectroscopically as a layered g-wave altermagnet with spin-split branches resolved directly in ARPES. In **Penrose quasicrystals**, collinear and coplanar altermagnetism emerges from a group-theory orthogonality mechanism. **BiFeO₃** ultrathin films show d-wave altermagnetic order at four unit cells under short-circuit boundary conditions. Two theory papers extend the framework: **flexural altermagnetism** in MnPS₃ (d- and i-wave states) and **i-wave altermagnetism in graphene antidot superlattices**. On the polar-altermagnet front, a careful XRD/DFT study of **Ca₃(Ru,Ti)₂O₇** finds no evidence for the DFT-predicted Pn2₁a distortion, providing quantitative upper bounds. Related work covers **spin textures at ferromagnet Fermi surfaces** generating current-gradient torques, and **Zeeman-field-induced three-spin interactions** coupling to scalar spin chirality.

- [Winding-Controlled Topological Descendants of Antialtermagnets](https://arxiv.org/abs/2610.33252)
- [Robust spin splitting and fermiology in the layered altermagnet CoNb4Se8](https://arxiv.org/abs/2502.20010)
- [Collinear and Coplanar Altermagnetism in a Penrose Quasicrystal](https://arxiv.org/abs/2610.35855)
- [Altermagnetic Signatures and Topological Textures in Ultrathin Multiferroic BiFeO₃](https://arxiv.org/abs/2601.09970)
- [Flexural Altermagnetism](https://arxiv.org/abs/2610.35238)
- [Intrinsic i-wave altermagnetism in 2D graphene superlattices](https://arxiv.org/abs/2604.19661)
- [Evaluating the Structural Basis for Polar Altermagnet Candidate Ca3(Ru,Ti)2O7](https://arxiv.org/abs/2606.16181)
- [Spin textures at the Fermi surface of ferromagnets and associated torque](https://arxiv.org/abs/2610.18800)
- [Zeeman-field-induced three-spin interactions and relativistic coupling to the scalar spin chirality](https://arxiv.org/abs/2610.35401)

## Topology, Quantum Geometry, and Nonlinear Transport

A **unified first-principles theory of finite-wave-vector photocurrents** introduces rank-four tensors ξ (phase-gradient) and ζ (intensity-gradient) coupling, showing responses survive in centrosymmetric GeS. **Electric-magnetic dipole interference** enables even-order nonlinear optics in centrosymmetric crystals, scaling with the fine-structure constant. A **Chern non-trivial square-net nodal line semimetal** achieves C = 2 via symmetry-informed SOC. **Orbital Hall response of spin-1 fermions** connects multiband quantum geometry to transverse orbital transport. **Second-harmonic Hall response of FQH fluids** is developed as a bulk probe with ν⁻² scaling. Additional results: **quantum-metric-driven real-space interference** detectable by Josephson STM, **nonsymmorphic time-reversal-doubled axion insulators** in Bi₄Br₃I/Bi₄BrI₃, **space-time Floquet operators** revealing fractional charge pumps, **topological zero-reflection points** in multi-terminal junctions, and **subspace-protected topological phases** with new bulk-boundary correspondence. A **layer-tensor response** framework unifies electrically switchable bilayer responses.

- [Unified First-Principles Theory of Finite-Wave-Vector Photocurrents in Crystals](https://arxiv.org/abs/2610.33264)
- [Spin and Charge Photocurrents from Electric-Magnetic Dipole Interference in Centrosymmetric Crystals](https://arxiv.org/abs/2610.34222)
- [Chern non-trivial two-dimensional square-net nodal line semimetal](https://arxiv.org/abs/2610.33303)
- [Orbital Hall response of spin-1 fermions with a curved central band](https://arxiv.org/abs/2610.33211)
- [Second-Harmonic Bulk Response of Fractional Quantum Hall Fluids](https://arxiv.org/abs/2610.33606)
- [Real-Space Interference from Quantum Metric](https://arxiv.org/abs/2610.14048)
- [Nonsymmorphic Time-Reversal-Doubled Axion Insulators](https://arxiv.org/abs/2603.01072)
- [Space-time Floquet operator: Nonreciprocity and fractional topology of space-time crystals](https://arxiv.org/abs/2510.16562)
- [Topological zero-reflection points in multi-terminal quantum wire junctions](https://arxiv.org/abs/2606.31586)
- [Subspace-Protected Topological Phases and Bulk-Boundary Correspondence](https://arxiv.org/abs/2508.20908)
- [Electrically Reversible Layer-Tensor Responses in Bilayers](https://arxiv.org/abs/2610.34067)

## Superconductivity: Pairing Symmetry and Vortex Physics

**Intra-unit-cell Josephson interferometry** on monolayer FeSe resolves nodal lines along Fe–Se directions, identifying nodeless d-wave pairing — a genuinely local phase-sensitive probe. **Chiral f-wave superconductivity adjacent to a Wigner crystal** in rhombohedral tetralayer graphene is predicted via parquet/Bethe-Salpeter calculations. A **fractionalization treatment of the bilayer t-J model** for La₃Ni₂O₇ shows a Coulomb pseudopotential suppresses s± in favor of d-wave. **Universal scaling of Little-Parks oscillation amplitude** incorporating thermal fluctuations resolves a long-standing theory-experiment discrepancy. In **granular boron-doped diamond**, phase-fluctuation-dominated behavior with λ(0) ≈ 8.8 μm is established. **Kagome flat-band DMQMC** finds T_c = 0.0314|U| with a wide preformed-pair regime. Other results include **chiral superconductivity mechanisms**, **1/9 plateau structure in kagome Heisenberg AFMs** (a 27-site spin-density wave), **T_c-mosaic limits on T-linear penetration depth**, **first-order transitions in weak Ising SOC superconductors**, and **Andreev reflection lattice-vs-continuum comparisons** revealing continuum breakdown.

- [Nodeless d-wave pairing in monolayer FeSe revealed by intra-unit-cell Josephson interferometry](https://arxiv.org/abs/2610.34382)
- [Chiral Superconductivity Adjacent to a Wigner Crystal in Rhombohedral Graphene](https://arxiv.org/abs/2610.33808)
- [The fate of s± superconductivity in the bilayer nickelate La3Ni2O7](https://arxiv.org/abs/2610.35814)
- [Universal Scaling of the Little-Parks Oscillation Amplitude](https://arxiv.org/abs/2610.34318)
- [Phase fluctuations dominated superconductivity in a thick Granular Boron-Doped Diamond film](https://arxiv.org/abs/2610.34319)
- [Fermionic superfluid transition and pairing scale separation in the kagome flat band](https://arxiv.org/abs/2610.34342)
- [Theory of the 1/9 Magnetization Plateau of the Spin-1/2 Kagome Heisenberg Antiferromagnet](https://arxiv.org/abs/2610.34439)
- [Magnetic susceptibility and superfluid density of inhomogeneous superconducting films: the Tc-mosaic model](https://arxiv.org/abs/2610.34796)
- [First-Order Transitions in Weak Ising Spin-Orbit-Coupled Superconductors](https://arxiv.org/abs/2605.03774)
- [Andreev Reflection at a Graphene Normal-Superconductor Interface: A Lattice-Continuum Comparison](https://arxiv.org/abs/2610.34270)
- [Chemical Substitution as a Route to Anomalous Surface Superconductivity in NiBi3](https://arxiv.org/abs/2610.33463)
- [Time-reversal symmetry breaking and inherent Josephson diodes in a multi-component order parameter superconductor](https://arxiv.org/abs/2504.19361)

## Strongly Correlated Electrons and Quantum Criticality

**DMFT on a realistic three-orbital t₂g model** places Sr₂IrO₄ and Ba₂IrO₄ in a cooperative itinerant-localized regime, identifying the two-peak optical conductivity as the reliable fingerprint. **Orbital-selective correlations** in Co₃Sn₂S₂ explain the flat band near E_F and predict a giant anomalous Nernst effect. **Symmetry-resolved quasilocal entanglement** in plaquette CDMFT probes distinct aspects of Mott and pseudogap physics. A **dynamic pseudogap model** is benchmarked against exact Monte Carlo, confirming continued-fraction exactness in the static limit. **Nonequilibrium distributional statistics** generalize Crooks' hyperensemble to constrain average energy and Shannon entropy. In magnetism, **spinon backscattering interactions** are quantified in CuPzN, and **dilute disorder** via electron irradiation in YCu₃(OH)₆.₅Br₂.₅ suppresses magnetization plateaus, revealing a disorder-dominated regime. A review of **spin hydrodynamics in graphene** predicts thermovortical magnetization.

- [Cooperation of itinerant and localized physics in the magnetic phase diagram of 214 Ruddlesden-Popper iridates](https://arxiv.org/abs/2610.33196)
- [Orbital-selective correlations in kagome flat bands of Co3Sn2S2](https://arxiv.org/abs/2610.35255)
- [Symmetry-resolved quasilocal entanglement as a key to Mott and pseudogap physics in plaquette CDMFT](https://arxiv.org/abs/2610.34470)
- [Dynamic Pseudogap Model: Analytic Results vs Monte Carlo Numerics](https://arxiv.org/abs/2610.33436)
- [Distributional statistics of nonequilibrium](https://arxiv.org/abs/2610.33383)
- [Quasiparticle Interactions in the S = 1/2 Heisenberg Antiferromagnetic Chain CuPzN](https://arxiv.org/abs/2610.34536)
- [Tuning from intrinsic to disorder-dominated quantum states in a kagome antiferromagnet](https://arxiv.org/abs/2610.34230)
- [Transport and Phase competition in three-dimensional Hubbard-Holstein model at half-filling](https://arxiv.org/abs/2604.18219)
- [Spin-hydrodynamics in graphene and thermovortical magnetization](https://arxiv.org/abs/2409.07764)

## Quantum Devices, Qubits, and Quantum Thermodynamics

A **dephasing-powered open quantum-dot battery** achieves ergotropic efficiency approaching unity with long-lived charged states and two extraction protocols. **Zeptojoule microwave calorimetry** in graphene reaches 2.90 zJ switching energy with 19.5 ns recovery, with measured heat capacity and e-ph coupling explaining the sensitivity gap. **Real-time correlated TLS spectroscopy** in transmons links T1/T2 excursions to strongly coupled defects. Other device results: **phase-modulated concatenated driving** protects silicon hole-spin coherence; **FPGA-based multi-parameter feedback** stabilizes a Si double dot with >6 dB suppression to 5 kHz; **CNOT gate modeling** in Ge/GeSi quantifies nonadiabatic and charge-noise limits; and **emergent Z₃ parafermions** in triangular triple dots are shown to be tunably relocatable. Theory contributions include **Kubo–Thermalization correspondence**, **Jensen–Mercer two-sided entropy production bounds**, **thermodynamic circuit complexity**, and **hidden Fisher information** revealing readout-complexity bottlenecks in many-body sensors.

- [Dephasing-powered open quantum-dot battery](https://arxiv.org/abs/2610.33408)
- [Zeptojoule Microwave Calorimetry with Nanosecond Recovery in Graphene](https://arxiv.org/abs/2610.33414)
- [Real-Time Correlation of Relaxation, Dephasing, and Two-level System Dynamics in Transmon Qubits](https://arxiv.org/abs/2610.34485)
- [Coherence protection of a silicon hole spin qubit with phase-modulated microwave driving](https://arxiv.org/abs/2608.19696)
- [Real-Time FPGA-Based Multi-Parameter Feedback Stabilization of a Silicon Double Quantum Dot](https://arxiv.org/abs/2608.10325)
- [Modeling the CNOT gate in Germanium double quantum dots](https://arxiv.org/abs/2610.35799)
- [Emergent parafermions with tunable localization in a quantum circuit network](https://arxiv.org/abs/2610.33815)
- [The Kubo-Thermalization Correspondence](https://arxiv.org/abs/2605.06666)
- [Jensen-Mercer two-sided bounds for entropy production rate](https://arxiv.org/abs/2610.34112)
- [The Thermodynamic Complexity of Circuits](https://arxiv.org/abs/2610.33193)
- [Hidden Fisher Information in Many-Body Quantum Sensors](https://arxiv.org/abs/2610.33893)
- [Parametrically Enhanced Ergotropy and Charging Power in a Three-Mode Bosonic Quantum Battery](https://arxiv.org/abs/2610.35734)

## Spintronics, Magnonics, and Orbitronics

Observations of a **spontaneous magnetic diode effect** in Co₁/₃TaS₂ show chirality-controlled nonreciprocity from noncoplanar spin texture, reversed by magnetic handedness. **Synthetic staggered fields** enable room-temperature Néel vector switching at 7.4×10⁹ A/m², the lowest reported, with resonance-based electrical detection. **Interfacial orbital Rashba-Edelstein effect** in CoO/Cu/Pt trilayers establishes Cu-oxide interfaces as reproducible orbital current sources; a complementary study argues orbital currents are **local and spin-mediated** in Ni/Ti/Au, challenging long-range orbital transport assumptions. A **magnetoelectric exchange spring** in BaTiO₃/LSMO achieves attojoule-level spin-wave control and 16 Boolean logic gates. **SiC substrates** enable thick-NiFe SHNOs with 13.1 pW and Q = 23,000. Higher-harmonic spin-wave excitation via **superconducting vortex antennas** is demonstrated. In sliding multiferroic Fe₃GaTe₂, **charge-spin conversion is ferroelectric-switchable**, and a comparison of Fe₃GaTe₂/Fe₃GeTe₂ Edelstein responses isolates chemical substitution effects. **Pseudoangular momentum matching** governs selective magnon-phonon hybridization.

- [Spontaneous magnetic diode effect in Co1/3TaS2](https://arxiv.org/abs/2610.34586)
- [Synthetic staggered fields switch Neel vectors probed by magnetic resonance](https://arxiv.org/abs/2610.34624)
- [Interfacial Orbital Rashba Edelstein Effect Identified in CoO/Cu/Pt Trilayers](https://arxiv.org/abs/2610.34292)
- [Orbitronics: orbit-spin interconversions for long range orbital propagation enabled by spin current](https://arxiv.org/abs/2603.28075)
- [Magnetoelectric Exchange Spring for Spin-Wave Logic with Ultralow Energy Consumption](https://arxiv.org/abs/2610.34693)
- [High-Q, high-power spin Hall nano-oscillators with thick NiFe layers enabled by SiC substrates](https://arxiv.org/abs/2610.35245)
- [Higher-harmonic spin-wave excitation by a superconducting antenna with vortices](https://arxiv.org/abs/2610.35268)
- [Controllable charge-spin conversion in sliding multiferroic metal Fe3GaTe2](https://arxiv.org/abs/2610.34295)
- [Edelstein Effect in Ferromagnetic Monolayers Fe3GaTe2 and Fe3GeTe2](https://arxiv.org/abs/2610.34296)
- [Equivalent Pseudo-angular Momentum Governs Selective Magnon-Phonon Hybridization](https://arxiv.org/abs/2610.34857)
- [Crystal-surface polarity enables nonreciprocal transport in a centrosymmetric kagome magnet](https://arxiv.org/abs/2610.34312)

## Electron-Phonon Coupling and Phonon Transport

**Soft x-ray ARPES on ScN** resolves a quasiparticle kink at −2.3 eV, phonon satellites, and a −124.3 meV zero-point gap renormalization, with thermal expansion and e-ph coupling contributing comparably to the anomalous gap increase. **Chiral phonon coupling to PT-partner states** in bilayer MoS₂ shows helicity-selective interaction via a pseudospin-like mechanism. **Raman/PL thermometry of monolayer WS₂** spans 5–1273 K with distinct lattice-anharmonicity and bandgap-renormalization indicators. In thermal transport, an **electrochemical intercalation switch** in Li_aZrS₂ achieves cross-plane κ reduction from 3.7 to 0.05 W/m·K; **CsAg₃S₂** shows simultaneous suppression of particle- and wave-like channels with a temperature-driven crossover; and a **nonlocal Einstein relation** is derived for confined phonon hydrodynamics.

- [Phonon-Dressed Quasiparticles in Epitaxial Scandium Nitride Resolved by Soft X-ray ARPES](https://arxiv.org/abs/2610.33533)
- [Helicity-Selective Electron-Phonon Coupling Between PT-Partner States in 2H-bilayer MoS2](https://arxiv.org/abs/2610.34830)
- [Optical Thermometry in Monolayer WS2: Raman and Photoluminescence Spectroscopy from 5 K to 1273 K](https://arxiv.org/abs/2610.35214)
- [High-efficiency solid-state electrochemical thermal switching through phonon engineering of 2D materials](https://arxiv.org/abs/2610.35547)
- [Simultaneous suppression and temperature-driven crossover of particle-like and wave-like thermal transport in trigonal CsAg3S2](https://arxiv.org/abs/2610.35360)
- [Nonlocal Einstein Relation in Confined Phonon Hydrodynamics](https://arxiv.org/abs/2610.35109)
- [Phonon-assisted shift-current from first-principles: application to AlN monolayer](https://arxiv.org/abs/2610.35662)

## Soft Matter, Active Matter, and Nonequilibrium Dynamics

**Bacteria-driven droplet rotation** in a 3D aqueous two-phase system is reported, with an R⁻¹ scaling law from collective interfacial swimming; a companion paper shows **motility–wetting coupling** controls LLPS morphology and coalescence. **Elasto-plastocapillarity** is introduced as a framework for yield-stress fluid free-surface flows. A **universal constitutive relation for static droplet retention** is validated across liquids and volumes. In colloidal systems, **bimodal depletion gels** are mapped onto the monodisperse phase diagram via a contact-weighted second virial coefficient, and **CB-CMC hydrogels** exhibit generalized time-aging and time-shear-rate superposition principles. A study of **homogeneous vs. shear-banded yielding** (Carbopol vs. emulsion) finds shared ballistic/Fickian ingredients but different statistics. Additional results: **salt creeping as a relaxation oscillator**, a **microscopically derived stochastic thin-film equation**, and **interfacial defecets** in elastic sheets.

- [Interfacial bacteria-driven rotation of free-floating active droplets](https://arxiv.org/abs/2610.35242)
- [Active motility and wetting cooperatively regulate liquid-liquid phase separation](https://arxiv.org/abs/2511.18077)
- [Elasto-Plastocapillarity: Surface-Tension-Driven Flows of Yield-Stress Fluids](https://arxiv.org/abs/2610.33345)
- [A Universal Constitutive Relation for Static Droplet Retention](https://arxiv.org/abs/2610.33100)
- [Mapping bimodal colloidal depletion systems onto the monodisperse gelation phase diagram](https://arxiv.org/abs/2610.33394)
- [Aging dynamics and generalized superposition principles in carbon black-carboxymethylcellulose hydrogels](https://arxiv.org/abs/2610.33682)
- [Multiscale dynamics in yield stress fluids during homogeneous and shear-banded yielding](https://arxiv.org/abs/2402.00221)
- [Precipitation-dissolution cycling drives intermittent salt creeping](https://arxiv.org/abs/2607.11587)
- [Microscopic Derivation of Stochastic Thin-Film Equation and Extensions to Two-Layer and Evaporating Films](https://arxiv.org/abs/2610.35422)
- [Wrinkling dynamics of thin crystalline sheets and its dependency on topological defects](https://arxiv.org/abs/2610.35786)

## Quantum Dynamics, Floquet Engineering, and Entanglement

**Subsystem periodic driving** of an AA ladder cannot fully delocalize a localized chain; instead a mixed phase appears whose delocalized fraction varies nonmonotonically, explained by local effective Hamiltonians up to a crossover frequency. A **Fibonacci-driven central-spin model** yields long-lived time quasicrystals and Bell-cat/spin-cat generation at Clifford points. The **imaginary-time Mpemba effect** is made controllably exact via local twists acting as mode selectors. A **dynamic helimagnetism** theory shows pure spin currents stabilize static helices and added charge current enables coherently precessing helices with current-tunable chirality. **Multipartite dynamics** are shown to continue after bipartite entanglement equilibration, probing distinct physical channels. **Deep thermalization in free fermions** produces a Gaussian Scrooge ensemble, and a related work connects deep thermalization to resource quantification.

- [Study of localization properties under subsystem periodic driving](https://arxiv.org/abs/2610.33189)
- [Quantum state revivals, time quasicrystals, and entanglement steering in a Fibonacci-driven central-spin model](https://arxiv.org/abs/2610.35555)
- [Twist-controlled imaginary-time Mpemba effect in quantum spin systems](https://arxiv.org/abs/2610.35784)
- [Dynamic helimagnetism via charged spin current](https://arxiv.org/abs/2610.34927)
- [Multipartite dynamics beyond bipartite entanglement equilibration](https://arxiv.org/abs/2610.35377)
- [Gaussian Scrooge Ensemble from Deep Thermalization in Free-Fermions](https://arxiv.org/abs/2610.10279)
- [Deep Thermalization and Measurements of Quantum Resources](https://arxiv.org/abs/2512.09999)
- [The Ising lattice gas and the surface diffusion of CO on Cu(001) at finite coverage](https://arxiv.org/abs/2610.33147)
- [Exact Magnetic Confinement of a Doped Hole by Kinetic Frustration](https://arxiv.org/abs/2610.33585)

## Structural Materials, Alloys, and Synthesis

**Induction-assisted hot rotary swaging** of dual-phase Zr-4Nb-2Al is shown to refine prior-β grains to ~100 μm and develop strong ⟨11-20⟩α fibre texture with tailorable strength–ductility balance. **Ni-Mn-Sn powder** studies decouple particle-size from processing effects, showing single-crystalline particles below ~20–30 μm have near-zero transition width. **PFDD with DFT-derived γ-surfaces** outperforms MD-derived surfaces for stacking-fault width prediction in Cu-Al. A **multiscale Zr/Ta/Ce analysis** covers Ta growth phase maps as a function of O₂ partial pressure (relevant for superconducting circuits), while other work covers Co/Ir/Co trilayer structural-magnetic evolution, Ni on GeSn interfacial stability, and epitaxial D0₁₉ Mn₃Ge growth. **Phase-field dislocation dynamics**, **wetting**, and **ultrahigh-temperature carbide thermal transport** from first principles round out the section.

- [Evolution of microstructure and crystallographic texture in a novel Zr-4Nb-2Al alloy during hot rotary swaging](https://arxiv.org/abs/2610.33247)
- [First-order magnetostructural transition in Ni-Mn-Sn powder - A matter of particle and grain size](https://arxiv.org/abs/2610.33556)
- [Phase field dislocation dynamics prediction of stacking fault widths in Cu-Al Alloys using generalised stacking fault energy from DFT and interatomic potentials](https://arxiv.org/abs/2610.34420)
- [Growth Phase Map of α and β Tantalum as a Function of Growth Temperature and Oxygen Partial Pressure](https://arxiv.org/abs/2610.35768)
- [Co layer Thickness Driven Structural Evolution and Magnetic Behaviour of Co/Ir/Co Trilayers](https://arxiv.org/abs/2610.33595)
- [Investigation of the Microstructural and Magnetic Properties of Ni on GeSn Layers](https://arxiv.org/abs/2610.35273)
- [Optimised growth of epitaxial D019 Mn3Ge(0001) thin films via single target sputtering](https://arxiv.org/abs/2610.34736)
- [First-Principles-Informed Modeling of Thermal Transport and Laser-Induced Heating in Ultrahigh-Temperature Carbides](https://arxiv.org/abs/2610.33838)
- [Eutectic and peritectic equilibria in coherent binary alloys](https://arxiv.org/abs/2602.15251)
- [Controlling Surface Chemistry in Tin-Lead Perovskites for High-Efficiency Solar Cells](https://arxiv.org/abs/2610.34293)
- [Impact of organic spacer cations on the light and thermal stability of two-dimensional lead halide perovskites](https://arxiv.org/abs/2610.35247)

## 2D Materials and Heterostructures

**Momentum-selective graphene spectroscopy** of moiré excitons shows graphene-rate ratios invert with spacer thickness and that chiral p₊/d₋ states are dark optically but transfer efficiently — enabling near-field momentum-resolved spectroscopy. **Dynamical proximity operators** from DFT downfolding capture energy-dependent exchange resonances in graphene/hBN/Co, intervalley coupling in graphene/PtSe₂, and spatially modulated Rashba/valley-Zeeman SOC in graphene/WSe₂. **STM/STS of Td-MoTe₂** attributes hollow defects to Te vacancies that weakly perturb graphene overlayers, making graphene/MoTe₂ heterostructures defect-tolerant. **Exfoliated tetracene** molecular crystals show thickness-tunable Davydov splitting and Stokes shift, extending dimensional control to molecular 2D materials. A **van der Waals ReS₂/hBN/InSe floating-gate** transistor demonstrates broadband optoelectronic synaptic learning, and **α-MnTe surface termination** is shown to be controllable via substrate-induced surfactants.

- [Momentum-selective graphene spectroscopy of moiré excitons](https://arxiv.org/abs/2610.33989)
- [First-Principles Wannier Representation of Proximity Effects](https://arxiv.org/abs/2607.25690)
- [Nanoscale mapping of native defects in Td-MoTe2 and their impact on graphene-based van der Waals heterostructures](https://arxiv.org/abs/2610.34924)
- [Dimensional Control of Excitonic Interactions in Exfoliated 2D Molecular Crystals](https://arxiv.org/abs/2609.09923)
- [A van der Waals Floating-Gate Platform for Broadband Optoelectronic Neuromorphic Computing](https://arxiv.org/abs/2610.34738)
- [Control of the Electronic and Atomic Structure of the Altermagnetic α-MnTe Surface via Substrate-Induced Surfactants](https://arxiv.org/abs/2610.35236)
- [Anomalous mass renormalization in two-dimensional electron systems on ultra-wide bandgap semiconductor β-Ga2O3](https://arxiv.org/abs/2507.16137)
- [Direct observation of a spin-polarized surface Dirac gap in the antiferromagnetic topological insulator NdBi](https://arxiv.org/abs/2610.35353)

## Defects, Electrochemistry, and Functional Oxides

A **grand-canonical stability map** for vacancies in Si and SiC in contact with water couples charge state to H/O content, showing the bare Si vacancy is never lowest-energy near neutral pH and that hydrogen should not passivate the SiC carbon vacancy except under cathodic bias. **Electrostructural bistability** in TiO₂ is established as a rapid, deterministic defect-engineering route distinct from electrothermal bistability in Si. **First-principles defect calculations** quantify nonradiative capture at N_C and NV centers in diamond, identifying fast capture into excited states. **XAFS + DFT** shows Nb donors lower Co oxidation state in SrTiO₃ and suppress oxygen-vacancy formation. **EPR** reveals annealing-atmosphere control of paramagnetic defects in ZnO. Two ferroelectric surface papers analyze **photoinduced charging and spatially selective photochemistry**, and a PLD-grown **SrTiO₃ shell on TiO₂ nanorods** achieves polarization-controlled charge separation with a volcano-shaped thickness dependence.

- [Charge state and hydration of vacancies in silicon and silicon carbide in contact with water: A grand-canonical first-principles stability map](https://arxiv.org/abs/2610.33469)
- [Harnessing Electrostructural Bistability to Control Defects in Polarizable Materials](https://arxiv.org/abs/2610.33698)
- [Charge dynamics at nitrogen impurities and nitrogen-vacancy centers in diamond](https://arxiv.org/abs/2605.24768)
- [Effect of niobium doping on the local structure and oxidation state of Co atoms in SrTiO3](https://arxiv.org/abs/2610.33680)
- [Annealing-atmosphere control of paramagnetic defects in ZnO microparticles](https://arxiv.org/abs/2610.33870)
- [Photoinduced charging and spatially selective photochemistry on ferroelectric surfaces](https://arxiv.org/abs/2610.34465)
- [Pulsed Laser Deposition of Ferroelectric SrTiO3 Shells Enables Polarization-Controlled Charge Separation in TiO2 Photoanode](https://arxiv.org/abs/2610.35454)
- [First-Principles Investigation of the Structural, Electronic, Optical, Elastic, and Thermoelectric Properties of X2MoSeO6 (X = K, Rb, Cs)](https://arxiv.org/abs/2610.33457)

## Thermodynamics and Statistical Mechanics Foundations

A **hyperensemble framework** generalizes Jaynesian priors to constrained nonequilibrium distributions with analytic predictions testable against superstatistics. **Path-space large deviation theory** on lattices is developed for interacting particle systems, with a large-spin limit yielding lattice analogues of MFT Hamiltonians and connections to integrable spin chains. **A Hamiltonian-level necessary and sufficient condition for Yang-Baxter integrability** (the Reshetikhin condition) is proven, reducing integrability to conservation of the energy current. A derivation of the **second law from equal a priori probabilities** via the phase-space continuity equation is proposed, with explicit boundaries where it fails. Additional results: **Coulomb gas cumulants beyond rotational invariance**, **Shannon entropy as an order parameter** for confined 2D Coulomb systems, and **rigorous absence of hidden analytic conserved quantities** in harmonically confined hard rods.

- [Distributional statistics of nonequilibrium](https://arxiv.org/abs/2610.33383)
- [Large spin large deviations for interacting particle systems](https://arxiv.org/abs/2610.33523)
- [Path space large deviation on a lattice for interacting particle systems](https://arxiv.org/abs/2610.33524)
- [A Simple Necessary and Sufficient Condition for Yang--Baxter Integrability](https://arxiv.org/abs/2607.29660)
- [Deriving the second law of thermodynamics and exploring its boundaries](https://arxiv.org/abs/2607.28765)
- [Linear statistics in the Coulomb gas: cumulants beyond rotational invariance](https://arxiv.org/abs/2610.33659)
- [Shannon Entropy as an Order Parameter for the Two-Dimensional Confined Coulomb Systems: Exact Balance Law, Topological Charge Sum Rule, and Boundary Saturation](https://arxiv.org/abs/2609.15428)
- [Absence of hidden analytic conserved quantities in harmonically confined rods](https://arxiv.org/abs/2607.18872)
- [Simplified Parisi Ansatz III: Constructive Cavity Method and Ultrametricity](https://arxiv.org/abs/2610.34710)
- [Random Matrix Spectra from Boltzmann-Weighted Lattice Ensembles](https://arxiv.org/abs/2605.21254)

## Optics, Photonics, and Metamaterials

A **static-material Doppler effect** is realized with direction-dependent waveguide networks simulating moving-source compression/expansion, enabling vortex, analogue black hole, and wormhole designs. **Axion quasibound states in the continuum** convert symmetry-protected BICs into axion qBICs, enabling achiral all-optical detection and >10⁵-fold SHG enhancement. **Symmetry-driven in-situ physical adjoint computing** extends beyond reciprocity via three classes of transpose symmetry, and a complementary framework handles **asymmetric couplings** with experiment counts independent of parameter number. **Third-harmonic generation in transition metal trichalcogenides** reveals anisotropy ratios up to 6.5 and a thickness-dependent relaxation of Pe