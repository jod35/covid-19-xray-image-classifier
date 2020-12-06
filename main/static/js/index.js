


Dropzone.options.filedrop = {
    init: function() {
        const loadingSection=document.querySelector('.loading');

        this.on("addedfile", function (file) {
            loadingSection.style.visibility="visible";
          });

        this.on("success", function(file,response) { 
            // alert(response.message);
            loadingSection.innerText="Predicting Image Class";

            setTimeout(function(){
                loadingSection.innerText=response.message;
            },2000);
        });

        
    }
};
