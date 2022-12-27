from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession
import json
from typing import Any, Dict

def run_pipeline(pipeline_name = '__default__', env = 'base', extra_params = {}) -> Dict[str, Any]:
    project_name = 'linear_regression'
    configure_project(project_name)
    extra_params_dict = json.loads(extra_params)
    with KedroSession.create(env = env, extra_params = extra_params_dict) as session:
        outputs = session.run(pipeline_name = pipeline_name)
        return outputs