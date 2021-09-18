document.addEventListener('DOMContentLoaded', function(){


    const btn1=document.querySelector('#btn1');
    btn1.onclick = () => {

        btn1.classList.add("active");
        btn2.classList.remove("active");
        document.querySelector('#received-view').style.display = 'block';
        document.querySelector('#sent-view').style.display = 'none';

    }

    const btn2=document.querySelector('#btn2');
    btn2.onclick = () => {

        btn2.classList.add("active");
        btn1.classList.remove("active");
        document.querySelector('#sent-view').style.display = 'block';
        document.querySelector('#received-view').style.display = 'none';

    }

    //default
    btn();

});



function btn(){
    btn1.classList.add("active");
    document.querySelector('#received-view').style.display = 'block';
    document.querySelector('#sent-view').style.display = 'none';
}