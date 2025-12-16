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
│  ├─ axis_doc_tool_plan.md
│  ├─ Protocol_Coverage_Matrix.md
│  ├─ examples/
│  │  ├─ sample_output_camera.md
│  │  ├─ sample_output_site_summary.md
│  │  └─ sample_snapshot.json
│  └─ screenshots/
├─ scripts/
│  ├─ dev_run_single.sh
│  ├─ dev_run_scan.sh
│  └─ dev_make_pdf_demo.sh
├─ src/
│  └─ axis_doc/
│     ├─ __init__.py
│     ├─ __main__.py              # enables: python -m axis_doc
│     ├─ cli.py                   # CLI entrypoint + argument parsing
│     ├─ tui.py                   # Rich-based TUI flow (wizard/screens)
│     ├─ app.py                   # orchestrator (common flow used by CLI+TUI)
│     ├─ config.py                # load/save tool config, defaults, paths
│     ├─ localization.py          # language selection + translations
│     ├─ ipparse.py               # parse single/group/batch + validation
│     ├─ discovery.py             # scan mode (optional probing + selection list)
│     ├─ audit.py                 # audit mode: snapshot compare + diff reporting
│     ├─ logging_setup.py         # consistent logging config
│     ├─ errors.py                # custom exceptions
│     ├─ models/
│     │  ├─ __init__.py
│     │  ├─ camera_doc.py         # CameraDocumentation + nested models
│     │  └─ snapshot.py           # snapshot schema + versioning
│     ├─ axis/
│     │  ├─ __init__.py
│     │  ├─ client.py             # AxisDeviceClient (HTTP, auth, retries)
│     │  ├─ endpoints.py          # endpoint registry + feature flags
│     │  ├─ parsers.py            # parse raw API responses to models
│     │  └─ capabilities.py       # model/firmware capability detection
│     ├─ collector/
│     │  ├─ __init__.py
│     │  ├─ collector.py          # CameraInfoCollector (builds CameraDocumentation)
│     │  └─ prompts.py            # technician-input questions (language-aware)
│     ├─ render/
│     │  ├─ __init__.py
│     │  ├─ renderer.py           # renders per-camera + site summary
│     │  ├─ markdown.py           # md generation helpers (tables, sections)
│     │  ├─ pdf.py                # optional PDF rendering adapter
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
   └─ axis_fixtures/
      ├─ vapix_systeminfo.xml
      ├─ vapix_params.txt
      └─ sample_plainconfig.txt
    
