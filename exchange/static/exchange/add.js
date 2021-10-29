document.addEventListener('DOMContentLoaded', function(){

    const load = document.querySelector('#load-btn')
    load.onclick = () => add_balance(load.value);

    //default
    btn();

});



function btn(){
    document.querySelector('#balance-view').style.display = 'block';
    document.querySelector('#add-view').style.display = 'none';
}



function add_balance(username){

    document.querySelector('#add-view').style.display = 'block';
    document.querySelector('#balance-view').style.display = 'none';
    console.log(username);
    

    document.querySelector('#load-submit').onsubmit = () => {

    const add_amount=parseInt(document.querySelector('#add-amount').value);
    const card_number=document.querySelector('#card_number').value;

    console.log(add_amount);
    console.log(card_number);


        if(card_number.length==12){
            fetch(`/add_usd/${username}`, {
                method: 'PUT',
                body: JSON.stringify({
                    amount: add_amount,
                    card_number: card_number
                })
            })
            
            document.querySelector('#message').innerHTML = `Loaded USD ${add_amount} to Balance`;
            location.reload()
            return false;
        }
        
        else{
            document.querySelector('#message').innerHTML = `Invalid Card Number`;
            return false;
        }

    };
}