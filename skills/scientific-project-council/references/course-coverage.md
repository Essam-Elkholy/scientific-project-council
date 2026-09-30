# Course Coverage Standard (PBL and any project with required courses)

In PBL, the course list is the assignment. A technically excellent project that only decorates itself with course names should not pass. This file defines what real coverage means so the Research Architect and the Judge rate it consistently.

## Contents

- The three-part test
- Rating scale
- Artificial-attachment red flags
- Course-by-course guide
- How to handle unlisted or vague courses

## The three-part test

A course counts as covered only to the extent that all three hold:

1. **Concept**: the project applies a core concept of that course (not just a tool from its lab).
2. **Work**: the team performs non-trivial technical work with that concept: designs, derives, implements, tunes, or analyzes something themselves.
3. **Assessable**: a professor of that course could ask about it, see evidence of it (a model, derivation, plot, measurement, experiment), and grade it.

Library use alone does not establish coverage. Reusing a library can still support strong coverage when the students formulate, analyze, compare, and experimentally evaluate the relevant concepts. Assess their work and learning outcomes, not whether every component was written from scratch.

## Rating scale

| Rating | Meaning |
|---|---|
| STRONG | Passes all three parts, and an experiment or analysis in the project depends on it (for example, a control design compared against a baseline controller with measured error). |
| MEDIUM | Real concept and real work, but the analysis is thin or the component is small relative to the whole project. |
| WEAK | Course is present but mostly through tool use or a trivial component; a professor could not grade much beyond "it runs". |
| MISSING | Nothing in the design would need that course's knowledge. |

Do not round up out of politeness. STRONG coverage needs substantial work and assessable evidence. A component need not lie on the system critical path to demonstrate strong coverage; rigorous theoretical analysis, an experiment, or a justified design comparison may suffice under the course rubric.

## Artificial-attachment red flags

- Using a microcontroller only to switch an LED, read one sensor, or forward data does **not** count as strong Embedded Systems coverage. Strong coverage needs things like timing or interrupt design, peripheral configuration, resource-constrained implementation, power or latency measurement.
- Calling a pretrained neural-network API without understanding, training, evaluation, or experimentation may **not** count as strong AI coverage. Strong coverage can involve a defined task, justified model choices, dataset and split, a baseline, metrics, and error analysis; training or fine-tuning is required only when the learning outcomes demand it.
- Displaying sensor values does **not** automatically count as meaningful Signal Processing. Strong coverage needs filtering, sampling or spectral analysis, noise characterization, and measured effect on a downstream result.
- Using a PID library without analysis does **not** automatically count as strong Control Systems coverage. Strong coverage needs plant modeling or identification, controller design and tuning rationale, and measured response (rise time, overshoot, steady-state error) against a baseline.
- A dashboard or app wrapped around finished components does not cover Software Engineering, Databases, or Networks unless architecture, schema, protocol, or testing decisions are made and evaluated.
- Listing a course "for the report" (background chapter, no implementation) is MISSING coverage.

## Course-by-course guide

Use as a calibration aid; adapt to the syllabus the student describes.

| Course area | Looks strong when the project includes | Looks weak when |
|---|---|---|
| Embedded Systems | Firmware architecture, interrupts/timers, peripheral drivers, real-time constraints, memory/power/latency measurements | Board is just a sensor-to-PC bridge or Arduino sketch from a tutorial |
| AI / Machine Learning | Problem formulation, dataset handling and split, justified model analysis or training/fine-tuning, baseline, metrics, ablation or error analysis | Only calls a hosted model or reruns a public notebook |
| Computer Vision | Image pipeline design, classical baseline vs learned model, evaluation on held-out data, robustness tests (lighting, occlusion) | Uses an off-the-shelf detector on a webcam and shows boxes |
| Signal Processing | Sampling/aliasing decisions, filter design, spectral or time-frequency analysis, SNR measurement | Plots raw signal, applies a moving average with no justification |
| Control Systems | Plant model or identification, controller design (PID/state-space/MPC), stability/response analysis, disturbance tests | Tunes a library PID by trial with no metrics |
| Robotics | Kinematics/dynamics, motion planning, localization or perception loop, quantified task success | Remote-controls a kit robot |
| Communications / Networks | Protocol or channel modeling, throughput/latency/BER measurement, comparison of schemes | Sends data over existing Wi-Fi/Bluetooth without measurement |
| Electronics / Circuits | Designed and analyzed circuit (simulation vs measurement), component selection with calculations | Module wired from a datasheet example |
| Power / Energy | Sizing, efficiency measurement, converter or storage analysis | Uses a ready module with no analysis |
| Databases / Software Engineering | Schema/architecture decisions justified, testing, performance or scalability evaluation | CRUD app without evaluation |
| Biomedical | Signal acquisition and conditioning, validation against a reference device or dataset, clinically relevant metrics | Displays a sensor number with no validation |
| Mechanical | Design calculations, simulation/FEA, prototype testing against predicted values | CAD model with no analysis |

## Unlisted or vague courses

- If the required course list is UNKNOWN, report that course coverage cannot yet be assessed; do not invent course requirements. For a PBL proposal this blocks unconditional approval, but other parts can still be evaluated. Ask only if the missing information fundamentally prevents a useful evaluation.
- If the student gave course names but no syllabus, judge against the standard content of that course and say that this is an assumption; invite the student to correct it with syllabus topics.
- If the professor's requirement is only a topic ("must include AI"), treat that as one required area and apply the same three-part test.
- A project may cover fewer courses well rather than many superficially. When there are too many courses to integrate in one semester, say which courses can be strong, which realistically end WEAK, and recommend cutting scope or negotiating the course list; do not fake coverage to make the list fit.

## FPGA image-processing example

This is an assessment example, not a verdict on a particular proposal.

| Area | Assessable student work | Evidence | Superficial substitute |
| --- | --- | --- | --- |
| Digital Design / FPGA | Design a streaming datapath, line buffers, fixed-point arithmetic, and control; verify boundary handling and overflow | RTL simulation against a software reference, synthesis resource/timing reports, and measured throughput | Run an existing FPGA example without explaining or evaluating it |
| Image Processing | Explain filtering and Sobel gradients; investigate noise, quantization, thresholds, and boundaries | Controlled comparisons with the original image and a justified software baseline | Display an edge image without measuring or analyzing anything |
| Hardware-software integration | Specify the transfer format, buffering, and throughput requirements | End-to-end latency including transfer overhead, throughput, and error checks | Ignore communication time when claiming acceleration |
| Medical image-analysis objective | Define a dataset-specific localization task and evaluate a separate proposed localization method | Appropriate ground truth, held-out evaluation, a baseline, and error analysis | Treat a Sobel edge map as proof of tumor localization |

Do not infer clinical capability from an image-filter demonstration. Treat any downstream localization claim as a separate unproven objective requiring evidence. A course-level hardware project can be academically meaningful without asserting diagnostic performance.
