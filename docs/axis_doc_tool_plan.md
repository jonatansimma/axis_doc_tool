# axis_doc_tool – Full Planning Document

*Version 1.1 – Functional Specification*

---

## 1. Purpose and Scope

### 1.1 Primary purpose

`axis_doc_tool` is a **portable, Python-based post-installation documentation tool** for Axis network cameras. The tool automatically gathers as much technical information as possible via Axis APIs and combines it with minimal technician-provided metadata to generate consistent, high-quality documentation.

The tool is designed to be:

* Lightweight
* Read-only (no configuration changes)
* Easy to deploy on new systems
* Suitable for both single-camera and multi-camera sites

### 1.2 Output formats

Supported output formats:

* **Markdown (.md)** – primary and canonical format
* **Plain text (.txt)** – simplified fallback
* **PDF (.pdf)** – optional rendered output

HTML output is **explicitly excluded**.

### 1.3 Valfri kamerabild (Snapshot) – fältfunktion (v1.1)

Snapshot-stöd ingår från v1.1 som en **valfri** funktion som är **avstängd som standard**.

När snapshot är aktiverat kan verktyget hämta **stillbilder från kameran** och spara dem lokalt tillsammans med rapporten.

Krav och regler:

* **Alltid manuell opt-in** per körning och/eller per kamera (TUI/CLI)
* **Extra bekräftelse** innan bild tas: teknikern måste skriva in ett slumpat ord från en lista (för att förhindra oavsiktliga klick/Enter-spam)
* **Endast vid tillfället** (inga natt-bilder eller väntelogik)
* Bilder **länkas** från Markdown (inte inbäddning som standard)

Snapshot-varianter (ingen nattlogik, endast när teknikern kör verktyget):

* **Enkel kamera (en sensor/lins):** 1 bild
* **Multisensor/multilins:** 1 bild per lins/sensor + 1 "gruppvy" (om kameran exponerar en sammansatt vy). Om gruppvy inte finns dokumenteras detta tydligt i rapporten.
* **PTZ:** 1 bild i "Home" + 1 bild per **Preset-position** (alla presets som finns vid körningstillfället, alternativt ett urval om teknikern väljer det i TUI).

Obs: Snapshots används som dokumentationsunderlag och **är inte ett bevis på verifierad bildkvalitet eller korrekt maskning**.

### 1.4 Functional focus

* Automated data collection using Axis APIs (VAPIX primarily)
* Minimal human-assisted input for physical installation details
* Per-camera documentation
* Mandatory site summary documentation
* Optional audit / verification functionality

### 1.5 Non-goals

* No camera configuration or modification
* No video processing or live preview
* No database backend
* No heavy system dependencies

---

## 2. Operation Modes

All camera targets are entered **manually by the user**. No CSV or YAML files are used for IP input.

### 2.1 Single-IP Mode

Input:

```
192.168.0.90
```

Processes exactly one camera.

### 2.2 Group-IP Mode (contiguous range)

Input:

```
192.168.0.90-95
```

Expands to all IPs in the range.

### 2.3 Batch-IP Mode (non-adjacent IPs)

Input:

```
192.168.0.90, 192.168.0.96, 192.168.0.98
```

Processes multiple cameras in the same subnet.

### 2.4 Scan Mode

* User specifies a subnet (e.g. `192.168.0.0/24`)
* Tool probes the subnet for Axis devices
* Discovered devices are presented in the TUI for selection

### 2.5 Audit Mode

* Loads a previously stored JSON snapshot
* Queries live camera state
* Compares current values against stored documentation
* Reports differences for compliance and inspection purposes

---

## 3. User Interface Design

### 3.1 Interface approach

The tool uses a **Rich-based TUI** layered on top of a full CLI implementation.

* TUI is the default interactive interface
* CLI provides full feature parity for automation
* TUI is optional and non-blocking

### 3.2 TUI features

* Language selection screen
* IP input wizard (Single / Group / Batch / Scan)
* Credential entry (once per session)
* Camera discovery and selection list
* Progress display per camera
* Human-input wizard for physical installation data
* **Snapshot prompt (optional):** opt-in + “random word” confirmation before capture
* Completion summary with output file paths

### 3.3 Fallback rules

* If Rich rendering is unavailable, the tool falls back to CLI prompts
* All TUI actions map directly to CLI flags or prompts

---

## 4. Information Collected

### 4.1 Identity and Hardware

**From API:**

* Camera model
* Serial number
* MAC address
* Axis OS / firmware version
* Hardware revision (if available)
* Device hostname

**From technician:**

* Site name
* Building and floor
* Room / area
* Mounting type (wall / ceiling / pole / other)
* Mounting height
* Direction / field of view description
* Free-text notes

---

### 4.2 Network and Security

**From API:**

* IPv4 / IPv6 address
* Subnet mask
* Default gateway
* DNS servers
* NTP configuration and sync state
* HTTPS status
* Certificate subject and validity
* Enabled services (HTTP, HTTPS, ONVIF, SNMP, MQTT, SSH, etc.)

**From technician:**

* VLAN ID
* Switch name and port

---

### 4.3 Video and Image Configuration

**From API:**

* Capture mode (resolution / aspect)
* Stream profiles (codec, resolution, FPS, bitrate/compression)
* WDR status and level
* Day/night mode and thresholds
* IR illumination mode and intensity
* Exposure mode and parameters
* Orientation (rotation / flip)
* Privacy masks
* Overlays (text and image)

---

### 4.4 PTZ and Multi-Sensor (if supported)

**From API:**

* Presets
* Guard tours
* PTZ limits
* Compass orientation
* Autotracking / gatekeeper settings
* Multi-sensor channel data

---

### 4.5 Storage and Recording

**From API:**

* SD card presence, size, usage, health
* NAS / edge storage configuration
* Camera-side recording rules (if visible)

**From technician:**

* Recording expectations when VMS-controlled

---

### 4.6 Events and Analytics

**From API:**

* Event rules (triggers and actions)
* Installed ACAP applications
* Analytics configuration where readable

---

### 4.7 Health and Maintenance

**From API:**

* Firmware version
* Uptime
* Temperature (if supported)
* Last reboot reason
* Critical warnings

**From technician:**

* Installation date
* Technician name / initials
* Project or work-order ID

---

### 4.8 Snapshots (optional, v1.1)

**From API (when enabled):**

* Snapshot(s) captured at runtime
* Capture timestamp per image
* Capture mode used (single / per-lens / PTZ home+presets)

**From tool (generated):**

* File paths to saved images
* Capture status (ok/failed) + error message (if any)

**Rules:**

* Ingen hantering av nattläge (inga extra väntetider, inga dag/natt-par). Bilder tas när teknikern är på plats och kör verktyget.
* Snapshots är dokumentationsunderlag och innebär inte att bildkvalitet/maskning är verifierad.

---

## 5. Language Support

* Tool supports multiple languages for:

  * TUI interface
  * Generated documentation
  * Section headers and standard phrasing

* Language selected at startup

* Implemented using external translation files (`locales/`)

* Default language: English

---

## 6. Output Structure

### 6.1 Per-Camera Documentation (Markdown)

Sections:

1. Header
2. Identity & Installation
3. Network & Security
4. Video & Image Settings
5. PTZ / Multi-Sensor (if applicable)
6. Storage & Recording
7. Events & Analytics
8. Health & Maintenance
9. Snapshots (if enabled)

**Snapshot section rules:**

* Markdown contains **links** to saved image files (default)
* Report must state that snapshots are "captured at time" and not a verification

---

### 6.2 Snapshot file structure (v1.1)

When enabled, snapshots are saved under the camera’s output folder:

* Single-sensor camera:

  * `snapshots/snapshot.jpg`

* Multi-sensor / multi-lens:

  * `snapshots/lens_01.jpg`
  * `snapshots/lens_02.jpg`
  * …
  * `snapshots/group_view.jpg` *(if available)*

* PTZ:

  * `snapshots/ptz_home.jpg`
  * `snapshots/preset_<preset-name-sanitized>.jpg` *(en per preset; kan vara "alla" eller ett tekniker-val via TUI)*

Filename rules:

* Preset names are sanitized (a–z, 0–9, dash/underscore)
* On collision, append an incrementing suffix

---

### 6.3 Site Summary Document (Mandatory)

Includes a table with the following columns:

* Camera name
* IP address
* Subnet mask
* Default gateway
* Model
* Serial number
* MAC address
* Location
* Direction / field of view

Followed by:

* Storage architecture summary
* Analytics coverage summary
* Event routing summary

---

## 7. Internal Architecture (OOP)

### 7.1 Core Modules

* `client.py` – AxisDeviceClient (API communication)
* `models.py` – Data models (CameraDocumentation and sub-models)
* `collector.py` – Combines API data and technician input
* `renderer.py` – Markdown and PDF generation
* `localization.py` – Language and translation handling

**Added in v1.1 (Snapshots):**

* `axis/snapshot.py` – SnapshotCapture (fetches and saves still images)
* `models/snapshot.py` – Snapshot model and status fields

### 7.2 Interfaces

* `tui.py` – Rich-based interactive interface
* `cli.py` – Full CLI alternative for automation

---

## 8. Prerequisites and Distribution

### 8.1 Requirements

* Python ≥ 3.10
* requests
* rich
* jinja2
* pydantic (or dataclasses)
* pyyaml
* Optional: PDF rendering dependency

### 8.2 Deployment

* pip / pipx installation
* Virtual environment friendly
* Optional single-file `.pyz` distribution later

No administrator privileges required.

---

## 9. High-Level Workflow

1. Start tool → select language
2. Choose operation mode (Single / Group / Batch / Scan / Audit)
3. Enter credentials
4. Select cameras
5. Automatic data collection
6. Technician completes installation details
7. **Optional:** teknikern aktiverar snapshots → slump-ord-bekräftelse → capture (single/per-lens + ev. gruppvy / PTZ home + presets)
8. Generate documentation outputs
9. Optional snapshot JSON saved for audit use

---

*End of planning document*
