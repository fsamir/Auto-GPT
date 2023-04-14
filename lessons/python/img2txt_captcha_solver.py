import os
from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key(os.environ.get('ANTICAPTCHA_KEY'))

def solve_captcha(captcha_file):
    captcha_text = solver.solve_and_return_solution(captcha_file)
    if captcha_text != 0:
        return captcha_text
    else:
        return solver.error_code
