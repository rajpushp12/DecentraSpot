document.addEventListener('DOMContentLoaded', function(){

    const load = document.querySelector('#load-btn')
    load.onclick = () => add_balance(load.value);

    const transfer = document.querySelector('#transfer-btn')
    transfer.onclick = () => transfer_curr();

    //default
    btn();

});



function btn(){
    document.querySelector('#balance-view').style.display = 'block';
    document.querySelector('#add-view').style.display = 'none';
    document.querySelector('#transfer-view').style.display = 'none';
    document.querySelector('#request-view').style.display = 'none';
}



function add_balance(username){

    document.querySelector('#balance-view').style.display = 'none';
    document.querySelector('#transfer-view').style.display = 'none';
    document.querySelector('#request-view').style.display = 'none';
    document.querySelector('#add-view').style.display = 'block';
    console.log(username);
    

    document.querySelector('#load-submit').onsubmit = () => {

    const add_amount=parseInt(document.querySelector('#add-amount').value);
    const card_number=document.querySelector('#card_number').value;

    console.log(add_amount);
    console.log(card_number);

        fetch(`/add_usd/${username}`, {
            method: 'PUT',
            body: JSON.stringify({
                amount: add_amount,
                card_number: card_number
            })
        });

        console.log('done');
    };
}



function transfer_curr(){
    document.querySelector('#transfer-view').style.display = 'block';
    document.querySelector('#balance-view').style.display = 'none';
    document.querySelector('#request-view').style.display = 'none';
    document.querySelector('#add-view').style.display = 'none';

}

