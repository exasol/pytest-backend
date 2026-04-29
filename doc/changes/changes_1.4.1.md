# 1.4.1 - 2026-04-29

## Summary

## Security Issues

This release fixes vulnerabilities by updating dependencies:

| Dependency   | Vulnerability       | Affected | Fixed in |
|--------------|---------------------|----------|----------|
| black        | CVE-2026-32274      | 25.12.0  | 26.3.1   |
| cryptography | CVE-2026-34073      | 46.0.5   | 46.0.6   |
| cryptography | CVE-2026-39892      | 46.0.5   | 46.0.7   |
| pytest       | CVE-2025-71176      | 8.4.2    | 9.0.3    |
| tornado      | GHSA-78cv-mqj4-43f7 | 6.5.4    | 6.5.5    |
| tornado      | CVE-2026-31958      | 6.5.4    | 6.5.5    |
| tornado      | CVE-2026-35536      | 6.5.4    | 6.5.5    |
| pyasn1       | CVE-2026-30922      | 0.6.2    | 0.6.3    |
| pygments     | CVE-2026-4539       | 2.19.2   | 2.20.0   |

* #13: Updated dependencies:
    * Updated cryptography to version 46.0.6 (fixes CVE-2026-34073)
    * Updated pyasn1 to version 0.6.3 (fixes CVE-2026-30922)
    * Updated requests to version 2.33.0 (fixes CVE-2026-25645)
    * Updated tornado to version 6.6.5 (fixes several security issues)
* #21: Relocked transitive dependencies and increased allowed versions for pytest, pyexasol, exasol-toolbox, and exasol-integration-test-docker-environment

## Refactoring

 * #16: Updated to latest PTB 6.1.1, regenerated workflows and added `.workflow-patcher.yml`

## Dependency Updates

### `main`

* Updated dependency `exasol-integration-test-docker-environment:5.0.0` to `6.1.0`
* Updated dependency `exasol-saas-api:2.8.0` to `2.10.0`
* Updated dependency `pytest:8.4.2` to `9.0.3`

### `dev`

* Updated dependency `exasol-bucketfs:2.1.0` to `2.2.0`
* Updated dependency `exasol-toolbox:5.1.1` to `7.0.0`
* Updated dependency `pyexasol:1.3.0` to `2.2.1`
* Updated dependency `types-pyyaml:6.0.12.20250915` to `6.0.12.20260408`