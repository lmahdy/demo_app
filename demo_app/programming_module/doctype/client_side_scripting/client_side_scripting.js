// Copyright (c) 2023, Mahdi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {//this means when the doctype is opened this function will be called means it will be executed to do some work
	// refresh: function(frm) {//this is the function which will be called when the doctype is refreshed
    //      frappe.msgprint("Hello Mahdi");//this is the function which will print the message on the screen
	// 	 //frappe.throw("This is the error message ya mahdi")
	// }
    // onload: function(frm) {//frm is in the parameter which is the current form
	// frappe.msgprint("Hello Mahdi");
	// }//the onload function will be called when the doctype is loaded
	// validate: function(frm) {//the validate function will be called when the doctype is validated
	// 	frappe.throw("Hello Mahdi from validate")
	// }
	// before_save: function(frm) {//the before_save function will be called before the doctype is saved
	// 	frappe.throw("Hello Mahdi from before_save")
	// }

    // after_save: function(frm) {//the after_save function will be called after the doctype is saved
	// 	frappe.throw("Hello Mahdi from after_save")
	// }
	// enable: function(frm) {
	// 	frappe.msgprint("Hello Mahdi from enable")
	// }
	// age : function(frm) {
	// 	frappe.msgprint("Hello Mahdi from age")
	// }
	// family_members_on_form_rendered: function(frm) {
	// 	frappe.msgprint("Hello Mahdi from familymembes_on_form_rendered")
	// }
	// before_submit: function(frm) {
	// 	frappe.throw("Hello Mahdi from before_submit")
	// }
	// on_submit: function(frm) {
	// 	frappe.msgprint("Hello Mahdi from on_submit")
	// }
	// before_cancel: function(frm) {
	// 	frappe.throw("Hello Mahdi from before_cancel")
	// }
	// after_cancel: function(frm) {
	// 	frappe.msgprint("Hello Mahdi from after_cancel")
	// }

	// value fetching
	// after_save: function(frm){
	// 	frappe.msgprint(__("The full name is '{0}'", [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]));
	//     for (let row of frm.doc.family_members) {
	//  	frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'",
	//  		[row.idx,row.name1,row.relation]))
	// }	
	// }


	// 23
/////////////////////////////////////////////////////////////////
//////////////	 frm.set_intro & frm.is_new()	/////////////////
/////////////////////////////////////////////////////////////////
	// refresh:function(frm){
		
	// 	// frm.set_intro('Now you can ctreate a new Client Side Scripting doctype')

	// 	if(frm.is_new()){
	// 		frm.set_intro('Now you can ctreate a new Client Side Scripting doctype')
	// 	}//this will be executed when the doctype is new means when the doctype is not saved
	// }



// 24
/////////////////////////////////////////////////////////////////
//////////////			frm.set_value			/////////////////
/////////////////////////////////////////////////////////////////

	// validate:function(frm){
	// 	// frm.set_value('full_name',frm.doc.first_name +" "+ frm.doc.middle_name+" "+frm.doc.laste_name)
	
	
	// 	let row = frm.add_child('family_members',{
	// 		name1:'Johnson jose',
	// 		relation: 'Father',
	// 		age:56,
	// 	})
	// }

	// 25
/////////////////////////////////////////////////////////////////
//////////////			set_df_property	 		/////////////////
/////////////////////////////////////////////////////////////////
	
	//  enable:function(frm){

	// 		//  frm.set_df_property('first_name','reqd',1)//this will make the first_name field required the parameters are field name,property name and value of the property means 1 or 0 means true or false reqd means required the difference between putting  1 or 0 is that if we put 1 then the field will be required and if we put 0 then the field will not be required
	// 		// // frm.refresh_field('first_name');

	// 		//  frm.set_df_property('middle_name','read_only',1)
	// 		// // frm.refresh_field('middle_name');
			
	// 		frm.toggle_reqd('age',true)

	// }


	// 25
/////////////////////////////////////////////////////////////////
//////////////				Button 				/////////////////
/////////////////////////////////////////////////////////////////
 
	refresh:function(frm){

	 	// frm.add_custom_button('Click Me Button',() =>{
		
		// 	frappe.msgprint(__('You Clicked Me!!'));
		// })
		
		frm.add_custom_button('Click Me1',() =>{
		
			frappe.msgprint(__('You Clicked 1 !!'));
		},'click me')

		frm.add_custom_button('Click Me2',() =>{
		
			frappe.msgprint(__('You Clicked 2 !!'));
		},'click me')
	}



});
// frappe.ui.form.on('Family Members', {//this is the function which will be called when the doctype is refreshed
// // name1: function(frm){
// // 	frappe.msgprint("Hello Mahdi from name1")
// // }
//  age(frm,cdt,cdn){
// 	frappe.msgprint("Hello Mahdi from age")
//  }
// })
