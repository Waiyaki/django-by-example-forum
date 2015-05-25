$(function(){
    // Navbar
    // Make home active if at home
    if (window.location.pathname === '/forum/'){
        $('#home').addClass('active');
    }

    var updateThreadAndForum = function(){
        var $newFormContent = $('<input type="hidden" name="csrfmiddlewaretoken" value=""><div class="form-group"><legend>Edit</legend></div><div id="form-content"><div class="form-group"><label for="id_title">Subject</label><input type="text" id="id_title" maxlength="60" name="title" class="form-control"></div><div class="form-group"><label for="id_description">Description</label><textarea class="form-control" maxlength="255" rows="3" id="id_description" name="description" placeholder="A short description of the topic"></textarea></div><div class="form-group"><button class="btn btn-primary" type="submit">Update</button></div></div>');

        update($newFormContent, '.threadforum', 'id_description');
    }

    var updatePostAndComment = function(){
        // A function that will provide the markup necessary to edit a Post or Comment Object
        var $newFormContent = $('<input type="hidden" name="csrfmiddlewaretoken" value=""><div class="form-group"><legend>Edit</legend></div><div id="form-content"><div class="form-group"><label for="id_title">Title</label><input type="text" id="id_title" maxlength="60" name="title" class="form-control"></div><div class="form-group"><label for="id_body">Description</label><textarea class="form-control" maxlength="255" rows="3" id="id_body" name="body"></textarea></div><div class="form-group"><button class="btn btn-primary" type="submit">Update</button></div></div>');

        update($newFormContent, '.compost', 'id_body');
    }


    var update = function(form, formclass, contentId){
        // Get common properties
        var csrfToken = $('input:hidden').val();
        var titleValue = $('#id_title').val();
        var content = $('#' + contentId).val();

        // empty form and append new content
        $(formclass).html('');
        $(formclass).append(form);
        $('input:hidden').val(csrfToken);
        $('#id_title').val(titleValue);
        $('#' + contentId).val(content); // Generalise the body id in both forms
    }

    updateThreadAndForum();
    updatePostAndComment();
})
