# Copyright (c) 2023, Mahdi and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):
	pass

	


    # ... (other methods)


	
	# def validate(self):
	# 	frappe.msgprint("Hello World")

	# def before_save(self):
	# 	frappe.throw("Hello World")
	# def before_insert(self):
	# 	frappe.throw("Hello World")

	# def after_insert(self):
	# 	frappe.throw("Hello World after insert")

	# def on_update(self):
	# 	frappe.throw("Hello World")

	# def before_submit(self):
	# 	frappe.throw("Hello World")

	# def on_submit(self):
	# 	frappe.msgprint("Hello World")

	# def on_cancel(self):
	# 	frappe.msgprint("Hello World")

	# def on_trash(self):
	# 	frappe.msgprint("Hello World")

	# def after_delete(self):
	# 	frappe.msgprint("Hello World")

	# 2 #################################################
#####################################################
################### Value fetching  #################

	# def validate(self):
	# 	frappe.msgprint(_("Hello My  full name is '{0}' ").format(
	# 		self.first_name +" "+ self.middle_name+" "+self.last_name))
			
	# def validate(self):			
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}. The family member name is '{1}' and relation is '{2}'").format(
	# 			row.idx,row.name1,row.relation))

# 3 ###################################################################################################
####################################################################################################
############ frappe.get_doc(doctype, name)  #########
#  Returns a Document object of the record identified by doctype and name

	# frappe.get_doc(doctype, name)
	
	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(_("The First Name is {0} and Age is {1}").format(doc.first_name,doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}. The family member name is '{1}' and relation is '{2}'").format(
	# 			row.idx,row.name1,row.relation))

	# 4 ###################################################################################################
####################################################################################################
###### frappe.new_doc(doctype) #########
# ''' create a new Document '''

# frappe.new_doc(doctype)
	
	# def validate(self):# means before saving the document
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Jake'
	# 	doc.last_name = 'Jay'
	# 	doc.age = 13
	# 	doc.append("family_members",{   "name1":"Jain",
	# 									"relation":"Sister",
	# 									"age":14
	# 								})
	# 	doc.insert()
# 5 ###################################################################################################
####################################################################################################
####### frappe.delete_doc(doctype, name)###
# frappe.delete_doc(doctype, name)

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', 'PR-0022')
# 6 ###################################################################################################
####################################################################################################
# Document Methods

#### doc.insert()

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Bally'
	# 	doc.age = 13
	# 	doc.insert()
	

	# some escape hatches that can be used to skip certain checks
	# doc.insert(
	#     ignore_permissions=True, # ignore write permissions during insert
	#     ignore_links=True, # ignore Link validation in the document
	#     ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
	#     ignore_mandatory=True # insert even if mandatory fields are not set
	# )
##### doc.save()

	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Dany'
	# 	doc.age = 31
	# 	doc.save()

	# 	doc.save(
	#     ignore_permissions=True, # ignore write permissions during insert
	#     ignore_version=True # do not create a version record
	# )
	# doc.delete()

	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'PR-0023')
	# 	doc.delete()

	# doc.db_set()

	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'PR-0022')
	# 	doc.db_set('age', 45)


	# 7 ###################################################################################################
####################################################################################################
############# Database API

# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 			filters={
	# 				'enable': 1
	# 			},
	# 			fields=['first_name', 'age']
	# 			)
	# 	for d in doc:
	# 		frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))

# 8 ###################################################################################################
####################################################################################################

# frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0022', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(first_name,age))

	# 9 ###################################################################################################
####################################################################################################
# frappe.db.set_value(doctype, name, fieldname, value)
	
	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting', 'PR-0022', 'age', 77)

	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0022', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and new age is {1}").format(first_name,age))

	# 10 ###################################################################################################
####################################################################################################

# frappe.db.exists(doctype, name)
	
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting', 'PR-00111'): # True
	# 		frappe.msgprint(_("The Document is Exists in Database"))	
	# 	else:
	# 		frappe.msgprint(_("The Document does not Exists in Database"))	

# 11 ###################################################################################################
####################################################################################################

# frappe.db.count(doctype, filters)
	
	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting', {'enable': 1}) # True
	# 	frappe.msgprint(_("The Enable Document Count is {0}").format(doc_count))

# 12 ###################################################################################################
# ####################################################################################################


# # frappe.db.sql(query, filters, as_dict)

	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data = frappe.db.sql("""
	# 							SELECT
	# 								first_name,
	# 								age
	# 							FROM 
	# 								`tabClient Side Scripting` 
	# 							WHERE 
	# 								enable = 1
	# 						""", as_dict=1)

	# 	for d in data:
	# 		frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))

# 13 ##################################################
#######################################################
#################### Server Side Call ###############
########## js
	# enable: function(frm) {
	# 		frm.call({
	# 			doc: frm.doc,
	# 			method: 'frm_call',
	# 			args: {
	# 				msg: "Hello"
	# 			},
	# 			freeze: true,
	# 			freeze_message: __('Calling frm_call Method'),
	# 			callback: function(r) {
	# 				frappe.msgprint(r.message)
					
	# 				// frappe.msgprint("Server Side calling Compleated")

	# 				// frm.refresh_field('medication_orders');
	# 			}
	# 		});
	# 	}
########## py 

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	# frappe.msgprint(msg)

	# 	self.mob_no= 77677656

	# 	# return "Hi This Message from frm_call"

	# 14 ##################################################
#######################################################
#################### Server Side Call #################
########## js
	# enable: function(frm) {
	# 		frappe.call({
	# 			method: "demo_app.programming_module.doctype.server_side_scripting.server_side_scripting.frappe_call",
	# 			args: {
	# 				msg: "Hello"
	# 			},
	# 			freeze: true,
	# 			freeze_message: __('Calling frappe_call Method'),
	# 			callback: function(r) {
	# 				frappe.msgprint(r.message)
	# 			}
	# 		});
	# 	}

########## py 
# @frappe.whitelist()
# def frappe_call(msg):
# 	# import time
# 	# time.sleep(5)
# 	# frappe.msgprint(msg)

# 	return "Hi This Message from frappe_call"








	