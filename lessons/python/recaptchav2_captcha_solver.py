import os
from anticaptchaofficial.recaptchav2proxyless import *

def solve_captcha(website_url, website_key):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_soft_id(0)
    solver.set_key(os.environ.get('ANTICAPTCHA_KEY'))
    solver.set_website_url(website_url)
    solver.set_website_key(website_key)
    #set optional custom parameter which Google made for their search page Recaptcha v2
    #solver.set_data_s('"data-s" token from Google Search results "protection"')


    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        return g_response
    else:
        return solver.error_code
