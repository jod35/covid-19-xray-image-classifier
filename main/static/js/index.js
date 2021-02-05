Dropzone.options.filedrop = {
  
   //activate the dropzone
  init: function () {


    const loadingSection = document.querySelector(".loading");
    const messageSection = document.querySelector(".msg");
    const loadSpinner = document.querySelector(".load-img");

    this.on("addedfile", function (file) {
      loadingSection.style.visibility = "visible";
      loadSpinner.style.visibility = "visible";
    });

    //when sending the file (uploading)
    this.on("sending", function (file) {
      messageSection.innerText = "Uploading ...";
    });

    //if file is uploaded, 
    this.on("success", function (file, response) {
      messageSection.innerText = "Predicting Image Class ...";

      setTimeout(function () {
        loadSpinner.style.visibility = "hidden";

        //show us the results
        let html = `
                
                <div class="prediction">
                    <div>
                        <h4>Covid Prediction </h4>
                        <p>Neural Network Output: <strong class="pred">${response.message.covid_result.Output}</strong></p>
                     
                        <p >Class : <strong class="pred">${response.message.covid_result.class}</strong> </p>
                     
                        <strong>
                          <p>
                              Note: A value closer to 1 signifies illness <br> while one closer to 0 
                              shows normalness
                          </p>
                        </strong>
                    </div>
                    <div>
                        <h4>Other Predictions </h4>
                        <p>Neural Network Output: <strong class="pred">${response.message.pneumonia_result.Output}</strong></p>
                     
                        <p >Class : <strong class="pred">${response.message.pneumonia_result.class}</strong> </p>
                     
                        <strong>
                          <p> 
                              Note: A value closer to 1 signifies illness <br> while one closer to 0 
                              shows normalness
                          </p>
                        </strong>
                    </div>
                </div>
                
                `;
        messageSection.innerHTML = html;
        console.log(response.message);
      }, 5000); 

      this.removeAllFiles(true);
    });

    this.on("error", function (file, response) {
      messageSection.innerText =
        "Sorry An Error Occured during Processing the image.";
      messageSection.style.color = "red";
      loadSpinner.style.visibility = "hidden";
    });
  },
};
