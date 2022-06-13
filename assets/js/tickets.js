(function() {
    let buttons = document.querySelectorAll('.add_button');
    const url = 'http://127.0.0.1:8000/tickets/';
    const token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    let items = [];
    
    let data = {
        headers:{
            'Accept': "application/json",
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"items":items}),
        // body: {"items":items},
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
            
            data.headers['X-CSRFToken'] = token;

            fetch(url, data)
            .then(data => {return data.json()})
            .then(resp=>{console.log(resp)})
            .catch(err=>{console.log(err)})
        });
    })
})();