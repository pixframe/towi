# ###### API RESPONSES ########## #

USER_NOT_FOUND = {
    'status': 'USER_NOT_FOUND',
    'message': 'Invalid email or password try again.'
}

ERROR_MISSING_EMAIL_PASSWORD = {
    'status': 'ERROR',
    'message': 'Missing parameters email or password'
}

ERROR_MISSING_USERKEY = {
    'status': 'ERROR',
    'message': 'Missing userKey parameter'
}

ERROR_MISSING_JSON = {
    'status': 'ERROR',
    'message': 'Missing jsonToDb parameter'
}

ERROR_PARSING_JSON = {
    'status': 'ERROR',
    'message': 'Invalid json'
}

ERROR_MISSING_PARAMETERS = {
    'status': 'ERROR',
    'message': 'Missing parameters'
}

ERROR_MISSING_MD5_DEVICE = {
    'status': 'ERROR',
    'message': 'Missing md5_device parameter'
}

ERROR_INVALID_MD5 = {
    'status': 'ERROR',
    'message': 'Invalid md5 hash',
    'code': '406'
}

ERROR_INVALID_EMAIL = {
    'status': 'ERROR',
    'message': 'Invalid email',
}

ERROR_NOT_FOUND = {
    'status': 'ERROR',
    'message': 'Matching query does not exists',
    'code': 666
}
