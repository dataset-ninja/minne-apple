import supervisely as sly
from dataset_tools.convert.minneapple.main import to_supervisely

api = sly.Api.from_env()
project_id = to_supervisely(api)

print("Project id is", project_id)
