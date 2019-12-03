
  document.addEventListener('DOMContentLoaded', function() {
    
    document.querySelector('#form-submit').onsubmit = () => {
      alert("helo");


      const request = new XMLHttpRequest();
      request.open('POST', '/upload/');
      request.onload = () => {
        const data = JSON.parse(request.response);
        const img = new Image(256,256);
        const par = document.createElement('p');
        const divcol = document.createElement('div');
        divcol.className = 'col-sm-12 col-md-6';
        if(data.success){
          const image_url = data.image;
          const diagnostic = data.diagnostic;
          img.src = image_url;
          par.innerHTML = diagnostic;
        }
        else{
          div.innerHTML = 'There was an error loading the image';
        }
        divcol.appendChild(img);
        divcol.appendChild(par);
        document.getElementById('result-div').hidden = false;
        document.querySelector('#image-body').append(divcol);
        //document.querySelector('#image-body').append(par);
      }
      const myForm = document.getElementById('form-submit');
      const formData = new FormData(myForm);

      request.send(formData); 
      return false;
    };
  });