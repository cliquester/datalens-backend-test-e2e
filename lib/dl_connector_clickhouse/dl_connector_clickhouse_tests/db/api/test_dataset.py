from dl_api_lib_testing.connector.dataset_suite import DefaultConnectorDatasetTestSuite

from dl_connector_clickhouse_tests.db.api.base import ClickHouseDatasetTestBase


class TestClickHouseDataset(ClickHouseDatasetTestBase, DefaultConnectorDatasetTestSuite):
    pass
