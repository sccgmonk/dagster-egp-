from dagster import Definitions, load_assets_from_modules,fs_io_manager
from dagster_pipelines import assets
from dagster_pipelines.schedules import kpi_fy_monthly_job_schedule
# from dagster_pipelines.resources.fs_io_manager import fs_io_manager



defs = Definitions(
    assets=load_assets_from_modules([assets]),
    schedules=[kpi_fy_monthly_job_schedule],

    resources={"io_manager": fs_io_manager.configured({"base_dir": "/opt/dagster/app/storage"})},

)