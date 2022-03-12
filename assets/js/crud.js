(function() {
    let buttons = document.querySelectorAll('.record-delete');
    console.log(buttons);

    buttons.forEach(button => {
        console.log('button');
        button.addEventListener('click', event => {
            let url_delete = button.getAttribute('data-record-del-url');
            let delete_modal = new bootstrap.Modal(document.getElementById('delete-modal'), {
                // backdrop: 'static',
                keyboard: false
            });
            let form_delete = document.getElementById('form-delete');
            form_delete.setAttribute('action', url_delete);
            delete_modal.show();
        });
    })
})();