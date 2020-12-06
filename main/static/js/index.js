Dropzone.options.filedrop = {
    init: function () {
        const loadingSection = document.querySelector('.loading');
        const messageSection = document.querySelector('.msg');
        const loadSpinner = document.querySelector('.load-img');

        this.on("addedfile", function (file) {

            loadingSection.style.visibility = "visible";
            loadSpinner.style.visibility="visible";
        });

        //when sending the file (uploading)
        this.on("sending", function (file) {
            messageSection.innerText = "Uploading ...";
        });



        this.on("success", function (file, response) {
            messageSection.innerText = "Predicting Image Class";



            setTimeout(function () {
                loadSpinner.style.visibility = "hidden";
                let html=`
                
                <div class="prediction">
                    <h4>Results</h4>
                    <p>File: ${file}</p>
                    <p>Predicted as : ${response.message.class}</p>
                    <p>Accuracy score: ${response.message.score}</p>
                    <p>Predictions: ${response.message.predictions}</p>
                </div>
                
                `
                messageSection.innerHTML = html;
                console.log(response.message);
            }, 5000);



            this.removeAllFiles(true);


        });


    }
};
