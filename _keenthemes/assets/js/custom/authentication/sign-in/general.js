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

/***/ "../src/js/custom/authentication/sign-in/general.js":
/*!**********************************************************!*\
  !*** ../src/js/custom/authentication/sign-in/general.js ***!
  \**********************************************************/
/***/ (() => {

eval("\n\n// Class definition\nvar KTSigninGeneral = function () {\n    // Elements\n    var form;\n    var submitButton;\n    var validator;\n\n    // Handle form\n    var handleValidation = function (e) {\n        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/\n        validator = FormValidation.formValidation(\n            form,\n            {\n                fields: {\n                    'email': {\n                        validators: {\n                            regexp: {\n                                regexp: /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/,\n                                message: 'The value is not a valid email address',\n                            },\n                            notEmpty: {\n                                message: 'Email address is required'\n                            }\n                        }\n                    },\n                    'password': {\n                        validators: {\n                            notEmpty: {\n                                message: 'The password is required'\n                            }\n                        }\n                    }\n                },\n                plugins: {\n                    trigger: new FormValidation.plugins.Trigger(),\n                    bootstrap: new FormValidation.plugins.Bootstrap5({\n                        rowSelector: '.fv-row',\n                        eleInvalidClass: '',  // comment to enable invalid state icons\n                        eleValidClass: '' // comment to enable valid state icons\n                    })\n                }\n            }\n        );\n    }\n\n    var handleSubmitDemo = function (e) {\n        // Handle form submit\n        submitButton.addEventListener('click', function (e) {\n            // Prevent button default action\n            e.preventDefault();\n\n            // Validate form\n            validator.validate().then(function (status) {\n                if (status == 'Valid') {\n                    // Show loading indication\n                    submitButton.setAttribute('data-kt-indicator', 'on');\n\n                    // Disable button to avoid multiple click\n                    submitButton.disabled = true;\n\n\n                    // Simulate ajax request\n                    setTimeout(function () {\n                        // Hide loading indication\n                        submitButton.removeAttribute('data-kt-indicator');\n\n                        // Enable button\n                        submitButton.disabled = false;\n\n                        // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/\n                        Swal.fire({\n                            text: \"You have successfully logged in!\",\n                            icon: \"success\",\n                            buttonsStyling: false,\n                            confirmButtonText: \"Ok, got it!\",\n                            customClass: {\n                                confirmButton: \"btn btn-primary\"\n                            }\n                        }).then(function (result) {\n                            if (result.isConfirmed) {\n                                form.querySelector('[name=\"email\"]').value = \"\";\n                                form.querySelector('[name=\"password\"]').value = \"\";\n\n                                //form.submit(); // submit form\n                                var redirectUrl = form.getAttribute('data-kt-redirect-url');\n                                if (redirectUrl) {\n                                    location.href = redirectUrl;\n                                }\n                            }\n                        });\n                    }, 2000);\n                } else {\n                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/\n                    Swal.fire({\n                        text: \"Sorry, looks like there are some errors detected, please try again.\",\n                        icon: \"error\",\n                        buttonsStyling: false,\n                        confirmButtonText: \"Ok, got it!\",\n                        customClass: {\n                            confirmButton: \"btn btn-primary\"\n                        }\n                    });\n                }\n            });\n        });\n    }\n\n    var handleSubmitAjax = function (e) {\n        // Handle form submit\n        submitButton.addEventListener('click', function (e) {\n            // Prevent button default action\n            e.preventDefault();\n\n            // Validate form\n            validator.validate().then(function (status) {\n                if (status == 'Valid') {\n                    // Show loading indication\n                    submitButton.setAttribute('data-kt-indicator', 'on');\n\n                    // Disable button to avoid multiple click\n                    submitButton.disabled = true;\n\n                    // Check axios library docs: https://axios-http.com/docs/intro\n                    axios.post(submitButton.closest('form').getAttribute('action'), new FormData(form)).then(function (response) {\n                        if (response) {\n                            form.reset();\n\n                            // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/\n                            Swal.fire({\n                                text: \"You have successfully logged in!\",\n                                icon: \"success\",\n                                buttonsStyling: false,\n                                confirmButtonText: \"Ok, got it!\",\n                                customClass: {\n                                    confirmButton: \"btn btn-primary\"\n                                }\n                            });\n\n                            const redirectUrl = form.getAttribute('data-kt-redirect-url');\n\n                            if (redirectUrl) {\n                                location.href = redirectUrl;\n                            }\n                        } else {\n                            // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/\n                            Swal.fire({\n                                text: \"Sorry, the email or password is incorrect, please try again.\",\n                                icon: \"error\",\n                                buttonsStyling: false,\n                                confirmButtonText: \"Ok, got it!\",\n                                customClass: {\n                                    confirmButton: \"btn btn-primary\"\n                                }\n                            });\n                        }\n                    }).catch(function (error) {\n                        Swal.fire({\n                            text: \"Sorry, looks like there are some errors detected, please try again.\",\n                            icon: \"error\",\n                            buttonsStyling: false,\n                            confirmButtonText: \"Ok, got it!\",\n                            customClass: {\n                                confirmButton: \"btn btn-primary\"\n                            }\n                        });\n                    }).then(() => {\n                        // Hide loading indication\n                        submitButton.removeAttribute('data-kt-indicator');\n\n                        // Enable button\n                        submitButton.disabled = false;\n                    });\n                } else {\n                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/\n                    Swal.fire({\n                        text: \"Sorry, looks like there are some errors detected, please try again.\",\n                        icon: \"error\",\n                        buttonsStyling: false,\n                        confirmButtonText: \"Ok, got it!\",\n                        customClass: {\n                            confirmButton: \"btn btn-primary\"\n                        }\n                    });\n                }\n            });\n        });\n    }\n\n    var isValidUrl = function(url) {\n        try {\n            new URL(url);\n            return true;\n        } catch (e) {\n            return false;\n        }\n    }\n\n    // Public functions\n    return {\n        // Initialization\n        init: function () {\n            form = document.querySelector('#kt_sign_in_form');\n            submitButton = document.querySelector('#kt_sign_in_submit');\n\n            handleValidation();\n\n            if (isValidUrl(submitButton.closest('form').getAttribute('action'))) {\n                handleSubmitAjax(); // use for ajax submit\n            } else {\n                handleSubmitDemo(); // used for demo purposes only\n            }\n        }\n    };\n}();\n\n// On document ready\nKTUtil.onDOMContentLoaded(function () {\n    KTSigninGeneral.init();\n});\n\n\n//# sourceURL=webpack://keenthemes/../src/js/custom/authentication/sign-in/general.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["../src/js/custom/authentication/sign-in/general.js"]();
/******/ 	
/******/ })()
;