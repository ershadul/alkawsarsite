from server_errors.models import ServerError

def create_server_error(title, error_type, description):
    """
    Create and save a ServerError object.
    """
    try:
        error = ServerError()
        error.title = title
        error.error_type = error_type
        error.description = description
        error.save()
        return error
    except Exception, e:
        raise e