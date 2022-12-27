"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from linear_regression.nodes.predict import predict


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=predict.load_model, 
            inputs='model', 
            outputs='model_loaded',
            name='load_model'             
        ),       
         node(
            func=predict.parse_payload, 
            inputs=['params:ft_1', 'params:ft_2'], 
            outputs='model_inputs',
            name='parse_payload'             
        ), 
        node(
            func=predict.predict, 
            inputs=['model', 'model_inputs'], 
            outputs='model_outputs',
            name='predict'             
        ),
        node(
            func=predict.np_to_pd, 
            inputs='model_outputs', 
            outputs=['pipeline_outputs', 'data_scored'],
            name='convert_np_pd'             
        )        
    ])
