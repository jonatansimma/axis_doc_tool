# axis_doc_tool

Portable, read-only documentation tool for Axis network cameras.  
Generates per-camera documentation and a mandatory site summary to support faster, more consistent field work and provide reliable **metadata** for filling in and signing official protocols.

---

## Status

Early development.  
The repository currently contains planning documents, protocol mappings, and project scaffolding. Core functionality is under active implementation.

---

## Purpose

`axis_doc_tool` is intended to:

- Collect as much **technical configuration data as possible automatically** via Axis APIs
- Combine this with **minimal technician-provided metadata**
- Produce **clear, consistent documentation** suitable as underlay for official protocols

The tool is explicitly designed to be:

- Lightweight
- Portable
- Read-only (no configuration changes)
- Safe to run on-site and in controlled environments

---

## What the tool does

- Connects to Axis network cameras using read-only APIs (VAPIX)
- Collects:
  - Identity and hardware data
  - Network and security configuration
  - Video, image, PTZ, and analytics configuration
  - Health and status information
- Prompts the technician for:
  - Physical installation details
  - Location and field-of-view descriptions
- Generates:
  - One documentation report per camera
  - One mandatory site summary report

Supported output formats:
- **Markdown (.md)** – canonical format
- **Plain text (.txt)** – simplified fallback
- **PDF (.pdf)** – optional rendered output

HTML output is intentionally **not supported**.

---

## What the tool does NOT do

- Does not modify camera configuration
- Does not perform live viewing or video streaming
- Does not verify image quality, focus, masking, or framing
- Does not replace physical inspection or functional testing
- Does not replace official protocols or signatures

---

## Operation modes (intended)

- **Single IP**
192.168.0.90

- **Group / range**
192.168.0.90-95

- **Batch (non-adjacent)**
192.168.0.90, 192.168.0.96, 192.168.0.98

- **Scan mode**
- Probe a subnet and select discovered Axis devices

- **Audit mode**
- Compare live camera state against a previously stored snapshot

All camera targets are entered manually.  
No CSV or YAML files are used for IP input.

---

## Snapshot support (optional, v1.1)

From version **1.1**, `axis_doc_tool` includes **optional snapshot (still image) capture** as a **field-time documentation aid**.

Snapshot capture is:

- **Disabled by default**
- **Read-only**
- Intended to provide **documentation underlay**, not verification

The tool makes **no claims** about:
- image quality validation
- correct masking
- customer acceptance
- physical or visual inspection

---

## When snapshots are captured

Snapshots are taken **only when the technician is on site and actively running the tool**.

Rules:
- Always **manual opt-in**
- **Extra confirmation** before capture (random-word confirmation)
- **No night images**
- **No day/night image pairs**
- Images are **linked** from Markdown reports (not embedded by default)

Snapshots are stored locally together with the generated documentation.

---

## Snapshot variants

Depending on camera capabilities, the following snapshot types are supported:

### Single-sensor camera
- **1 image**

### Multi-sensor / multi-lens camera
- **1 image per lens/sensor**
- **+ 1 group view** *if the camera exposes a composite view*
- If no group view is available, this is explicitly noted in the report

### PTZ camera
- **1 image in Home position**
- **+ 1 image per preset position**

---

## Snapshot limitations (explicit non-goals)

Snapshots:

- Do **not** replace physical inspection
- Do **not** imply correct focus, exposure, or framing
- Do **not** imply correct privacy masking
- Do **not** replace official test images required by local procedures

They exist solely to support faster, more consistent documentation.

---

## Protocol alignment

Snapshot capture supports the protocol rows commonly phrased as:

- **“Testbild sparad”** (Protokoll – Enskild Kamera)
- **“Testbild sparad (om tillämpligt)”** (Protokoll – Anläggning)

When snapshots are enabled, the report includes:
- snapshot status (captured / failed)
- file paths to the saved images

Final responsibility for protocol sign-off **always remains with the technician**.

---

## Output layout (intended)

Example:
output/
<site-name>/
site_summary.md
camera-192.168.0.90/
camera_report.md
snapshots/
lens_01.jpg
lens_02.jpg
group_view.jpg

---

## Requirements

- Python **3.10+** (developed on Python 3.13)
- Network access to target cameras

Core dependencies include:
- requests
- rich
- jinja2
- pydantic
- PyYAML

---

## Install (development)

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Optional extras:
```bash
pip install -e ".[dev]"
pip install -e ".[pdf]"
```

---

## Run (development)

Once entry points are implemented:
```bash
axis-doc --help
axis-doc-tui
```
Or as a module:
```bash
python -m axis_doc --help
```

---

## Documentation

- Full planning document: docs/axis_doc_tool_plan.md (v1.1)
- Protocol coverage matrix: docs/Protocol_Coverage_Matrix.md

---

## License
See LICENSE

---

This project is intended as an internal technical aid for Axis camera documentation workflows.
