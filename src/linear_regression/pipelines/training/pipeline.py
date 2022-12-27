"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from linear_regression.nodes.training import training

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
            node(
                func=training.clean_data, 
                inputs=['data_x', 'data_y'], 
                outputs=['data_x_cleaned', 'data_y_cleaned'],
                name='clean'     
            ),
            node(
                func=training.pd_to_np, 
                inputs=['data_x_cleaned', 'data_y_cleaned'], 
                outputs=['x', 'y'],
                name='convert_pd_np'                   
            ),
            node(
                func=training.add_noise, 
                inputs=['x', 'y'], 
                outputs='y_with_noise',
                name='make_noise'                    
            ),
            node(
                func=training.train, 
                inputs=['x', 'y_with_noise'], 
                outputs='model',
                name='train'               
            ),
            node(
                func=training.save_model, 
                inputs=['model'],
                outputs=None,
                name='save'               
            ),
            
    ])
