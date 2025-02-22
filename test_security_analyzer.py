import pytest
from security_analyzer import SecurityAnalyzer

def test_exec_detection():
    code = "exec('malicious_code')"
    sa = SecurityAnalyzer(code)
    sa.analyze_security()
    assert any("exec" in v for v in sa.vulnerabilities)

def test_hardcoded_credentials():
    code = "api_key='12345'"
    sa = SecurityAnalyzer(code)
    sa.analyze_security()
    assert any("Hardcoded credentials" in v for v in sa.vulnerabilities)
