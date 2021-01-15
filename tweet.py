from markf import generate_text
from init import initial


API = initial()
txt = generate_text()
API.update_status(txt)