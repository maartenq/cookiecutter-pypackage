# tests/{{ cookiecutter.project_slug }}/test_main.py
# vim: ai et ts=4 sw=4 sts=4 ft=python fileencoding=utf-8


from {{cookiecutter.project_slug}} import main


def test_main_has_a_doc_string():
    assert main.__doc__
