# {{ cookiecutter.project_slug }}/__init__.py
# vim: ai et ts=4 sw=4 sts=4 ft=python fileencoding=utf-8

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

# Version set by setuptools_scm
try:
    from importlib.metadata import version
except ImportError:
    # Python version < 3.8
    from pkg_resources import get_distribution

    __version__ = get_distribution('{{ cookiecutter.project_slug }}').version
else:
    __version__ = version('{{ cookiecutter.project_slug }}')
