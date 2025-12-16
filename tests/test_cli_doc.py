from axis_doc.app import App


def test_cli_doc_generates_markdown():
    app = App()
    result = app.run(mode="cli-doc", targets_text="192.168.1.10-12 192.168.1.0/30")
    assert result.exit_code == 0
    assert result.ok is True


def test_cli_doc_rejects_all_invalid():
    app = App()
    result = app.run(mode="cli-doc", targets_text="junk not_an_ip")
    assert result.exit_code == 2
    assert result.ok is False
