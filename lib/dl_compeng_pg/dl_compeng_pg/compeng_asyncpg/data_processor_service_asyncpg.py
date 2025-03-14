from __future__ import annotations

from typing import Type

import attr

from dl_compeng_pg.compeng_asyncpg.pool_asyncpg import AsyncpgPoolWrapper
from dl_compeng_pg.compeng_asyncpg.processor_asyncpg import AsyncpgOperationProcessor
from dl_compeng_pg.compeng_pg_base.data_processor_service_pg import CompEngPgService
from dl_compeng_pg.compeng_pg_base.pool_base import BasePgPoolWrapper
from dl_core.data_processing.processing.processor import OperationProcessorAsyncBase
from dl_core.services_registry.top_level import ServicesRegistry


@attr.s
class AsyncpgCompEngService(CompEngPgService[AsyncpgPoolWrapper]):
    def _get_pool_wrapper_cls(self) -> Type[BasePgPoolWrapper]:
        return AsyncpgPoolWrapper

    def get_data_processor(  # type: ignore  # 2024-01-29 # TODO: Return type "OperationProcessorAsyncBase" of "get_data_processor" incompatible with return type "ExecutorBasedOperationProcessor" in supertype "DataProcessorService"  [override]
        self,
        service_registry: ServicesRegistry,
        reporting_enabled: bool,
    ) -> OperationProcessorAsyncBase:
        return AsyncpgOperationProcessor(
            service_registry=service_registry,
            pg_pool=self.pool,
            reporting_enabled=reporting_enabled,
        )
