# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt"


from __future__ import unicode_literals
import frappe

def on_session_creation(login_manager):
	"""
		called after login
		update login_from and delete parallel sessions
	"""
	if frappe.session['user'] not in ('Guest'):
		# create feed
		from frappe.utils import nowtime
		from frappe.profile import get_user_fullname
		frappe.db.begin()
		make_feed('Login', 'Profile', login_manager.user, login_manager.user,
			'%s logged in at %s' % (get_user_fullname(login_manager.user), nowtime()), 
			login_manager.user=='Administrator' and '#8CA2B3' or '#1B750D')
		frappe.db.commit()