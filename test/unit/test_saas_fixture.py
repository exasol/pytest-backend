from unittest.mock import Mock

import exasol.pytest_backend as backend


def test_backend_aware_saas_database_id_uses_resolved_id():
    saas_api_access = Mock()
    saas_api_access.wait_until_running.return_value = "resolved-id"

    fixture = backend.backend_aware_saas_database_id.__wrapped__
    actual = list(
        fixture(
            saas_api_access=saas_api_access,
            backend_aware_saas_database_id_async="initial-id",
        )
    )

    assert actual == ["resolved-id"]
    saas_api_access.wait_until_running.assert_called_once_with("initial-id")


def test_backend_aware_saas_database_id_without_saas_access():
    fixture = backend.backend_aware_saas_database_id.__wrapped__
    actual = list(
        fixture(
            saas_api_access=None,
            backend_aware_saas_database_id_async="initial-id",
        )
    )
    assert actual == ["initial-id"]
