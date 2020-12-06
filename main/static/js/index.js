const loadingSection=document.querySelector('.loading');
loadingSection.style.display="";

Dropzone.options.filedrop = {
    init: function() {
        this.on("success", function(file,response) { 
            alert(response.message);
            console.log(response.message);
        });
    }
};
