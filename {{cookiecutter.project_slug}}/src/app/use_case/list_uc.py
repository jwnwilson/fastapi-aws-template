from typing import List

from hex_lib.ports.db import DbAdapter
from hex_lib.ports.storage import StorageAdapter

from app.domain.data import DataEntity


def list_uc(
    db_adapter: DbAdapter,
    task_storage_adapter: StorageAdapter,
    template_storage_adapter: StorageAdapter,
) -> List[str]:
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # create pdf
    entity = DataEntity(
        db_adapter=db_adapter,
        task_storage_adapter=task_storage_adapter,
        template_storage_adapter=template_storage_adapter,
    )
    task_data: List[str] = entity.list()
    return task_data
