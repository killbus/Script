import os

COOKIE_NAME = "zgydCookie"

def initEnv():
    env = os.environ
    #env[COOKIE_NAME] = "deviceid_pdj_jd=c47ff7d041fe987dd5e55268ec597b90;PDJ_H5_PIN=JD_d55e6035cd88000;o2o_m_h5_sid=e3127ec1-2681-4ae2-90cf-9b0337d1a690"
    #env[COOKIE_NAME] += "&"+"deviceid_pdj_jd=b45731944c35d4b86e71d0e762e7bf3f; PDJ_H5_PIN=JD_dd213238cc61000; o2o_m_h5_sid=23579b92-2c53-4863-afb3-2862fd6eb6f3"
    #env[COOKIE_NAME] += "&"+"deviceid_pdj_jd=bccc214679bd9b11a51c1559324610af;PDJ_H5_PIN=JD_dd99acd70d23000;o2o_m_h5_sid=2744ad2d-8455-4ed5-8053-eeac64176cbf"
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []