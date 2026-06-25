# 1.5.0 - 2026-06-25

## Summary

## Security Issues

This release fixes vulnerabilities by updating dependencies:

| Dependency | Vulnerability | Affected | Fixed in |
|------------|---------------|----------|----------|
| cryptography | GHSA-537c-gmf6-5ccf | 47.0.0 | 48.0.1 |
| gitpython | GHSA-mv93-w799-cj2w | 3.1.49 | 3.1.50 |
| idna | PYSEC-2026-215 | 3.13 | 3.15 |
| msgpack | GHSA-6v7p-g79w-8964 | 1.1.2 | 1.2.1 |
| pip | PYSEC-2026-196 | 26.1 | 26.1.2 |
| tornado | CVE-2026-49854 | 6.5.5 | 6.5.6 |
| tornado | CVE-2026-49853 | 6.5.5 | 6.5.6 |
| tornado | CVE-2026-49855 | 6.5.5 | 6.5.6 |
| tornado | GHSA-pw6j-qg29-8w7f | 6.5.5 | 6.5.7 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-141 | 2.6.3 | 2.7.0 |

## Refactoring

* #25: Updated to `exasol-toolbox` 8.1.1
* #6: Updated mypy checks to include all packages from Exasol
* #31: Updated to `exasol-toolbox` 8.2.0
* #27: Fixed SonarQube warnings
* #34: Fixed SonarQube Cloud warning
* #39: Updated to `exasol-toolbox` 9.0.0
* #41: Updated to `exasol-toolbox` 10.0.0
* #3: Added support to Python3.14
* #44: Split the `slow-checks.yml` into `slow-checks-itde.yml` and `slow-checks-saas.yml`

## Dependency Updates

### `main`

* Updated dependency `exasol-integration-test-docker-environment:6.1.0` to `6.2.0`
* Updated dependency `pytest:9.0.3` to `9.1.1`

### `dev`

* Updated dependency `exasol-toolbox:7.0.0` to `10.0.0`
* Updated dependency `pyexasol:2.2.1` to `2.2.2`
* Updated dependency `types-pyyaml:6.0.12.20260408` to `6.0.12.20260518`