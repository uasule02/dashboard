/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "../src/js/custom/apps/customers/add.js":
/*!**********************************************!*\
  !*** ../src/js/custom/apps/customers/add.js ***!
  \**********************************************/
/***/ (() => {

eval("\n\n// Class definition\nvar KTModalCustomersAdd = function () {\n    var submitButton;\n    var cancelButton;\n\tvar closeButton;\n    var validator;\n    var form;\n    var modal;\n\n    // Init form inputs\n    var handleForm = function () {\n        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/\n\t\tvalidator = FormValidation.formValidation(\n\t\t\tform,\n\t\t\t{\n\t\t\t\tfields: {\n                    'name': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Customer name is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n                    'email': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Customer email is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'first-name': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'First name is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'last-name': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Last name is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'country': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Country is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'address1': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Address 1 is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'city': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'City is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'state': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'State is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t},\n\t\t\t\t\t'postcode': {\n\t\t\t\t\t\tvalidators: {\n\t\t\t\t\t\t\tnotEmpty: {\n\t\t\t\t\t\t\t\tmessage: 'Postcode is required'\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\tplugins: {\n\t\t\t\t\ttrigger: new FormValidation.plugins.Trigger(),\n\t\t\t\t\tbootstrap: new FormValidation.plugins.Bootstrap5({\n\t\t\t\t\t\trowSelector: '.fv-row',\n                        eleInvalidClass: '',\n                        eleValidClass: ''\n\t\t\t\t\t})\n\t\t\t\t}\n\t\t\t}\n\t\t);\n\n\t\t// Revalidate country field. For more info, plase visit the official plugin site: https://select2.org/\n        $(form.querySelector('[name=\"country\"]')).on('change', function() {\n            // Revalidate the field when an option is chosen\n            validator.revalidateField('country');\n        });\n\n\t\t// Action buttons\n\t\tsubmitButton.addEventListener('click', function (e) {\n\t\t\te.preventDefault();\n\n\t\t\t// Validate form before submit\n\t\t\tif (validator) {\n\t\t\t\tvalidator.validate().then(function (status) {\n\t\t\t\t\tconsole.log('validated!');\n\n\t\t\t\t\tif (status == 'Valid') {\n\t\t\t\t\t\tsubmitButton.setAttribute('data-kt-indicator', 'on');\n\n\t\t\t\t\t\t// Disable submit button whilst loading\n\t\t\t\t\t\tsubmitButton.disabled = true;\n\n\t\t\t\t\t\tsetTimeout(function() {\n\t\t\t\t\t\t\tsubmitButton.removeAttribute('data-kt-indicator');\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\tSwal.fire({\n\t\t\t\t\t\t\t\ttext: \"Form has been successfully submitted!\",\n\t\t\t\t\t\t\t\ticon: \"success\",\n\t\t\t\t\t\t\t\tbuttonsStyling: false,\n\t\t\t\t\t\t\t\tconfirmButtonText: \"Ok, got it!\",\n\t\t\t\t\t\t\t\tcustomClass: {\n\t\t\t\t\t\t\t\t\tconfirmButton: \"btn btn-primary\"\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t}).then(function (result) {\n\t\t\t\t\t\t\t\tif (result.isConfirmed) {\n\t\t\t\t\t\t\t\t\t// Hide modal\n\t\t\t\t\t\t\t\t\tmodal.hide();\n\n\t\t\t\t\t\t\t\t\t// Enable submit button after loading\n\t\t\t\t\t\t\t\t\tsubmitButton.disabled = false;\n\n\t\t\t\t\t\t\t\t\t// Redirect to customers list page\n\t\t\t\t\t\t\t\t\twindow.location = form.getAttribute(\"data-kt-redirect\");\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t});\t\t\t\t\t\t\t\n\t\t\t\t\t\t}, 2000);   \t\t\t\t\t\t\n\t\t\t\t\t} else {\n\t\t\t\t\t\tSwal.fire({\n\t\t\t\t\t\t\ttext: \"Sorry, looks like there are some errors detected, please try again.\",\n\t\t\t\t\t\t\ticon: \"error\",\n\t\t\t\t\t\t\tbuttonsStyling: false,\n\t\t\t\t\t\t\tconfirmButtonText: \"Ok, got it!\",\n\t\t\t\t\t\t\tcustomClass: {\n\t\t\t\t\t\t\t\tconfirmButton: \"btn btn-primary\"\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t});\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t}\n\t\t});\n\n        cancelButton.addEventListener('click', function (e) {\n            e.preventDefault();\n\n            Swal.fire({\n                text: \"Are you sure you would like to cancel?\",\n                icon: \"warning\",\n                showCancelButton: true,\n                buttonsStyling: false,\n                confirmButtonText: \"Yes, cancel it!\",\n                cancelButtonText: \"No, return\",\n                customClass: {\n                    confirmButton: \"btn btn-primary\",\n                    cancelButton: \"btn btn-active-light\"\n                }\n            }).then(function (result) {\n                if (result.value) {\n                    form.reset(); // Reset form\t\n                    modal.hide(); // Hide modal\t\t\t\t\n                } else if (result.dismiss === 'cancel') {\n                    Swal.fire({\n                        text: \"Your form has not been cancelled!.\",\n                        icon: \"error\",\n                        buttonsStyling: false,\n                        confirmButtonText: \"Ok, got it!\",\n                        customClass: {\n                            confirmButton: \"btn btn-primary\",\n                        }\n                    });\n                }\n            });\n        });\n\n\t\tcloseButton.addEventListener('click', function(e){\n\t\t\te.preventDefault();\n\n            Swal.fire({\n                text: \"Are you sure you would like to cancel?\",\n                icon: \"warning\",\n                showCancelButton: true,\n                buttonsStyling: false,\n                confirmButtonText: \"Yes, cancel it!\",\n                cancelButtonText: \"No, return\",\n                customClass: {\n                    confirmButton: \"btn btn-primary\",\n                    cancelButton: \"btn btn-active-light\"\n                }\n            }).then(function (result) {\n                if (result.value) {\n                    form.reset(); // Reset form\t\n                    modal.hide(); // Hide modal\t\t\t\t\n                } else if (result.dismiss === 'cancel') {\n                    Swal.fire({\n                        text: \"Your form has not been cancelled!.\",\n                        icon: \"error\",\n                        buttonsStyling: false,\n                        confirmButtonText: \"Ok, got it!\",\n                        customClass: {\n                            confirmButton: \"btn btn-primary\",\n                        }\n                    });\n                }\n            });\n\t\t})\n    }\n\n    return {\n        // Public functions\n        init: function () {\n            // Elements\n            modal = new bootstrap.Modal(document.querySelector('#kt_modal_add_customer'));\n\n            form = document.querySelector('#kt_modal_add_customer_form');\n            submitButton = form.querySelector('#kt_modal_add_customer_submit');\n            cancelButton = form.querySelector('#kt_modal_add_customer_cancel');\n\t\t\tcloseButton = form.querySelector('#kt_modal_add_customer_close');\n\n            handleForm();\n        }\n    };\n}();\n\n// On document ready\nKTUtil.onDOMContentLoaded(function () {\n\tKTModalCustomersAdd.init();\n});\n\n//# sourceURL=webpack://keenthemes/../src/js/custom/apps/customers/add.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["../src/js/custom/apps/customers/add.js"]();
/******/ 	
/******/ })()
;