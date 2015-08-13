/**
 * Created by alejandrojnm on 7/19/14.
 */
    $(document).ready(function() {
        $('#login-form').bootstrapValidator({
            message: 'This is no valid',
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            submitHandler: function(validator, form, submitButton) {
                // Use Ajax to submit form data
                    $.post(form.attr('action'), form.serialize(), function(result) {
                        if (result.status == true || result.status == 'true') {
                        // You can reload the current location
                        window.location = result.url;

                        // Or use Javascript to update your page, such as showing the account name
                        // $('#welcome').html('Hello ' + result.username);
                    } else {
                        // The account is not found
                        // Show the errors
                        $('#msg').html(result.msg).removeClass('hide');

                        // Enable the submit buttons
                        $('#login-form').bootstrapValidator('disableSubmitButtons', false);
                    }
                }, 'json');
            },
            fields: {
                user: {
                    validators: {
                        notEmpty: {
                            message: 'This field cant be empty'
                        }
                    }
                },
                passwd: {
                    validators: {
                        notEmpty: {
                            message: 'This field cant be empty'
                        }
                    }
                }
            }
        });
    });