import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from transformers import pipeline, set_seed 

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here 
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    for text in request.text:
        response = generator(text, max_length=30 )
        
        response = response[0]["generated_text"].split('.')
        response = response[0]

        output.append(response)

    return SimpleText(dict(text=output))