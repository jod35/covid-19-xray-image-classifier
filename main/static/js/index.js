const file_input=document.querySelector('#file-input');
const imageNameDisplay=document.querySelector('.image-name');
const messageContainer=document.querySelector('.message');
const messageCloseButton=document.querySelector('#close-btn');
const fileForm=document.querySelector('form');
const API_URL='/api/'

file_input.addEventListener('input',()=>{
    imageNameDisplay.innerText=file_input.value;
});







// fileForm.addEventListener('submit',(event)=>{

//     console.log("Hello");

//     let formData=new FormData(fileForm);

//     formData.append('file_path',file_input.files);

//     let newFile={
//         filename:formData.get('filename'),
//         file_path:formData.get('file_path'),
//         decription:formData.get('description')
//     }

//         //Function to post form data to database
//     const postformData=(formdata)=>{
//         fetch('/api/predict',
//             {
//                 body:formdata,
//                 method:"POST",
//                 headers:{
//                     "content-type":"application/json"
//                 }
//             })
//     }

    
//     postformData(JSON.stringify(newFile))
//     .then(response=>response.json())
//     .then(data=>console.log(data))
    
//     event.preventDefault();
// })