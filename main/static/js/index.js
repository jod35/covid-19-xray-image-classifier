


Dropzone.options.filedrop = {
    init: function() {
        const loadingSection=document.querySelector('.loading');
        const messageSection=document.querySelector('.msg');
        const loadSpinner=document.querySelector('.load-img');
        
        this.on("addedfile", function (file) {
            
            loadingSection.style.visibility="visible";
          });

        //when sending the file (uploading)
        this.on("sending",function(file){
            messageSection.innerText="Uploading ...";
        });

       

        this.on("success", function(file,response) { 
            messageSection.innerText="Predicting Image Class";

            

            setTimeout(function(){
                loadSpinner.style.visibility="hidden";
                messageSection.innerText=response.message;
            },3000);
            

            
            this.removeAllFiles(true);

           
        });

        
    }
};
