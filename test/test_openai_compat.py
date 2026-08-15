from types import SimpleNamespace

from scripts.test_openai_compat import stream_delta_content


def test_stream_delta_content_ignores_empty_choices_event():
    assert stream_delta_content(SimpleNamespace(choices=[])) is None
    assert stream_delta_content(SimpleNamespace(choices=None)) is None


def test_stream_delta_content_reads_content_when_present():
    chunk = SimpleNamespace(
        choices=[SimpleNamespace(delta=SimpleNamespace(content="成功"))]
    )

    assert stream_delta_content(chunk) == "成功"
