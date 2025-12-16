folder_structure v1.1

axis_doc_tool/
├─ README.md
├─ LICENSE
├─ CHANGELOG.md
├─ pyproject.toml
├─ .gitignore
├─ .editorconfig
├─ ruff.toml
├─ mypy.ini
├─ pytest.ini

├─ docs/
│  ├─ axis_doc_tool_plan.md          # now v1.1
│  ├─ Protocol_Coverage_Matrix.md
│  ├─ folder_structure.md
│  ├─ examples/
│  │  ├─ sample_output_camera.md
│  │  ├─ sample_output_site_summary.md
│  │  ├─ sample_snapshot_layout/
│  │  │  ├─ lens_1.jpg
│  │  │  ├─ lens_2.jpg
│  │  │  ├─ group_view.jpg
│  │  │  ├─ ptz_home.jpg
│  │  │  └─ preset_gate.jpg
│  │  └─ sample_snapshot.json
│  └─ screenshots/

├─ scripts/
│  ├─ dev_run_single.sh
│  ├─ dev_run_scan.sh
│  └─ dev_make_pdf_demo.sh

├─ src/
│  └─ axis_doc/
│     ├─ __init__.py
│     ├─ __main__.py                 # python -m axis_doc
│     ├─ cli.py                      # CLI entrypoint
│     ├─ tui.py                      # Rich-based TUI
│     ├─ app.py                      # orchestration layer
│     ├─ config.py                   # runtime config + defaults
│     ├─ localization.py             # language handling
│     ├─ ipparse.py                  # single/group/batch parsing
│     ├─ discovery.py                # scan mode
│     ├─ audit.py                    # audit mode (incl snapshot diff)
│     ├─ logging_setup.py
│     ├─ errors.py
│     │  
│     ├─ models/
│     │  ├─ __pychache__
│     │  ├─ __init__.py
│     │  ├─ camera_doc.py            # CameraDocumentation
│     │  ├─ snapshot.py              # snapshot metadata + schema
│     │  └─ capabilities.py          # resolved capabilities per camera

│     ├─ axis/
│     │  ├─ __init__.py
│     │  ├─ client.py                # AxisDeviceClient
│     │  ├─ endpoints.py             # endpoint registry
│     │  ├─ parsers.py               # VAPIX → models
│     │  └─ capabilities.py          # Axis-reported capabilities

│     ├─ collector/
│     │  ├─ __init__.py
│     │  ├─ collector.py             # builds CameraDocumentation
│     │  ├─ prompts.py               # technician questions
│     │  └─ snapshot_flow.py         # when/if snapshots are taken

│     ├─ snapshot/
│     │  ├─ __init__.py
│     │  ├─ controller.py            # high-level snapshot orchestration
│     │  ├─ vapix.py                 # VAPIX snapshot calls
│     │  ├─ ptz.py                   # home + preset handling
│     │  ├─ multisensor.py           # per-lens + group view logic
│     │  ├─ naming.py                # filenames + folder layout
│     │  └─ guards.py                # random-word confirmation, safety checks

│     ├─ render/
│     │  ├─ __init__.py
│     │  ├─ renderer.py
│     │  ├─ markdown.py
│     │  ├─ pdf.py
│     │  └─ templates/
│     │     ├─ camera_report.md.j2
│     │     ├─ site_summary.md.j2
│     │     └─ audit_report.md.j2

│     └─ locales/
│        ├─ sv-SE.yml
│        └─ en-US.yml

└─ tests/
   ├─ test_ipparse.py
   ├─ test_localization.py
   ├─ test_models_validation.py
   ├─ test_render_markdown.py
   ├─ test_audit_diff.py
   ├─ test_snapshot_guard.py
   ├─ test_snapshot_naming.py
   ├─ test_snapshot_capabilities.py
   └─ axis_fixtures/
      ├─ vapix_systeminfo.xml
      ├─ vapix_params.txt
      ├─ sample_plainconfig.txt
      └─ sample_snapshot_response.jpg
