"use strict";

// import { initializeApp } from 'firebase/app';
// import { firebaseConfig } from '../../secrete/firebase_config.js';



// const app = initializeApp(firebaseConfig);

let indexContainer = document.querySelector('#index_container');
let loginLink = document.querySelector('.login_link');
let email = document.querySelector('.email');
let password = document.querySelector('.password');
let setDefaultLocation = document.querySelector('.set_default_location');
let createLink = document.querySelector('.create_link');
let checkbox = document.querySelector('.restaurant_registration input');
let createAccountButton = document.querySelector('.create_account_button');
let loginButton = document.querySelector('.login_button');

let inCreate = document.querySelectorAll('.in_create');
let inLogin = document.querySelectorAll('.in_login');


indexContainer.addEventListener('click',function(e){

    if(e.target == loginLink){
        inCreate.forEach((create)=>{
            create.classList.add('hide');
        });

        inLogin.forEach((login)=>{
            login.classList.remove('hide');
        });
    }else if(e.target == createLink){
        inCreate.forEach((create)=>{
            create.classList.remove('hide');
        });

        inLogin.forEach((login)=>{
            login.classList.add('hide');
        });
    }
});

