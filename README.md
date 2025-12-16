# axis_doc_tool

Portable, read-only documentation tool for Axis network cameras. Generates per-camera reports and a site summary (Markdown/TXT, optional PDF), intended to speed up field work and provide reliable “metadata” for filling and signing official protocols.

## Status

Early development. The repo contains planning documents and scaffolding. Core functionality is under active implementation.

## What it does (intended)

- Connects to Axis cameras (read-only)
- Collects technical configuration and status via Axis APIs (VAPIX)
- Prompts technician for human-only installation metadata (location, mount, direction/FOV, etc.)
- Generates:
  - One report per camera (Markdown; optional TXT/PDF)
  - One site summary report (Markdown; optional TXT/PDF)
- Optional **snapshot capture** (off by default):
  - Multi-lens/multi-sensor: 1 image per lens + 1 group view *if available*
  - PTZ: 1 image in Home + 1 image per preset
  - No night images / no day-night pairs

## What it does NOT do

- Does not modify camera configuration
- Does not claim to verify physical checks, visual quality, customer acceptance, or handover steps
- Does not handle night-image capture logic

## Run modes (intended)

- Single IP: `192.168.0.90`
- Group/range: `192.168.0.90-95`
- Batch list: `192.168.0.90, 192.168.0.96, 192.168.0.98`
- Scan mode (discover devices in subnet)
- Audit mode (compare against stored snapshot)

## Security / snapshot safety

Snapshot capture is optional and requires an explicit technician confirmation step to avoid accidental capture. Images are stored locally alongside the report outputs and are referenced by link in Markdown (not embedded by default).

## Requirements

- Python 3.10+ (developed on Python 3.13)
- Network access to target cameras

## Install (development)

From the repo root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
