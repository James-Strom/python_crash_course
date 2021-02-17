from printing_models import print_models as pm
from printing_models import show_completed_models as scm

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)