(function() {
    let buttons = document.querySelectorAll('.add_button');
    const url = 'http://127.0.0.1:8000/tickets/';
    let items = [];

    const data = {
        headers:{"content-type":"application/json; charset=UFT-8;"},
        credentials: "same-origin",
        body:{items},
        method:"POST"
    };

    buttons.forEach(button => {
        button.addEventListener('click', event => {

            if (button.classList.contains('btn-primary')) {
                button.classList.replace('btn-primary', 'btn-success');
                button.innerHTML = 'Selected';
            } else {
                button.classList.replace('btn-success', 'btn-primary');
                button.innerHTML = 'Add';
            }
            fetch(url, data)
            .then(resp=>{console.log(resp)})
            .catch(err=>{console.log(err)})
        });
    })
})();