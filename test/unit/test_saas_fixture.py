from unittest.mock import Mock

import exasol.pytest_backend as backend


def test_backend_aware_saas_database_id_uses_resolved_id(monkeypatch):
    saas_api_access = Mock()
    wait_mock = Mock(return_value="resolved-id")
    monkeypatch.setattr(backend, "_wait_until_saas_database_running", wait_mock)

    fixture = backend.backend_aware_saas_database_id.__wrapped__
    actual = list(
        fixture(
            saas_api_access=saas_api_access,
            backend_aware_saas_database_id_async="initial-id",
            saas_database_name="db-name",
        )
    )

    assert actual == ["resolved-id"]
    wait_mock.assert_called_once_with(saas_api_access, "db-name", "initial-id")


def test_backend_aware_saas_database_id_without_saas_access():
    fixture = backend.backend_aware_saas_database_id.__wrapped__
    actual = list(
        fixture(
            saas_api_access=None,
            backend_aware_saas_database_id_async="initial-id",
            saas_database_name="db-name",
        )
    )
    assert actual == ["initial-id"]
