import sys, os

# importing grand-parent folder
ml_folder = os.path.dirname(os.path.abspath('../'))
sys.path.insert(0,ml_folder)

from core.validate_url import validate_url

from pytorch import RegressorLinear

best_model:dict = {}

def run(label_type=""):
    pass


