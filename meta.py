
def import_class(path_string):
    '''
    The normal __import__ from string does not works with classes. Furthermore,
    when it is called on a long path, it returns just the topmost package. This
    function returns the last package or class specified with the given path
    string.
    >>> mock_log('log')
    >>> c = import_class('xml.dom.minidom.parseString')
    importing class: module_path: ['xml', 'dom', 'minidom']
    attributes: ['dom', 'minidom', 'parseString']
    >>> from xml.dom.minidom import parseString
    >>> dir(c) == dir(parseString)
    True
    '''
    path_parts  = path_string.split('.')
    module_path = path_parts[:-1]
    attributes  = path_parts[1:]
    log.debug('importing class: module_path: {0}\nattributes: {1}'.format(module_path, attributes))
    try:
        c = __import__('.'.join(module_path))
        for part in attributes: c = getattr(c, part)
        return c
    except Exception as e:
        raise Exception('error importing the class {0!r}, probably it is not available from your python environment: {1}'.format(path_string, e))

