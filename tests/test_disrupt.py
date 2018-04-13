# -*- coding: utf-8 -*-
import pytest


def test_help_message(testdir):
    result = testdir.runpytest(
        '--markers',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '@pytest.mark.disrupt*'
    ])


def test_disrupt_marker(testdir):
    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest

        @pytest.mark.disrupt('reboot','hostname')
        def test_disrupt_mark():
            assert True
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_disrupt_marker.py::test_disrupt_mark PASSED*',
    ])

    assert result.ret == 0


@pytest.mark.disrupt('reboot', 'hostname')
def test_real_disrupt_marker():
    assert True
