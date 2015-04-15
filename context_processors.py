def language(request):
    return {'language': request.language, 'locals': request.locals}