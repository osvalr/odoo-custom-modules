import functools
import xmlrpclib
HOST = 'localhost'
PORT = 10080
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
    print "[%d] Session %s (%s seats)" % (session['id'], session['name'], session['seats'])
print sessions

# 3.create a new session for the "Functional" course
course_id = call('openacademy.course', 'search', [('name','ilike','Curso XPath')])[0]

# 3.create a new session
session_id = call('openacademy.session', 'create', {
    'name' : 'My session',
    'course_id' : course_id,
})