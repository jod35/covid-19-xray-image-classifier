Dropzone.options.filedrop = {
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

    this.on("success", function (file, response) {
      messageSection.innerText = "Predicting Image Class ...";

      setTimeout(function () {
        loadSpinner.style.visibility = "hidden";
        let html = `
                
                <div class="prediction">
                    <h4>Results</h4>
                    <p>Neural Network Output: ${response.message.data.Output}</p>
                    <p>Class : ${response.message.data.class} </p>
                    <p> Severity is measured on a scale of 0 - 1. Values near 1 show illness as values near 0 show normalness"</p>
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
